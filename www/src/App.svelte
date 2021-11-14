<script>
	import { onMount } from "svelte";

	import LeftBar from "./Components/LeftBar.svelte";
	import Main from "./Components/Main.svelte";
	import RightBar from "./Components/RightBar.svelte";
	import config from "./config";

	import createAuth0Client from "@auth0/auth0-spa-js";
	import LoadingIndicator from "./Components/Misc/LoadingIndicator.svelte";

	let tab = 4;
	let backend_server = config.backend.ip;

	let auth0 = null;
	let isAuthenticated = null;
	let user = null;
	let authenticationCompleted = false;
	let superuser = false;

	const login = async () => {
		authenticationCompleted = false;
		await auth0.loginWithRedirect({
			redirect_uri: window.location.origin,
		});
	};

	const logout = () => {
		auth0.logout({
			returnTo: window.location.origin,
		});
	};

	const updateUser = async () => {
		// Update user and authentication status
		isAuthenticated = await auth0.isAuthenticated();
		user = await auth0.getUser();
		authenticationCompleted = true;

		// Turn of welcome screen if user is logged in
		if (isAuthenticated) {
			tab = 1;
			superuser = await fetchSuperUser(user.email);
		}
	};

	const configureClient = async () => {
		auth0 = await createAuth0Client({
			domain: config.auth0.domain,
			client_id: config.auth0.clientId,
		});
	};

	onMount(async () => {
		await configureClient();

		updateUser();

		const isAuthenticated = await auth0.isAuthenticated();

		if (isAuthenticated) {
			return;
		}

		const query = window.location.search;
		if (query.includes("code=") && query.includes("state=")) {
			await auth0.handleRedirectCallback();

			updateUser();

			window.history.replaceState({}, document.title, "/");
		}
		authenticationCompleted = true;
	});

	const fetchSuperUser = async (email) => {
		const response = fetch(backend_server + "user/auth?email=" + email);

		let re = await (await response).json();
		return re.user.superuser;
	};
</script>

<div>
	{#if authenticationCompleted}
		<LeftBar
			{isAuthenticated}
			{user}
			{superuser}
			login={() => login()}
			logout={() => logout()}
		/>
		<Main {tab} {backend_server} {user} login={() => login()} />
		<RightBar bind:selection={tab} hidden={!isAuthenticated} />
	{:else}
		<span>
			<LoadingIndicator />
		</span>
	{/if}
</div>

<style>
	div {
		width: 100%;
		height: 100%;

		display: grid;
		grid-template-columns: 15% auto 15%;
	}

	span {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
	}
</style>

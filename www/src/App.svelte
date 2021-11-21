<script>
	import auth0 from "./auth0";
	import { _user } from "./user";

	import { onMount } from "svelte";
	import LeftBar from "./Components/LeftBar.svelte";
	import Main from "./Components/Main.svelte";
	import RightBar from "./Components/RightBar.svelte";

	import LoadingIndicator from "./Components/Misc/LoadingIndicator.svelte";
	import Button from "./Components/Misc/Button.svelte";
	import ScreenLogin from "./Components/ScreenLogin.svelte";

	let tab = 0;
	let isAuthenticating = true;
	let isAuthenticated = false;

	let auth0_client = null;

	// Subscribe to user data
	let user = null;
	_user.subscribable.subscribe((value) => {
		user = value;
	});

	const auth0_authenticate = async () => {
		isAuthenticating = true;

		auth0_client = await auth0.createClient();

		isAuthenticated = await auth0_client.isAuthenticated();
		if (isAuthenticated) {
			tab = 0;
			_user.authorize(await auth0_client.getUser());
		} else {
			tab = 4;
		}

		isAuthenticating = false;
	};

	// Fetch user data
	onMount(async () => {
		await auth0_authenticate();
	});

	const handleAfterLogin = async () => {
		await auth0_authenticate();
	};

	const handleLogin = async () => {
		await auth0.login(
			auth0_client,
			window.location.origin,
			async (client) => {
				await handleAfterLogin(client);
			}
		);
	};
</script>

<div>
	{#if user != null && !isAuthenticating}
		<LeftBar
			logout={() => auth0.logout(auth0_client, window.location.origin)}
		/>
		<Main
			{tab}
			handleLogin={async () => {
				await auth0.login(
					auth0_client,
					window.location.origin,
					async (client) => {
						await handleAfterLogin(client);
					}
				);
			}}
		/>
		<RightBar bind:selection={tab} hidden={user == null} />
	{:else if !isAuthenticated && !isAuthenticating}
		<ScreenLogin login={async () => await handleLogin()} />
	{:else}
		<LoadingIndicator />
	{/if}
</div>

<style>
	div {
		width: 100%;
		height: 100%;

		display: grid;
		grid-template-columns: 15% auto 15%;
	}
</style>

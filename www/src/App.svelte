<script>
	import auth0 from "./auth0";
	import { _user } from "./user";

	import { onMount } from "svelte";
	import LeftBar from "./Components/LeftBar.svelte";
	import Main from "./Components/Main.svelte";
	import RightBar from "./Components/RightBar.svelte";

	import LoadingIndicator from "./Components/Misc/LoadingIndicator.svelte";
	import Button from "./Components/Misc/Button.svelte";

	let tab = 4;

	// Subscribe to user data
	let user = null;
	_user.subscribable.subscribe((value) => {
		user = value;
	});

	// Fetch user data
	let auth0_client = null;
	onMount(async () => {
		auth0_client = await auth0.createClient();

		const isAuthenticated = await auth0_client.isAuthenticated();
		if (isAuthenticated) {
			tab = 0;
			_user.authorize(await auth0_client.getUser());
		}
	});

	const handleAfterLogin = async () => {
		auth0_client = await auth0.createClient();
		const isAuthenticated = await uth0_client.isAuthenticated();
		if (isAuthenticated) {
			tab = 0;
			_user.authorize(await auth0_client.getUser());
		}
	};
</script>

<div>
	{#if user != null || tab == 4}
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
</style>

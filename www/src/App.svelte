<script>
	import auth0 from "./auth0";
	import _user from "./user";

	import { onMount } from "svelte";
	import LeftBar from "./Components/LeftBar.svelte";
	import Main from "./Components/Main.svelte";
	import RightBar from "./Components/RightBar.svelte";
	import ScreenLogin from './Components/ScreenLogin.svelte'
	import LoadingIndicator from "./Components/Misc/LoadingIndicator.svelte";
	import ScreenYourAnswers from "./Components/ScreenYourAnswers.svelte";
import ScreenSettings from "./Components/Misc/ScreenSettings.svelte";

	let tab = 0;
	let tabs_group = 0;
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

	const handleLeftBarClick = (n) => {
		tabs_group = 1;
		tab = n
	}

	const handleRightBarClick = (n) => {
		tabs_group = 0;
		tab = n;
	}
</script>

<div>
	{#if user != null && !isAuthenticating}
		<LeftBar
			logout={() => auth0.logout(auth0_client, window.location.origin)}
			click={(n) => handleLeftBarClick(n)}
		/>
		{#if tabs_group == 1}
			{#if tab == 0}
				<ScreenYourAnswers/>	
			{:else if tab == 1}
				<ScreenSettings/>
			{/if}
		{:else}
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
		{/if}
		<RightBar 
			click={(n) => handleRightBarClick(n)}
			hidden={user == null} 
			unselected={tabs_group!=0}
		/>
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

		font-family: 'Nunito';
	}
</style>

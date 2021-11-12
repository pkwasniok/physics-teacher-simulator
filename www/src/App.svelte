<script>
	import { onMount } from "svelte";

	import LeftBar from "./Components/LeftBar.svelte";
	import Main from "./Components/Main.svelte";
	import RightBar from "./Components/RightBar.svelte";
	import config from "./config";

	import createAuth0Client from "@auth0/auth0-spa-js";

	let tab = 0;
	let backend_server = "http://localhost:5000/";

	let auth0 = null;

	onMount(() => {
		console.log(config.auth0.domain);
	});
</script>

<div>
	<LeftBar />
	<Main {tab} {backend_server} />
	<RightBar bind:selection={tab} />
</div>

<style>
	div {
		width: 100%;
		height: 100%;

		display: grid;
		grid-template-columns: 15% auto 15%;
	}
</style>

<script>
	import LeftBar from "./Components/LeftBar.svelte";
	import Main from "./Components/Main.svelte";
	import RightBar from "./Components/RightBar.svelte";

	let tab = 2;
</script>

<div>
	<LeftBar />
	<Main {tab} />
	<RightBar bind:selection={tab} />
</div>

<style>
	div {
		width: 100%;
		height: 100%;

		display: grid;
		grid-template-columns: 15% auto 15%;

		background-image: url("../img/background.png");
	}
</style>

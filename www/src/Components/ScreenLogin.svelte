<script>
    import Button from "./Misc/Button.svelte";

    export let login;
</script>

<div>
    <Button on:click={login}>Login</Button>
</div>

<style>
    div {
        grid-column-start: 2;
        grid-column-end: 2;
    }
</style>

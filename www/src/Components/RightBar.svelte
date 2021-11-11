<script>
    import RightBarButton from "./RightBarButton.svelte";

    export let selection = 0;
</script>

<div>
    <RightBarButton on:click={() => (selection = 0)} selected={selection == 0}>
        Daily <br /> question
    </RightBarButton>

    <RightBarButton on:click={() => (selection = 1)} selected={selection == 1}>
        Review <br /> answers
    </RightBarButton>

    <RightBarButton on:click={() => (selection = 2)} selected={selection == 2}>
        Ranking
    </RightBarButton>

    <RightBarButton on:click={() => (selection = 3)} selected={selection == 3}>
        Add new <br /> question
    </RightBarButton>
</div>

<style>
    div {
        grid-column-start: 3;
        grid-column-end: 3;

        display: flex;
        flex-direction: column;
        align-items: right;
        justify-content: space-around;

        text-align: right;
    }
</style>

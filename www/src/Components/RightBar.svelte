<script>
    import RightBarButton from "./RightBarButton.svelte";

    export let selection = 0;
    export let hidden = false;
    export let click;
    export let unselected = false;

    const handleClick = (n) => {
        selection = n;
        click(n)
    }
</script>

<div>
    <span class={hidden ? "hidden" : ""}>
        <RightBarButton
            on:click={() => handleClick(0)}
            selected={selection == 0 && !unselected}
        >
            Daily <br /> question
        </RightBarButton>

        <RightBarButton
            on:click={() => handleClick(1)}
            selected={selection == 1 && !unselected}
        >
            Review <br /> answers
        </RightBarButton>

        <RightBarButton
            on:click={() =>  handleClick(2)}
            selected={selection == 2 && !unselected}
        >
            Ranking
        </RightBarButton>

        <!--<RightBarButton
            on:click={() => (selection = 3)}
            selected={selection == 3}
        >
            Add new <br /> question
        </RightBarButton>-->
    </span>
</div>

<style>
    div {
        grid-column-start: 3;
        grid-column-end: 3;

        display: flex;
        flex-direction: column;
        align-items: right;
        justify-content: space-evenly;

        text-align: right;

        transition: all 1s linear;
    }

    .hidden {
        position: absolute;
        transform: translateX(120%);
    }
</style>

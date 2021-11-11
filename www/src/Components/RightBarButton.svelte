<script>
    export let selected = false;
</script>

<button class={selected ? "selected" : ""} on:click>
    <slot />
</button>

<style>
    button {
        background: transparent;

        border: none;
        border-right: 0px white solid;

        font-size: 43px;
        text-align: right;
        color: white;
        font-family: "Nunito";

        transition: all 0.2s linear;
    }

    button:hover {
        border-width: 15px;
    }

    .selected {
        border-width: 8px;

        transition: all 0.1s linear;
    }
</style>

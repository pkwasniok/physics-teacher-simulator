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
        border-radius: 15px 0 0 15px;
        border-right: 0px white solid;

        font-size: 43px;
        text-align: right;
        color: white;
        font-family: "Nunito";

        transition: all 0.2s linear;

        cursor: pointer;
    }

    button:hover {
        border-width: 15px;
    }

    button:active {
        background-color: rgba(0, 0, 0, 0);
    }

    .selected {
        border-width: 8px;

        transition: all 0.1s linear;
    }
</style>

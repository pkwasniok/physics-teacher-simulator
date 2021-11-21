<script>
    export let fontSize = 21;
</script>

<button style="font-size: {fontSize}px;" on:click> <slot /> </button>

<style>
    button {
        background: transparent;

        padding: 3px;
        margin: 0;

        border: none;
        border-radius: 5px;

        color: white;

        outline: none;

        cursor: pointer;

        transition: 0.3s;
    }

    button:hover {
        background-color: rgba(255, 255, 255, 0.5);
    }
</style>

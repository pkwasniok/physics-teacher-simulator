<script>
    export let fontSize = 21;
    export let disabled = false;
    export let click

    const handleClick = () => {
        if(!disabled)
            click()
    }
</script>

<button style="font-size: {fontSize}px;" class={disabled ? "disabled" : ""} on:click={() => handleClick()}> <slot /> </button>

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

    .disabled {
        cursor: default;
        color: rgba(255,255,255,0.3)
    }

    .disabled:hover{
        background: transparent;
    }
</style>

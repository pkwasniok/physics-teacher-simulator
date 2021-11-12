<button on:click><slot /></button>

<style>
    button {
        color: white;
        font-family: "Nunito";
        font-size: 23px;

        background-color: transparent;

        border: 0;
        border-bottom: 0px solid white;
        border-radius: 7px 7px 0 0;

        margin: 0;
        padding: 3px;
        margin-top: 15px;

        transition: all 0.1s linear;

        cursor: pointer;
    }

    button:hover {
        margin-top: 7px;
        border-width: 8px;
    }

    button:active {
        background-color: rgba(255, 255, 255, 0.3);
    }
</style>

<script>
    import { fly, fade } from "svelte/transition";
    import GenericButton from "./GenericButton.svelte";

    export let submit;
    export let cancel;

    const handleClick = () => {};
</script>

<div id="background" transition:fade />
<div id="popup" transition:fly={{ y: 200, duration: 1500 }}>
    <span id="container-header">
        <h1>Are you sure you want to submit your answer?</h1>
        <h2>Answer can't be changed later</h2>
    </span>
    <span id="container-buttons">
        <GenericButton on:click={cancel}>Cancel</GenericButton>
        <GenericButton on:click={submit}>Submit</GenericButton>
    </span>
</div>

<style>
    #background {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);

        backdrop-filter: blur(3px);

        width: 100vw;
        height: 100vh;

        z-index: 2;

        background-color: rgba(255, 255, 255, 0.3);
    }
    #popup {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);

        padding: 15px;

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;

        background-color: rgba(14, 42, 71, 1);

        border: 3px solid white;
        border-radius: 5px;

        z-index: 3;
        backdrop-filter: none;

        -webkit-box-shadow: 3px 3px 10px 0px #000;
        -moz-box-shadow: 3px 3px 10px 0px #000;
        box-shadow: 3px 3px 10px 0px #000;
    }

    #container-header {
        width: 100%;

        text-align: center;
    }

    #container-buttons {
        width: 100%;

        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-evenly;
    }

    h1 {
        font-size: 23px;

        margin: 0;
        padding: 0;
    }

    h2 {
        font-size: 17px;
        color: #bfbfbf;

        padding: 0;
        margin: 0;
        margin-bottom: 15px;
    }
</style>

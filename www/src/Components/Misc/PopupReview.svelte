<script>
    import { fly, fade } from "svelte/transition";
    import GenericButton from "./GenericButton.svelte";

    export let submit;
    export let cancel;
    export let content;
    export let comment;
</script>

<div id="background" transition:fade />
<div id="popup" transition:fly={{ y: 200, duration: 1500 }}>
    <p>
        {content}
    </p>
    <textarea
        bind:value={comment}
        placeholder="You can leave comment here..."
    />
    <span class="control">
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

        z-index: 2;

        width: 100vw;
        height: 100vh;

        backdrop-filter: blur(3px);

        background-color: rgba(255, 255, 255, 0.3);
    }

    #popup {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);

        width: 50vw;
        height: 35vh;

        border: 3px solid white;
        border-radius: 5px;

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-evenly;

        z-index: 3;

        background-color: rgba(14, 42, 71, 1);

        -webkit-box-shadow: 3px 3px 10px 0px #000;
        -moz-box-shadow: 3px 3px 10px 0px #000;
        box-shadow: 3px 3px 10px 0px #000;
    }

    p {
        margin: 10px;
        padding: 0;

        text-align: center;
        font-size: 21px;
    }

    textarea {
        resize: none;

        width: 85%;
        height: 60%;

        color: white;

        border: 2px solid white;
        border-radius: 3px;

        outline: none;

        background-color: rgba(0, 0, 0, 0.6);
    }

    textarea::-webkit-scrollbar {
        width: 6px;

        padding: 2px;

        background: transparent;
    }

    textarea::-webkit-scrollbar-thumb {
        background-color: rgba(255, 255, 255, 0.3);

        border-radius: 5px;
    }

    span {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-around;

        width: 100%;
    }
</style>

<script>
    export let submit;
    export let cancel;
    export let content;
    export let comment;
</script>

<div>
    <p>
        {content}
    </p>
    <textarea
        bind:value={comment}
        placeholder="You can leave comment here..."
    />
    <span class="control">
        <button on:click={cancel}>Cancel</button>
        <button on:click={submit}>Submit</button>
    </span>
</div>

<style>
    div {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);

        width: 50%;
        height: 35%;

        border: 3px solid white;
        border-radius: 5px;

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-evenly;

        background-color: rgba(14, 42, 71, 1);

        -webkit-box-shadow: 3px 3px 10px 0px #000;
        -moz-box-shadow: 3px 3px 10px 0px #000;
        box-shadow: 3px 3px 10px 0px #000;
    }

    button {
        border: none;
        border-radius: 5px;

        background: transparent;

        color: white;
        font-size: 20px;

        margin: 0;
        padding: 5px;

        transition: all 0.15s linear;

        cursor: pointer;
    }

    button:hover {
        background-color: rgba(255, 255, 255, 0.9);
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

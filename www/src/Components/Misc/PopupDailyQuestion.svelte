<script>
    export let submit;
    export let cancel;
</script>

<div>
    <span id="container-header">
        <h1>Are you sure you want to submit your answer?</h1>
        <h2>Answer can't be changed later</h2>
    </span>
    <span id="container-buttons">
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

        padding: 15px;

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;

        background-color: rgba(14, 42, 71, 1);

        border: 3px solid white;
        border-radius: 5px;
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

<script>
    import Button from "./Misc/Button.svelte";
</script>

<div>
    <h2>Wyjaśnij pojęcie ruch oraz podaj kilka przykładów ruchu</h2>
    <h3>Kinematyka</h3>

    <textarea resizeable="none" placeholder="Type your answer here..." />
    <Button>Submit</Button>
</div>

<style>
    div {
        width: 100%;
        height: 100%;

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    textarea {
        background-color: rgba(0, 0, 0, 0.3);

        color: white;

        resize: none;
        width: 80%;
        height: 60%;

        outline: none;
        border-radius: 10px;
        border: 3px solid #afafaf;
    }

    textarea::placeholder {
        color: rgba(220, 220, 220, 0.8);
    }

    h2 {
        margin: 0;
        padding: 0;
    }

    h3 {
        margin: 0;
        padding: 0;
        margin-bottom: 20px;

        color: #bfbfbf;
        font-weight: 100;
    }
</style>

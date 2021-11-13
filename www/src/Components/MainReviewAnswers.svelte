<script>
    import LoadingIndicator from "./Misc/LoadingIndicator.svelte";

    export let backend_server;

    const fetchAnswers = (async () => {
        const response = fetch(backend_server + "answers");
        return (await response).json();
    })();
</script>

<div>
    {#await fetchAnswers}
        <LoadingIndicator />
    {:then answers}
        <span class="container">
            {#each answers.answers as answer}
                <span class="element">
                    <h4>Question: {answer.question}</h4>
                    <p>{answer.answer}</p>
                </span>
            {/each}
        </span>
    {/await}
</div>

<style>
    div {
        max-height: 900px;

        padding: 10px;

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;

        overflow-y: scroll;
    }

    .element {
        border: 3px solid white;

        padding: 5px;
        margin-top: 20px;
    }

    h4 {
        padding: 0;
        margin: 0;
    }

    p {
        padding: 0;
        margin: 0;

        overflow: visible;
    }
</style>

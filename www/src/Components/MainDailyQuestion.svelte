<script>
    import Button from "./Misc/Button.svelte";
    import LoadingIndicator from "./Misc/LoadingIndicator.svelte";

    export let backend_server;

    const fetchDailyQuestion = (async () => {
        const response = fetch(backend_server + "daily_question");
        return (await response).json();
    })();

    const postAnswer = (answer, question, email) => {
        let data = {
            question: question,
            answer: answer,
            email: email,
        };

        fetch(backend_server + "answer", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });
    };
</script>

<div>
    {#await fetchDailyQuestion}
        <LoadingIndicator />
    {:then daily_question}
        <h2>{daily_question.question}</h2>
        <h3>{daily_question.branch}</h3>
        <textarea resizeable="none" placeholder="Type your answer here..." />
        <Button
            on:click={() =>
                postAnswer(
                    "Essa",
                    daily_question.question,
                    "kwasniokpatryk@gmail.com"
                )}>Submit</Button
        >
    {/await}
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

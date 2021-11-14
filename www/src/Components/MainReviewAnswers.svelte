<script>
    import LoadingIndicator from "./Misc/LoadingIndicator.svelte";
    import MainReviewAnswersTab from "./Misc/MainReviewAnswersTab.svelte";

    export let backend_server;
    export let user;

    const fetchAnswers = (async () => {
        let response = fetch(backend_server + "answer/get?email=" + user.email);
        response = (await response).json();

        console.log(await response);
        return response;
    })();
</script>

<div id="container">
    {#await fetchAnswers}
        <LoadingIndicator />
    {:then answers}
        <div id="answers-container">
            {#each answers.answers as answer}
                <MainReviewAnswersTab {answer} {backend_server} />
            {/each}
        </div>
    {/await}
</div>

<style>
    #container {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);

        height: 100%;
        width: 70vw;

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
    }

    #answers-container {
        padding-right: 10px;

        overflow-y: scroll;
    }

    ::-webkit-scrollbar {
        width: 10px;

        background: transparent;
    }

    ::-webkit-scrollbar-thumb {
        background-color: #5d6f8177;

        border-radius: 10px;
    }
</style>

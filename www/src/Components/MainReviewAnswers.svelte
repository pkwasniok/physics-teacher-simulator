<script>
    import { onMount } from "svelte";

    import LoadingIndicator from "./Misc/LoadingIndicator.svelte";
    import MainReviewAnswersTab from "./Misc/MainReviewAnswersTab.svelte";

    export let backend_server;
    export let user;

    let answers = null;

    const fetchAnswers = async () => {
        let response = fetch(backend_server + "answer/get?email=" + user.email);
        response = (await response).json();
        return response;
    };

    const refetchData = async () => {
        answers = null;
        answers = await fetchAnswers();
    };

    onMount(async () => {
        answers = await fetchAnswers();
    });
</script>

<div id="container">
    {#if answers == null}}
        <LoadingIndicator />
    {:else}
        <div id="answers-container">
            {#each answers.answers as answer}
                <MainReviewAnswersTab
                    {answer}
                    {backend_server}
                    onSubmit={() => refetchData()}
                />
            {/each}
        </div>
    {/if}
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

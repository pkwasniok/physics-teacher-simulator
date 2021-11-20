<script>
    import { onMount } from "svelte";

    import api from "../api";
    import { _user } from "../user";
    import LoadingIndicator from "./Misc/LoadingIndicator.svelte";
    import MainReviewAnswersTab from "./Misc/MainReviewAnswersTab.svelte";

    let answers = null;

    let user = null;
    _user.subscribable.subscribe((value) => {
        user = value;
    });

    onMount(async () => {
        _user.reAuthorize();
        answers = await api.get("answer/get?email=" + user.email);
    });

    const handleTabSubmit = async () => {
        answers = null;
        answers = await api.get("answer/get?email=" + user.email);
    };
</script>

<div id="container">
    {#if answers == null}
        <LoadingIndicator />
    {:else}
        <div id="answers-container">
            {#each answers.answers as answer}
                <MainReviewAnswersTab
                    {answer}
                    onSubmit={async () => await handleTabSubmit()}
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

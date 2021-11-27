<script>
    import { onMount } from "svelte";

    import api from "../api";
    import _user from "../user";
    import LoadingIndicator from "./Misc/LoadingIndicator.svelte";
    import MainReviewAnswersTab from "./Misc/MainReviewAnswersTab.svelte";

    let answers = null;
    let separated = false;

    let user = null;
    _user.subscribable.subscribe((value) => {
        user = value;
    });

    onMount(async () => {
        _user.reAuthorize();
        answers = await api.get("answer/get?email=" + user.email);

        answers.answers = answers.answers.sort((a, b) => {
            if (b.reviewed && !a.reviewed) {
                return -1;
            } else if (a.reviewed && !b.reviewed) {
                return 1;
            } else {
                return 0;
            }
        });

        console.log(answers)
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
        {#if answers.answers.length > 0}
        <div id="answers-container">
            {#each answers.answers as answer}
                <MainReviewAnswersTab
                    {answer}
                    onSubmit={async () => await handleTabSubmit()}
                />
            {/each}
        </div>
        {:else}
            <h1>Here's empty :(</h1>
        {/if}
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

        scrollbar-width: 10px;
        scrollbar-base-color: transparent;
        scrollbar-color: #5d6f8177;
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

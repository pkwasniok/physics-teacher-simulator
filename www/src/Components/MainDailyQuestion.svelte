<script>
    import { onMount } from "svelte";

    import api from "../api";
    import { _user } from "../user";
    import Button from "./Misc/Button.svelte";
    import LoadingIndicator from "./Misc/LoadingIndicator.svelte";
    import PopupDailyQuestion from "./Misc/PopupDailyQuestion.svelte";

    let daily_question = null;
    let answer;
    let popup = false;

    let user = null;
    _user.subscribable.subscribe((value) => {
        user = value;
    });

    onMount(async () => {
        daily_question = await api.get("daily_question");
        _user.reAuthorize();
    });

    const handlePopupSubmit = async () => {
        popup = false;
        await api.post("answer/post", {
            email: user.email,
            question: daily_question.question,
            answer: answer,
        });
        _user.reAuthorize();
    };

    let timestamp = null;
    let seconds = 0,
        minutes = 0,
        hours = 0;
    const interval = setInterval(() => {
        timestamp = new Date(
            Date.parse("2021-11-21T08:00:00.000Z") - new Date().getTime()
        );
        seconds = timestamp.getSeconds();
        minutes = timestamp.getMinutes();
        hours = timestamp.getHours() - 2;
    }, 1000);
</script>

<div>
    {#if !user.daily_question_answered}
        {#if daily_question != null}
            <h2>{daily_question.question}</h2>
            <h3>{daily_question.branch}</h3>
            <textarea
                bind:value={answer}
                resizeable="none"
                placeholder="Type your answer here..."
            />
            <Button on:click={() => (popup = true)}>Submit</Button>
            {#if popup}
                <PopupDailyQuestion
                    cancel={() => (popup = false)}
                    submit={async () => await handlePopupSubmit()}
                />
            {/if}
        {:else}
            <LoadingIndicator />
        {/if}
    {:else}
        <h1>Your answer has been submitted!</h1>
        <h2>
            Next daily question will be available in {hours} h {minutes} m {seconds}
            s
        </h2>
    {/if}
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
        border: 3px solid white;
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

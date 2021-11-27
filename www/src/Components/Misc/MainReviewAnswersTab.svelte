<script>
    import api from "../../api";
    import _user from "../../user"
    import GenericButton from "./GenericButton.svelte";
    import PopupReview from "./PopupReview.svelte";

    import { fly } from "svelte/transition";

    export let answer;
    export let onSubmit;
    let expand = false;
    let stars = [false, false, false, false, false];
    const path_star_empty = "./img/star_empty.png";
    const path_star_filled = "./img/star_filled.png";
    let popup = false;
    let comment = "";

    //Set rate bare to user points when answer is reviewed
    if (answer.reviewed) {
        stars = stars.fill(true, 0, answer.points);
    }

    let user = null;
    _user.subscribable.subscribe((value) => {
        user = value
    })

    const formatDateTime = (datetime) => {
        let _datetime = new Date(Date.parse(datetime));

        return (
            _datetime.getDate() +
            "-" +
            (_datetime.getMonth() + 1) +
            "-" +
            _datetime.getFullYear() +
            " " +
            (_datetime.getHours() - 1) +
            ":" +
            _datetime.getMinutes()
        );
    };

    const handleStarClick = (index) => {
        if (!answer.reviewed) {
            stars = stars.fill(false);
            stars = stars.fill(true, 0, index + 1);
        }
    };

    const handleReviewSubmit = async () => {
        popup = false;

        const body = {
            answer_id: answer.id,
            email: user.email,
            points: stars.filter(Boolean).length,
            comment: comment,
        };

        await api.post("answer/review/post", body);

        onSubmit();
    };
</script>

<div class="answer" >
    <span class="answer-header" on:mousedown={() => (expand = !expand)}>
        <h2 class={answer.reviewed ? "" : "answer-unreviewed"}>
            Question: {answer.question}
        </h2>

        <h2>{formatDateTime(answer.time)}</h2>
    </span>
    <p class:hidden={expand}>{answer.answer}</p>
    <span class="answer-rating">
        <span class="answer-rating-stars">
            <img
                on:mousedown={() => handleStarClick(0)}
                src={stars[0] ? path_star_filled : path_star_empty}
                alt=""
                class={answer.reviewed ? "disabled" : ""}
            />
            <img
                on:mousedown={() => handleStarClick(1)}
                src={stars[1] ? path_star_filled : path_star_empty}
                alt=""
                class={answer.reviewed ? "disabled" : ""}
            />
            <img
                on:mousedown={() => handleStarClick(2)}
                src={stars[2] ? path_star_filled : path_star_empty}
                alt=""
                class={answer.reviewed ? "disabled" : ""}
            />
            <img
                on:mousedown={() => handleStarClick(3)}
                src={stars[3] ? path_star_filled : path_star_empty}
                alt=""
                class={answer.reviewed ? "disabled" : ""}
            />
            <img
                on:mousedown={() => handleStarClick(4)}
                src={stars[4] ? path_star_filled : path_star_empty}
                alt=""
                class={answer.reviewed ? "disabled" : ""}
            />
        </span>
        {#if !answer.reviewed}
            <GenericButton
                click={() => (popup = true)}
                disabled={!stars[0]}
                fontSize={17}
            >
                Submit review
            </GenericButton>
        {:else}
            <h2>Reviewed</h2>
        {/if}
    </span>
</div>
{#if popup}
    <PopupReview
        content={"Are you sure you want to submit your review?"}
        submit={() => handleReviewSubmit()}
        cancel={() => (popup = false)}
        bind:comment
    />
{/if}

<style>
    .answer {
        width: 70vw;

        border: 3px solid white;
        border-radius: 5px;

        background-color: rgba(0, 0, 0, 0.3);

        margin-bottom: 15px;
        margin-top: 15px;
        padding: 10px;
    }

    .answer-header {
        display: flex;
        flex-direction: row;
        justify-content: space-between;

        cursor: pointer;
    }

    .answer-unreviewed {
        border-left: 5px solid white;
        padding-left: 5px;
    }

    .hidden {
        max-height: 250px;
        transition: max-height 0.3s linear;
    }

    .answer-rating {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        width: 100%;

        margin-top: 15px;
        margin-bottom: 5px;
    }

    .answer-rating-stars {
        display: flex;
        flex-direction: row;
        align-items: center;
        width: fit-content;
    }

    img {
        width: 20px;
        aspect-ratio: 1;
        margin-left: 10px;

        cursor: pointer;

        user-select: none;
    }


    h2{
        margin: 0;
        padding: 0;

        font-size: 18px;
    }

    p {
        margin: 0;
        padding: 0;
        margin-top: 15px;

        overflow: hidden;
        max-height: 0;

        transition: all 0.7s linear;
    }
</style>

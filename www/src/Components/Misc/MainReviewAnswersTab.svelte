<script>
    export let answer;
    let expand = false;

    const formatDateTime = (datetime) => {
        let _datetime = new Date(datetime);

        return (
            _datetime.getDay() +
            "-" +
            _datetime.getMonth() +
            "-" +
            _datetime.getFullYear() +
            " " +
            _datetime.getHours() +
            ":" +
            _datetime.getMinutes()
        );
    };

    let stars = [false, false, false, false, false];
    let final = null;

    $: console.log(checkStar(0, stars, final));

    const checkStar = (star_index, stars, final) => {
        return final != null ? final[star_index] : stars[star_index];
    };

    const path_star_empty = "./img/star_empty.png";
    const path_star_filled = "./img/star_filled.png";
</script>

<div
    class="answer"
    on:mouseenter={() => (expand = true)}
    on:mouseleave={() => (expand = false)}
>
    <span class="answer-header">
        <h4>Question: {answer.question}</h4>
        <h4>{formatDateTime(answer.time)}</h4>
    </span>
    <p class:hidden={expand}>{answer.answer}</p>
    <span class="answer-rating">
        <span class="answer-rating-stars">
            <img
                on:mousedown={() => {
                    stars = stars.fill(false);
                    stars = stars.fill(true, 0, 1);
                }}
                src={stars[0] ? path_star_filled : path_star_empty}
                alt=""
            />
            <img
                on:mousedown={() => {
                    stars = stars.fill(false);
                    stars = stars.fill(true, 0, 2);
                }}
                src={stars[1] ? path_star_filled : path_star_empty}
                alt=""
            />
            <img
                on:mousedown={() => {
                    stars = stars.fill(false);
                    stars = stars.fill(true, 0, 3);
                }}
                src={stars[2] ? path_star_filled : path_star_empty}
                alt=""
            />
            <img
                on:mousedown={() => {
                    stars = stars.fill(false);
                    stars = stars.fill(true, 0, 4);
                }}
                src={stars[3] ? path_star_filled : path_star_empty}
                alt=""
            />
            <img
                on:mousedown={() => {
                    stars = stars.fill(false);
                    stars = stars.fill(true, 0, 5);
                }}
                src={stars[4] ? path_star_filled : path_star_empty}
                alt=""
            />
        </span>
        <button>Submit review</button>
    </span>
</div>

<style>
    .answer {
        width: 70vw;

        border: 3px solid white;
        border-radius: 5px;

        margin-bottom: 15px;
        margin-top: 15px;
        padding: 10px;
    }

    .answer-header {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    .hidden {
        max-height: 1000px;
        transition: max-height 0.3s linear;
        margin-top: 15px;
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

    button {
        margin: 0;
        padding: 0;
        padding: 3px;
        padding-left: 5px;
        padding-right: 3px;

        background: transparent;

        border: none;
        border-radius: 3px;

        color: white;
        font-size: 17px;

        cursor: pointer;
    }

    button:hover {
        background: rgba(255, 255, 255, 0.3);
    }

    img {
        width: 20px;
        aspect-ratio: 1;
        padding-left: 10px;

        cursor: pointer;
    }

    h4 {
        margin: 0;
        padding: 0;
    }

    p {
        margin: 0;
        padding: 0;

        overflow: hidden;
        max-height: 0;

        transition: all 0.4s ease-out;
    }
</style>

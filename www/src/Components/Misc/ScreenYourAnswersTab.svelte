<script>
    import { onMount } from "svelte";

    export let answer;

    let points = null;
    let expand = false;
    let comment_selector = 0;

    onMount(() => {
        answer.reviews.forEach(element => {
            points += element.points
        });
    })

    const handleHeaderClick = () => {
        expand = !expand;
    }

    const handleArrowClick = (direction) => {
        comment_selector += (direction ? 1 : -1)

        if(comment_selector >= answer.reviews.length){
            comment_selector = 0;
        }else if(comment_selector < 0){
            comment_selector = answer.reviews.length-1
        }
    }

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
</script>

<div class='tab'>
   <div class='header' on:click={() => handleHeaderClick()}>
       <h2>Q: {answer.question}</h2>
       <h2>{points} ⭐ | {formatDateTime(answer.time)}</h2>
   </div> 
   <div class='content-collapsible {expand ? '' : ' collapsed'}' >
        <div class='separator'>
            <span class='separator-text'>Answer</span>
            <span class='separator-line'/>
        </div>

        {answer.answer}

        <div class='separator'>
            <span class='separator-text'>Comments {comment_selector+1}/{answer.reviews.length}</span>
            <span class='separator-line'/>
        </div>

        <div class='comments'>
            <img src="./img/arrow-left.png" alt="" on:click={() => handleArrowClick(false)}/>
            <p>{answer.reviews[comment_selector].comment}</p>
            <img src="./img/arrow-right.png" alt="" on:click={() => handleArrowClick(true)}/>
        </div>
   </div>
</div>

<style>
    .tab{
        width: 100%;

        background-color: rgba(0, 0, 0, 0.3);

        border-radius: 5px;
        border: 3px solid white;

        padding: 10px;
        margin-top: 15px;
        margin-bottom: 15px;

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
    }

    .header{
        width: 100%;

        display: flex;
        flex-direction: row;
        align-items:center;
        justify-content:space-between;

        cursor: pointer;
    }

    .content-collapsible{
        width: 100%;

        max-height: 450px;

        overflow-y: hidden;

        transition: all 0.7s linear;
    }

    .collapsed{
        max-height:0;
    }

    .comments img{
        aspect-ratio: 1;
        width: 25px;
        margin: 5px;

        cursor: pointer;
    }

    .comments img:hover{
        filter:hue-rotate(180deg);
        filter:invert(50%);
    }

    p{
        margin: 0;
        padding: 0;
        margin-left: 10px;
        margin-right: 10px;

        text-align: left;
    }

    h2{
        margin: 0;
        padding: 0;
        
        font-size: 18px;
    }

    .separator{
        width: 100%;

        display:flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;

        margin-top: 15px;
        margin-bottom: 15px;

        font-weight: bold;
    }

    .separator-text{
        margin-right: 10px;
        white-space: nowrap;
        width:auto;
    }

    .separator-line{
        width: 100%;

        height: 1px;

        background-color: white;
    }

    .comments{
        width: 100%;

        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;

        margin-bottom: 10px;
    }
</style>

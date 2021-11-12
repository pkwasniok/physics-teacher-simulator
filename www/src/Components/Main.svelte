<script>
    import MainDailyQuestion from "./MainDailyQuestion.svelte";
    import MainRanking from "./MainRanking.svelte";
    import MainReviewAnswers from "./MainReviewAnswers.svelte";
    import MainAddNewQuestion from "./MainAddNewQuestion.svelte";

    export let tab = 0;
    export let backend_server;
    export let user;
</script>

<div>
    {#if tab == 0}
        <MainDailyQuestion {backend_server} {user} />
    {:else if tab == 1}
        <MainReviewAnswers {backend_server} />
    {:else if tab == 2}
        <MainRanking {backend_server} />
    {:else if tab == 3}
        <MainAddNewQuestion />
    {/if}
</div>

<style>
    div {
        grid-column-start: 2;
        grid-column-end: 2;

        color: white;
        font-family: "Nunito";
    }
</style>

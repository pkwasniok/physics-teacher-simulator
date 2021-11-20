<script>
    import MainDailyQuestion from "./MainDailyQuestion.svelte";
    import MainRanking from "./MainRanking.svelte";
    import MainReviewAnswers from "./MainReviewAnswers.svelte";
    import MainAddNewQuestion from "./MainAddNewQuestion.svelte";
    import MainWelcomeScreen from "../../Components/MainWelcomeScreen.svelte";

    export let tab = 0;

    export let handleLogin;
</script>

<div>
    {#if tab == 0}
        <MainDailyQuestion />
    {:else if tab == 1}
        <MainReviewAnswers />
    {:else if tab == 2}
        <MainRanking />
    {:else if tab == 3}
        <!--<MainAddNewQuestion />-->
    {:else if tab == 4}
        <MainWelcomeScreen login={handleLogin} />
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

<script>
    import { onMount } from "svelte";

    import _user from '../user'
    import api from '../api'
    
    import LoadingIndicator from "./Misc/LoadingIndicator.svelte";
    import ScreenYourAnswersTab from './Misc/ScreenYourAnswersTab.svelte'

    let answers = null;

    let user = null;
    _user.subscribable.subscribe((value) => {
        user = value;
    })

    onMount(async () => {
        await _user.reAuthorize()
        answers = await api.get('user/answers?email=' + user.email)
        console.log(answers)
    })
</script>

<div id="container">
    <h1>Your answers</h1>
    {#if answers != null}
        {#each answers.answers as answer}
            <ScreenYourAnswersTab {answer}/> 
        {/each}
    {:else}
        <LoadingIndicator/>
    {/if}
</div>

<style>
    #container{
        height: 100%;
        width: 100%;

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;

        color: white;
    }    
</style>
<script>
    import Button from "../src/Components/Misc/Button.svelte";

    export let login;
</script>

// TODO: Redo whole screen, because actual one sucks

<div>
    <h1>Welcom to physics teacher simulator!</h1>
    <p>
        At the beginning I would like to say hello and thank you to every
        fizyczny świr for visiting my website! This app was created for making
        learning more fun and competetive - you aren't learning only by
        answering some boring questions, besides that you can anonymously review
        ohers answers and let others review your answers! By reviewing and
        letting others review you answer, you can gain stars, which are part of
        competetive aspect of my app. More modes will be added in future.
    </p>
    <img
        src="https://ultimastatus.com/wp-content/uploads/2021/06/whenn-all-the-forces-physics-meme.jpg"
    />
    <p id="greetings">Live long and prosper!</p>
    <Button on:click={login}>Login</Button>
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

    #greetings {
        width: 100%;
        text-align: left;
    }
</style>

<script>
    import _user from "../user";
    import Button from "./Misc/Button.svelte";

    export let logout;
    export let click;

    let user = null;
    _user.subscribable.subscribe((value) => {
        user = value;
    });

    const handleClick = (n) => {
        click(n)
    }
</script>

<div>
    <h1>Physics⚛️ <br /> teacher <br /> simulator</h1>

    <span>
        {#if user != null}
            <img src={user.picture} alt="" />
            <Button on:click={() => handleClick(0)}>You answers</Button>
            <Button on:click={() => handleClick(1)}>Settings</Button>
            {#if user.superuser}
                <Button onpkwasniokpkwasniok:click={() => handleClick(2)}>Superuser</Button>
            {/if}
            <Button on:click={logout}>Logout</Button>
        {/if}
    </span>

    <h3>
        Made by:
        <a href="https://github.com/pkwasniok" target="blank"> pkwasniok </a>
    </h3>
</div>

<style>
    div {
        grid-column-start: 1;
        grid-column-end: 1;

        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: space-between;

        color: white;
        font-family: "Nunito";
    }

    img {
        border-radius: 50%;
    }

    h1 {
        width: 100%;

        margin: 0;
        padding: 0;
        margin-top: 4px;
        margin-left: 25px;

        color: white;
        font-size: 45px;
        font-weight: bold;

        cursor: default;
    }

    h3 {
        width: 100%;

        margin: 0;
        padding: 0;
        margin-left: 20px;
        margin-bottom: 8px;

        cursor: default;
    }

    span {
        height: 70%;

        margin-left: 18%;

        display: flex;
        flex-direction: column;
        align-items: center;
    }

    a {
        cursor: pointer;
    }
</style>

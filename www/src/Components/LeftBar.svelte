<script>
    import Button from "./Misc/Button.svelte";

    export let isAuthenticated;
    export let user;
    export let superuser;

    export let logout;
</script>

<div>
    <h1>Physics⚛️ <br /> teacher <br /> simulator</h1>

    <span>
        {#if isAuthenticated}
            <img src={user.picture} alt="" />
            <Button>You answers</Button>
            <Button>Settings</Button>
            {#if superuser}
                <Button>Superuser</Button>
            {/if}
        {/if}
        <Button hidden={!isAuthenticated} on:click={logout}>Logout</Button>
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

<script>
    import Button from "./Misc/Button.svelte";
</script>

<div>
    <h1>Physics⚛️ <br /> teacher <br /> simulator</h1>

    <span>
        <Button>Login</Button>
        <Button disabled={true}>Logout</Button>
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
        align-items: center;
        justify-content: space-between;

        color: white;
        font-family: "Nunito";
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
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    a {
        cursor: pointer;
    }
</style>

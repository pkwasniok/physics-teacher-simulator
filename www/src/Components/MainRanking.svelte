<script>
    import LoadingIndicator from "./Misc/LoadingIndicator.svelte";

    export let backend_server;

    const fetchUsers = (async () => {
        const response = fetch(backend_server + "user/ranking");
        return (await response).json();
    })();
</script>

<div>
    {#await fetchUsers}
        <LoadingIndicator />
    {:then users}
        <table>
            <tr>
                <th>Username</th>
                <th>Points</th>
            </tr>
            {#each users.response as user}
                <tr>
                    <th>{user.username}</th>
                    <th>{user.points}⭐</th>
                </tr>
            {/each}
        </table>
    {/await}
</div>

<style>
    div {
        width: 100%;
        height: 100%;

        display: flex;
        flex-direction: column;
        align-content: center;
        justify-content: center;
    }

    table,
    th,
    tr {
        border: 3px solid #afafaf;
        border-collapse: collapse;
    }
</style>

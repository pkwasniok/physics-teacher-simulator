<script>
    import { onMount } from "svelte";
    import { fly } from "svelte/transition";

    import api from "../api";
    import LoadingIndicator from "./Misc/LoadingIndicator.svelte";

    let ranking = null;
    onMount(async () => {
        ranking = await api.get("user/ranking");
    });
</script>

<div transition:fly={{ y: -200, duration: 800 }}>
    {#if ranking != null}
        <table>
            <tr>
                <th>Username</th>
                <th>Points</th>
            </tr>
            {#each ranking.ranking as user}
                <tr>
                    <th>{user.username}</th>
                    <th>{user.points}⭐</th>
                </tr>
            {/each}
        </table>
    {:else}
        <LoadingIndicator />
    {/if}
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

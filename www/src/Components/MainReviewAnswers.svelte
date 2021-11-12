<script>
    import LoadingIndicator from "./Misc/LoadingIndicator.svelte";

    export let backend_server;

    const fetchAnswers = (async () => {
        const response = fetch(backend_server + "answers");
        return (await response).json();
    })();
</script>

<div>
    {#await fetchAnswers}
        <LoadingIndicator />
    {:then answers}
        <table>
            <tr>
                <td>Username</td>
                <td>Question</td>
            </tr>
            {#each answers.answers as answer}
                <tr>
                    <td colspan="2">
                        <table>
                            <tr>
                                <td>{answer.username}</td>
                                <td>{answer.question}</td>
                                <td><button>More</button></td>
                            </tr>
                        </table>
                    </td>
                </tr>
            {/each}
        </table>
    {/await}
</div>

<style>
    div {
        height: 100%;
        width: 100%;

        display: flex;
        align-items: center;
        justify-content: center;
    }

    button {
        background: transparent;

        padding: 0;
        margin: 0;
        padding-left: 5px;
        margin-right: 5px;
        padding-right: 5px;

        color: white;

        border: none;
        border-radius: 0 5px 5px 0;
        border-left: 0px solid white;

        transition: all 0.1s linear;

        cursor: pointer;
    }

    button:hover {
        border-width: 5px;
        margin-right: 0;
    }

    button:active {
        background-color: rgba(255, 255, 255, 0.3);
    }

    table,
    tr,
    td {
        border: 2px solid white;
        border-collapse: collapse;
    }
</style>

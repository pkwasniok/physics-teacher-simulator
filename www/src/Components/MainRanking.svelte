<script>
    import { dataset_dev } from "svelte/internal";
    import App from "../App.svelte";

    const fetchUsers = async () => {
        const response = self.fetch("http://127.0.0.1:5000/users", {
            mode: "no-cors",
        });

        console.log(response);

        if (response.ok) {
            console.log(response);
            return response;
        }
    };
</script>

<div>
    {#await fetchUsers}
        <h3>Loading data...</h3>
    {:then users}
        {console.log(users)}
        <h2>{users}</h2>
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
    td {
        border: 3px solid #afafaf;
        border-collapse: collapse;
    }
</style>

<script>
    import { onMount } from "svelte";
    import _user from "../../user";
    import api from '../../api'
    import GenericButton from "./GenericButton.svelte";
    import LoadingIndicator from "./LoadingIndicator.svelte";

    let username = null;

    let user = null;
    _user.subscribable.subscribe((value) => {
        user = value;
    })

    onMount(async () => {
        username = user.username;
        await _user.reAuthorize();
    })

    const handleSaveButtonClick = async () => {
        await api.post('user/settings/username', {
            email: user.email,
            username: username
        })
        _user.reAuthorize()
    }
</script>

<div id='container'>
    <h1>Settings</h1>
    
    {#if user != null}
        <div class='tab'>
            <span class='tab-text'>Personal informations</span>
            <span class='tab-line'/>
        </div>
        
        <div class='settings'>
            Username: <input maxlength="12" bind:value={username} type="text"/>    <br/>
        </div>

        <GenericButton click={async () => await handleSaveButtonClick()}>Save all</GenericButton>
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

    .settings{
        width: 100%;
        
        text-align: left;
        font-size: 20px;
    }

    .settings input{
        width: 180px;

        color: white;
        text-align: center;

        background: transparent;
        
        outline: none;
        border: none;
        border-bottom: 2px solid white;

        padding: 1px;
        margin-bottom:2px;

        transition: all 0.11s linear;
    }

    .settings input:focus{
        border-bottom: 4px solid white;
        margin-bottom: 0;
    }

    .tab{
        width: 100%;

        display:flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;

        margin-top: 15px;
        margin-bottom: 15px;

        font-weight: bold;
    }

    .tab-text{
        margin-right: 10px;
        font-size: 21px;
        white-space: nowrap;
        width:auto;
    }

    .tab-line{
        width: 100%;

        height: 3px;

        background-color: white;

        border-radius: 3px;
    }
</style>
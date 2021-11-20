import config from "./config";
import createAuth0Client from "@auth0/auth0-spa-js";

const createClient = async () => {
    let auth0Client = await createAuth0Client({
        domain: config.auth0.domain,
        client_id: config.auth0.clientId
    })

    return auth0Client
}

const login = async (client, location_origin, handleAfterLogin) => {
    await client.loginWithPopup({
        redirect_uri: location_origin
    })

    handleAfterLogin(await client.getUser())
}

const logout = (client, location_origin) => {
    client.logout({
        returnTo: location_origin
    })
}

const auth0 = {
    createClient,
    login,
    logout
}

export default auth0;
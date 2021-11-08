let p_question = document.getElementById('question')
let p_branch = document.getElementById('branch')

let auth0 = null;

const fetchAuthConfig = () => fetch('./auth_config.json')

const configureClient = async () => {
    const response = await fetchAuthConfig()
    const config = await response.json()

    auth0 = await createAuth0Client({
        domain: config.domain,
        client_id: config.clientId
    })
}

const auth0_login = async () => {
    await auth0.loginWithRedirect({
        redirect_uri: window.location.origin
    })
}

const auth0_logout = async () => {
    auth0.logout({
        returnTo: window.location.origin
    })
}

const updateUi = async () => {
    const isAuthenticated = await auth0.isAuthenticated();
    document.getElementById('login').disabled = isAuthenticated;
    document.getElementById('logout').disabled = !isAuthenticated;

    if (isAuthenticated) {
        const user = await auth0.getUser()

        document.getElementById('user-img').innerHTML = "<img src=\"" + user.picture + "\">"
        document.getElementById('user-name').innerHTML = user.given_name

        console.log(user)
    }
}

window.onload = async () => {
    await configureClient();

    updateUi();

    const isAuthenticated = await auth0.isAuthenticated();
    if (isAuthenticated)
        return;

    const query = window.location.search;
    if (query.includes("code=") && query.includes("state=")) {
        // When user is authenticated
        await auth0.handleRedirectCallback();

        updateUi();

        window.history.replaceState({}, document.title, "/")
    }
}


fetch('http://127.0.0.1:5000/', { credentials: 'same-origin' }).then((response) => {
    return response.json()
}).then((data) => {
    console.log(data)
    p_question.innerHTML = data.question
    p_branch.innerHTML = data.branch
}).catch((error) => {
    console.error(error)
})
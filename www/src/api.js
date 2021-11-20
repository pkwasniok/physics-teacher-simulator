import config from "./config";

const get = async (endpoint) => {
    let response = await fetch(config.backend.ip + endpoint)
    response = await (response.json())

    if (response.status == 'OK') {
        return await response
    } else {
        console.log("API: " + response.status)
        return null
    }
}

const post = async (endpoint, body) => {
    await fetch(config.backend.ip + endpoint, {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json'
        }
    })

}

const api = {
    get,
    post
}

export default api
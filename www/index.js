item = document.getElementById('content');

fetch('http://127.0.0.1:5000/', { credentials: 'same-origin' }).then((response) => {
    return response.json()
}).then((data) => {
    console.log(data)
    item.innerHTML = data.question + ' (' + data.branch + ')'
}).catch((error) => {
    console.error(error)
})
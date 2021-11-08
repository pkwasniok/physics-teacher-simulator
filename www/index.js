p_question = document.getElementById('question')
p_branch = document.getElementById('branch')

fetch('http://127.0.0.1:5000/', { credentials: 'same-origin' }).then((response) => {
    return response.json()
}).then((data) => {
    console.log(data)
    p_question.innerHTML = data.question
    p_branch.innerHTML = data.branch
}).catch((error) => {
    console.error(error)
})
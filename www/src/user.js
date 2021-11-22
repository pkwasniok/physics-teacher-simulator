import api from './api'
import { writable } from 'svelte/store'

let subscribable = writable(null)

const authorize = async (user_auth0) => {
    let user_db = await api.get('user/auth?email=' + user_auth0.email)

    subscribable.set({
        email: user_auth0.email,
        username: user_db.user.username,
        picture: user_auth0.picture,
        superuser: user_db.user.superuser,
        daily_question_answered: user_db.user.daily_question_answered
    })
}

const reAuthorize = async () => {
    let user = null;
    subscribable.subscribe((value) => {
        user = value
    })

    let user_db = await api.get('user/auth?email=' + user.email)
    user_db = user_db.user

    subscribable.update(n =>
        n = {
            email: n.email,
            username: user_db.username,
            picture: n.picture,
            superuser: user_db.superuser,
            daily_question_answered: user_db.daily_question_answered
        }
    )
}

const _user = {
    subscribable,
    authorize,
    reAuthorize
}

export default _user;
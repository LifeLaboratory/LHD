const axios = require('axios')

export function registerUser (data) {
  return axios.post(`${process.env.VUE_APP_BACKEND}/api/user/register`, JSON.stringify(data),
    {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(function (response) {
      return response.data
    })
    .catch(function (error) {
      console.log(error)
      return false
    })
}

export function authUser (data) {
    return axios.post(`${process.env.VUE_APP_BACKEND}/api/user/login`, JSON.stringify(data),
        {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(function (response) {
            console.log(response.data)
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}

export function getPerson () {
    return axios.get(`${process.env.VUE_APP_BACKEND}/api/person`)
        .then(function (response) {
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}

export function getRating () {
    return axios.get(`${process.env.VUE_APP_BACKEND}/api/rating`)
        .then(function (response) {
            console.log(response)
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}

export function getProfile () {
    return axios.get(`${process.env.VUE_APP_BACKEND}/api/user/profile`,
        {
            headers: {
                session: localStorage.getItem('session')
            }
        })
        .then(function (response) {
            console.log(response)
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}

export function getProfileInfo (id_user) {
    return axios.get(`${process.env.VUE_APP_BACKEND}/api/user/` + id_user,
        {
            headers: {
                session: localStorage.getItem('session')
            }
        })
        .then(function (response) {
            console.log(response)
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}

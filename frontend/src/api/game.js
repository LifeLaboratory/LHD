const axios = require('axios')

export function getGame (session) {
  return axios.get(`${process.env.VUE_APP_BACKEND}/api/game`,
    {
      headers: {
        'Session': session
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

export function newGame (session, id) {
  return axios.post(`${process.env.VUE_APP_BACKEND}/api/game`,
    JSON.stringify( {"id_person": id} ),
    {
      headers: {
        'Session': session,
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

export function sendAnswer (session, ans) {
  return axios.post(`${process.env.VUE_APP_BACKEND}/api/game/question`,
    JSON.stringify( {"answer": ans} ),
    {
      headers: {
        'Session': session,
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

export function resumeGame (session) {
  return axios.get(`${process.env.VUE_APP_BACKEND}/api/game`,
    {
      headers: {
        'Session': session,
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
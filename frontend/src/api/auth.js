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

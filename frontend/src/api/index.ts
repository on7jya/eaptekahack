const axios = require('axios');


export const getCourses = () => {
    axios.get('http://127.0.0.1:8000/api/course', { headers: { "Access-Control-Allow-Origin": "*", 'Access-Control-Request-Method': 'GET' }, withCredentials: false })

        .then(function (response: any) {
            // handle success
            console.log(response);
        })
}
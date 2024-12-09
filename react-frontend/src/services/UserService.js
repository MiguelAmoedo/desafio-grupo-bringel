import axios from "axios";

const apiUrl = "https://localhost:5000";

console.log(apiUrl)
var usersServices = {
    getUser: async (id) => {
        const users = axios.get(`http://${apiUrl}/users/`);
        return await users;
    },
    getById: async (id) => {
        const users = axios.get(`http://${apiUrl}/users/` + id);
        return await users;
    },
    putUser: async (dados) => {
        const users = axios.put(`http://${apiUrl}/users/`, id);
        return await users;
    },
    createUser: async (dados) => {
        const users = axios.post(`http://${apiUrl}/users/login`, id);
        return await users;
    },

};

export default usersServices;
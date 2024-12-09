import axios from "axios";

const apiUrl = "https://localhost:5000";

console.log(apiUrl)
var materialsServices = {
    getMaterial: async (id) => {
        const materials = axios.get(`http://${apiUrl}/materials/`);
        return await materials;
    },
    getById: async (id) => {
        const materials = axios.get(`http://${apiUrl}/materials/` + id);
        return await materials;
    },
    putMaterial: async (dados) => {
        const materials = axios.put(`http://${apiUrl}/materials/`, id);
        return await materials;
    },
    createUser: async (dados) => {
        const materials = axios.post(`http://${apiUrl}/materials/login`, id);
        return await materials;
    },

};

export default materialsServices;
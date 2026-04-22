import axios from "axios";

const API = axios.create({
  baseURL: "https://inventory-management-production-2a9a.up.railway.app",
});

// 🔐 token auto attach
API.interceptors.request.use((req) => {
  const token = localStorage.getItem("token");
  if (token) {
    req.headers.Authorization = `Bearer ${token}`;
  }
  return req;
});

export default API;
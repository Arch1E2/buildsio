import { createApp } from "vue";
import App from "./App.vue";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import Axios from "axios";

Axios.defaults.headers.common = { 'X-Requested-With': 'XMLHttpRequest' }
Axios.defaults.baseURL = (process.env.API_PATH !== 'production') ? 'http://localhost:8000/' : '';

const app = createApp(App)

app.use(ElementPlus)
app.mount('#app')
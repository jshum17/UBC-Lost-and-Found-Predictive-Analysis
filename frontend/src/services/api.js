// src/services/api.js
import axios from 'axios';

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:5000/api',
    headers: {
        'Content-Type': 'application/json',
    },
});

export default {
    getSummary() {
        return apiClient.get('/summary');
    },
    getMonthlyTrend() {
        return apiClient.get('/monthly_trend');
    },
    getCount2024() {
        return apiClient.get('/count2024');
    },
    getCount2025() {
        return apiClient.get('/count2025');
    },
    getItems() {
        return apiClient.get('/lost_items');
    },
    getDailyForecast() {
        return apiClient.get('/forecast/daily');
    }
};
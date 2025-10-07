// API Client - Modern Fetch-based
const API_BASE = '';
let authToken = localStorage.getItem('nazanin_token');

class APIClient {
    constructor() {
        this.baseURL = API_BASE;
        this.token = authToken;
    }

    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        
        const config = {
            ...options,
            headers: {
                'Content-Type': 'application/json',
                ...options.headers,
            },
        };

        if (this.token) {
            config.headers['Authorization'] = `Bearer ${this.token}`;
        }

        if (options.body) {
            config.body = JSON.stringify(options.body);
        }

        try {
            const response = await fetch(url, config);
            
            if (!response.ok) {
                if (response.status === 401) {
                    // Unauthorized - redirect to login
                    this.logout();
                    throw new Error('Unauthorized');
                }
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    async get(endpoint, params = {}) {
        const queryString = new URLSearchParams(params).toString();
        const url = queryString ? `${endpoint}?${queryString}` : endpoint;
        return this.request(url);
    }

    async post(endpoint, body) {
        return this.request(endpoint, {
            method: 'POST',
            body,
        });
    }

    async put(endpoint, body) {
        return this.request(endpoint, {
            method: 'PUT',
            body,
        });
    }

    async delete(endpoint) {
        return this.request(endpoint, {
            method: 'DELETE',
        });
    }

    setToken(token) {
        this.token = token;
        localStorage.setItem('nazanin_token', token);
    }

    logout() {
        this.token = null;
        localStorage.removeItem('nazanin_token');
        window.location.href = '/login';
    }
}

const api = new APIClient();

// Auth methods
async function login(username, password) {
    try {
        const response = await api.post('/api/auth/login', { username, password });
        if (response.success) {
            api.setToken(response.token);
            return response;
        }
        throw new Error('Login failed');
    } catch (error) {
        console.error('Login error:', error);
        throw error;
    }
}

function logout() {
    api.logout();
}

// System methods
async function getSystemStatus() {
    return api.get('/api/status');
}

async function initializeSystem() {
    return api.post('/api/system/initialize');
}

async function startSystem() {
    return api.post('/api/system/start');
}

async function stopSystem() {
    return api.post('/api/system/stop');
}

async function getStats() {
    return api.get('/api/stats');
}

// Sheets methods
async function getSheetsData(spreadsheet, sheet) {
    return api.post('/api/sheets/get', { spreadsheet, sheet, operation: 'get' });
}

async function appendSheetRow(spreadsheet, sheet, row) {
    return api.post('/api/sheets/append', {
        spreadsheet,
        sheet,
        operation: 'append',
        data: { row }
    });
}

// Config methods
async function getConfig() {
    return api.get('/api/config');
}

async function updateConfig(section, key, value) {
    return api.post('/api/config/update', { section, key, value });
}

async function updateAPIKeys(provider, keys) {
    return api.post('/api/config/api-keys', { provider, keys });
}

// Content methods
async function generateContent(type, topic, platform = 'youtube', details = {}) {
    return api.post('/api/content/generate', { type, topic, platform, details });
}

async function getContentIdeas(platform = 'youtube', count = 10) {
    return api.get('/api/content/ideas', { platform, count });
}

// Analytics methods
async function getAnalyticsOverview() {
    return api.get('/api/analytics/overview');
}

async function getPerformanceData(days = 7) {
    return api.get('/api/analytics/performance', { days });
}

// Tasks methods
async function getTasks() {
    return api.get('/api/tasks');
}

async function createTask(title, description, priority = 'medium', deadline = null) {
    return api.post('/api/tasks/create', { title, description, priority, deadline });
}

// Logs methods
async function getLogs(limit = 100) {
    return api.get('/api/logs', { limit });
}

async function getSecurityLogs() {
    return api.get('/api/security/logs');
}

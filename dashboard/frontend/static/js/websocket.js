// WebSocket Client for Real-time Updates
class WebSocketClient {
    constructor(url) {
        this.url = url;
        this.ws = null;
        this.reconnectInterval = 5000;
        this.reconnectTimer = null;
        this.listeners = new Map();
        this.connected = false;
    }

    connect() {
        try {
            const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
            const host = window.location.host;
            this.ws = new WebSocket(`${protocol}//${host}/ws`);

            this.ws.onopen = () => {
                console.log('🔌 WebSocket connected');
                this.connected = true;
                this.updateIndicator('connected');
                this.emit('connected');
                
                // Clear reconnect timer
                if (this.reconnectTimer) {
                    clearTimeout(this.reconnectTimer);
                    this.reconnectTimer = null;
                }
            };

            this.ws.onmessage = (event) => {
                try {
                    const data = JSON.parse(event.data);
                    console.log('📨 WebSocket message:', data);
                    this.emit('message', data);
                    
                    // Handle specific message types
                    if (data.type) {
                        this.emit(data.type, data);
                    }
                } catch (error) {
                    console.error('Error parsing WebSocket message:', error);
                }
            };

            this.ws.onerror = (error) => {
                console.error('❌ WebSocket error:', error);
                this.connected = false;
                this.updateIndicator('error');
                this.emit('error', error);
            };

            this.ws.onclose = () => {
                console.log('🔌 WebSocket disconnected');
                this.connected = false;
                this.updateIndicator('disconnected');
                this.emit('disconnected');
                
                // Attempt to reconnect
                this.reconnectTimer = setTimeout(() => {
                    console.log('🔄 Attempting to reconnect...');
                    this.connect();
                }, this.reconnectInterval);
            };
        } catch (error) {
            console.error('Error connecting to WebSocket:', error);
        }
    }

    disconnect() {
        if (this.ws) {
            this.ws.close();
            this.ws = null;
        }
        if (this.reconnectTimer) {
            clearTimeout(this.reconnectTimer);
            this.reconnectTimer = null;
        }
    }

    send(data) {
        if (this.ws && this.ws.readyState === WebSocket.OPEN) {
            this.ws.send(JSON.stringify(data));
        } else {
            console.warn('WebSocket not connected');
        }
    }

    on(event, callback) {
        if (!this.listeners.has(event)) {
            this.listeners.set(event, []);
        }
        this.listeners.get(event).push(callback);
    }

    off(event, callback) {
        if (this.listeners.has(event)) {
            const callbacks = this.listeners.get(event);
            const index = callbacks.indexOf(callback);
            if (index > -1) {
                callbacks.splice(index, 1);
            }
        }
    }

    emit(event, data) {
        if (this.listeners.has(event)) {
            this.listeners.get(event).forEach(callback => {
                try {
                    callback(data);
                } catch (error) {
                    console.error(`Error in ${event} listener:`, error);
                }
            });
        }
    }

    updateIndicator(status) {
        const indicator = document.getElementById('ws-indicator');
        if (!indicator) return;

        indicator.className = 'ws-indicator ' + status;

        const statusTexts = {
            connected: 'Connected',
            disconnected: 'Disconnected',
            error: 'Error',
            connecting: 'Connecting...'
        };

        const span = indicator.querySelector('span');
        if (span) {
            span.textContent = statusTexts[status] || 'Unknown';
        }
    }
}

// Create global WebSocket instance
const ws = new WebSocketClient();

// Auto-connect on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        ws.connect();
    });
} else {
    ws.connect();
}

// Listen for live updates
ws.on('message', (data) => {
    // Update UI with real-time data
    if (data.organism_age !== undefined) {
        const ageElement = document.getElementById('organism-age');
        if (ageElement) {
            ageElement.textContent = data.organism_age;
        }
    }

    if (data.energy !== undefined) {
        const energyBar = document.getElementById('energy-bar');
        const energyValue = document.getElementById('energy-value');
        if (energyBar) {
            energyBar.style.width = `${data.energy}%`;
        }
        if (energyValue) {
            energyValue.textContent = `${Math.round(data.energy)}%`;
        }
    }
});

// Handle specific events
ws.on('system_initialized', () => {
    showNotification('System Ready', 'Nazanin initialized successfully', 'success');
});

ws.on('config_updated', (data) => {
    showNotification('Config Updated', `${data.section}.${data.key} updated`, 'info');
});

ws.on('sheet_updated', (data) => {
    showNotification('Sheet Updated', `${data.spreadsheet}/${data.sheet}`, 'info');
});

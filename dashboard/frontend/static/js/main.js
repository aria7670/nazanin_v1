// Main Dashboard JS - Core functionality
let systemStatus = null;
let statsRefreshInterval = null;

// ═══════════════════════════════════════════════════════════
// INITIALIZATION
// ═══════════════════════════════════════════════════════════

async function initializeDashboard() {
    console.log('🚀 Initializing Nazanin Dashboard...');
    
    // Hide loading screen after a delay
    setTimeout(() => {
        const loadingScreen = document.getElementById('loading-screen');
        if (loadingScreen) {
            loadingScreen.style.opacity = '0';
            setTimeout(() => {
                loadingScreen.style.display = 'none';
            }, 300);
        }
    }, 1000);

    // Setup event listeners
    setupEventListeners();
    
    // Load initial data
    await loadSystemStatus();
    
    // Start auto-refresh
    startAutoRefresh();
    
    console.log('✅ Dashboard initialized');
}

// ═══════════════════════════════════════════════════════════
// EVENT LISTENERS
// ═══════════════════════════════════════════════════════════

function setupEventListeners() {
    // Sidebar toggle
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');
    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', () => {
            sidebar.classList.toggle('collapsed');
        });
    }

    // Mobile menu toggle
    const mobileToggle = document.getElementById('mobile-menu-toggle');
    if (mobileToggle && sidebar) {
        mobileToggle.addEventListener('click', () => {
            sidebar.classList.toggle('active');
        });
    }

    // Theme toggle
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }

    // Fullscreen toggle
    const fullscreenBtn = document.getElementById('fullscreen-btn');
    if (fullscreenBtn) {
        fullscreenBtn.addEventListener('click', toggleFullscreen);
    }

    // Notifications
    const notificationBtn = document.getElementById('notification-btn');
    const notificationsPanel = document.getElementById('notifications-panel');
    if (notificationBtn && notificationsPanel) {
        notificationBtn.addEventListener('click', () => {
            notificationsPanel.classList.toggle('active');
        });
    }

    // Global search
    const globalSearch = document.getElementById('global-search');
    if (globalSearch) {
        globalSearch.addEventListener('input', handleGlobalSearch);
    }

    // Close panels on outside click
    document.addEventListener('click', (e) => {
        const notificationsPanel = document.getElementById('notifications-panel');
        const notificationBtn = document.getElementById('notification-btn');
        
        if (notificationsPanel && notificationBtn) {
            if (!notificationsPanel.contains(e.target) && !notificationBtn.contains(e.target)) {
                notificationsPanel.classList.remove('active');
            }
        }
    });
}

// ═══════════════════════════════════════════════════════════
// SYSTEM STATUS
// ═══════════════════════════════════════════════════════════

async function loadSystemStatus() {
    try {
        const status = await getSystemStatus();
        systemStatus = status;
        updateSystemStatusUI(status);
    } catch (error) {
        console.error('Error loading system status:', error);
        updateSystemStatusUI({
            initialized: false,
            running: false,
            message: 'Error loading status'
        });
    }
}

function updateSystemStatusUI(status) {
    const statusElement = document.getElementById('system-status');
    if (!statusElement) return;

    const indicator = statusElement.querySelector('.status-indicator');
    const text = statusElement.querySelector('span');

    if (status.running) {
        if (indicator) indicator.style.background = 'var(--color-success)';
        if (text) text.textContent = 'Running';
    } else if (status.initialized) {
        if (indicator) indicator.style.background = 'var(--color-warning)';
        if (text) text.textContent = 'Initialized';
    } else {
        if (indicator) indicator.style.background = 'var(--color-danger)';
        if (text) text.textContent = 'Stopped';
    }
}

// ═══════════════════════════════════════════════════════════
// AUTO REFRESH
// ═══════════════════════════════════════════════════════════

function startAutoRefresh() {
    if (statsRefreshInterval) {
        clearInterval(statsRefreshInterval);
    }
    
    statsRefreshInterval = setInterval(async () => {
        await loadSystemStatus();
    }, 30000); // Every 30 seconds
}

function stopAutoRefresh() {
    if (statsRefreshInterval) {
        clearInterval(statsRefreshInterval);
        statsRefreshInterval = null;
    }
}

// ═══════════════════════════════════════════════════════════
// THEME TOGGLE
// ═══════════════════════════════════════════════════════════

function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    const icon = document.querySelector('#theme-toggle i');
    if (icon) {
        icon.className = newTheme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
    }
}

// Load saved theme
function loadTheme() {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    
    const icon = document.querySelector('#theme-toggle i');
    if (icon) {
        icon.className = savedTheme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
    }
}

// ═══════════════════════════════════════════════════════════
// FULLSCREEN
// ═══════════════════════════════════════════════════════════

function toggleFullscreen() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
}

// ═══════════════════════════════════════════════════════════
// NOTIFICATIONS
// ═══════════════════════════════════════════════════════════

function showNotification(title, message, type = 'info') {
    // Create notification toast
    const toast = document.createElement('div');
    toast.className = `notification-toast ${type}`;
    toast.innerHTML = `
        <div class="toast-icon">
            <i class="fas fa-${getNotificationIcon(type)}"></i>
        </div>
        <div class="toast-content">
            <h4>${title}</h4>
            <p>${message}</p>
        </div>
        <button class="toast-close" onclick="this.parentElement.remove()">
            <i class="fas fa-times"></i>
        </button>
    `;
    
    // Add to page
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        document.body.appendChild(container);
    }
    
    container.appendChild(toast);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
    }, 5000);
}

function getNotificationIcon(type) {
    const icons = {
        success: 'check-circle',
        error: 'exclamation-circle',
        warning: 'exclamation-triangle',
        info: 'info-circle'
    };
    return icons[type] || 'info-circle';
}

function closeNotifications() {
    const panel = document.getElementById('notifications-panel');
    if (panel) {
        panel.classList.remove('active');
    }
}

// ═══════════════════════════════════════════════════════════
// GLOBAL SEARCH
// ═══════════════════════════════════════════════════════════

function handleGlobalSearch(e) {
    const query = e.target.value.toLowerCase();
    console.log('Search:', query);
    
    // Implement search functionality
    // This could search through:
    // - Nav items
    // - Recent activities
    // - Settings
    // - Content
}

// ═══════════════════════════════════════════════════════════
// UTILITY FUNCTIONS
// ═══════════════════════════════════════════════════════════

function formatNumber(num) {
    if (num >= 1000000) {
        return (num / 1000000).toFixed(1) + 'M';
    }
    if (num >= 1000) {
        return (num / 1000).toFixed(1) + 'K';
    }
    return num.toString();
}

function formatDate(date) {
    const d = new Date(date);
    return d.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

function formatTime(date) {
    const d = new Date(date);
    return d.toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit'
    });
}

function formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('Copied', 'Text copied to clipboard', 'success');
    }).catch(() => {
        showNotification('Error', 'Failed to copy', 'error');
    });
}

// ═══════════════════════════════════════════════════════════
// INIT ON LOAD
// ═══════════════════════════════════════════════════════════

// Load theme on startup
loadTheme();

// Cleanup on unload
window.addEventListener('beforeunload', () => {
    stopAutoRefresh();
    if (window.ws) {
        ws.disconnect();
    }
});

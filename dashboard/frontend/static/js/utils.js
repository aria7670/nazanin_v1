// Utility Functions
const utils = {
    formatNumber(num) {
        if (num >= 1000000) return (num / 1000000).toFixed(1) + 'M';
        if (num >= 1000) return (num / 1000).toFixed(1) + 'K';
        return num.toString();
    },
    
    formatDate(date) {
        const d = new Date(date);
        return d.toLocaleDateString();
    },
    
    formatTime(date) {
        const d = new Date(date);
        return d.toLocaleTimeString();
    },
    
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    copy(text) {
        navigator.clipboard.writeText(text).then(() => {
            showNotification('Copied', 'Text copied to clipboard', 'success');
        });
    }
};

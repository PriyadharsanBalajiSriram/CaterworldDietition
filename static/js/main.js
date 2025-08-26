// Real-time BMI Calculator
function calculateBMI() {
    const height = document.getElementById('height');
    const weight = document.getElementById('weight');
    
    if (height && weight && height.value && weight.value) {
        fetch('/api/calculate_bmi', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                height: parseFloat(height.value),
                weight: parseFloat(weight.value)
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                const bmiDisplay = document.getElementById('bmi-display');
                bmiDisplay.innerHTML = `
                    <div class="d-flex justify-content-between align-items-center">
                        <span><strong>BMI: ${data.bmi}</strong></span>
                        <span class="badge ${getBMIBadgeClass(data.bmi)} fs-6">${data.category}</span>
                    </div>
                `;
                bmiDisplay.className = `alert ${getBMIAlertClass(data.bmi)} text-center`;
            }
        })
        .catch(error => {
            console.error('BMI calculation error:', error);
            const bmiDisplay = document.getElementById('bmi-display');
            bmiDisplay.innerHTML = '<i class="fas fa-exclamation-triangle text-warning me-2"></i>Error calculating BMI';
            bmiDisplay.className = 'alert alert-warning text-center';
        });
    }
}

function getBMIAlertClass(bmi) {
    if (bmi < 18.5) return 'alert-warning';
    if (bmi >= 18.5 && bmi < 25) return 'alert-success';
    if (bmi >= 25 && bmi < 30) return 'alert-warning';
    return 'alert-danger';
}

function getBMIBadgeClass(bmi) {
    if (bmi < 18.5) return 'bg-warning';
    if (bmi >= 18.5 && bmi < 25) return 'bg-success';
    if (bmi >= 25 && bmi < 30) return 'bg-warning';
    return 'bg-danger';
}

// Form submission handling
document.addEventListener('DOMContentLoaded', function() {
    const heightInput = document.getElementById('height');
    const weightInput = document.getElementById('weight');
    const form = document.getElementById('dietForm');
    
    // Add real-time BMI calculation
    if (heightInput && weightInput) {
        heightInput.addEventListener('input', debounce(calculateBMI, 500));
        weightInput.addEventListener('input', debounce(calculateBMI, 500));
    }
    
    // Handle form submission
    if (form) {
        form.addEventListener('submit', function(e) {
            const submitBtn = document.getElementById('submitBtn');
            const submitText = document.getElementById('submitText');
            const loadingText = document.getElementById('loadingText');
            
            if (submitBtn && submitText && loadingText) {
                submitText.style.display = 'none';
                loadingText.style.display = 'inline';
                submitBtn.disabled = true;
            }
            
            // Show progress indicator
            showProgressIndicator();
        });
    }
    
    // Format diet plan content
    formatDietPlans();
});

// Debounce function for better performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Show progress indicator during form processing
function showProgressIndicator() {
    const progressHtml = `
        <div id="progress-indicator" class="text-center mt-3">
            <div class="progress mb-2">
                <div class="progress-bar progress-bar-striped progress-bar-animated bg-success" 
                     role="progressbar" style="width: 0%"></div>
            </div>
            <small class="text-muted">Processing your request...</small>
        </div>
    `;
    
    const form = document.getElementById('dietForm');
    if (form) {
        form.insertAdjacentHTML('afterend', progressHtml);
        
        // Animate progress bar
        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 10;
            if (progress > 90) progress = 90;
            
            const progressBar = document.querySelector('#progress-indicator .progress-bar');
            if (progressBar) {
                progressBar.style.width = progress + '%';
            }
            
            if (progress >= 90) {
                clearInterval(interval);
            }
        }, 500);
    }
}

// Format diet plan content for better readability
function formatDietPlans() {
    const dietContents = document.querySelectorAll('.diet-plan-content');
    
    dietContents.forEach(content => {
        let html = content.innerHTML;
        
        // Convert markdown-style headers to HTML
        html = html.replace(/^### (.*$)/gm, '<h4 class="text-success mt-3 mb-2">$1</h4>');
        html = html.replace(/^## (.*$)/gm, '<h3 class="text-success mt-4 mb-3">$1</h3>');
        html = html.replace(/^# (.*$)/gm, '<h2 class="text-success mt-4 mb-3">$1</h2>');
        
        // Convert bold text
        html = html.replace(/\*\*(.*?)\*\*/g, '<strong class="text-primary">$1</strong>');
        
        // Convert bullet points
        html = html.replace(/^- (.*$)/gm, '<li>$1</li>');
        html = html.replace(/(<li>.*<\/li>)/s, '<ul class="ms-3">$1</ul>');
        
        // Convert numbered lists
        html = html.replace(/^(\d+\.) (.*$)/gm, '<li>$2</li>');
        
        content.innerHTML = html;
    });
}

# AI Dietitian App

A smart Flask web application that uses LLM agents to create personalized diet plans based on user health data, dietary preferences, and restrictions.

## Features

- **BMI Calculation**: Automatic BMI calculation and health category assessment
- **AI-Powered Diet Plans**: Uses Google's Gemini AI for intelligent meal planning
- **Dual-Agent System**: Initial plan generation + reflection/improvement agent
- **Personalized Recommendations**: Considers allergies, preferences, and health goals
- **Modern Web Interface**: Responsive design with real-time BMI calculation
- **Plan Export**: Download and print diet plans

## Getting Started

### Prerequisites
- Python 3.8+
- Google Gemini API key

### Installation

Clone the repository:































How to Run the AI Dietitian App
Here's a complete step-by-step guide to get the app running:

Prerequisites
Python 3.8 or higher

Google Gemini API key (free tier available)

Step-by-Step Setup
1. Create Project Directory
bash
mkdir ai-dietitian
cd ai-dietitian
2. Create All Files
Create the folder structure and copy all the code files I provided:

bash
# Create directories
mkdir models services templates static static/css static/js data data/generated_plans

# Create empty files
touch app.py requirements.txt .env README.md
touch models/__init__.py models/state.py
touch services/__init__.py services/bmi_calculator.py services/dietitian_agent.py services/reflection_agent.py
touch templates/base.html templates/index.html templates/form.html templates/results.html
touch static/css/styles.css static/js/main.js
3. Install Dependencies
bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install requirements
pip install Flask==2.3.3 python-dotenv==1.0.0 google-generativeai==0.3.0 Werkzeug==2.3.7
4. Get Google Gemini API Key
Go to Google AI Studio

Sign in with your Google account

Click "Create API Key"

Copy the generated API key

Configure Environment Variables
Create .env file with:

text
GEMINI_API_KEY=your_actual_gemini_api_key_here
SECRET_KEY=your_secret_key_for_flask_sessions
 Copy All Code Files
Copy all the code I provided into their respective files:

Copy the app.py content

Copy all template files (base.html, index.html, form.html, results.html)

Copy the CSS and JavaScript files

Copy all the service files

 Run the Application
bash
python app.py
You should see output like:

text
 * Running on http://127.0.0.1:5000
 * Debug mode: on
 Open in Browser
Open your web browser and go to: http://localhost:5000


File Structure Check:
text
ai-dietitian/
├── app.py                    ✓ Main Flask app
├── requirements.txt          ✓ Dependencies
├── .env                     ✓ API keys
├── models/
│   ├── __init__.py          ✓ Empty file
│   └── state.py             ✓ State class
├── services/
│   ├── __init__.py          ✓ Empty file
│   ├── bmi_calculator.py    ✓ BMI functions
│   ├── dietitian_agent.py   ✓ AI diet agent
│   └── reflection_agent.py  ✓ AI reflection agent
├── templates/
│   ├── base.html            ✓ Base template
│   ├── index.html           ✓ Home page
│   ├── form.html            ✓ Input form
│   └── results.html         ✓ Results page
├── static/
│   ├── css/
│   │   └── styles.css       ✓ Styling
│   └── js/
│       └── main.js          ✓ JavaScript
└── data/

    └── generated_plans/     ✓ Saved plans folder




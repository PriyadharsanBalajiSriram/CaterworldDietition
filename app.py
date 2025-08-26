from flask import Flask, render_template, request, jsonify, session
import os
from dotenv import load_dotenv
import json
from datetime import datetime

from models.state import State
from services.bmi_calculator import calculate_bmi, get_bmi_category, create_state_from_user_input
from services.reflection_agent import ReflectionAgent
from services.dietition_agent import DietitianAgent

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Initialize agents
dietitian_agent = DietitianAgent()
reflection_agent = ReflectionAgent()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process_form():
    try:
        # Extract user inputs from form
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        allergies = request.form['allergies'].strip()
        preferences = request.form['preferences'].strip()
        
        # Create initial state from user inputs (with calculated BMI)
        state: State = create_state_from_user_input(
            height_cm=height,
            weight_kg=weight,
            allergies=allergies,
            preferences=preferences
        )
        
        # Generate initial diet plan (fills result_initial)
        state = dietitian_agent.process_state(state)
        
        # Generate reflected/improved plan (fills result_reflected)
        state = reflection_agent.process_state(state)
        
        # Calculate BMI category for display
        bmi_category = get_bmi_category(state['BMI'])
        
        # Save to session
        session['diet_plan'] = dict(state)  # Convert to dict for JSON serialization
        session['bmi_category'] = bmi_category
        
        # Save to file
        save_diet_plan(state)
        
        return render_template('results.html', 
                             state=state, 
                             bmi_category=bmi_category)
        
    except ValueError as ve:
        return f"Input error: {str(ve)}", 400
    except Exception as e:
        return f"Error processing form: {str(e)}", 500

@app.route('/api/calculate_bmi', methods=['POST'])
def api_calculate_bmi():
    """API endpoint for real-time BMI calculation"""
    try:
        data = request.get_json()
        height = float(data['height'])
        weight = float(data['weight'])
        
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        return jsonify({
            'bmi': bmi,
            'category': category,
            'status': 'success'
        })
    except (ValueError, KeyError) as e:
        return jsonify({'error': f'Invalid input: {str(e)}', 'status': 'error'}), 400
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 500

@app.route('/results')
def view_results():
    """View saved results from session"""
    if 'diet_plan' not in session:
        return redirect(url_for('form'))
    
    state = session['diet_plan']
    bmi_category = session.get('bmi_category', 'Unknown')
    
    return render_template('results.html', 
                         state=state, 
                         bmi_category=bmi_category)

def save_diet_plan(state: State):
    """Save the generated diet plan to file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"diet_plan_{timestamp}.json"
    
    os.makedirs('data/generated_plans', exist_ok=True)
    
    # Convert state to dict for JSON serialization
    plan_data = {
        **dict(state),
        'generated_at': timestamp,
        'bmi_category': get_bmi_category(state['BMI'])
    }
    
    with open(f'data/generated_plans/{filename}', 'w', encoding='utf-8') as f:
        json.dump(plan_data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True)

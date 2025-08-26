from models.state import State

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """Calculate BMI from weight and height."""
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 2)

def get_bmi_category(bmi: float) -> str:
    """Get BMI category based on value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def create_state_from_user_input(height_cm: float, weight_kg: float, 
                                allergies: str, preferences: str) -> State:
    """Create State object from user inputs with calculated BMI."""
    bmi = calculate_bmi(weight_kg, height_cm)
    
    state: State = {
        'BMI': bmi,
        'Height_in_cm': height_cm,
        'Weight_in_kg': weight_kg,
        'Allergic_stuff': allergies,
        'preferences': preferences,
        'result_initial': '',  # To be filled by dietitian agent
        'result_reflected': ''  # To be filled by reflection agent
    }
    
    return state

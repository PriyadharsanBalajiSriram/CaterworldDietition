import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

from models.state import State

class DietitianAgent:
    def __init__(self):
        #genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        ChatGoogleGenerativeAI.configure(api_key=os.getenv('GEMINI_API_KEY'))
        #self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.model=ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    
    def generate_initial_diet_plan(self, state: State) -> str:
        """Generate initial diet plan and update state.result_initial."""
        prompt = f"""
        As an expert dietitian, create a personalized diet plan for a person with the following details:
        
        - BMI: {state['BMI']} 
        - Height: {state['Height_in_cm']} cm
        - Weight: {state['Weight_in_kg']} kg
        - Allergies/Restrictions: {state['Allergic_stuff'] if state['Allergic_stuff'] else 'None'}
        - Dietary Preferences & Goals: {state['preferences']}
        
        Please provide:
        1. A detailed daily meal plan (breakfast, lunch, dinner, snacks)
        2. Nutritional recommendations based on BMI
        3. Portion size suggestions
        4. Health tips specific to their BMI range
        5. Foods to avoid based on allergies
        6. Calorie recommendations
        
        Format the response in clear sections with proper headings.
        Make it practical and easy to follow.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating diet plan: {str(e)}"
    
    def process_state(self, state: State) -> State:
        """Process state and fill result_initial."""
        state['result_initial'] = self.generate_initial_diet_plan(state)
        return state

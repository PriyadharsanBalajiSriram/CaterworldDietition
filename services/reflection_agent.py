import os
import google.generativeai as genai
from models.state import State
import ChatGoogleGenerativeAI

class ReflectionAgent:
    def __init__(self):
        ChatGoogleGenerativeAI.configure(api_key=os.getenv('GEMINI_API_KEY'))
        #genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        #self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.model=ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    
    def generate_reflected_plan(self, state: State) -> str:
        """Generate improved diet plan based on initial plan and user data."""
        prompt = f"""
        Review and enhance the following diet plan to make it more comprehensive and actionable:
        
        ORIGINAL DIET PLAN:
        {state['result_initial']}
        
        USER PROFILE:
        - BMI: {state['BMI']}
        - Height: {state['Height_in_cm']} cm
        - Weight: {state['Weight_in_kg']} kg
        - Allergies: {state['Allergic_stuff'] if state['Allergic_stuff'] else 'None'}
        - Preferences: {state['preferences']}
        
        Please enhance the plan by:
        1. Adding specific meal timing recommendations
        2. Including detailed hydration guidelines
        3. Suggesting weekly meal prep strategies
        4. Adding complementary exercise recommendations
        5. Providing alternative food options for variety
        6. Including shopping list suggestions
        7. Adding progress tracking tips
        8. Addressing any gaps in the original plan
        
        Make the enhanced plan more detailed, actionable, and user-friendly.
        Focus on long-term sustainability and practical implementation.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error in reflection: {str(e)}"
    
    def process_state(self, state: State) -> State:
        """Process state and fill result_reflected."""
        if not state['result_initial']:
            raise ValueError("result_initial must be populated before reflection")
        
        state['result_reflected'] = self.generate_reflected_plan(state)
        return state

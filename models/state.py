from typing import TypedDict

class State(TypedDict):
    BMI: float
    Height_in_cm: float
    Weight_in_kg: float
    Allergic_stuff: str
    preferences: str
    result_initial: str
    result_reflected: str

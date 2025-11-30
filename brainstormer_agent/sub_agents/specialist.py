from brainstormer_agent.config import get_model, SMART_MODEL_NAME

class SpecialistAgent:
    def __init__(self):
        self.model = get_model(SMART_MODEL_NAME)
        
    def run(self, method: str, context: str, problem: str) -> str:
        """
        Generates brainstorming ideas using the selected method and context.
        """
        
        method_instructions = {
            "SCAMPER": "Apply the SCAMPER method (Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, Reverse) to generate innovative ideas.",
            "Six Thinking Hats": "Apply the Six Thinking Hats method. Generate ideas/perspectives for each hat: White (Facts), Red (Emotions), Black (Cautions), Yellow (Benefits), Green (Creativity), Blue (Process).",
            "Reverse Brainstorming": "Apply Reverse Brainstorming. First, identify how to cause the problem or make it worse. Then, reverse those ideas to find solutions.",
            "Starbursting": "Apply Starbursting. Generate questions starting with Who, What, Where, When, Why, and How to explore the idea thoroughly."
        }
        
        instruction = method_instructions.get(method, "Generate creative ideas to solve the problem.")
        
        prompt = f"""
        You are a Creative Specialist.
        
        Problem: "{problem}"
        Context: "{context}"
        Method: "{method}"
        
        Instructions:
        {instruction}
        
        Output structured, clear, and actionable ideas.
        """
        
        response = self.model.generate_content(prompt)
        return response.text

from brainstormer_agent.config import get_model, SMART_MODEL_NAME
from pydantic import BaseModel

class MethodDecision(BaseModel):
    method: str
    reasoning: str

class FacilitatorAgent:
    def __init__(self):
        self.model = get_model(SMART_MODEL_NAME)
        
    def run(self, problem: str, context: str) -> MethodDecision:
        """
        Analyzes the problem and context to select the best brainstorming method.
        """
        prompt = f"""
        You are a Facilitator for a brainstorming session.
        
        Problem: "{problem}"
        Context: "{context}"
        
        Select ONE best brainstorming method from this list:
        1. SCAMPER (For product innovation, modification, or improvement)
        2. Six Thinking Hats (For comprehensive team analysis and looking at a decision from multiple perspectives)
        3. Reverse Brainstorming (For problem-solving, risk analysis, and identifying potential failures)
        4. Starbursting (For asking the right questions and exploring a new idea thoroughly)
        
        Return the response in JSON format with keys "method" and "reasoning".
        The "method" should be exactly one of: "SCAMPER", "Six Thinking Hats", "Reverse Brainstorming", "Starbursting".
        """
        
        # Using structured output for reliability if available, otherwise parsing JSON
        # For simplicity in this implementation, we'll ask for JSON and parse it.
        # Ideally, we would use response_schema if supported by the SDK version/model.
        
        response = self.model.generate_content(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        
        import json
        try:
            data = json.loads(response.text)
            return MethodDecision(method=data.get("method", "SCAMPER"), reasoning=data.get("reasoning", ""))
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails
            return MethodDecision(method="SCAMPER", reasoning="Defaulting to SCAMPER due to parsing error.")

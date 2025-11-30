from brainstormer_agent.config import get_model, FAST_MODEL_NAME
from brainstormer_agent.tools import web_search_tool

class ResearcherAgent:
    def __init__(self):
        self.model = get_model(FAST_MODEL_NAME)
        
    def run(self, topic: str) -> str:
        """
        Generates a search query, performs search, and summarizes findings.
        """
        # Step 1: Generate Search Query
        prompt_query = f"""
        You are a research assistant. Given the user topic: "{topic}",
        generate a single, effective search query to understand market trends, 
        user pain points, or relevant context. 
        Output ONLY the search query.
        """
        response_query = self.model.generate_content(prompt_query)
        search_query = response_query.text.strip()
        
        # Step 2: Perform Search
        search_results = web_search_tool(search_query)
        
        # Step 3: Summarize Findings
        prompt_summary = f"""
        You are a research analyst. 
        User Topic: "{topic}"
        Search Results:
        {search_results}
        
        Summarize these findings into a concise "Context Brief". 
        Focus on key trends, facts, and insights relevant to brainstorming ideas for the topic.
        """
        response_summary = self.model.generate_content(prompt_summary)
        return response_summary.text

from brainstormer_agent.sub_agents.researcher import ResearcherAgent
from brainstormer_agent.sub_agents.facilitator import FacilitatorAgent
from brainstormer_agent.sub_agents.specialist import SpecialistAgent
from brainstormer_agent.tools import save_brainstorm_to_file

class InteractiveBrainstormerAgent:
    def __init__(self):
        self.researcher_agent = ResearcherAgent()
        self.facilitator_agent = FacilitatorAgent()
        self.specialist_agent = SpecialistAgent()
        
    def run(self, user_input: str):
        print("Thinking... Gathering context...")
        context_brief = self.researcher_agent.run(user_input)
        
        print(f"Context found: {context_brief[:100]}...")
        
        print("Deciding on best brainstorming strategy...")
        method_decision = self.facilitator_agent.run(
            problem=user_input, 
            context=context_brief
        )
        print(f"Selected Method: {method_decision.method}")
        print(f"Reasoning: {method_decision.reasoning}")
        
        print("Brainstorming in progress...")
        ideas = self.specialist_agent.run(
            method=method_decision.method,
            context=context_brief,
            problem=user_input
        )
        
        return ideas, method_decision.method

if __name__ == "__main__":
    agent = InteractiveBrainstormerAgent()
    user_problem = input("Enter your problem statement: ")
    ideas, method = agent.run(user_problem)
    
    print("\n--- Brainstorming Results ---\n")
    print(ideas)
    
    save_choice = input("\nDo you want to save this to a file? (y/n): ")
    if save_choice.lower() == 'y':
        filename = input("Enter filename (default: brainstorm.md): ") or "brainstorm.md"
        result = save_brainstorm_to_file(f"# Brainstorming Session: {method}\n\n## Problem\n{user_problem}\n\n## Ideas\n{ideas}", filename)
        print(result)

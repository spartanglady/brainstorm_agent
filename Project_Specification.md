# Project Specification: The Gemini Brainstorming Orchestrator

## 1\. Project Overview

We are building a **Multi-Agent System** using the **Google Agent Development Kit (ADK)** logic. The system acts as an intelligent creative partner. Instead of a user simply selecting a brainstorming template, the system analyzes the user's problem, researches context from the web, selects the optimal brainstorming framework (e.g., SCAMPER, Six Thinking Hats), and generates structured ideas.

**Key Requirements:**

  * **Stack:** Python 3.11+, Google Gemini API (1.5 Pro & Flash), Google ADK patterns.
  * **Architecture:** Hierarchical Multi-Agent System (Orchestrator + Sub-Agents).
  * **Key Feature:** Tool Use (Web Search) for grounding ideas in reality.

## 2\. Directory Structure


```text
brainstormer_agent/          # Main Package
├── __init__.py
├── agent.py                 # The Main Orchestrator (Entry Point)
├── config.py                # Model configurations and API keys
├── tools.py                 # Custom tools (Search, File I/O)
└── sub_agents/              # Specialized Worker Agents
    ├── __init__.py
    ├── facilitator.py       # Decides the strategy (The Manager)
    ├── researcher.py        # Gathers context (The Analyst)
    └── specialist.py        # Generates ideas (The Creative)
tests/
├── test_agent.py            # Integration tests
requirements.txt             # Dependencies
README.md                    # Documentation
```

## 3\. Component Specifications

### A. Configuration (`config.py`)

  * **Models:** Define two model configurations.
      * `FAST_MODEL`: `gemini-1.5-flash-002` (For research and categorization tasks).
      * `SMART_MODEL`: `gemini-1.5-pro-002` (For the Orchestrator and complex ideation).
  * **Environment:** Load `GOOGLE_API_KEY` from environment variables.

### B. The Tools (`tools.py`)

Implement the following two functions as tools compatible with the ADK/Gemini function calling:

1.  **`web_search_tool(query: str) -> str`**:
      * *Purpose:* Performs a search (using `googlesearch-python` or `duckduckgo-search`) to get real-world context on the topic.
      * *Returns:* A string summary of the top 3 search results.
2.  **`save_brainstorm_to_file(content: str, filename: str) -> str`**:
      * *Purpose:* Saves the final brainstorming session to a local Markdown file.
      * *Returns:* Success message with file path.

### C. Sub-Agent 1: The Researcher (`sub_agents/researcher.py`)

  * **Role:** Context Gatherer.
  * **Tools:** Access to `web_search_tool`.
  * **Behavior:**
      * Receives a user topic (e.g., "How to sell more artisanal soap").
      * Generates a search query to understand market trends or user pain points.
      * Summarizes the findings into a "Context Brief."

### D. Sub-Agent 2: The Facilitator (`sub_agents/facilitator.py`)

  * **Role:** Strategist / Router.
  * **Tools:** None (Pure reasoning).
  * **Behavior:**
      * Analyzes the User Input + Researcher's Context Brief.
      * Selects **one** best brainstorming method from this list:
        1.  **SCAMPER** (For product innovation).
        2.  **Six Thinking Hats** (For comprehensive team analysis).
        3.  **Reverse Brainstorming** (For problem-solving/risk analysis).
        4.  **Starbursting** (For asking the right questions).
      * **Output:** Returns the selected method name and a short reasoning string.

### E. Sub-Agent 3: The Specialist (`sub_agents/specialist.py`)

  * **Role:** The Executor.
  * **Tools:** None.
  * **Behavior:**
      * Takes the *Method* (from Facilitator), *Context* (from Researcher), and *User Problem*.
      * Generates the actual brainstorming output.
      * **Prompting:** Must have distinct system instructions for each of the 4 methods supported by the Facilitator.

### F. The Orchestrator (`agent.py`)

  * **Class Name:** `InteractiveBrainstormerAgent`
  * **Flow:**
    1.  **Input:** User provides a problem statement.
    2.  **Step 1 (Research):** Call `researcher_agent` to get context.
    3.  **Step 2 (Plan):** Call `facilitator_agent` to pick the method.
    4.  **Step 3 (Execute):** Call `specialist_agent` to generate ideas using the Research + Method.
    5.  **Step 4 (Feedback Loop):** Present result to user. Ask: "Do you want to refine this or save it?"
    6.  **Step 5 (Action):** If save, call `save_brainstorm_to_file`.

## 4\. Operational Flow (Pseudocode)

*Use this logic to structure the `run()` method in `agent.py`*

```python
def run(self, user_input):
    print("Thinking... Gathering context...")
    context_brief = self.researcher_agent.run(user_input)
    
    print(f"Context found: {context_brief[:50]}...")
    
    print("Deciding on best brainstorming strategy...")
    method_decision = self.facilitator_agent.run(
        problem=user_input, 
        context=context_brief
    )
    print(f"Selected Method: {method_decision.method}")
    
    print("Brainstorming in progress...")
    ideas = self.specialist_agent.run(
        method=method_decision.method,
        context=context_brief,
        problem=user_input
    )
    
    return ideas
```
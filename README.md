# Gemini Brainstorming Orchestrator

An intelligent Multi-Agent System that acts as a creative partner for brainstorming. It uses Google Gemini models to research context, select the best brainstorming framework, and generate structured ideas.

## Features

-   **Multi-Agent Architecture**:
    -   **Researcher**: Gathers real-world context using web search.
    -   **Facilitator**: Selects the optimal brainstorming method (SCAMPER, Six Hats, etc.).
    -   **Specialist**: Generates creative ideas based on the method and context.
-   **Tool Integration**: Uses Google Search for grounding and File I/O for saving results.
-   **Interactive CLI**: Simple command-line interface for user interaction.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure Environment**:
    Create a `.env` file in the root directory and add your Google API Key:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

## Usage

Run the agent:

```bash
python -m brainstormer_agent.agent
```

Follow the prompts to enter your problem statement. The agent will research, plan, and generate ideas. You can then save the results to a Markdown file.

## Project Structure

-   `brainstormer_agent/`: Main package.
    -   `agent.py`: Entry point (Orchestrator).
    -   `sub_agents/`: Worker agents (Researcher, Facilitator, Specialist).
    -   `tools.py`: Custom tools.
    -   `config.py`: Configuration.
-   `tests/`: Unit/Integration tests.

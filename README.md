# Research Agent Project

This project implements a multi-agent system using the Google Agent Development Kit (ADK) to perform web research, cross-check the findings, and synthesize a final answer.

## Overview

The system consists of three main agents orchestrated by a root sequential agent:

1.  **Web Research Agent (`webresearch_agent`):**
    *   Takes a research question as input.
    *   Uses the `google_search` tool to find relevant information online.
    *   Constructs an initial answer based on the search results, citing sources.
    *   *(Optionally uses the `memorize` tool to store findings for the next agent).*

2.  **Cross-Check Agent (`crosscheck_agent`):**
    *   Receives the research question and the answer from the Web Research Agent (potentially via memory/state).
    *   Uses the `google_search` tool to independently verify the factual claims made in the answer.
    *   Provides a verdict (Correct, Incorrect, Unverifiable, Misleading) for each claim with justifications and citations.
    *   Gives an overall assessment of the answer's accuracy.
    *   *(Optionally uses the `memorize` tool to store the verification report).*

3.  **Final Synthesizer Agent (`final_synthesizer_agent`):**
    *   Takes the original question, the initial answer, and the cross-check report (potentially via memory/state).
    *   Synthesizes a polished, factually reliable final answer for the user, incorporating the feedback from the Cross-Check Agent.

## Project Structure

```
ResearchAgent/
├── __init__.py             # Makes ResearchAgent a Python package
├── .env                    # Stores API keys and environment variables (needs to be created)
├── agent.py                # Defines the root SequentialAgent and the final synthesizer agent
├── memory.py               # Contains memory tools (e.g., memorize) for state management
├── prompt.py               # Contains the prompt for the final synthesizer agent
├── README.md               # This file
├── Test_Eval.evalset.json  # Example evaluation set (if used)
│
├── crosscheckagent/
│   ├── __init__.py         # Makes crosscheckagent a sub-package
│   ├── agent.py            # Defines the Cross-Check Agent
│   └── prompt.py           # Contains the prompt for the Cross-Check Agent
│
└── webresearch/
    ├── __init__.py         # Makes webresearch a sub-package
    ├── agent.py            # Defines the Web Research Agent
    └── prompt.py           # Contains the prompt for the Web Research Agent
```

## Setup

1.  **Clone the repository (if applicable).**
2.  **Install dependencies:**
    *   It's recommended to use a virtual environment:
        ```bash
        # Navigate to the directory containing the ResearchAgent folder
        python -m venv .venv
        source .venv/bin/activate # On Windows use `.venv\Scripts\activate`
        ```
    *   Install the required packages (including ADK):
        ```bash
        # Ensure your virtual environment is active
        pip install google-adk google-search-results # Add other dependencies if needed

        # Or install with evaluation extras if you plan to run evaluations:
        # pip install "google-adk[eval]" google-search-results
        ```
3.  **API Keys:**
    *   This project uses Google Search via the `google_search` tool, which likely requires API keys (e.g., SerpApi API Key). The Gemini models might also require an API key.
    *   Create a `.env` file in the `ResearchAgent` directory (alongside `agent.py`).
    *   Add your API keys to the `.env` file. For example:
        ```dotenv
        # ResearchAgent/.env file
        SERPAPI_API_KEY=your_serpapi_api_key_here
        GEMINI_API_KEY=your_gemini_api_key_here
        ```
    *   *(Note: Ensure the specific environment variable names match what the `google_search` tool or the underlying model expects. Check the ADK documentation or tool implementation if unsure.)*

## Running the Agent

1.  **Navigate to the parent directory** containing the `ResearchAgent` folder in your terminal (e.g., `ResearchAgent_GoogleADK`).
2.  **Ensure your virtual environment is activated** (e.g., `source .venv/bin/activate`).
3.  **Run the ADK web server:**
    ```bash
    adk web
    ```
4.  **Access the web UI:** Open your browser and go to `http://localhost:8000` (or the address provided by the `adk web` command).
5.  Select the `ResearchAgent` application from the UI.
6.  Enter your research question and run the agent sequence.

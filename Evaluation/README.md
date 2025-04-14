# Evaluation Datasets for ResearchAgent

This directory contains evaluation datasets (`.evalset.json` files) used for testing and evaluating the `ResearchAgent` application.

## Creating Evaluation Datasets

Evaluation datasets define test scenarios, including input questions and expected outcomes or criteria for success. There are two primary ways to create these datasets:

1.  **Manual Creation (Recommended):**
    *   You can create or edit `.evalset.json` files directly using a text editor.
    *   This method provides full control over the structure and content of your evaluation scenarios.
    *   Refer to the Google Agent Development Kit (ADK) documentation for the specific JSON schema and required fields for evaluation sets.
    *   The `Test_Eval.evalset.json` file in this directory serves as an example.

2.  **Using the ADK Web UI:**
    *   The ADK web interface (`adk web`) provides tools to create and manage evaluation datasets through a graphical interface.
    *   Run `adk web` in your terminal (from the directory containing `ResearchAgent`).
    *   Navigate to the evaluation section in the web UI (usually accessible at `http://localhost:8000`).
    *   You can create new datasets, add test cases, and define evaluation criteria through the UI. Datasets created via the UI are typically saved within the project structure.

Choose the method that best suits your workflow and the complexity of your evaluation needs. Manual creation is often preferred for precise control and versioning, while the UI can be convenient for quick additions or exploration.

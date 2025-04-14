from google.adk import Agent
from google.adk.agents import SequentialAgent
from .crosscheckagent.agent import crosscheck_agent
from .webresearch.agent import webresearch_agent
from . import prompt
# Agent responsible for synthesizing the final answer
final_synthesizer_agent = Agent(
    model='gemini-2.0-flash', # Or choose another appropriate model
    name='final_synthesizer_agent',
    instruction=prompt.FINAL_ANSWER_SYNTHESIZER_PROMPT,
    # No tools needed for synthesis based on prior agent outputs
)

# The root sequential agent orchestrates the process
root_agent = SequentialAgent(
    name='Research_and_Verification_Agent',
    # No instruction needed for the orchestrator itself
    sub_agents=[
        webresearch_agent,      # Step 1: Research
        crosscheck_agent,       # Step 2: Verify
        final_synthesizer_agent # Step 3: Synthesize Final Answer
    ]
)

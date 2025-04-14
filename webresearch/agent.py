from google.adk import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse
from google.adk.tools import google_search
from google.genai import types
from . import prompt


webresearch_agent = Agent(
    model='gemini-2.0-flash',
    name='webresearch_agent',
    instruction=prompt.WEB_RESEARCH_AGENT_PROMPT,
    tools=[google_search],
    #after_model_callback=_render_reference,
)
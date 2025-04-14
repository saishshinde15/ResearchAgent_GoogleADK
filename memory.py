## Note that this is not needed as the agents have built in memory.But for long run / long memory , this is a good approach.

"""The 'memorize' tool for agents to affect session states."""

from google.adk.tools import ToolContext

# Note: This function will be registered as a tool in the agent definition.
def memorize(key: str, value: str, tool_context: ToolContext):
    """
    Memorize pieces of information, one key-value pair at a time.
    Use this to store results or context for later agents in the sequence.

    Args:
        key: the label (string) indexing the memory to store the value.
             Use descriptive keys like 'research_findings' or 'verification_report'.
        value: the information (string) to be stored.
        tool_context: The ADK tool context, providing access to session state.

    Returns:
        A status message confirming the storage.
    """
    # Access the session state dictionary via tool_context
    mem_dict = tool_context.state
    mem_dict[key] = value
    print(f"[Memory Tool] Stored key='{key}'") # Added print for debugging
    return {"status": f'Successfully stored information under key "{key}".'}

# If needed later, other functions like memorize_list or forget can be added here
# following the same pattern.

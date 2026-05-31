#!/usr/bin/env python
"""
Module 08-05: Human Approval Tool – Human‑in‑the‑Loop (HITL) for Sensitive Operations

Some actions (sending emails, deleting files, transferring money) require human approval.
LangGraph's `interrupt_before` provides native support for this pattern.
"""

from langgraph.graph import StateGraph, END
from langgraph.checkpoint import MemorySaver
from typing import TypedDict, Optional

# ------------------------------------------------------------
# 1. Define state
# ------------------------------------------------------------
class ApprovalState(TypedDict):
    messages: list
    action_approved: Optional[bool]
    action_details: dict

# ------------------------------------------------------------
# 2. Node: propose an action (e.g., send email)
# ------------------------------------------------------------
def propose_action(state: ApprovalState) -> dict:
    # In a real agent, this would come from an LLM decision.
    action = {
        "type": "email_send",
        "to": "ceo@company.com",
        "subject": "Q4 Report",
        "body": "Attached is the Q4 report."
    }
    return {"action_details": action}

# ------------------------------------------------------------
# 3. Node: human approval (will be interrupted)
# ------------------------------------------------------------
def request_approval(state: ApprovalState) -> dict:
    """This node will be interrupted. The user resumes with approval."""
    from langgraph.types import interrupt
    # interrupt() pauses the graph and returns user input when resumed.
    user_decision = interrupt({
        "type": "approval_request",
        "action": state["action_details"],
        "message": "Please approve or reject the action (yes/no):"
    })
    approved = user_decision.strip().lower() == "yes"
    return {"action_approved": approved}

# ------------------------------------------------------------
# 4. Node: execute the approved action
# ------------------------------------------------------------
def execute_action(state: ApprovalState) -> dict:
    if state.get("action_approved"):
        # Actually perform the action (e.g., send email)
        result = f"Action executed: {state['action_details']}"
    else:
        result = "Action rejected by human."
    return {"messages": [("assistant", result)]}

# ------------------------------------------------------------
# 5. Build graph with interrupt_before on the approval node
# ------------------------------------------------------------
builder = StateGraph(ApprovalState)
builder.add_node("propose", propose_action)
builder.add_node("approve", request_approval)
builder.add_node("execute", execute_action)

builder.set_entry_point("propose")
builder.add_edge("propose", "approve")
builder.add_edge("approve", "execute")
builder.add_edge("execute", END)

checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer, interrupt_before=["approve"])

# ------------------------------------------------------------
# 6. Run and simulate human intervention
# ------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("Human‑in‑the‑Loop (HITL) Tool Approval")
    print("=" * 60)

    config = {"configurable": {"thread_id": "session-1"}}

    # Start the graph – it will stop at the "approve" node
    print("Starting workflow...")
    for event in graph.stream({}, config):
        print(event)

    # Get current state and show interruption point
    state = graph.get_state(config)
    print(f"\nPaused before node: {state.next}")

    # Simulate human input: approve
    print("\n👤 Human approves action...")
    graph.update_state(config, {"action_approved": True}, as_node="approve")

    # Resume execution
    print("\nResuming...")
    for event in graph.stream(None, config):
        print(event)

    print("\nWorkflow completed with approval.")
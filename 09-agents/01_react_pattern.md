
---

## `09-agents/01_react_pattern.md`

```markdown
# The ReAct Pattern (Reasoning + Acting)

The ReAct pattern, introduced by Yao et al. (2022), is the foundation of modern AI agents. It interleaves **reasoning** (thinking) and **acting** (using tools) in a loop.

## The Loop

For each step, the agent outputs:

1. **Thought**: Internal reasoning about what to do next.
2. **Action**: Which tool to call, and with what arguments.
3. **Observation**: The result of the tool call.

The loop repeats until the agent has enough information to produce a **Final Answer**.

## Example

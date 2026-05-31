#!/usr/bin/env python
"""
Module 08-04: Structured Tools – Using Pydantic for Complex Inputs

For tools with many arguments or complex validation, define a Pydantic model
and pass it as `args_schema`. This gives the LLM a precise schema and enables
automatic validation.
"""

from langchain.tools import StructuredTool
from pydantic import BaseModel, Field
from typing import List, Optional

# ------------------------------------------------------------
# 1. Define a Pydantic model for the tool's input
# ------------------------------------------------------------
class SendEmailInput(BaseModel):
    to: str = Field(description="Recipient email address")
    subject: str = Field(description="Email subject line")
    body: str = Field(description="Email body content")
    cc: Optional[List[str]] = Field(default=None, description="CC recipients")

# ------------------------------------------------------------
# 2. Define the actual function that sends an email (simulated)
# ------------------------------------------------------------
def send_email(to: str, subject: str, body: str, cc: Optional[List[str]] = None) -> str:
    """Simulate sending an email."""
    cc_text = f", CC: {cc}" if cc else ""
    return f"Email sent to {to}{cc_text} with subject '{subject}'"

# ------------------------------------------------------------
# 3. Create a StructuredTool using the schema
# ------------------------------------------------------------
email_tool = StructuredTool.from_function(
    func=send_email,
    name="send_email",
    description="Send an email. Use this when the user asks to send a message.",
    args_schema=SendEmailInput,
)

# ------------------------------------------------------------
# 4. Inspect and test the tool
# ------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("StructuredTool with Pydantic Schema")
    print("=" * 60)

    print(f"Tool name: {email_tool.name}")
    print(f"Description: {email_tool.description}")
    print(f"Input schema: {email_tool.args}")
    print()

    # Invoke with proper arguments
    result = email_tool.invoke({
        "to": "alice@example.com",
        "subject": "Hello",
        "body": "This is a test email.",
        "cc": ["bob@example.com"]
    })
    print("Invocation result:", result)

    # Invalid input (missing required field) – would raise validation error
    try:
        email_tool.invoke({"to": "alice@example.com"})
    except Exception as e:
        print("\nValidation error (as expected):", e)
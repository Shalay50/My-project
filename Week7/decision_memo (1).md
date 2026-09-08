# Decision Memo

### 1. What did planning buy over ReAct?
- **Failures caught upfront:** `validate_plan` intercepted structural errors, missing tool definitions (`tool_not_found`), and invalid parameters before executing any actions.
- **ReAct comparison:** In a traditional ReAct loop, the agent would execute blindly, waste steps, incur environment errors, and trigger real-world side effects iteratively. Planning prevents this overhead.

### 2. What did it cost?
- **Token and Resource Cost:** Multi-round planning significantly increases token consumption (scaling up to a 3x multiplier when increasing maximum version capacity).
- **Adaptivity Trade-off:** While it allows self-correction, a high budget leads to wasted compute when trapped in unresolvable loops.

### 3. Where did reflection help, and where did it not? *(High Weight)*
- **Where it helped:** Reflection successfully guided minor plan adjustments and parameter corrections across iterative versions.
- **Where it failed (G4 test):** On G4, reflection was completely ineffective because no amount of re-planning can invent a tool that does not exist in the environment, causing the agent to exhaust its entire budget on a structural wall.

### 4. What did the detectors catch that the critic missed? *(High Weight)*
- **Goal Drift on G1:** The specialized detectors caught instances of **goal drift** (where a plan dropped an original requirement while attempting to fix another), whereas the standard LLM-based critic overlooked it and mistakenly approved flawed revisions.

### 5. Where does your agent still trust something it should not?
- The agent inherently trusts the model-generated feedback loop, especially when the same LLM acts as both the planner and the critic, creating shared blind spots rather than relying on truly independent verification.

### 6. What did this lab not tell you?
- The evaluation relied strictly on four goals written by one person, evaluated by one model, with only one run each—leaving **no variance estimate**. Additionally, using the same underlying model for both planning and critique compromises the independence of the check.

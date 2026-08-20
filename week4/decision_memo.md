# Part 10 — Decision Memo Answers

### 1. What did you build, and which control caught which failure?
- We built a guarded AI agent system powered by Qwen/Qwen2.5-1.5B-Instruct featuring multi-layered programmatic validation controls. 
- Gate 2 (args_model) catches schema and structural formatting mismatches.
- Gate 3 (KNOWN_ORDER_IDS) catches fabricated, non-existent, or unauthorized identifiers.
- Gate 4 (coheres) catches business logic and threshold breaches.
- Gate 5 catches final answers that lack supporting evidence in the execution trace.

### 2. Which failure did no control catch, and why not?
- Implicit prompt injections inside unstructured data bodies can evade basic programmatic controls if the model fails before reaching tool execution. 
- The primary systemic breakdown was structural formatting failure (stop: malformed) rather than semantic bypass.

### 3. What would you add first, and why that first?
- We would add a robust output parsing, repair wrapper, or constrained decoding framework first to prevent immediate malformed crashes.

### 4. How often could the model not follow the contract? Quote REPAIRS, and say what that implies about running a 1.5B model in production.
- The model frequently failed the formatting contract, resulting in stop: malformed and recording repairs: {'fence_or_prose': ...}, implying a high operational tax for small models.

### 5. Where does your agent still trust something it should not?
- The agent implicitly trusts the base model's ability to cleanly separate data from instructions in raw text inputs.

### 6. What did this lab not tell you?
- This setup did not account for model variance (single run under greedy decoding) and used a smoke test set rather than a full production evaluation suite.

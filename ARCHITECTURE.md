## 2. `ARCHITECTURE.md`

```markdown
# Architecture Overview

Below, sketch (ASCII, hand-drawn JPEG/PNG pasted in, or ASCII art) the high-level components of your agent.

Front-end (React + Tailwind)
│
│ User input
│
Backend (Google Cloud Functions / Vertex AI Workflow)
├── Planner Module (planner.py)
│    └─ Define sub-tasks
│
├── Executor Module (executor.py)
│    └─ Gemini API calls, agent logic execution
│
├── Memory Module (memory.py)
│    └─ Persistent JSON output storage (Cloud Storage or Firestore)
│
├── Logging & Monitoring
│    └─ Google Cloud Logging & Observability
│
├── JSON output → Frontend
│
Frontend Approval Workflow
├── Approve → Next Agent
└── Regenerate → Re-run Current Agent


## Components

1. **User Interface**  
   - E.g., Streamlit, CLI, Slack bot  

2. **Agent Core**  
   - **Planner**: how you break down tasks  
   - **Executor**: LLM prompt + tool-calling logic  
   - **Memory**: vector store, cache, or on-disk logs  

3. **Tools / APIs**  
   - E.g., Google Gemini API, Tools, etc

4. **Observability**  
   - Logging of each reasoning step  
   - Error handling / retries  


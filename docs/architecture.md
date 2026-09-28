# Architecture

```text
Web UI
  |
FastAPI
  |
Change Agent
  |------ Hindsight recall
  |------ Hindsight reflect
  |------ LLM
  |
Outcome -> Hindsight retain

Hindsight bank = durable team engineering experience
```

Memory should capture durable experience:
- service
- change type
- context
- failure mode
- outcome
- root cause
- mitigation
- lesson learned
- timestamp
- change identifier

Do not store secrets or transient chat.

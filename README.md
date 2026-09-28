# Engineering Change Memory Agent

An AI agent that helps DevOps/SRE engineers make engineering-change decisions using the team's accumulated operational experience.

## Core loop
Change -> Hindsight recall -> agent recommendation -> real outcome -> Hindsight retain -> better future recommendation

## MVP
- Submit an upcoming engineering change.
- Retrieve similar past engineering experiences from Hindsight.
- Reflect over those experiences.
- Generate a recommendation with evidence.
- Record the eventual outcome.
- Retain the outcome for future recommendations.

## Run
1. Copy `.env.example` to `.env`.
2. Start Hindsight (Cloud or self-hosted).
3. `pip install -r backend/requirements.txt`
4. `uvicorn backend.main:app --reload`

Do not put API keys in Git. Do not connect this prototype to production infrastructure.

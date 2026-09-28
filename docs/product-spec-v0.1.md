# Product Specification v0.1

## Working name
Engineering Change Memory Agent

## Target user
DevOps / SRE / platform engineer responsible for reviewing an upcoming engineering change.

## Problem
Teams repeatedly encounter similar engineering situations, but useful knowledge is scattered across incidents, deployments, postmortems and team memory. A stateless AI can analyze the current change but does not inherently know what this team previously learned.

## Core value proposition
> Before you make an engineering change, ask what your team has already learned from similar changes.

## One workflow
1. Engineer describes an upcoming change.
2. Agent retrieves similar remembered experiences.
3. Hindsight reflects across those experiences.
4. Agent recommends rollout strategy and safeguards.
5. Engineer performs the change.
6. Engineer records the outcome.
7. Hindsight retains the outcome.
8. A later similar change gets a recommendation informed by the new experience.

## Must have
- Hindsight integration
- Synthetic engineering history
- Change input
- Recall
- Reflection
- Recommendation
- Evidence / remembered experiences
- Outcome recording
- Retention
- Before-memory vs after-memory demonstration

## Explicitly out of scope
- Autonomous production deployments
- Automatic rollback
- Kubernetes management
- Full CI/CD platform
- Full observability platform
- Production credentials
- Generic chatbot
- Generic risk-score dashboard

## Killer demo
1. Propose a connection-pool change.
2. Show limited/no relevant team experience.
3. Record an incident and lesson.
4. Propose a similar change later.
5. Show Hindsight retrieving the incident plus a successful prior canary.
6. Show the recommendation change because of those experiences.

## Success test
A judge should understand within 60 seconds:
- the engineering problem,
- the recommendation,
- what Hindsight remembered,
- how the recommendation changed after learning.

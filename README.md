Absolutely bro. Replace \*\*everything\*\* in `README.md` with this exact content:



````markdown

\# Engineering Change Memory



> Make the next engineering change using what your team already learned.



Engineering Change Memory is an AI-powered change advisor for DevOps/SRE teams.



It uses \*\*Hindsight\*\* to remember previous engineering changes, incidents, outcomes, mitigations, and lessons learned — then uses that accumulated experience to influence recommendations for future changes.



The goal is simple:



\*\*Don't make every engineering change as if the team has never seen it before.\*\*



\---



\## The Problem



Engineering teams accumulate valuable knowledge across deployments, incidents, postmortems, and operational decisions.



But when a new change arrives, that experience is often difficult to retrieve and apply consistently.



A conventional change workflow might look like:



```text

Upcoming Change

&#x20;     ↓

Analyze Current Change

&#x20;     ↓

Make Recommendation

&#x20;     ↓

Deploy

````



The missing piece is the team's accumulated experience.



Engineering Change Memory adds that layer:



```text

Upcoming Change

&#x20;     ↓

Hindsight Recall

&#x20;     ↓

Relevant Past Experiences

&#x20;     ↓

Hindsight Reflection

&#x20;     ↓

Evidence-Based Recommendation

&#x20;     ↓

Real Outcome

&#x20;     ↓

Hindsight Retain

&#x20;     ↓

Better Future Recommendations

```



\---



\## What Makes Memory Important



Memory is not just displayed to the user.



It changes the agent's future decision-making.



For example:



\### Before the team has relevant experience



The agent may have no team-specific evidence for a large database connection-pool change.



It can identify uncertainty, but it cannot honestly claim that the team's previous deployments showed a particular failure pattern.



\### After the team records an incident



Suppose a previous deployment increased the `payments-api` database connection pool from `50` to `120`.



That deployment caused:



\* database saturation

\* increased latency

\* a rollback



The team then resolved the issue by:



\* adding database saturation alerts

\* moving to a staged rollout



That experience becomes memory.



\### On a future similar change



Hindsight can retrieve the previous experience and the agent can recommend:



\* a staged or canary rollout

\* database utilization monitoring

\* saturation alerts

\* gradual expansion

\* a rollback plan



The recommendation is now grounded in \*\*what this team previously experienced\*\*.



\---



\## Core Memory Loop



```text

CHANGE

&#x20; │

&#x20; ▼

RECALL

Find similar engineering experiences

&#x20; │

&#x20; ▼

REFLECT

Reason over what the team learned

&#x20; │

&#x20; ▼

DECIDE

Generate an evidence-based recommendation

&#x20; │

&#x20; ▼

OUTCOME

Record what actually happened

&#x20; │

&#x20; ▼

RETAIN

Store the new experience in Hindsight

&#x20; │

&#x20; └──────────────► Future changes

```



This creates a learning loop rather than a one-shot AI recommendation.



\---



\## Hindsight Integration



The project uses Hindsight for three key operations:



\### 1. Retain



Engineering experiences are stored in Hindsight, including:



\* deployment context

\* outcomes

\* incidents

\* root causes

\* resolutions

\* lessons learned



\### 2. Recall



When a new change is submitted, the agent searches Hindsight for relevant previous experiences.



The retrieval focuses on factors such as:



\* service

\* change type

\* failure modes

\* mitigations

\* outcomes

\* lessons learned



\### 3. Reflect



The agent then asks Hindsight to reason over the remembered experiences and identify what the team should do for the upcoming change.



The final recommendation is generated from the retrieved memories and reflection.



\---



\## Example



\### Previous experience



```text

payments-api



Database connection pool:

50 → 120



Outcome:

Incident



Root cause:

Database capacity was overwhelmed.



Resolution:

Rollback + database saturation alerts +

staged rollout.



Lesson:

Large connection-pool increases should use

a staged/canary rollout with database

utilization monitoring.

```



\### New change



```text

payments-api



Database connection pool:

50 → 120



Environment:

Production



Context:

High expected traffic

```



\### Agent recommendation



The agent can now use the remembered experience to recommend:



```text

• Start with a small canary

• Monitor database utilization

• Configure saturation alerts

• Expand gradually after healthy metrics

• Keep rollback available

```



The important part is not simply that the agent recommends a canary.



It is that the recommendation is connected to a \*\*remembered engineering outcome\*\*.



\---



\## What We Built



The current MVP supports:



\* Submit an upcoming engineering change

\* Retrieve similar experiences from Hindsight

\* Reflect over remembered experiences

\* Generate an evidence-grounded recommendation

\* Show the memory evidence behind the recommendation

\* Record the actual change outcome

\* Retain the outcome in Hindsight

\* Use newly retained experience in future recommendations



\---



\## Architecture



```text

┌─────────────────────────────┐

│          Frontend           │

│     Engineering Change UI   │

└──────────────┬──────────────┘

&#x20;              │

&#x20;              ▼

┌─────────────────────────────┐

│         FastAPI API         │

│                             │

│  /analyze      /outcome     │

└──────────────┬──────────────┘

&#x20;              │

&#x20;              ▼

┌─────────────────────────────┐

│       Change Agent          │

│                             │

│  Recall → Reflect → Decide  │

└──────────────┬──────────────┘

&#x20;              │

&#x20;      ┌───────┴────────┐

&#x20;      ▼                ▼

┌─────────────┐   ┌─────────────┐

│  Hindsight  │   │     LLM     │

│    Memory   │   │  Reasoning  │

└─────────────┘   └─────────────┘

&#x20;      │

&#x20;      ▼

Engineering experiences

```



\---



\## Technology



\* \*\*Python\*\*

\* \*\*FastAPI\*\*

\* \*\*Hindsight\*\*

\* \*\*Hindsight Python SDK\*\*

\* \*\*OpenAI-compatible LLM API\*\*

\* \*\*Groq\*\*

\* \*\*HTML/CSS/JavaScript\*\*



The application is designed so that engineering history is stored in Hindsight rather than being hard-coded into the recommendation logic.



\---



\## Project Structure



```text

engineering-change-memory/

│

├── agent/

│   └── change\_agent.py

│

├── backend/

│   ├── main.py

│   └── requirements.txt

│

├── data/

│   └── sample/

│

├── docs/

│   ├── architecture.md

│   ├── product-spec-v0.1.md

│   └── team-tasks.md

│

├── frontend/

│   └── index.html

│

├── hindsight/

│   └── adapter.py

│

├── tests/

│   └── test\_health.py

│

├── .env.example

├── .gitignore

└── README.md

```



\---



\## Running Locally



\### 1. Clone the repository



```bash

git clone https://github.com/Msarthak0303/engineering-change-memory.git

cd engineering-change-memory

```



\### 2. Create the environment



```bash

python -m venv .venv

```



Activate it on Windows:



```cmd

.venv\\Scripts\\activate

```



\### 3. Install dependencies



```bash

pip install -r backend/requirements.txt

```



\### 4. Configure environment variables



Copy:



```text

.env.example

```



to:



```text

.env

```



Then configure your Hindsight and LLM credentials.



\*\*Never commit `.env` or API keys to Git.\*\*



\### 5. Start the API



```bash

uvicorn backend.main:app --reload

```



Open:



```text

http://127.0.0.1:8000/

```



API documentation is available at:



```text

http://127.0.0.1:8000/docs

```



\---



\## Scope



This is a prototype for learning from engineering change history.



It is intentionally \*\*not\*\* an autonomous production deployment system.



The current project does not:



\* deploy directly to production

\* automatically modify infrastructure

\* automatically roll back production systems

\* replace observability platforms

\* replace CI/CD systems



The goal is to demonstrate how accumulated engineering experience can influence future change decisions.



\---



\## Demo



Coming soon.



The final demo will show the same engineering change being evaluated:



1\. Without relevant team memory

2\. After a previous outcome has been retained

3\. With the recommendation changing because of that experience



\---



\## Why This Approach



Engineering knowledge becomes more valuable when it compounds.



A deployment incident should not disappear into an old ticket or postmortem.



It should become experience that can influence the next similar engineering decision.



\*\*Engineering Change Memory turns operational history into reusable team experience.\*\*

# Project Plan, Risks and Dependencies

**Project:** Intelligent Kanban System with an AI Assistant
**Team:** Akbope Bakytkeldy (product and frontend), Symbat Saparbay (backend and AI)
**Supervisor:** Alibek Orynbek
**Task tracking:** [YouTrack](https://ai-kanban-thesis.youtrack.cloud/projects/DEMO)

## 1. Responsibilities

| Area | Owner | Main responsibilities |
|---|---|---|
| Product | Akbope | Proposal and scope, user research, requirements and user stories, use cases, verification plan, manual baseline |
| Frontend | Akbope | Prototype, React application, board and task screens, command input, proposal review and confirmation screens |
| Backend | Symbat | Database schema, REST API and WebSocket events, authentication and permissions, task history, notifications |
| AI and speech | Symbat | Speech-to-text pipeline and benchmark, command parsing with the LLM, validation of AI output, AI evaluation datasets |
| Shared | Both | Literature and system analysis, architecture decisions, pull-request review of each other's work, test execution, demo video |

Each important pull request is reviewed and approved by the other team member before merging.

## 2. Milestones

Dates after pre-defense 1 are proposed targets and will be confirmed with the supervisor.

| # | Milestone | Content | Target date | Status |
|---|---|---|---|---|
| M1 | Analysis and design (pre-defense 1) | Proposal, user interviews, literature review, existing-system and technology comparisons, requirements, architecture diagrams, database schema and API, prototype and user testing, verification plan | 24 Oct 2026 | Done, tag `pre-defense-1` |
| M2 | Core platform | Authentication, workspaces and projects, persistent Kanban board, manual task management (US-01, US-02, US-04, US-05) | To be confirmed | Planned |
| M3 | AI task creation (first working MVP) | Voice recording, transcription with correction, task proposals from voice and text, several tasks per message, confirmation, safety rules (US-07–US-09, US-15–US-17); STT benchmark run | To be confirmed | Planned |
| M4 | Pre-defense 2 | MVP demonstration, first verification results, updated documentation | To be confirmed | Planned |
| M5 | Full AI actions | Update task, status, assignee, deadline and priority commands, search, members, comments and history, multilingual interface (Should stories) | To be confirmed | Planned |
| M6 | Summaries and notifications | Project and meeting summaries, notifications (US-13, US-18) | To be confirmed | Planned |
| M7 | Evaluation and final pre-defense | All 36 verification cases run, AI metrics against agreed targets, comparison with baselines, demo video, final report | To be confirmed | Planned |

### Next steps after pre-defense 1

1. Confirm MVP priorities and numerical quality targets with the supervisor.
2. Collect the speech dataset (Kazakh, Russian, English and mixed recordings with reference transcripts) and run the STT benchmark.
3. Set up the application repository structure, CI and development environment.
4. Implement M2 and start M3.

## 3. Risks

Probability and impact: H = high, M = medium, L = low.

| ID | Risk | P | I | Mitigation | Owner |
|---|---|---|---|---|---|
| R1 | Low transcription accuracy for Kazakh and mixed speech | H | H | Kazakh fine-tuned model with language routing; manual language selection; editable transcript before extraction; benchmark on our own recordings | Symbat |
| R2 | No GPU available for self-hosted speech recognition | M | H | Smaller models with int8 on CPU; cloud STT fallback; request university resources | Symbat |
| R3 | LLM invents or misreads assignees, deadlines or tasks | M | H | JSON schema validation; backend lookup of members and tasks; source phrase check for deadlines; mandatory confirmation | Symbat |
| R4 | Cloud LLM cost or unavailability | M | M | Low-cost model class; usage limits; local LLM mode as fallback; manual board always works | Symbat |
| R5 | Scope too large for the available time | H | H | Must/Should/Later priorities; deliver the MVP first; agree scope with the supervisor | Both |
| R6 | Users do not notice the confirmation step or proposal selection | M | M | Prototype findings F7 and F8 addressed in the UI; repeat usability tests | Akbope |
| R7 | Too few participants and recordings for meaningful evaluation | M | M | Recruit participants early; prepare datasets before implementation of the AI service | Both |
| R8 | Unauthorized access to project data or voice recordings | L | H | Backend permission checks; private storage with presigned URLs; retention limit; permission test cases V29–V31 | Symbat |
| R9 | Work concentrated on one person or near deadlines | M | M | Task ownership in YouTrack; weekly progress check; small pull requests reviewed by the teammate | Both |

## 4. Dependencies

| Dependency | Needed for | Status |
|---|---|---|
| Supervisor agreement on MVP scope and quality targets | M2–M3 planning, evaluation | Requested |
| GPU server or cloud API access (speech and LLM) | M3, STT benchmark | Not yet available |
| Kazakh speech models and KSC2 data | STT benchmark, M3 | Publicly available |
| Recorded commands and reference transcripts from participants | STT benchmark, AI evaluation | Not yet collected |
| Participants for usability and baseline tests | M4, M7 | Three prototype participants so far |
| Database schema and API specification (BE-06) | Frontend and backend implementation | Done |
| Prototype findings F1–F8 | Frontend implementation | Done |

## 5. Task ID mapping

Early branches and commits used internal labels (KAN-1, FE-xx, BE-xx). The table maps them to YouTrack issues.

| Label | YouTrack | Deliverable | Owner |
|---|---|---|---|
| KAN-1, FE-01 | DEMO-25 | Project proposal and scope | Akbope |
| FE-02 | DEMO-26 | Project README | Akbope |
| FE-03 | DEMO-27 | Product requirements and user stories | Akbope |
| FE-04 | DEMO-28 | Core screens and interactive prototype | Akbope |
| FE-05 | DEMO-29 | Use case diagram and user flows | Akbope |
| FE-06 | DEMO-31 | User interviews | Akbope |
| FE-07 | DEMO-30 | Prototype testing with users | Akbope |
| FE-08 | DEMO-33 | Align requirements and README | Akbope |
| FE-09 | DEMO-34 | Verification and evaluation plan | Akbope |
| BE-01 | DEMO-20 | Literature review | Symbat |
| BE-02 | DEMO-21 | Existing system comparison | Symbat |
| BE-03 | DEMO-22 | Technology selection | Symbat |
| BE-04 | DEMO-23 | System context diagram | Symbat |
| BE-05 | DEMO-24 | Backend component diagram | Symbat |
| BE-06 | DEMO-32 | Database schema and API specification | Symbat |
| — | DEMO-35 | Pre-defense fixes: BE-02, BE-03 | Symbat |
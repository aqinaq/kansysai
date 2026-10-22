# Intelligent Kanban System with an AI Assistant

A diploma project for managing tasks on a Kanban board through manual actions, voice commands, and text commands. The assistant will propose one or more actions from a message. Users will review and confirm changes before they are saved.

## Problem and target users

Work instructions and meeting decisions are often communicated verbally. Recording each task manually takes time, and its owner or deadline may be unclear. One message may contain several assignments.

The intended users are employees, project managers, teachers, and students. Three initial user interviews informed the task-review and clarification flows; further prototype testing is planned.

## Project scope

The first working MVP is planned to include a persistent Kanban board, manual task management, voice transcription with user correction, and creation of one or more task proposals from voice or text. Users will review each proposal separately. The backend will validate confirmed actions before saving them.

The planned complete product also includes commands for updating existing tasks, task search, project and meeting summaries, comments, history, notifications, and Kazakh, Russian, English, and mixed-language interaction. The [product requirements](docs/product-requirements.md) describe the full scope and proposed MVP priorities.

Missing assignees, deadlines, and tasks must not be invented. Ambiguous commands must be clarified, and data-changing actions require user confirmation.

## Team

- Akbope Bakytkeldy — Product and Frontend
- Symbat Saparbay — AI and Backend
- Supervisor: Alibek Orynbek

Both team members contribute to project documentation and review each other's pull requests.

## Current status

The project is in the analysis and design stage. This repository contains the proposal, user interviews, product requirements, literature and existing-system reviews, technology comparison, architecture diagrams, database schema, API specification, and an interactive interface prototype.

The prototype demonstrates a Kanban board, task editing, multiple task proposals, clarification, and confirmation using sample data. **Voice recording and AI responses are simulated.** Prototype changes are stored in browser memory and reset when the page reloads. A persistent application with real speech recognition and backend AI processing is not available yet.

The prototype evaluation currently documents an internal walkthrough. Testing with independent users is still in progress.

## Project documents

- [Project proposal](docs/project-proposal.md)
- [Product requirements and user stories](docs/product-requirements.md)
- [User interview findings](docs/research/user-interviews.md)
- [Literature review](docs/be-01/BE01.pdf)
- [Existing-system comparison](docs/be-02/BE02.pdf)
- [Technology selection](docs/be-03/BE03.pdf)
- [System context diagram](docs/be-04/BE04.pdf)
- [Backend component diagram](docs/be-05/BE05.pdf)
- [Database schema and API specification](docs/be-06/BE06.pdf)
- [Use-case overview](docs/diagrams/use-case-diagram.md)
- [User flows](docs/user-flows.md)
- [Preliminary prototype evaluation](docs/research/prototype-feedback.md)
- [Interface screenshots](screenshots/)
- [YouTrack project](https://ai-kanban-thesis.youtrack.cloud/projects/DEMO)

The diagram and technical-document folders also contain editable source files.

## Proposed technology stack

The [technology comparison](docs/be-03/BE03.pdf) proposes React, TypeScript, and Vite for the frontend; FastAPI for the backend; PostgreSQL for application data; and separate speech-to-text and command-processing services. REST endpoints and WebSocket events are planned for application interaction. These choices are documented designs, not an implemented stack.

## Open the interface prototype

Open [`prototype/index.html`](prototype/index.html) in a modern browser. No installation, API key, or backend is needed. See the [prototype instructions and limitations](prototype/README.md) before demonstrating it.

The prototype uses sample commands and sample board data. It must not be presented as a working speech-recognition or AI implementation.

## Development workflow

Work is tracked in [YouTrack](https://ai-kanban-thesis.youtrack.cloud/projects/DEMO). Changes are developed in task branches and submitted through GitHub pull requests for teammate review. New branches, commits, and pull requests should reference their YouTrack issue ID. Each completed issue should link to its reviewed deliverable.

Setup and test instructions for the persistent application will be added when that implementation is available.

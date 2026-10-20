# Intelligent Kanban System with an AI Assistant

A diploma project for generating tasks and meeting summaries from voice messages. The system will transcribe recordings, identify actionable tasks, and let users review the results before adding tasks to a Kanban board.

## Problem and target users

Work instructions, assignments, and meeting decisions are often communicated verbally. Turning these discussions into clear tasks manually takes time, and important details may be missed.

The intended users include employees, project managers, teachers, and students who need to organize tasks from voice messages and meeting recordings.

## Expected outcome

The planned system will let a user:

1. Submit a voice message or meeting recording.
2. View its transcription.
3. Review one or more suggested tasks, including their titles, descriptions, assignees, and deadlines when provided.
4. View a summary of the meeting when applicable.
5. Edit, confirm, or reject the suggested tasks.
6. Add confirmed tasks to a Kanban board.

Task details will remain editable, and tasks will be saved only after user confirmation. Missing assignees or deadlines will not be invented by the system.

## Team

- Akbope Bakytkeldy — Product and Frontend
- Symbat Saparbay — AI and Backend
- Supervisor: Alibek Orynbek

Both team members review each other's pull requests and contribute to the project documentation and presentation.

## Current status

The project is in the analysis and design stage. The repository contains an initial project proposal and a draft literature review. A technology comparison and proposed stack have been submitted for review.

The next deliverables include user research, finalized requirements, architectural diagrams, and an interface prototype. The project documents will be updated to reflect the latest agreed requirements, including multiple tasks per message and meeting summaries.

A complete application is not available yet. The technology choices will be documented after the comparison has been reviewed and agreed upon by the team.

## Project documents

- [Project proposal](docs/project-proposal.md)
- [Literature review](docs/research/literature-review.md)
- [YouTrack project](https://ai-kanban-thesis.youtrack.cloud/projects/DEMO)

## Development workflow

Work is tracked in YouTrack. Each meaningful task has an assignee, a deadline, and acceptance criteria.

Changes are developed in separate Git branches and submitted through pull requests. The other team member reviews each pull request before it is merged into `main`. Branch names, commits, and pull requests reference the relevant YouTrack issue.

Setup, run, and test instructions will be added when the first runnable implementation is available.

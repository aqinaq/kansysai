# Project Proposal

## Project title
Development of an Intelligent Kanban System with an AI Assistant for Automatic Task Generation from Voice Messages

## Team
- Akbope Bakytkeldy | SE-2426 | Product and frontend
- Symbat Saparbay | SE-2424 | Backend and AI
- Supervisor: Alibek Orynbek

## Problem
Team members often communicate assignments through voice messages and meetings. Recording each assignment manually takes time, and the task owner, deadline, or required action may be unclear. A single message may contain several separate tasks.

In three interviews with potential users, participants described using different places to record tasks and checking unclear details with other people. All three said they would review an AI-suggested task before accepting it. These interviews inform the design but are not a representative survey.

## Target users
Employees and small project teams, project managers, teachers, and students who organize work discussed in messages or meetings. Their specific needs will continue to be checked through prototype testing.

## Aim
Develop a Kanban system that turns voice or text instructions into editable task suggestions. The user reviews each suggestion, resolves unclear details, and confirms which actions should be saved to the board.

## Objectives
1. Provide a Kanban board where users can create, edit, and move tasks.
2. Convert supported voice input to text and allow the user to correct the transcript.
3. Identify one or more tasks in a message and extract details that are actually provided.
4. Show each proposed task separately for editing, confirmation, or rejection.
5. Ask for clarification when an assignee, deadline, or intended task is unclear.
6. Save changes only after user confirmation and backend validation.

## Main user scenario
1. A user selects a project and submits a voice message or text command.
2. For voice input, the system displays the transcript so the user can correct it.
3. The assistant identifies the requested action and proposes one or more separate tasks.
4. Each proposal shows its title, assignee, deadline, and priority when these details are available. Missing or ambiguous details remain visible instead of being invented.
5. The user edits, confirms, or rejects each proposal.
6. The backend validates the confirmed proposals and adds them to the Kanban board.
7. The board displays the saved tasks.

## First working version
- A usable Kanban board with manual task creation, editing, and movement.
- Voice input, transcription, and correction of recognized text.
- Creation of one or more task suggestions from a voice or text message.
- Separate review, editing, confirmation, or rejection of each suggestion.
- Clarification or an unassigned state when the responsible person is unknown.
- Backend validation before confirmed tasks are saved.

## Planned product scope after the first working version
- User accounts, workspaces, project members, and access permissions.
- Voice and text commands to update existing tasks, status, assignee, deadline, and priority.
- Task search and project summaries based on real project data.
- Comments, change history, notifications, and meeting summaries.
- Evaluation of Kazakh, Russian, English, and mixed-language commands.

## Safety rule
The assistant must not save or change project data when the command is ambiguous or the user has not confirmed the proposed action.

## Evidence and next evaluation
The initial user evidence is documented in `docs/research/user-interviews.md`. The interactive prototype and its limitations are documented in `prototype/README.md`. The next evaluation will test the prototype with potential users and record task completion, confusion, and proposed improvements.

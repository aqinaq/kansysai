# Product Requirements and User Stories

Original issue: [DEMO-27](https://ai-kanban-thesis.youtrack.cloud/issue/DEMO-27)  
Scope and status update: [DEMO-33](https://ai-kanban-thesis.youtrack.cloud/projects/DEMO/issues/DEMO-33)  
Status: Draft for team review; MVP priorities are proposed pending team agreement

## 1. Product goal

Develop a Kanban application that helps users manage tasks manually and through voice and text commands. A message may produce one or more separate task proposals.

The AI assistant interprets commands and proposes actions. Users can inspect and correct a transcript, resolve unclear details, and review each proposal. Changes are applied only after user confirmation and backend validation.

## 2. Target users

- Employees managing individual and team tasks
- Project managers coordinating work
- Teachers assigning and monitoring work
- Students organizing individual and group projects

These are intended user groups. Three initial user interviews informed the review and clarification flows; further prototype testing is planned. The interviews do not represent all potential users.

## 3. Team

- Akbope Bakytkeldy — Product and Frontend
- Symbat Saparbay — AI and Backend
- Supervisor — Alibek Orynbek

## 4. Product scope

The planned product includes:

- Registration and login
- Workspaces, projects, and Kanban boards
- Project membership and access permissions
- Task creation, editing, deletion, and assignment
- Deadlines, priorities, statuses, and column movement
- Comments and task history
- Voice and text commands
- Multiple tasks extracted from one message
- Meeting summaries and action items
- Project queries using real database records
- Notifications about changes and approaching deadlines
- Kazakh, Russian, English, and mixed-language input

## 5. MVP boundary and priorities

The first working MVP will demonstrate a persistent project Kanban board and task creation from voice or text input. A user can inspect and correct the transcript, review one or more proposed tasks separately, resolve unclear details, and confirm which tasks are saved. Manual board operations and backend validation support this flow. The prototype currently demonstrates these interactions with simulated voice and AI behavior; it is not the working MVP.

The priorities below describe the **first working MVP**, not whether a story belongs in the final product. All 18 stories remain in the planned product scope. The assignments are proposed for team and supervisor review before implementation planning is finalized.

| Priority | Meaning |
| --- | --- |
| Must | Needed for the first working MVP or to perform its actions safely |
| Should | Important for the next iteration after the MVP |
| Later | Planned for the complete product after the first MVP |

### Story priorities and planned verification

The checks describe expected verification, not tests already passed. A story marked Should or Later may still contain a safety rule that applies to the MVP: task assignment must use a valid project member, and MVP task changes must be recorded in an audit trail.

| Story | MVP priority | How fulfilment will be checked |
| --- | --- | --- |
| US-01 Registration and login | Must | Register, log in, reject invalid credentials, and deny protected project data to an unauthenticated user. |
| US-02 Workspaces and projects | Must | Create a project in a workspace, reload, and confirm that only accessible projects appear. |
| US-03 Project membership | Should | Add a member, display membership, reject an unauthorized membership change, and reject assignment to a nonmember. In the MVP, any assignee used by task creation must already be a valid project member. |
| US-04 Manual task management | Must | Create and edit a task, reload the board, and check that invalid titles and unauthorized deletion are rejected. |
| US-05 Kanban board | Must | Move a task to a valid column and confirm its saved position after reloading. |
| US-06 Comments and history | Should | Add a comment and inspect its author and time; change a task and inspect the history entry. The MVP must still record who made its task changes. |
| US-07 Voice input and transcription | Must | Submit supported audio, view processing and transcript, correct the text before extraction, and check failure handling. |
| US-08 Task creation by voice or text | Must | Produce editable drafts from both inputs; confirm one draft and reject another; verify that only the confirmed draft is saved. |
| US-09 Multiple tasks per message | Must | Submit one message with several assignments and verify separate, independently selectable drafts. |
| US-10 Updating existing tasks | Should | Match a task, preview changes, resolve multiple matches, and verify no update before confirmation. |
| US-11 Status, assignee, deadline, and priority commands | Should | Test each command type, invalid values, relative dates, and ambiguous values before any change is saved. |
| US-12 Task search | Should | Search accessible stored tasks, check filters and empty results, and confirm no invented records appear. |
| US-13 Project and meeting summaries | Later | Compare summaries and action items with accessible project records or supplied meeting input; check missing details and confirmation. |
| US-14 Multilingual interaction | Should | Test Kazakh, Russian, English, and mixed speech; inspect language selection, editable fields, and interface localization. MVP voice support must state its tested languages honestly. |
| US-15 Unclear and unrelated commands | Must | Submit ambiguous, missing-detail, and unrelated inputs; verify clarification or explanation and no unconfirmed data change. |
| US-16 Access protection | Must | Try manual and AI actions with an unauthorized account and guessed IDs; verify the backend rejects access. |
| US-17 Duplicate prevention and failures | Must | Confirm the same command twice and simulate processing failure; verify no duplicate task or false success. |
| US-18 Notifications | Later | Trigger an assignment or approaching deadline and verify notification content, timing, and access rules. |

The first MVP is planned to implement **Create Task** from the AI action list below. The other seven actions remain planned product requirements and are specified in the API design; their implementation priority will be agreed during the next milestone plan.

## 6. AI actions

The complete product must support these eight actions:

1. Create Task — propose one or more new tasks.
2. Update Task — propose changes to an existing task.
3. Change Status — propose moving a task to another status.
4. Assign User — propose assigning a project member.
5. Change Deadline — propose a new deadline.
6. Change Priority — propose a new priority.
7. Search Tasks — retrieve tasks matching a request.
8. Project Summary — summarize accessible project information.

Each action must have defined input parameters, a response structure,
validation rules, and error handling in the API specification.

## 7. Processing flow

Voice input → transcription and user correction → intent recognition → field extraction → validation and clarification → review of each proposed action → user confirmation → backend action → updated Kanban board

Text commands enter the same flow after the transcription step. One message may yield several proposed actions, which the user can accept or reject separately.

Search and summary actions read accessible project data.
Actions that change data require confirmation.

## 8. User stories and acceptance criteria

### US-01 Registration and login

As a user, I want to register and log in so that I can access my work.

Acceptance criteria:
- A user can register with valid account information and log in.
- Invalid login details produce a clear error.
- Unauthenticated users cannot access protected project data.

### US-02 Workspaces and projects

As a user, I want to organize work into workspaces and projects.

Acceptance criteria:
- Authorized users can create workspaces and projects.
- A project belongs to the selected workspace.
- Only projects accessible to the current user are displayed.

### US-03 Project membership

As an authorized project user, I want to add members so we can work together.

Acceptance criteria:
- Members can be added through the agreed membership mechanism.
- The project displays its members.
- Unauthorized users cannot change membership.
- Tasks can be assigned only to valid project members.

### US-04 Manual task management

As a user, I want to create, edit, and delete tasks manually.

Acceptance criteria:
- A task requires a non-empty title.
- Supported fields include description, assignee, deadline,
  priority, and status.
- Saved changes appear on the board.
- Deletion requires confirmation and a permission check.

### US-05 Kanban board

As a user, I want to move tasks between columns to track progress.

Acceptance criteria:
- The board shows tasks in their current columns.
- Authorized users can move tasks between valid columns.
- A saved move remains correct after reloading the board.

### US-06 Comments and history

As a user, I want to discuss tasks and see their change history.

Acceptance criteria:
- Authorized users can add comments to tasks.
- Comments show the author and time.
- Task history records who changed a task, when, and what changed.

### US-07 Voice input and transcription

As a user, I want to submit a recording and review the recognized text.

Acceptance criteria:
- The interface accepts supported audio input and shows processing status.
- A successful transcription is displayed.
- The user can correct the transcription before task extraction.
- Unsupported or failed audio input produces a clear error.

### US-08 Task creation by voice or text

As a user, I want to create tasks using natural-language commands.

Acceptance criteria:
- Both voice and text input can produce task drafts.
- Drafts show the extracted task fields before saving.
- The user can edit, confirm, or reject each draft.
- No task is saved without confirmation.

### US-09 Multiple tasks per message

As a user, I want one message to produce several separate tasks.

Acceptance criteria:
- A message containing several clear assignments produces separate drafts.
- Each draft can be reviewed, edited, accepted, or rejected independently.
- Rejected drafts are not saved.

### US-10 Updating existing tasks

As a user, I want to update a task through a command.

Acceptance criteria:
- The assistant identifies a task within the accessible project.
- The preview shows the proposed changes.
- If several tasks match, the user must select the intended task.
- Changes are applied only after confirmation.

### US-11 Status, assignee, deadline, and priority commands

As a user, I want to change individual task fields through commands.

Acceptance criteria:
- Change Status, Assign User, Change Deadline, and Change Priority
  are supported as distinct actions.
- Status and priority values must be valid.
- Assignees must be valid project members.
- Relative deadlines use an explicit reference date and timezone.
- Ambiguous values require clarification before saving.

### US-12 Task search

As a user, I want to ask questions such as “Which tasks are overdue?”

Acceptance criteria:
- Results come from accessible database records.
- Applied filters are reflected in the results.
- No matches produce an empty-result message.
- The assistant does not invent tasks or dates.

### US-13 Project and meeting summaries

As a user, I want project summaries and action items from meeting input.

Acceptance criteria:
- Project summaries use only accessible project records.
- Meeting summaries are based on the supplied input.
- Identified action items appear as task drafts.
- Missing assignees or deadlines remain visible as missing information.
- Task creation requires user confirmation.

### US-14 Multilingual interaction

As a user, I want to use Kazakh, Russian, English, and mixed speech.

Acceptance criteria:
- The test set includes all three languages and mixed-language input.
- Users can select a language when automatic detection is unsuitable.
- Transcripts and generated fields remain editable.
- Interface localization covers Kazakh, Russian, and English.

### US-15 Unclear and unrelated commands

As a user, I want the assistant to ask for clarification when needed.

Acceptance criteria:
- Missing or ambiguous information produces a clarification request.
- Unrelated messages produce an appropriate explanation.
- The assistant does not invent missing people, tasks, or deadlines.
- No data-changing action occurs while the command remains ambiguous.

### US-16 Access protection

As a user, I want my project data protected from unauthorized access.

Acceptance criteria:
- The backend checks permissions for manual and AI actions.
- Search and summaries exclude inaccessible records.
- Unauthorized task changes are rejected.
- Guessing a project or task identifier does not bypass permissions.

### US-17 Duplicate prevention and failures

As a user, I want retries and service failures handled safely.

Acceptance criteria:
- Repeated confirmation of the same request does not create duplicate tasks.
- Failed processing displays an understandable error.
- A failed request is not displayed as successfully completed.
- Users can retry without unintentionally repeating a completed action.

### US-18 Notifications

As a user, I want to know about relevant changes and approaching deadlines.

Acceptance criteria:
- Relevant task changes and approaching deadlines generate notifications
  according to the agreed notification rules.
- Notifications refer to real, accessible tasks.
- Notification timing and delivery channels are documented before implementation.

## 9. Quality requirements

- Apply access checks on the backend.
- Validate AI output before executing actions.
- Keep user confirmation separate from task extraction.
- Protect stored recordings, transcripts, and user information.
- Record user actions and important task changes.
- Display loading, success, empty, and error states clearly.
- Measure AI accuracy and response time on representative inputs.

## 10. Verification

Prepare at least 30 test cases covering:

- Manual Kanban operations
- All eight AI actions
- Multiple tasks in one message
- Kazakh, Russian, English, and mixed speech
- Recognition errors and corrected transcripts
- Missing assignees and ambiguous deadlines
- Unauthorized access attempts
- Duplicate submissions
- Unrelated commands and unavailable AI services

Each case must record:
- Input and preconditions
- Expected result
- Actual result
- Pass or fail

## 11. Decisions to confirm

- Project roles and exact permission rules
- Supported audio formats and recording-length limits
- Default timezone and rules for relative dates
- Notification timing and delivery channels
- Data retention policy
- Performance targets and AI quality thresholds
- Features required for the next demonstration

# FE-05: User Flows

Status: Draft for team review.

These flows describe the intended product behavior. FE-04 demonstrates selected interactions with simulated AI responses and voice recording.

## Common preconditions

- The user is authenticated.
- A workspace and project are selected.
- The user has permission to access the requested information.
- Changes require the appropriate project permissions.

## Flow 1: Create several tasks

**Goal:** Turn one voice or text message into several tasks.

**Example command:**
“Create a prototype task for Akbope and an API task for Symbat, both due October 23, 2026.”

### Main flow

1. The user opens the AI assistant from the Kanban board.
2. The user types a command or submits a voice message.
3. For voice input, the system displays the transcription.
4. The user can correct the transcription before continuing.
5. The system interprets the command and prepares task proposals.
6. The preview displays each proposed title, assignee, deadline, and other extracted details.
7. The user edits details or deselects unwanted proposals.
8. The user confirms the selected proposals.
9. The system validates permissions and task data.
10. The system creates the confirmed tasks and displays them on the board.

### Alternative outcomes

- Missing or ambiguous details lead to Flow 3.
- Invalid fields are highlighted for correction.
- If no proposals are selected, confirmation is unavailable.
- Cancellation discards the proposals without changing the board.
- Processing failure displays an error and allows retry or text input.

**Postcondition:** Only selected and confirmed tasks are created.

## Flow 2: Update an existing task

**Goal:** Apply a requested change to the correct task.

**Example command:**
“Move the system context diagram task to Done.”

### Main flow

1. The user submits a voice or text command.
2. The system identifies the requested action and matching task.
3. If several tasks match, the system asks the user to select one.
4. The preview identifies the target task and shows the existing and proposed values.
5. The user reviews the change and edits permitted details if needed.
6. The user confirms the proposal.
7. The system rechecks permissions and the current task state.
8. The system applies the confirmed change.
9. The board displays the updated task.

### Alternative outcomes

- No matching task: ask the user to revise the request or select a task manually.
- Multiple matches: continue with Flow 3.
- No permission: explain the restriction and leave the task unchanged.
- Task changed since preview: refresh the proposal and request confirmation again.
- Cancellation: leave the task unchanged.

**Postcondition:** The confirmed task is updated without changing unrelated tasks or fields.

This flow also covers assignment, deadline, priority, title, and description changes.

## Flow 3: Resolve missing or ambiguous details

**Goal:** Clarify a proposal without guessing or changing the board prematurely.

### A. Ambiguous task

**Example:** “Move the diagram task to Done.”

1. The system finds several plausible matching tasks.
2. The clarification screen shows their titles and distinguishing details.
3. The user selects the intended task.
4. The system returns to the preview with the selected task.
5. The user reviews and confirms the change.

### B. Unknown or missing assignee

**Example:** “Create a demo video task and assign it to Alex.”

1. The system cannot match Alex to a workspace member.
2. The clarification screen explains the unresolved assignment.
3. The user chooses a workspace member, selects Unassigned if permitted, or edits the command.
4. The system returns to the updated preview.
5. The user reviews and confirms the proposal.

### Alternative outcomes

- The user cancels: no board changes are made.
- Required information remains unresolved: the affected proposal cannot be confirmed.
- The user deselects the affected proposal: other valid proposals can still be reviewed.

**Postcondition:** Clarification updates the preview only. Confirmation is still required to apply changes.

## Flow 4: Manage a task manually

1. The user opens a task card or selects Add task.
2. The task form displays the title, description, assignee, deadline, priority, and status.
3. The user edits the fields.
4. The system validates required fields and permissions.
5. The user selects Save changes or Create task.
6. The board displays the saved result.

Cancellation leaves the board unchanged.

## Flow 5: Search tasks or request a project summary

1. The user submits a search or summary request.
2. The system clarifies the project or search scope if necessary.
3. The system retrieves only information the user can access.
4. The system displays matching tasks or a project summary.
5. The user can open a task to inspect its details.

These actions do not modify board data and do not require a change-confirmation step.

## Common safeguards

- Do not invent task identifiers, assignees, or deadlines.
- Show interpreted dates clearly before confirmation.
- Prevent repeated confirmation from creating duplicate changes.
- Show which actions succeeded or failed if a request contains several actions.
- Preserve the user's editable input when processing fails.
- Support Kazakh, Russian, English, and mixed-language input as defined in the product requirements.

## Review checklist

- [ ] Flows match the product requirements.
- [ ] All eight AI actions are covered.
- [ ] Multiple-task creation is supported.
- [ ] Clarification returns to an editable preview.
- [ ] Cancellation does not change the board.
- [ ] Permission and processing failures are addressed.
- [ ] Symbat has reviewed backend consistency.

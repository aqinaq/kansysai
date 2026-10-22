# FE-07: Prototype Evaluation

**YouTrack:** [DEMO-30](https://ai-kanban-thesis.youtrack.cloud/issue/DEMO-30)  
**Evaluation date:** 22 October 2026  
**Artifact evaluated:** FE-04 interactive browser prototype (`prototype/index.html`)  
**Status:** Preliminary internal walkthrough; external participant testing has not yet been conducted.

## Purpose and method

This walkthrough checked whether the prototype supports the main task flows: selecting a project, editing a Kanban card, reviewing several AI-proposed tasks, and resolving an ambiguous task or assignee. One evaluator used the browser prototype and recorded the visible results after each action. The evaluation did not measure how easily independent users understand the interface.

The prototype contains illustrative project and task data. Voice recording and AI generation are simulated. Browser state resets when the page reloads.

## Results

| Scenario | Observed result |
| --- | --- |
| Select a project | The “Diploma project” card opened a Kanban board containing six sample tasks. |
| Edit a card | The deadline of “Design the core screens and user flows” changed from 23 to 25 October. The board showed 25 October after saving. |
| Review several proposals | The “Several tasks” sample produced two distinct task proposals. Each showed an editable title, assignee, deadline, and selection checkbox. |
| Confirm a subset | The second proposal was deselected. Confirmation added only “Build the interactive prototype” to the board, raising the task count from six to seven. |
| Clarify an ambiguous task | The diagram command offered two matching tasks. Selecting “Create system context diagram” returned to a preview of the proposed status change. Closing that preview did not apply the change. |
| Clarify an unknown assignee | The Alex sample offered Akbope, Symbat, and Unassigned. Selecting Unassigned returned to the preview. Closing it did not add a task. |
| Enter an unsupported command | “Please prepare slides for tomorrow” did not generate a preview. The command screen remained open because this prototype handles preset examples. |
| Open voice input | The voice tab displayed a simulated recording control and language examples. No real audio was captured or processed. |

## Findings

### F1. An edit can be lost during task clarification

**Severity:** Medium. In the ambiguous-task preview, the proposed title was changed to “My chosen diagram” before a target task was selected. After selecting “Create system context diagram,” the preview replaced that entered title with the existing task title. The interface permits an edit that is then silently discarded. The target task should be selected before those fields become editable, or the entered changes should be retained and shown as proposed updates.

### F2. A sample deadline will become stale

**Severity:** Low. The multiple-task sample uses 23 October 2026 as a fixed deadline. This helps repeat the same demonstration but becomes a past date after 23 October. A future-relative sample date would make later evaluations easier to interpret.

### F3. The sample projects share one board

**Severity:** Low for the prototype. The workspace screen shows two project choices, while the prototype documentation states that both use the same demo board. This is an illustrative shortcut. It does not demonstrate separate project data or project isolation.

## Limitations

This was an internal walkthrough by one evaluator. No participant completion rates, quotations, or usability conclusions are reported. The simulated AI and voice controls were assessed only as interface flows; transcription and task-extraction accuracy were outside this evaluation. Independent participant results are still required for the FE-07 user-testing task.

## Evidence and follow-up

The evaluated prototype is [prototype/index.html](../../prototype/index.html); its [README](../../prototype/README.md) explains the preset commands and simulated voice and AI. Reference screens: [board](../../screenshots/02-kanban-board.jpg), [proposal review](../../screenshots/05-ai-preview.jpg), [task clarification](../../screenshots/06-clarification-task.jpg), and [assignee clarification](../../screenshots/07-clarification-assignee.jpg). These are prototype screenshots, not participant evidence.

A second internal check on 22 October started from a fresh board with six tasks. The “Several tasks” preset generated two proposals. After deselecting the second, confirming added one task and the board displayed seven tasks. The assistant screen visibly labelled the AI and audio as a demo. This repeated the existing walkthrough; it was not an independent participant session.

### Prioritized changes

| Priority | Change | Reason and acceptance check |
| --- | --- | --- |
| 1 | Preserve edits when resolving an ambiguous target task, or require target selection before editing. | F1 can silently discard a user change. Reopen the preview after choosing a target and check that the entered title remains visible until the user confirms or cancels. |
| 2 | Replace the fixed 23 October 2026 sample deadline with a future-relative example. | F2 will soon show an expired date. Repeat the multiple-task sample on a later day and check that its proposed deadline is still in the future. |
| 3 | Make the shared demo board explicit at project selection until project-specific boards exist. | F3 may suggest project isolation that the prototype does not provide. Open both project cards and check that the explanation matches the data shown. |

The earlier role-based simulated walkthroughs are useful prompts for what to observe, but their student, team-lead, and coordinator personas do not count as three participants. The current demo label addresses part of the concern that people might mistake preset responses for live AI; whether actual users notice it remains untested.

## Independent participant sessions (pending)

Recruit at least three potential users and run separate sessions. Use P1, P2, and P3 instead of names in the report. Before each session, explain that voice input and AI responses are simulated; reload the prototype so each person starts from the same board. Give the participant the tasks below without telling them where to click. Ask them to think aloud, and record what they do and say before interpreting the result.

1. Open the Diploma project and find the task about core screens and user flows.
2. Change that task’s deadline, save it, and verify the board shows the new date.
3. Use the “Several tasks” example, review both proposals, deselect one, and confirm only the other.
4. Use the ambiguous diagram example and select the intended existing task. Check whether any edits survive clarification.
5. Use the unknown-assignee example and choose Unassigned, then decide whether to confirm or cancel.

For each task, record success, partial completion, or failure; where the participant hesitated or needed help; and any short anonymous quotation. Note when help was given, because assisted completion should not be counted as unassisted success. Keep observations separate from inferred causes and proposed fixes.

| Participant | Date | Tasks completed without help (of 5) | Observed problems or quotations |
| --- | --- | --- | --- |
| P1 | Pending | Pending | Pending |
| P2 | Pending | Pending | Pending |
| P3 | Pending | Pending | Pending |

After the sessions, replace “Pending” with evidence, summarize completion by task, rank new findings, and link any resulting fixes. Until then, DEMO-30 remains in progress and this document supports only an internal prototype walkthrough.


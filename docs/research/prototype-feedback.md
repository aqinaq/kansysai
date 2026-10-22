# FE-07: Prototype Evaluation

**YouTrack:** [DEMO-30](https://ai-kanban-thesis.youtrack.cloud/issue/DEMO-30)  
**Evaluation date:** 22 October 2026  
**Artifact evaluated:** FE-04 interactive browser prototype (`prototype/index.html`)  
**Status:** Three independent participant sessions documented; teammate review pending.

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

The results above came from one internal evaluator, so they are separate from the three independent participant accounts below. The participant accounts below include task-completion counts, hesitation, and assistance notes. Simulated AI and voice controls were assessed only as interface flows; transcription and task-extraction accuracy were outside this evaluation.

## Evidence and follow-up

The evaluated prototype is [prototype/index.html](../../prototype/index.html); its [README](../../prototype/README.md) explains the preset commands and simulated voice and AI. Reference screens: [board](../../screenshots/02-kanban-board.jpg), [proposal review](../../screenshots/05-ai-preview.jpg), [task clarification](../../screenshots/06-clarification-task.jpg), and [assignee clarification](../../screenshots/07-clarification-assignee.jpg). These are prototype screenshots, not participant evidence.

A second internal check on 22 October started from a fresh board with six tasks. The “Several tasks” preset generated two proposals. After deselecting the second, confirming added one task and the board displayed seven tasks. The assistant screen visibly labelled the AI and audio as a demo. This repeated the existing walkthrough; it was not an independent participant session.

### Prioritized changes from internal walkthrough

| Priority | Change | Reason and acceptance check |
| --- | --- | --- |
| 1 | Preserve edits when resolving an ambiguous target task, or require target selection before editing. | F1 can silently discard a user change. Reopen the preview after choosing a target and check that the entered title remains visible until the user confirms or cancels. |
| 2 | Replace the fixed 23 October 2026 sample deadline with a future-relative example. | F2 will soon show an expired date. Repeat the multiple-task sample on a later day and check that its proposed deadline is still in the future. |
| 3 | Make the shared demo board explicit at project selection until project-specific boards exist. | F3 may suggest project isolation that the prototype does not provide. Open both project cards and check that the explanation matches the data shown. |

The earlier role-based simulated walkthroughs are useful prompts for what to observe, but their student, team-lead, and coordinator personas do not count as three participants. The current demo label addresses part of the concern that people might mistake preset responses for live AI; whether actual users notice it remains untested.

## Independent participant feedback (21–22 October 2026)

Akbope confirmed that P1, P2, and P3 were three different people outside the diploma team. Each tried the prototype individually and attempted all five tasks. P1 tested on 21 October 2026; P2 and P3 tested on 22 October 2026. Before testing, all three were told that voice input and AI responses were simulated.

Each participant was asked to: (1) find the core screens task on the board; (2) edit its deadline; (3) use the “Several tasks” example and select which proposals to add; (4) resolve the ambiguous diagram task; and (5) resolve an unknown assignee and finish creating the proposed task. “Without help” means the participant completed the task without a facilitator prompt. These were prototype flows with preset assistant responses, not tests of live transcription or AI extraction.

### Task outcomes and observed behavior

| Participant | Tasks completed without help | Hesitation or assistance observed |
| --- | --- | --- |
| P1 | 1, 2, 3, and 5 — 4 of 5 | At task 4, two diagram tasks matched. P1 needed a prompt to read both choices before selecting one. |
| P2 | 1, 2, 3, 4, and 5 — 5 of 5 | At task 3, P2 paused to check whether deselecting a proposal would keep it off the board. No help was given. |
| P3 | 1, 2, and 4 — 3 of 5 | At task 3, P3 needed help finding the selection checkbox. At task 5, P3 chose Unassigned, closed the preview without confirming, and the task was not created. |

**P1 — board and clarification.** P1 found the core screens task, changed its deadline, saved, and checked that the new date appeared on the board. As a first-time Kanban user, P1 said the To do, In progress, and Done columns made task progress understandable. P1 expected to drag a card between columns for a quick status update and found editing its status inside the card slow. When two diagram tasks matched the assistant command, P1 was unsure which to choose until prompted to compare them.

**P2 — reviewing proposals.** P2 found and edited the core screens task without help. In the “Several tasks” flow, P2 checked the assignee and deadline on both proposals, deselected the second, and paused to verify what deselection would do. After confirming, only the selected task appeared on the board. P2 also completed the diagram and unknown-assignee tasks without help. P2 said a short description on each proposal would make the confirmation decision easier.

**P3 — selection and final confirmation.** P3 found and edited the core screens task. In the multiple-task preview, P3 did not notice the selection checkbox and needed it pointed out. P3 resolved the diagram clarification without help. In the unknown-assignee flow, P3 chose Unassigned and returned to the preview, then closed it believing the action was finished. The task was absent from the board. P3 asked for a more noticeable final Confirm step and an explanation that choosing an assignee only updates the preview.

### Interpretation and proposed changes

The following are product interpretations of the observations above; the participant actions and comments are recorded separately above.

- **F4 — Direct board status change (P1).** Provide drag-and-drop between To do, In progress, and Done for quick updates. Check that the card moves to the destination column and its status changes. Keep the task-details status control for deliberate edits and keyboard access.
- **F5 — Proposal description (P2).** Show a short description for each proposed task before confirmation, so users can judge what will be created. Confirm that descriptions of unselected proposals are not saved.
- **F6 — Disambiguation context (P1).** Show available identifying details alongside similar task names during clarification, such as project or board section, current status, and deadline. Do not imply separate project data where the shared-board demo has none.
- **F7 — Proposal selection visibility (P3).** Make the selection control and its effect clear in each proposal. Check that users can find it without a prompt and understand that unselected tasks will not be added.
- **F8 — Final confirmation clarity (P3).** Make Confirm prominent after assignee selection, and state that the choice only updates the proposal until confirmation. Check that a user who chooses Unassigned understands that the task has not yet been created and can complete the flow.

### Priority and follow-up

| Priority | Finding | Reason |
| --- | --- | --- |
| 1 | F8 — final confirmation clarity | P3 left task 5 unfinished and the task was not created. |
| 2 | F1 — preserve edits during clarification | The internal walkthrough found that a typed change can be silently lost. |
| 3 | F7 — proposal selection visibility | P3 needed help finding a required control in task 3. |
| 4 | F6 — disambiguation context | P1 needed a prompt in task 4 to compare similar choices. |
| 5 | F5 — proposal description | P2 completed the flow but wanted more information before confirming. |
| 6 | F4 — drag-and-drop status updates | P1 requested a faster routine status change; the current card editor worked. |
| 7 | F2 — future-relative sample deadline | The fixed sample date will become stale after 23 October. |
| 8 | F3 — shared-board explanation | Clarify the prototype shortcut until project-specific boards exist. |

No prototype UI change is included in this evaluation report. The five tasks, outcomes, and improvement priorities provide input for follow-up frontend issues. The three-participant minimum has been met. Teammate review and PR merge remain before closing DEMO-30.

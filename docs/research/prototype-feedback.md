# FE-07: Prototype Evaluation

**YouTrack:** [DEMO-30](https://ai-kanban-thesis.youtrack.cloud/issue/DEMO-30)  
**Evaluation date:** 22 October 2026  
**Artifact evaluated:** FE-04 interactive browser prototype (`prototype/index.html`)  
**Status:** Three independent participant sessions reported; detailed task outcomes remain incomplete.

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

The results above came from one internal evaluator, so they are separate from the three independent participant accounts below. The supplied participant accounts do not include task-by-task completion counts or full hesitation notes. Simulated AI and voice controls were assessed only as interface flows; transcription and task-extraction accuracy were outside this evaluation.

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

Akbope confirmed that these accounts came from three different people outside the diploma team. Each tried the prototype individually and attempted the same five tasks. One session was on 21 October 2026 and two were on 22 October 2026. The notes did not specify which account was from 21 October, so the date-to-participant mapping remains unverified. The reported highlights are assigned P1, P2, and P3 in the order supplied.

The common tasks were: find a board task; open and edit it; propose multiple tasks with a sample command; review and confirm selected proposals; and resolve a missing assignee or ambiguous task. The supplied accounts do not state each task's success or failure, whether help was needed, or whether participants were told in advance that voice and AI are simulated. These details should be added from session notes rather than inferred from the highlights.

| Participant | Session date | Reported observation | Requested improvement | Completed without help (of 5) |
| --- | --- | --- | --- | --- |
| P1 | 21 or 22 October; mapping unverified | First-time Kanban user found To do, In progress, and Done understandable. Opened a card and found its status control. Changing status through task details felt slow for a routine update. | Drag a card directly to another status column while retaining the task-details editor. | Not recorded |
| P2 | 21 or 22 October; mapping unverified | Tried the “Several tasks” sample. Reviewed two proposals with titles, assignees, and deadlines, and saw that a proposal could be unchecked. The review step felt clear and gave control. | Show a short task description in each proposal before confirmation. | Not recorded |
| P3 | 21 or 22 October; mapping unverified | Tried moving “the diagram task” to Done. The assistant offered two similar tasks; after a choice, the proposed status change could be reviewed. Current status and deadline helped distinguish the options. | Show more identifying context when choosing between similar tasks, where that context exists. | Not recorded |

### Findings from the participant accounts

- **F4 — Direct board status change.** P1 reported that opening a card, changing its status, and saving took too many steps for a quick update. Proposed change: support dragging a card between To do, In progress, and Done. Check that the card appears in the destination column and task details show the new status. Keep the details status control for deliberate edits and keyboard access. The current prototype resets on reload by design.
- **F5 — Proposal description.** P2 valued reviewing and deselecting proposals before confirmation but wanted more context. Proposed change: show a short, editable description for each proposal. Check that it appears before confirmation and is saved only for selected, confirmed tasks.
- **F6 — Disambiguation context.** P3 valued the clarification step but had to read similar diagram task names carefully. Proposed change: include an available project name or board section alongside the current status and deadline. Do not invent separate project data in the current shared-board demo.

**Provisional priority:** F1 lost edits during clarification; F4 direct board status change; F5 proposal descriptions; F6 clearer disambiguation; F2 future-relative demo deadline; F3 shared-board explanation. This order combines an internal defect with participant suggestions and should be revisited once task outcomes are recorded.

## Remaining evidence for DEMO-30

Three independent participant accounts and their qualitative feedback are documented anonymously. Add the task-by-task outcomes for P1–P3, hesitation and assistance notes, and whether the simulation was explained before each test. Keep observations separate from interpretations and update the priority order if the fuller results change it. DEMO-30 should remain In Progress until those records and teammate review are complete.

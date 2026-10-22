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

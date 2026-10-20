# FE-04 — Core screens and user flows

Open `index.html` in a browser. No installation, build, API key, or internet connection is required.

## Screens
1. Workspace and project selection
2. Kanban board with search
3. Task details and editing
4. Voice/text command input
5. Editable preview of several proposed tasks or changes
6. Clarification for an unknown assignee or ambiguous task

## Presentation walkthrough
- Choose Diploma project.
- Open Ask your assistant. Choose the Several tasks sample, then Generate preview.
- Edit the proposed title, assignee or deadline; deselect an action if needed.
- Confirm selected actions. Confirmed tasks appear on the board.
- Use the ambiguous change sample, select the intended diagram, inspect the status change, then confirm.
- Use the unknown assignee sample, choose a teammate or Unassigned, return to the preview and confirm.
- Click a board card, edit its fields and save.

## Prototype boundaries
AI output and voice recording are simulated and labeled. Sample commands are supported; this is not a speech recognition or language model implementation. Project selection is illustrative and shares one demo board. All edits are kept in memory and reset on reload. No GitHub or YouTrack data is changed by using this prototype.

## Browser checks
Verified in Chrome: initial screen, board, multiple-task confirmation, ambiguous-task clarification and return to preview, unknown-assignee clarification, unassigned-task creation, and task priority editing. Desktop layouts visually inspected. Mobile CSS is included but not browser-verified.

## Visual direction 02
Purple and lavender palette; Avenir Next with system fallbacks and italic Georgia display accents. Landing page includes an animated waveform, floating board illustration, orbit details, feature links, and an interactive three-step walkthrough. Motion respects prefers-reduced-motion. The workspace logo returns to the landing page. Verified landing step switching, opening the AI preview, and confirming its two tasks into the board after the redesign.

# User interviews: turning conversations into tasks

## Purpose
Understand how potential users record tasks from voice messages or meetings, what can go wrong, and what they would check before accepting AI-suggested tasks.

## Method
Three participants answered the same five questions. Participants are identified only as P2, P4, and P5. These are interview findings, not results from testing the prototype.

## Questions
1. What happened the last time you received tasks through a voice message or meeting?
2. Where do you record tasks now?
3. Have you misunderstood or missed a task? What happened?
4. Can one message contain several tasks? How do you identify the owner and deadline?
5. What would you check before adding AI-suggested tasks?

## Participant notes

### Student
- Received tasks through voice messages and saved them in Telegram Saved Messages; sometimes also uses a notebook.
- Has misunderstood tasks when the goal was unclear and asked a teacher or classmates for clarification.
- Said that when one voice message contains several tasks, it can be difficult to tell who should do what and when.
- Does not like the idea of automatically creating tasks from voice messages. Would check the original message, task details, and deadline before adding a suggested task.

### Employee in a small team
- Received tasks in a daily office meeting, wrote down key points, clarified unclear details, and added tasks to a to-do list.
- Their team lead records tasks on a YouTrack project board with owners, deadlines, and other details.
- Once misunderstood which course flow to test; checked with the team and corrected the task before starting.
- Said a developer's message can contain several tasks. Confirms each owner and deadline when these are unclear.
- Would check accuracy, completeness, assignee, and deadline before accepting suggested tasks.

### Project manager
- Received tasks during a meeting about an event, wrote them down, and contacted contractors afterward.
- Records tasks in notes, messages, or Excel tables.
- Sometimes misunderstands details or deadlines and asks a manager to clarify.
- Said one message can contain several tasks. Separates them and checks the owner and deadline of each.
- Would check that suggested tasks are correct and clear, with the right deadlines and responsible people.

## Findings supported by these interviews

1. **Task details need clarification.** All 3 participants described misunderstanding a task or checking unclear details with another person.
2. **People record tasks in different places.** Participants mentioned Telegram Saved Messages, a notebook, a to-do list, YouTrack, notes, messages, and Excel. We should not assume everyone already uses a Kanban board.
3. **Multiple tasks in one conversation matter.** P4 and P5 described separating several tasks from one message; P2 said this situation can make ownership and deadlines difficult to understand.
4. **Review before saving is essential.** All 3 would check suggested task details before accepting them. P2 specifically wants to check the original message and is uncomfortable with automatic task creation.

## Implications for the proposed system
- Show the original message or transcript alongside suggested tasks.
- Allow several separate task suggestions from one message.
- Make assignee and deadline visible and editable for each suggestion.
- Ask for clarification when important details are ambiguous.
- Require explicit user confirmation before adding tasks to the board.

## Limitations
These are three individual accounts, not a representative survey. P4 and P5 described meeting tasks; P2 described voice messages. The interviews show a relevant workflow and concerns, but they do not establish how often the problems occur across all users.

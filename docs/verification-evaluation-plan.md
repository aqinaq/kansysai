# Product Verification and Evaluation Plan

**Issue:** DEMO-34
**Status:** Draft for team review  
**Owners:** Akbope Bakytkeldy (product and frontend); Symbat Saparbay (backend and AI)

## 1. Purpose

This plan defines how the team will check the requirements in [Product Requirements and User Stories](product-requirements.md). It covers usability, manual task management, the eight AI actions, speech input, permissions, failures, and performance.

A planned test is not an achieved result. Each implementation test below has the status **Not run** until its actual result and evidence are recorded.

## 2. Evidence available now

The FE-04 browser prototype uses preset assistant responses and simulated voice input. It does not test live speech recognition, AI extraction, a persistent backend, or production permissions.

Three independent participants tested the prototype individually on 21–22 October 2026. All were told that voice and AI were simulated and attempted the same five tasks. Tasks completed without help were P1 **4/5**, P2 **5/5**, and P3 **3/5**. The observations, assistance notes, and proposed improvements are in the [FE-07 evaluation report](https://github.com/aqinaq/kansysai/pull/23). These are prototype usability results, not results for the full application.

## 3. Responsibilities

| Area | Owner | Responsibility |
| --- | --- | --- |
| Product | Akbope | Map user stories to scenarios; define expected user outcomes and the manual baseline. |
| Frontend | Akbope | Check task flows, review and confirmation screens, accessibility of controls, and loading, empty, success, and error states. |
| Backend | Symbat | Check data validation, persistence, permissions, duplicate prevention, task history, and notifications. |
| AI and speech | Symbat | Prepare command and audio datasets; measure transcription, intent and field extraction, response time, and safe handling of uncertainty. |
| Final review | Both | Review test coverage, thresholds, results, limitations, and conclusions. |

## 4. Test conditions and data

Before running implementation tests, record:

- Application version or Git commit, environment, browser, device, and test date.
- Test accounts with different project memberships and permissions.
- At least two workspaces and two projects, including a project inaccessible to one test account.
- Tasks with distinct and similar titles, different statuses, priorities, assignees, and deadlines.
- A fixed reference date and timezone for relative deadline tests.
- Audio and text samples in Kazakh, Russian, English, and mixed language.
- Expected transcripts, intents, task fields, and actions prepared before viewing system output.
- Whether an external speech or AI service was available during the test.

Use non-sensitive sample data. Reset the test database or record its starting state so that board counts and changes can be checked.

## 5. Measures

| Measure | How to record it |
| --- | --- |
| Task completion | Completed without help / attempted tasks, plus assisted and failed tasks separately. |
| Usability problems | Where the participant hesitated, asked for help, made an error, or misunderstood the result. |
| Manual baseline time | Time from opening manual task creation to seeing the saved task on the board. |
| Assistant workflow time | Time from submitting a command to seeing the confirmed task or change on the board. Record review and correction time. |
| Transcription quality | Word error rate or character error rate against a prepared reference transcript, reported by language. |
| Intent recognition | Correct action classification / evaluated commands, reported by action and language. |
| Field extraction | Precision and recall for title, assignee, deadline, priority, status, and task target, using a labelled dataset. |
| Response time | Median and 95th-percentile time from submission to preview; separately measure confirmation to saved result. |
| Confirmation safety | Count data-changing actions made before confirmation. Expected: **zero**. |
| Permission safety | Count unauthorized reads or writes that succeed. Expected: **zero**. |
| Duplicate prevention | Count additional tasks or changes caused by confirming or retrying the same request. Expected: **zero**. |

The team must agree on numerical targets for transcription, extraction, and response time **before** judging final results. Record the dataset size alongside every percentage.

## 6. Manual task-entry baseline

For the same prepared assignment, a participant will create tasks through the normal task form without using the assistant. Record the number of tasks, fields entered, completion time, corrections, errors, and whether the final board state matches the prepared expected result.

Repeat with the assistant workflow using equivalent input. Compare the workflows on the same task set and report the number of participants and attempts. This comparison is **planned; no baseline measurement has been run yet**.

## 7. Planned verification cases

All cases below are **Not run**. Record the actual result, pass/fail decision, and evidence when each case is performed.

| ID | User story | Scenario and expected result | Primary owner |
| --- | --- | --- | --- |
| V01 | US-01 | Register and log in with valid details; the user reaches their permitted workspace. | Symbat |
| V02 | US-01 | Use invalid credentials and open a protected URL while logged out; show an error and deny access. | Symbat |
| V03 | US-02 | Create a workspace and project; the project belongs to the selected workspace. | Akbope + Symbat |
| V04 | US-02, US-16 | Sign in as a user without project access; the project is not listed or readable. | Symbat |
| V05 | US-03 | Add a project member and assign a task to that member; both changes are shown. | Symbat |
| V06 | US-03 | Try to change membership or assign a non-member without permission; reject the action. | Symbat |
| V07 | US-04 | Create and edit a task manually; validate its title and show saved fields on the board. | Akbope + Symbat |
| V08 | US-04 | Request task deletion; require confirmation and permission before removal. | Akbope + Symbat |
| V09 | US-05 | Move a task to another valid column; its saved status remains correct after reload. | Akbope + Symbat |
| V10 | US-06 | Add a comment and change a task; show comment author/time and a correct history entry. | Akbope + Symbat |
| V11 | US-07, US-14 | Submit English audio; show processing, transcript, and an option to correct it. | Symbat |
| V12 | US-07, US-14 | Submit Kazakh audio; compare the transcript with a prepared reference. | Symbat |
| V13 | US-07, US-14 | Submit Russian audio; compare the transcript with a prepared reference. | Symbat |
| V14 | US-07, US-14 | Submit mixed-language audio; compare the transcript with a prepared reference. | Symbat |
| V15 | US-07 | Submit unsupported or failed audio; show a clear error and save no task. | Akbope + Symbat |
| V16 | US-08 | Enter a text command to create one task; show editable extracted fields and save only after confirmation. | Akbope + Symbat |
| V17 | US-08 | Use corrected voice transcription to create a task draft; use the corrected text for extraction. | Symbat |
| V18 | US-09 | Request several tasks in one message; create separate drafts and save only the selected, confirmed drafts. | Akbope + Symbat |
| V19 | US-10 | Update an existing task with two similar matches; require target selection and final confirmation. | Akbope + Symbat |
| V20 | US-11 | Use **Change Status**; reject invalid values and save a valid value only after confirmation. | Symbat |
| V21 | US-11 | Use **Assign User**; allow a project member and reject an invalid or inaccessible assignee. | Symbat |
| V22 | US-11 | Use **Change Deadline** with a relative date; interpret it using the recorded reference date and timezone. | Symbat |
| V23 | US-11 | Use **Change Priority**; reject invalid values and require confirmation. | Symbat |
| V24 | US-12 | Use **Search Tasks** with a filter and with no matches; return accessible records or an empty-result message. | Symbat |
| V25 | US-13 | Use **Project Summary**; summarize only records accessible to the current user. | Symbat |
| V26 | US-13 | Summarize meeting input and show action items as drafts; do not create them before confirmation. | Symbat |
| V27 | US-13, US-15 | Give a command with a missing assignee or unclear deadline; show missing information without inventing a value. | Akbope + Symbat |
| V28 | US-15 | Give an unrelated command; explain the limitation and make no data change. | Akbope + Symbat |
| V29 | US-16 | Attempt a manual or AI write in a project without access; the backend rejects it. | Symbat |
| V30 | US-16 | Search and summarize as a user lacking access; exclude inaccessible task data. | Symbat |
| V31 | US-16 | Guess another project or task identifier; the backend still denies access. | Symbat |
| V32 | US-17 | Confirm the same create request twice; only one task is created. | Symbat |
| V33 | US-17 | Simulate an unavailable AI service or failed request; show failure and allow a safe retry. | Akbope + Symbat |
| V34 | US-18 | Trigger an agreed task-change or approaching-deadline notification; verify its timing, channel, and task reference. | Symbat |
| V35 | US-14 | Change the interface language among Kazakh, Russian, and English; check key screens and editable fields. | Akbope |
| V36 | US-08, US-10, US-11 | Cancel or close a data-changing preview; confirm that no task or field is changed. | Akbope + Symbat |

The eight required assistant actions are covered by V16/V18 (**Create Task**), V19 (**Update Task**), V20 (**Change Status**), V21 (**Assign User**), V22 (**Change Deadline**), V23 (**Change Priority**), V24 (**Search Tasks**), and V25 (**Project Summary**).

## 8. Result record template

Copy this record for each executed case:

| Field | Record |
| --- | --- |
| Case ID and requirement | |
| Date, tester, version, and environment | |
| Input and preconditions | |
| Expected result | |
| Actual result | Not run |
| Pass/fail | Not run |
| Evidence link or screenshot | |
| Defect or follow-up issue | |

## 9. Current limitations and decisions

The prototype can provide usability evidence for its displayed flows, but its preset responses cannot establish speech recognition accuracy, AI extraction accuracy, backend permission safety, persistence, or production response time.

Before implementation evaluation, the team must agree on project roles, supported audio formats and limits, timezone rules, notification behavior, data retention, and numerical AI/performance targets. Any feature that is unavailable during testing must be marked **Not implemented** rather than **Pass**.

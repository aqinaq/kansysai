# Supervisor Feedback and Decisions

**Supervisor:** Alibek Orynbek
**Team:** Akbope Bakytkeldy (product and frontend), Symbat Saparbay (backend and AI)

This document records the supervisor's comments on key deliverables, the decisions the team made in response, and where the resulting changes can be found. Only comments actually received from the supervisor are recorded here.

## Review 1 — Literature review and project direction

**Date received:** 20 October 2026
**Deliverable reviewed:** first literature review draft (commits `b29f627`–`6840e7f`, 12–14 October 2026)
**Form:** written requirements document sent to the team (original text in the appendix)

### Summary of the comments

| ID | Comment | Category |
|---|---|---|
| S1 | The work resembles the preparation of a research paper rather than development of a real IT product. A working system with real-world use cases is required, not only voice-to-text and a single Kanban card. | Project direction |
| S2 | The system must support registration, workspaces, projects and boards, members, task CRUD, assignees, deadlines, priorities, statuses, column movement, comments and history, voice and text commands, and notifications. AI must be integrated into real business processes. | Functional scope |
| S3 | Seven AI use cases must be supported: create a task by voice; several tasks from one message; change an existing task; change status; query project data; create tasks from meeting results; Kazakh, Russian, English and mixed speech. | AI scenarios |
| S4 | The AI pipeline must be Voice → STT → intent recognition → entity extraction → validation → user confirmation → backend action → Kanban update. Eight actions must be specified with inputs, response structure, validation and error handling. The AI must not change data without confirmation or when a command is ambiguous. | AI design |
| S5 | Technology choices (frontend, backend, database, STT, LLM, local or cloud AI, component interaction, voice storage and data protection) must be justified from a real-product perspective, including Kazakh recognition quality, speed, cost and scalability. | Technology |
| S6 | Quality requirements: access control, handling of ambiguous commands, no invented assignees, deadlines or tasks, duplicate prevention, handling of AI and API failures, action history, and correction of the transcript before saving. | Quality |
| S7 | At least 30 test scenarios with expected result, actual result and pass/fail status, covering AI quality and system operations. | Testing |
| S8 | Deliverables for the next stage: PRD, use case diagram, at least 15 user stories with acceptance criteria, system architecture, UI/UX prototype, database schema, API specification, working MVP, test cases and a demo video. | Deliverables |
| S9 | All work must be traceable in the repository and YouTrack: each task needs an owner, description, done criteria and evidence; regular commits; recorded test results. | Process |

### Decisions and resulting changes

| Comment | Team decision | Evidence | Status |
|---|---|---|---|
| S1 | Reframe the project from a research prototype to a product. Keep the literature review as supporting analysis, and base requirements on user needs and the supervisor's scenarios. | PRD `0f393a5` (DEMO-21, PR #8); README realigned `4de54e0` (DEMO-20, PR #5); proposal scope updated `62642fe` (PR #21) | Done for analysis and design; working MVP pending |
| S2 | Adopt the full functional scope as 18 user stories. Define an MVP boundary (Must / Should / Later) so that a working system can be delivered first without dropping any requirement from the planned product. | `docs/product-requirements.md` (DEMO-21, PR #8; revised in FE-08, PR #22) | Done (MVP priorities to be confirmed with the supervisor) |
| S3 | Map each case to requirements and design: Cases 1–2 → US-08, US-09; Case 3 → US-10, US-11; Case 4 → US-11; Case 5 → US-12; Case 6 → US-13; Case 7 → US-14. Use the cases as comparison criteria for existing systems. | PRD; existing-system comparison criteria C3–C7 (`docs/be-02/BE02.pdf`, `849df8c`) | Done |
| S4 | Specify the eight actions in the API, with a common action-plan schema, validation, clarification and confirmation rules, and an idempotent confirm endpoint. | `docs/be-06/BE06.pdf` (DEMO-32, PR #17); use-case overview and AI action coverage (FE-05, PR #11) | Done |
| S5 | Compare 2–3 alternatives for each key decision. Selected: self-hosted Whisper with a Kazakh model and cloud fallback; cloud LLM with a local mode behind one interface; React; FastAPI; PostgreSQL; REST + WebSocket + Redis job queue; private object storage for audio. | `docs/be-03/BE03.pdf` (DEMO-22; `7e00217`, `0067acf`); STT benchmark script (`6671640`) | Done; STT choice provisional until the benchmark is run |
| S6 | Include each rule in the user stories, the quality requirements and the API (permissions, clarification, no invented values, idempotent confirmation, error format, audit history, transcript correction). | PRD US-15–US-17 and section 9; BE-06 integrity rules and error format | Done in design; to be verified in the MVP |
| S7 | Prepare 36 verification cases mapped to user stories, including all eight AI actions, all languages, mixed speech, permissions and duplicates, with a result template (expected, actual, pass/fail). | `docs/verification-evaluation-plan.md` (FE-09 / DEMO-34, PR #24) | Plan done; cases not run yet |
| S8 | Deliver the design artifacts before implementation. | PRD; use case overview (PR #11); architecture BE-04 and BE-05; prototype (FE-04, PR #10); BE-06 schema and API; test plan (PR #24) | Done: PRD, use cases, user stories, architecture, prototype, schema, API, test cases. Pending: working MVP, demo video |
| S9 | Track work in YouTrack (project DEMO); use task branches, pull requests with teammate review and the task ID in branch names and commits. | Git history and YouTrack project DEMO | In progress: early commits lack task IDs; see the ID mapping in the project plan |

### Open points to confirm with the supervisor

1. MVP priorities (Must / Should / Later) in the PRD.
2. Numerical quality targets and AI baselines (WER per language, intent accuracy, field F1, invented-value rate, response time).
3. Whether the team may use GitHub instead of GitLab (the feedback mentions GitLab; the diploma repository requirements allow either).

## Appendix — Original feedback text

> Тема: Development of an Intelligent Kanban System with an AI Assistant for Automatic Task Generation from Voice Messages
>
> Цель: Разработать полноценную интеллектуальную систему управления задачами на основе Kanban с AI-ассистентом, которая позволяет создавать и управлять задачами с помощью голосовых и текстовых команд.
>
> **1. Основное требование**
> Я ознакомился с вашим Literature Review. Сейчас ваша работа больше напоминает подготовку научной статьи, чем разработку реального IT-продукта.
> Мне необходимо увидеть работающую систему с реальными сценариями использования (real-world use cases).
> Представьте, что вы разрабатываете коммерческий продукт, которым будут пользоваться сотрудники компаний, руководители проектов, преподаватели и студенты.
> Не ограничивайтесь демонстрацией преобразования голоса в текст и создания одной Kanban-карточки.
>
> **2. Основные функциональные требования**
> Система должна поддерживать: регистрацию и авторизацию пользователей; создание рабочих пространств (Workspaces); создание проектов и Kanban-досок; добавление участников в проекты; создание, редактирование и удаление задач; назначение ответственных исполнителей; установку сроков, приоритетов и статусов; перемещение задач между колонками Kanban; комментарии и историю изменений; голосовое и текстовое управление задачами через AI-ассистента; уведомления об изменениях и приближающихся сроках.
> AI должен быть интегрирован в реальные бизнес-процессы системы, а не существовать как отдельная демонстрационная функция.
>
> **3. Реальные сценарии использования AI**
> Case 1. Создание задачи голосом: «Создай задачу для Данияра: подготовить презентацию проекта до пятницы, высокий приоритет». Система должна автоматически распознать речь, определить намерение пользователя, извлечь название задачи, исполнителя, срок и приоритет, найти Данияра среди участников проекта, показать пользователю предварительную карточку и после подтверждения создать задачу на Kanban-доске. Если система не находит исполнителя, она должна предложить выбрать его, а не придумывать данные.
> Case 2. Несколько задач из одного голосового сообщения: «Али должен закончить frontend до среды, Данияр проверить API до четверга, а Аружан подготовить документацию до пятницы». AI должен распознать три самостоятельные задачи, определить исполнителей и сроки и предложить создать три карточки.
> Case 3. Изменение существующей задачи: «Перенеси дедлайн задачи по авторизации на следующий понедельник и поменяй приоритет на высокий». AI должен найти соответствующую задачу, предложить изменения и после подтверждения обновить её. Если найдено несколько похожих задач, система должна запросить уточнение.
> Case 4. Управление статусом: «Задача по интеграции платежной системы завершена». AI должен найти соответствующую задачу и предложить переместить её в колонку Done.
> Case 5. Получение информации о проекте: «Какие задачи у нашей команды просрочены?» AI должен получить реальные данные из базы и показать список просроченных задач с ответственными и сроками. Нельзя генерировать вымышленные задачи или сроки.
> Case 6. Создание задач из итогов совещания: «Сегодня договорились, что Данияр подготовит API до четверга. Аружан сделает дизайн до пятницы. На следующей неделе нужно провести тестирование приложения». AI должен определить конкретные поручения, выделить отдельные задачи и показать, где отсутствуют необходимые сведения. Для задачи по тестированию, например, нужно запросить ответственного, если он не указан.
> Case 7. Многоязычные голосовые команды: система должна обрабатывать команды на казахском, русском и английском языках. Пример: «Даниярға ертеңге дейін API тексеру тапсырмасын бер». Система должна распознать задачу, определить исполнителя и срок. Отдельно проверьте смешанную речь, когда пользователь использует казахские, русские и английские технические термины в одном сообщении.
>
> **4. Требования к AI-компоненту**
> Необходимо реализовать последовательность: Voice Input → Speech-to-Text → Intent Recognition → Entity Extraction → Validation → User Confirmation → Backend Action → Kanban Update.
> AI должен поддерживать следующие действия: Create Task, Update Task, Change Status, Assign User, Change Deadline, Change Priority, Search Tasks, Project Summary.
> Для каждого действия необходимо определить входные параметры, структуру ответа, правила проверки и обработку ошибок.
> Критически важно: AI не должен самостоятельно изменять данные, если команда неоднозначна или пользователь не подтвердил действие.
>
> **5. Выбор технологий**
> Вы самостоятельно выбираете технологический стек, но должны обосновать решения с точки зрения реального продукта. Необходимо определить: Frontend и Backend; базу данных; Speech-to-Text сервис; LLM для обработки команд; локальное или облачное развертывание AI; архитектуру взаимодействия компонентов; способ хранения голосовых сообщений и защиты пользовательских данных.
> При выборе AI-сервисов учитывайте качество распознавания казахского языка, скорость обработки, стоимость, масштабируемость и возможность дальнейшего развития продукта.
>
> **6. Обязательные требования к качеству**
> Необходимо предусмотреть: проверку прав доступа к проектам и задачам; корректную обработку неоднозначных команд; запрет на выдумывание исполнителей, сроков и задач; защиту от случайного повторного создания задач; обработку ошибок AI и недоступности API; сохранение истории действий пользователей; возможность исправить результат распознавания до сохранения.
>
> **7. Тестирование продукта**
> Подготовьте минимум 30 тестовых сценариев, включая: простые голосовые команды; несколько задач в одном сообщении; казахский, русский и английский языки; смешанную речь; ошибки распознавания; отсутствующих исполнителей; неоднозначные сроки; попытки изменить чужие задачи; команды, не связанные с управлением задачами.
> Проверьте не только качество AI, но и правильность выполнения операций в системе. Для каждого сценария покажите ожидаемый результат, фактический результат и статус прохождения теста.
>
> **8. Ожидаемый результат**
> К следующему этапу разработки необходимо представить: Product Requirements Document (PRD) — описание продукта, пользователей, основных функций и ограничений; Use Case Diagram — сценарии взаимодействия пользователей с системой; User Stories — минимум 15 историй пользователей с критериями приемки; System Architecture — архитектуру Frontend, Backend, Database и AI; UI/UX Prototype — интерактивный прототип основных экранов; Database Schema — структуру базы данных; API Specification — описание основных API; Working MVP — работающий прототип с Kanban-доской и созданием задач через голосовые команды; Test Cases — не менее 30 сценариев проверки; Demo Video — видеодемонстрацию реального использования системы.
>
> **9. Организация разработки**
> Весь процесс должен быть отражён в GitLab и YouTrack. Каждая задача должна иметь ответственного, описание, критерии готовности и подтверждение выполнения. Необходимо регулярно делать коммиты, вести историю изменений и фиксировать результаты тестирования. Цифровой след обязателен. Я должен видеть, кто, что и когда разрабатывал.
>
> **10. Критерии оценки**
> Основной акцент при оценке будет сделан на: реальной работоспособности программного продукта; полноте реализованных пользовательских сценариев; качестве интеграции AI с Kanban-системой; удобстве использования; надёжности и безопасности; качестве архитектуры и исходного кода; реальных результатах тестирования; индивидуальном вкладе каждого участника команды.
> Главная задача — не просто показать, что AI умеет распознавать речь, а продемонстрировать, как AI помогает пользователю управлять реальными проектами и задачами.
> На защите я хочу увидеть не презентацию о возможностях системы, а работающий продукт: пользователь произносит команду, система её понимает, выполняет соответствующее действие и показывает результат на Kanban-доске.

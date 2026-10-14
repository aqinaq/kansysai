# Literature Review

**Project:** Development of an Intelligent Kanban System with an AI Assistant for Automatic Task Generation from Voice Messages  
**YouTrack:** DEMO-20  
**Document status:** Research draft for team review  
**Reviewed material:** 12 PDFs collected by the project team
## Project Title
Development of an Intelligent Kanban System with an AI Assistant
for Automatic Task Generation from Voice Messages

## 1. Introduction

Existing task management systems usually make people type out titles, descriptions, dates, etc. of tasks. The proposed system will be based on a different approach: the user records a message, ASR generates the transcript, AI finds actionable information in it, and then backend verifies a draft task that the user can review and add to the Kanban board.

The literature has been structured in accordance with three different search techniques that were applied to gather the papers: (1) broad concept-based, (2) narrow context-, method-, or language-based search, and (3) search based on adjacent techniques and technical issues. It should be noted that these labels refer to the way **the team conducted its search**, not the classifications made by the authors of the articles.

## 2. Research questions

1. How can AI support task-management and workflow automation?
2. Which ASR approaches merit evaluation for voice messages, especially in Kazakh?
3. How can task intent and fields such as title, due date, and assignee be extracted from spoken language?
4. How can a backend avoid storing incomplete or fabricated task information?
5. How should accuracy and reliability be evaluated before a Kanban card is created?

## 3. Search strategy and scope

There were three kinds of queries that the team implemented:

- **Type 1 – Broad terms:** AI-assisted task management, NLP-based project management, and autonomous workflow optimization.
- **Type 2 – Narrow terms or methods:** ASR in Kazakh, spoken task-oriented dialogue, intent detection, slot filling, action item extraction in meetings, and structured LLM output.
- **Type 3 – Related terms and contradictions:** API argument filling, speech-NLP integration, and structured hallucinations.

**Filtering strategy:** We filtered the supplied PDFs by the research problem, suggested method, results achieved, limitations, and possible application in our project. This is a narrative review of literature but not a systematic one. The selected materials represent research between 2021 and 2026. Some publications require further verification.

## 4. Type 1 – Broad searches: AI and task-management systems

### [1] Lekkala and Bandari (2026): Autonomous Workflow Optimization Using Multi Agent AI Systems

- **Problems:** Fixed scheduling and manual work handoffs coordination cannot be easily adapted to fluctuating workloads.
- **Methods:** The authors suggest an autonomous multi-agent workflow approach utilizing reinforcement learning, work in process (WIP) coordination, and work handoffs coordination techniques.
- **Findings reported:** According to the abstract, there was a decrease in cycle time and WIP, high workstations utilization rate; in conclusion, the results for simulations and deployment are provided. **However, the WIP reduction rate differs between abstract (27%) and conclusion (49% in simulations). Such figures cannot be compared.**
- **Relevance:** Helps to understand the importance of workflow phases, handoffs, and WIP in systems like Kanban.
- **Limitation for our project:** Concentrates on manufacturing/service operations and multiple autonomous agents. Our project concerns automatic card creation based on user voice brief message. Multi-agent optimization **is not needed** for our MVP.

### [2] Adebanjo et al. (2026): Design and Implementation of an AI-Powered Task Management System

- **Problem:** Entering tasks manually and lack of intelligent assistance make task management less convenient.
- **Method:** TaskWise employs natural language processing capabilities, scheduling and reminders, React/Tailwind front-end, Firebase/Firestore back-end services and synchronization.
- **Findings:** The paper discusses usability improvements due to task automation and natural language processing.
- **Relevance:** Close analogy of the product under consideration. Can be considered when discussing user-friendly task creation and quick response after natural language input.
- **Limitations:** Reliance on internet-enabled Firebase services; rule-contextual AI rather than history-learning one; lack of collaborative space; web version only; small test group of students.
- **Our difference:** In our case we specifically look at **speech → transcription → task extraction → user confirmation → Kanban card** process and should test each step separately.

### [3] Chen et al. (2021): Smart Project Management: Interactive Platform Using Natural Language Processing Technology

- **Problem:** Communication and document processing problems experienced by project stakeholders.
- **Method:** Construction-specific contract keyword detection using a pipeline of PSENet, CRNN, and BRNN-CNN architectures.
- **Findings reported:** The authors provide an example of a platform that allows for real-time document processing and communication in construction contract management.
- **Relevance:** Illustration of how domain-specific NLP may help cut out manual extraction from unstructured project data.
- **Shortcoming in relation to our project:** Relies on text/document analysis and construction contracts instead of speech command recognition and Kanban task generation. Architecture not to be used blindly.

## 5. Type 2 — Narrow searches: speech understanding and structured task extraction

### [4] Weld et al. (2022): A Survey of Joint Intent Detection and Slot Filling Models in Natural Language Understanding

- **Problem:** A user request includes both overall intent and values necessary to carry out the request.
- **Approach:** Survey on joint intent classification and slot filling, metrics, data sets, and deep learning architecture.
- **Findings:** The survey focuses on the strong link between intent recognition and extraction of semantic slots.
- **Significance:** It provides a theoretical foundation for `create_task` intent detection and slots like `title`, `due_date`, and `assignee` extraction.
- **Drawback:** A survey of models and experiments carried out based on the models. Not an implementation or a benchmark for our Kanban topic. Some of the methods are outdated relative to modern LLMs.

### [5] Kozhirbayev (2023): Speech Recognition in Kazakh: Wav2vec2.0 vs. Whisper

- **Problem:** It is difficult to recognize speech in Kazakh due to possible lack of annotated data.
- **Method:** Comparative analysis of wav2vec2.0, wav2vec2-XLS-R, and Whisper in Kazakh speech recognition.
- **Reported findings:** The paper reports the results of wav2vec2.0: **WER 8.7 and CER 2.8** on their test set and also approximately **CER 4** for large Whisper; metrics and configuration should be checked before generalizing model ranking.
- **Relevance:** A priority paper to choose and test ASR on Kazakh voice messages.
- **Limitation:** Results obtained on the paper's dataset do not ensure the same performance on student microphones, informal speech, noisy conditions, or Kazakh/Russian speech mix.

### [6] Si et al. (2023): SpokenWOZ: A Large-Scale Speech-Text Benchmark for Spoken Task-Oriented Dialogue Agents

- **Problem**: Written dialogue benchmarks could miss actual spoken language issues.
- **Method**: SpokenWOZ dataset and experiment with spoken task-oriented dialogue. Dataset consists of **~5,700 dialogues, 203,000 turns and 249 hours of audio** from eight domains.
- **Reported findings**: Paper finds that current systems fail to deal with spoken dialogue, even state tracking and task accomplishment.
- **Relevance**: Calls for evaluation of real voice samples, disfluencies, transcription mistakes, and multi-step instructions, not just typed text.
- **Limitation**: Benchmark is about conversational dialogue, not card generation and not Kazakh language benchmark.

### [7] Tanaka & Thompson (2025): Using Multi-Agent Systems for Action Item Extraction from Meeting Transcripts: A Comprehensive Review

- **Problem**: Meeting transcripts contain conversation, decision-making, and commitments to action.
- **Approach**: Review of multi-agent systems and LLMs and how to extract action items from meeting transcripts.
- **Result / Claim**: Authors consider the advantages of decomposition of this process through cooperative agents.
- **Contribution**: Useful in formulating task identification problems, e.g., separating an instruction from an off-hand comment and separating multiple action items.
- **Limitations**: This is not a study but a review. Do not use it as empirical evidence without checking its venue and publication metadata.

### [8] Sun et al. (2024): Speech-based Slot Filling using Large Language Models

- **Problem:** ASR mistakes could adversely impact downstream value extraction from voice commands.
- **Method:** Speech-based slot filling through LLMs using prompting, LoRA-based noise-robust fine-tuning, and linearised knowledge injection, as applied to SLURP.
- **Reported findings:** Improved SLU-F1 of the proposed Vicuna model compared with baselines Flan-T5-XL in limited data and zero-shot scenarios.
- **Relevance:** Highly relevant to our approach – ASR output is prone to mistakes, which requires reliable value extraction.
- **Limitations:** Dataset and models used are different from our intended Kanban application.

### [9] Li, Ramprasad, and Zhang (2024): A Simple but Effective Method for Enhancing Structured LLM Output for Information Extraction

- **Problem:** LLM outputs are unreliable when an exact structured format is needed.
- **Method:** Generate-and-Organize (G&O), where the extraction process involves first generating content and then organizing it into the structured format; assessed via named entity recognition and relation extraction.
- **Results reported:** Improved structured information extraction is reported by the authors in their evaluation.
- **Relevance:** One way of achieving task JSON. The backend needs to perform schema validation as well, irrespective of the prompt.
- **Limitation:** Named Entity Recognition and relation extraction do not exactly correspond to task determination and relative deadlines from voice transcripts.

## 6. Type 3 — Adjacent solutions and contradictions

### [10] Mok et al. (2024): LLM-Based Solutions for API Argument Filling in Task-Oriented Conversational Agents

- **Problem:** Output from conversational LLMs could fail to conform to the required schema and the exact wording of the user utterance.
- **Solution:** Grounding and prompting/training solutions to facilitate API argument filling.
- **Reported results:** The authors provide positive results on the usage of grounding methods in the problem of API argument filling.
- **Relevance:** The extracted task should align with a predefined backend schema and faithfully reflect the wording of the user's request. This is important for correct dates, names, and task attributes.
- **Limitations:** This study focuses on task-oriented API argument filling, not on Kanban services nor our target languages.

### [11] Pal (2023): Natural Language Processing and Speech Recognition

- **Problem Statement:** ASR and NLP functionalities need to be considered as a whole for interaction systems.
- **Approach:** General introduction and comparisons of transformer models for ASR/NLP and benchmarking, with multilingual and noisy speech considerations.
- **Findings Reported:** The paper outlines the developments and trade-offs in the field of speech and language technologies.
- **Relation to Task:** Provides general context for designing an ASR+NLP/LLM pipeline, without relying on the assumption that transcription alone constitutes a valid task.
- **Limitations:** General overview with less direct evidence regarding the task formulation; independently verify the quality of the publication and comparisons.

### [12] Hoang (2026): Structured Hallucinations in Tool-Using Agents: Measuring and Reducing LLM Synthesis Corruption in Production

- **Problem**: The LLM can secretly corrupt structured values even if the response is a syntactically valid JSON or Markdown object.
- **Method**: A benchmark derived from a production environment, involving 200 iterations of LLM synthesis of travel API results, including different formats and the use of SSE metadata as the transport mechanism.
- **Reported Findings**: For this particular test, LLM-mediated output formatting resulted in corruption of the structured task fields; avoiding the unnecessary re-synthesis process allowed tool values to persist.
- **Relevance**: Useful caution that a valid JSON object does **not** ensure correct task field values. Preserve the transcript, validate the output, and have users confirm fields in question.
- **Limitation**: Only one deployment and tested model; concerned with *reformatting structured tool outputs*, rather than extracting the information from an audio message. Errors are not generalizable to our use case.

## 7. Comparison of all 12 sources

| No. | Search type | Publication (year) | Main approach | Main value for our project | Main applicability limit |
|---|---|---|---|---|---|
| 1 | Broad | Lekkala & Bandari (2026) | Multi-agent workflow optimization | WIP and task-handoff concepts | Operations, not voice-to-task |
| 2 | Broad | Adebanjo et al. (2026) | NLP-enabled TaskWise platform | Comparable task-management product | Small evaluation; limited collaboration |
| 3 | Broad | Chen et al. (2021) | NLP and contract keyword detection | Domain-focused information extraction | Construction documents |
| 4 | Narrow | Weld et al. (2022) | Survey of intent and slot models | Intent and task-field design | Not a task-generation experiment |
| 5 | Narrow | Kozhirbayev (2023) | Kazakh ASR model comparison | Candidate ASR models and WER/CER | Domain and recording conditions vary |
| 6 | Narrow | Si et al. (2023) | SpokenWOZ benchmark | Realistic speech evaluation cases | Different domains/languages |
| 7 | Narrow | Tanaka & Thompson (2025) | Action-item extraction review | Multiple tasks and indirect commitments | Review, not a Kanban implementation |
| 8 | Narrow | Sun et al. (2024) | LLM slot filling under noisy ASR | Robust extraction from transcripts | Different dataset/models |
| 9 | Narrow | Li et al. (2024) | Generate and Organize (G&O) | Structured output strategy | Tested on NER/RE |
| 10 | Adjacent | Mok et al. (2024) | Grounded API argument filling | Faithfulness to schema and user text | Not Kanban-specific |
| 11 | Adjacent | Pal (2023) | ASR/NLP technology overview | End-to-end speech and language context | Broad review, verify claims |
| 12 | Adjacent | Hoang (2026) | Structured hallucination benchmark | Field fidelity and validation risks | Travel-data synthesis, not STT |

## 8. Synthesis: implications for our proposed solution

**8.1 A modular pipeline is appropriate.** The collected sources discuss speech recognition, spoken-language understanding, task/action-item extraction, and reliable structured output as separable problems. 
Our *proposed architecture* is:

`Voice message → ASR transcription → task/intent extraction → schema validation → user review → backend storage → Kanban card`

**8.2 Model selection is empirical.** The Kazakh ASR comparison inspires testing at minimum Whisper and an adequate wav2vec2 variant as a baseline, if the effort is doable. One should not make universal claims about model superiority on the basis of one particular dataset.

**8.3 Task extraction needs independent evaluation from transcription.** The intent/slot-filling and spoken-dialogue papers reveal that even a good transcript may cause wrong entities or actions to be extracted. Both need to be assessed.

**8.4 JSON syntax is not enough.** From the structured extraction, API argument filling, and hallucination papers follows the requirement for two complementary checks: (a) **schema validity** (types, required fields, valid statuses), and (b) **semantic correctness** with respect to the transcript. Schema checking needs to be done explicitly before storing data.

**8.5 Let's keep the MVP small.** While multi-agent workflow optimization is an interesting problem, it is not necessary for showing that voice-to-task creation works. A basic backend for ASR, task extraction, and validation is easier to argue and test.

## 9. Proposed evaluation plan 

| Component | Proposed measurement | Example of what to check |
|---|---|---|
| ASR | Word Error Rate (WER); optionally CER | Kazakh and Russian recordings; background noise |
| Intent | Precision, recall, F1 | Correctly distinguish task requests from ordinary speech |
| Task extraction | Field-level precision/recall/F1 or exact match | Title, deadline, assignee, description |
| Structured output | Schema-valid response rate | Correct data types, required fields, date formats |
| Faithfulness | Unsupported-value / fabricated-field rate | Did AI invent a deadline not spoken by the user? |
| End-to-end | Correct-task creation rate; user correction rate; latency | Can the user confirm and save the intended Kanban card? |

We should use a small labeled set of representative voice messages. For example: single-task commands, multiple tasks in one message, unclear dates, missing assignees, Kazakh/Russian messages, and messages containing no actionable task. Final metrics and thresholds require agreement with the team and supervisor.

## 10. Conclusion

The twelve collected publications cover complementary parts of the intelligent Kanban problem. Task-management studies establish product relevance; Kazakh ASR and spoken-dialogue studies highlight language and audio challenges; intent detection, slot filling, and structured extraction studies inform the AI pipeline; and API-grounding and hallucination studies identify reliability risks. Collectively, they **motivate**, but do not directly validate, our planned voice-to-Kanban workflow. The next step is to select candidate tools, build a baseline implementation, and measure its performance on representative user utterances before choosing a final technology stack.

## 11. References (from the supplied PDFs)

1. Lekkala, H. B., & Bandari, V. (2026). *Autonomous Workflow Optimization Using Multi Agent AI Systems: AI Agents Manage Stations, WIP, and Task Handoffs*. DOI printed in PDF: 10.46121/pspc.54.2.08. **Verify bibliographic metadata and venue.**
2. Adebanjo, O. A., Oluwasegun, A., Isaac, A., Oluwaseyi, A. J., & Emmanuel, A. (2026). *Design and Implementation of an AI-Powered Task Management System (TaskWise).* British Journal of Computer, Networking and Information Technology, 9(2), 20–34. https://doi.org/10.52589/BJCNIT-LA6S3NNL
3. Chen, J.-H., Su, M.-C., Azzizi, V.-T., Wang, T.-K., & Lin, W.-J. (2021). *Smart Project Management: Interactive Platform Using Natural Language Processing Technology.* Applied Sciences, 11, 1597. https://doi.org/10.3390/app11041597
4. Weld, H., Huang, X., Long, S., Poon, J., & Han, S. C. (2022). *A Survey of Joint Intent Detection and Slot Filling Models in Natural Language Understanding.* ACM Computing Surveys, 55(8), Article 156. https://doi.org/10.1145/3547138
5. Kozhirbayev, Z. (2023). *Kazakh Speech Recognition: Wav2vec2.0 vs. Whisper.* Journal of Advances in Information Technology, 14(6). **Confirm page range/complete DOI in PDF before submission.**
6. Si, S., Ma, W., Gao, H., Wu, Y., Lin, T.-E., Dai, Y., Li, H., Yan, R., Huang, F., & Li, Y. (2023). *SpokenWOZ: A Large-Scale Speech-Text Benchmark for Spoken Task-Oriented Dialogue Agents.* NeurIPS 2023, Datasets and Benchmarks. https://spokenwoz.github.io/SpokenWOZ-github.io/
7. Tanaka, H., & Thompson, G. (2025). *Multi-Agent Systems for Action Item Extraction from Meeting Transcripts: A Comprehensive Review.* Scientific Research Journal of Science, Engineering and Technology, 3(2). **Verify venue, pagination, and peer-review status.**
8. Sun, G., Feng, S., Jiang, D., Zhang, C., Gašić, M., & Woodland, P. C. (2024). *Speech-based Slot Filling using Large Language Models.* Findings of ACL 2024, 6351–6362. https://aclanthology.org/2024.findings-acl.379/
9. Li, Y., Ramprasad, R., & Zhang, C. (2024). *A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction.* Findings of EMNLP 2024, 5133–5148. **Verify ACL Anthology identifier before submission.**
10. Mok, J., Kachuee, M., Dai, S., Ray, S., Taghavi, T., & Yoon, S. (2024). *LLM-based Frameworks for API Argument Filling in Task-Oriented Conversational Systems.* NAACL 2024 Industry Track, 419–426. https://aclanthology.org/2024.naacl-industry.36/
11. Pal, M. (2023). *Natural Language Processing and Speech Recognition.* Excel International Journal of Technology, Engineering and Management, 10(1), 32–38. **Verify journal metadata and peer-review status.**
12. Hoang, T. (2026). *Structured Hallucination in Tool-Using Agents: Measuring and Mitigating LLM Synthesis Corruption in Production.* Second Workshop on Agents in the Wild (AIWILD) at ICML 2026. **Verify final proceedings URL.**
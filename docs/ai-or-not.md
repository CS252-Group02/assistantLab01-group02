

## 1. 10 Questions That Do NOT Need AI (Deterministic / Rule-Based)

These queries can be resolved entirely using table lookups, regular expressions, or static control handlers.

| # | User Query | Handler Component | One-line Reason |
| :---: | :--- | :--- | :--- |
| 1 | "Where is the Training Office?" | Lookup `data/offices.csv` | Direct lookup of the `room` column matching the office name in structured data. |
| 2 | "What are the Library opening hours?" | Lookup `data/offices.csv` | Direct retrieval of the fixed `hours` field for the specified facility in CSV. |
| 3 | "Hello" / "Hi" | Static intent dictionary | Exact keyword match against a predefined list of static greeting intents. |
| 4 | "Help" | Help command handler | Deterministic output returning the static list of supported commands and syntax. |
| 5 | "What is the campus Medical Center phone number?" | Contact directory lookup | Direct key-value query on fixed contact fields in the institutional directory. |
| 6 | "What day and date is it today?" | System runtime (`datetime`) | Exact retrieval of current date and time from the operating system clock. |
| 7 | "How much is the tuition fee per credit for Computer Science?" | Tuition fee table lookup | Deterministic query against the static fee schedule table. |
| 8 | "Which department occupies room I.101?" | Reverse lookup in CSV | Reverse query mapping room number to department name in `data/offices.csv`. |
| 9 | "Show today's class schedule for student 25125089" | Student portal API call | Deterministic API query fetching structured schedule records for a known student ID. |
| 10 | "quit" / "exit" | CLI flow controller | Standard control flow signal to terminate the interactive CLI session. |

---

## 2. 10 Questions That NEED AI (LLM / Generative AI / NLU)

These queries require deep natural language understanding, multi-step logical deduction, document synthesis, or contextual text generation.

| # | User Query | Required AI Capability | One-line Reason |
| :---: | :--- | :--- | :--- |
| 1 | "If I failed Linear Algebra, should I retake it during the summer semester or next semester to graduate on time?" | Multi-step reasoning | Requires logical deduction across prerequisite trees, credit caps, and individual degree progress. |
| 2 | "Summarize the academic merit scholarship criteria for 2026 from the student handbook." | Document summarization / RAG | Requires reading, extracting, and synthesizing key eligibility rules from lengthy regulatory texts. |
| 3 | "Draft an email to my professor requesting a 2-day extension on my final assignment due to medical reasons." | Natural language generation | Requires contextual text generation with appropriate tone, polite academic etiquette, and structured content. |
| 4 | "Hey guys, is the training office open this morning? I need to submit an urgent exam deferral form." | NLU & Ambiguity resolution | Requires parsing colloquial language, abbreviations, and extracting multiple intents in a single sentence. |
| 5 | "What is the difference in career opportunities between Computer Science and Software Engineering?" | Knowledge synthesis | Requires multi-perspective comparison and synthesis of broader industry knowledge and academic curricula. |
| 6 | "I feel completely overwhelmed and burned out by final project deadlines, what should I do?" | Empathetic guidance | Requires empathetic response framing, initial emotional support, and directing the student to university wellness resources. |
| 7 | "Explain Dijkstra's algorithm using an intuitive real-world analogy for a complete beginner." | Pedagogical explanation | Requires pedagogical translation of an abstract algorithmic concept into relatable everyday metaphors. |
| 8 | "What are the sequential administrative steps required to establish a new student academic club?" | Multi-document synthesis | Requires aggregating scattered guidelines from student affairs and union policies into a coherent procedural guide. |
| 9 | "I accidentally submitted an empty draft file and received a grade of 0; how can I file an academic appeal?" | Contextual policy advising | Requires interpreting the student's unique grievance context and advising on appropriate formal dispute procedures. |
| 10 | "Can you suggest a 6-month fullstack web development self-study roadmap for a first-year student?" | Personalized curriculum planning | Requires pacing and structuring technical learning milestones tailored to beginner capabilities. |

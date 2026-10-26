# PROJECT-BRIEF — UX Research Insight Validator

**Student:** Bingjie Zhou · **Target role:** UX Researcher / UX Designer  
**Proposed artifact:** A reproducible Python/AI audit workflow, evidence-linked reports, evaluation cases, and GitHub repository. **The pitch film exists; the validator itself has not been built or tested.**

### 1. What is it?
UX Research Insight Validator will review AI-generated interview findings for unsupported claims, overgeneralization, missing minority perspectives, and potential consequences for design decisions. It will produce an evidence-linked Markdown/JSON report.

### 2. Why care? What makes it different?
Fluent AI summaries can still misrepresent participants. Existing products such as **Dovetail** and **Looppanel** support research synthesis and evidence links. My narrower focus will be *auditing individual findings*: challenging questionable interpretations, preserving counterevidence, and tracing possible design risks, rather than generating another summary.

### 3. Who uses it in the first minute?
A UX researcher will open a sample report, select a finding, and inspect its exact quotes, conflicting viewpoints, and audit flags. A UX hiring manager will be able to review the corresponding prompts, tests, and source IDs.

### 4. What will it prove about me?
I will demonstrate UX research reasoning, prompt contracts, structured outputs, source grounding, verification, and evaluation. Evidence will include source-linked examples, manually labeled tests, a baseline comparison, and an honest record of detected and missed errors.

### 5. What is in, out, and first?
**In:** 3–5 synthetic interviews, quote checks, bias/minority-view flags, design-impact notes, and reports. **Out:** private participant records, transcription, a full dashboard, and automatic design decisions. **First runnable step:** verify that a cited quote appears in its identified synthetic transcript and return the source ID.

### 6. What could sink it?
The validator could hallucinate evidence or wrongly flag a legitimate interpretation. Literal quotation matching will be separated from uncertain semantic judgments, which will require human review. I will document false positives and false negatives.

### 7. Why this project?
UX coursework and the *Tonightly* app concept gave me practice with user needs and design trade-offs. I now want to learn reproducible AI verification and systematic evaluation while creating a relevant UX research portfolio piece. Existing work will be cited only where I can show it.

### Exists Today
- Project concept, scope, portfolio direction, and completed pitch film.
- UX coursework and the *Tonightly* concept; public descriptions of Dovetail and Looppanel.

### Will Exist
- Runnable audit workflow, synthetic interview data, source-linked reports.
- Approximately 8–12 manually labeled tests, baseline comparison, and failure analysis.

**Honesty:** No real interview participants, working validator, tested performance, or measured improvement is claimed.

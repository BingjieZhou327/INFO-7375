# SOURCES — UX Research Insight Validator Pitch Film

This register distinguishes external source material, student-authored/constructed content, AI assistance, and **author-confirmed CapCut postproduction**. Any additional imported media or licensing must be verified against the actual finished MP4.

## 1. Public references and comparisons

| Source | URL | Used for | Limits |
|---|---|---|---|
| Dovetail — User Research | https://dovetail.com/roles/research/ | Example of an existing research platform with AI-assisted synthesis and evidence organization | Mentioned as a real alternative; no claim that it lacks all audit or citation features |
| Looppanel — Auto-Analyze | https://help.looppanel.com/en/articles/11009985-how-to-auto-analyze-on-looppanel | Example of AI-supported research analysis | No invented market-share, benchmark, or superiority figures |
| Brutalist GitHub | https://github.com/nikbearbrown/brutalist.art | Toolkit, local Manim/Remotion rendering, show-tell guidance, quality gates | The repository and its source/artwork have their own license conditions; comply with them |
| Brutalist local documents | `README.md`, `HOW-TO.md`, `skills/make/show-tell/SKILL.md`, `reference/example-make_sheet.py` | Local instructions and structural example for film generation | The stock host persona/credits were **not appropriate** for this assignment and had to be removed from the submitted cut |
| INFO 7375 Final Project Pitch Film assignment | Northeastern Canvas assignment text | Length, seven questions, honesty, submission and build requirements | Instructor-provided course material; do not repost publicly |

All comparisons are qualitative project positioning; no external user studies, competitor tests or numerical advantage claims are asserted.

## 2. Authored or constructed components

- **Project concept and scope:** Bingjie Zhou, with iterative ChatGPT assistance.
- **English narration and 26-beat plan:** student project framing, drafted/refined with ChatGPT; see the final `beat_sheet.json` and the local script drafts.
- **Scene scripts:** `make_sheet.py`, `assemble_scenes.py`, `scenes_body.py` were drafted/adapted with ChatGPT help using the official Brutalist show-tell examples and illustration kit; locally revised in response to render and gate errors.
- **Artwork:** schematic, constructed illustrations rendered from local code and available Brutalist vector/Manim primitives. They do not represent real participant data or working validator screenshots.
- **Quote cards, participant examples, reports, feature modules and evaluations shown:** fictional/constructed depictions of intended functionality. No actual UX research outcomes or evaluation scores are represented.
- **Original concept discussed:** *Tonightly*; only refer to existing coursework/concept work honestly. No participant results, user counts or validated design impact implied.

## 3. AI use and responsibility

- **ChatGPT:** assisted with project positioning, drafting and editing the brief and script, producing/adapting Python storyboard and animation code, troubleshooting CLI errors, and documenting the build. The original private conversation is not included.
- **Kokoro `af_bella`:** free, locally generated temporary narration for film pacing and synchronization in the initial Brutalist render; **not the narrator in the final edit**. The student personally recorded the final English voiceover.
- **Claude:** No Claude-generated material is asserted in this package without a corresponding verified record. If Claude Code was subsequently used, document the prompt, outputs and dates here before submitting.
- **Student responsibilities:** review every claim, visually inspect the film, verify licensing, confirm final narrator, run checks on the final exported film, and explain the source files and decisions.

## 4. Third-party media and licenses (final audit)

| Asset actually used | Origin | License/permission status | Action |
|---|---|---|---|
| Brutalist drawn assets / code / typography | Local Brutalist clone and its dependencies | **Verify** the applicable license and font notices from the installed repository | Add the precise license(s) and preserve required notices |
| Dovetail / Looppanel references | Linked websites above | Factual mentions only; no website images needed | Ensure final film does not embed unlicensed screenshots |
| Background music / externally imported media (if any) | Not established by the records reviewed | Confirm actual origin and permissions if any were included | Do not claim that there was no background music or external media without verifying the completed CapCut timeline |
| English subtitles | Added in postproduction; final work edited in CapCut (Jianying) | Author-generated/final edited content; any external fonts or templates used require their own rights review | Auto-caption vs manual transcription was not specified |

## 5. Final production disclosure — recorded by the author

The author confirmed these facts on October 26, 2026:

- **Editing software:** CapCut (Jianying).
- **Final narration:** The author personally recorded the English voiceover used in the finished video. The original Kokoro `af_bella` audio was a preview/timing reference, **not** the final voiceover.
- **Subtitles:** English subtitles were added. The record does not establish whether transcription was automatic or manual, so no such claim is made.
- **Final export:** After trimming the Brutalist film, an FFmpeg safe-margin re-encode scaled the 960×544 edited image to 826×468 on a 960×544 `0xF3F1EB` background. The delivered-file candidate is `UX_Research_Insight_Validator_FINAL.mp4`. A separate **30-frame independent QC** of samples from that MP4 passed with 0 BLOCKER and 0 MAJOR. This does **not** independently verify audio synchronization, caption correctness, or the precise edit list.

**Additional licensing note:** Whether CapCut music, templates, stickers, fonts, or other external assets were used has not been provided. The author should check the completed timeline and record any such media and applicable license/attribution before submitting. The original Brutalist code, dependency and font-license notices likewise remain subject to their actual license terms.

To record the exact locally installed Brutalist commit, the author may run `git -C ~/Documents/INFO7375/brutalist.art rev-parse HEAD`; this value is not asserted here. No GitHub publication or Canvas submission is claimed.

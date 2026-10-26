# FRICTIONAL — Final Project Pitch Film

**Project:** UX Research Insight Validator  
**Owner:** Bingjie Zhou  
**Purpose:** An honest build/failure log for a *pitch film*, not a claim that the proposed research validator is already running.  
**Evidence basis:** Terminal outputs and screenshots shared during production; where a later action was reported without its settings or file being inspected, that uncertainty is stated.

## 2026-10-25 — Selected the proposal and planned the film
- Confirmed UX Research Insight Validator as a UX-research-oriented project. Proposed an evidence-auditing workflow, with emphasis on source checks, overlooked minority perspectives and potential design risks.
- Drafted the seven answers, narration, and 26-beat show-tell visual plan with ChatGPT assistance.
- **Decision:** Present the validator in future tense and label representations **CONSTRUCTED**, **PROPOSED**, or **HYPOTHETICAL**. No real user interviews or evaluation outcomes are shown.

## 2026-10-25 — Installed the free local toolchain
- Terminal version checks showed Python 3.13.9, Node.js 24.11.1, Git 2.39.5 and Homebrew 5.0.5. FFmpeg was initially missing (`zsh: command not found: ffmpeg`).
- Installed FFmpeg via `brew install ffmpeg`. Subsequent `ffmpeg -version` reported 9.0.2 with exit code 0.
- Cloned Brutalist and ran `./setup --install`. Readiness showed Kokoro audio, caption timing, Manim beats, Remotion and fonts as **ready**. Only Manim equation beats were blocked by absent LaTeX/dvisvgm, which the proposed film did not need.
- Verified `show-tell` exists with `./art --list`. Inspected its skill rules and `reference/example-make_sheet.py`.
- **Constraint:** Default show-tell bookends reference the instructor's persona/credit, conflicting with the course requirement to narrate as myself. Planned to remove host branding from the submitted version and record the deviation honestly.

## 2026-10-25 — Created draft storyboard and body animations
- Adapted 26 beats: 22 Manim body scenes plus four Remotion bookend scenes. Used `make_sheet.py` to generate `beat_sheet.json`; `assemble_scenes.py` joined local `iso_kit.py` with `scenes_body.py` to create `scenes.py`.
- `manim -ql -p scenes.py B00_Summary` successfully rendered the first test animation; `manim -ql -a scenes.py` rendered the remaining body scene previews.
- Created 26 local Kokoro (`af_bella`) narration segments. Initially checked an incorrect directory (`audio/`) and got “No such file or directory”; actual assets were in `mp3/`, with a `timings.json` file. No paid key was used.
- **Lesson:** Do not infer paths from expectations; inspect the installed toolkit's real outputs.

## 2026-10-25 — Fixed Manim layout overflow
- First strict `./art run` compiled B00 but halted at GATE B: one layout warning because the `CONSTRUCTED` footer sat below the safe area (reported lower boundary y ≈ -3.62 versus -3.4 limit).
- Changed `footer.to_edge(DOWN, buff=.38)` to `buff=.85`, rebuilt `scenes.py` and ran `manim_layout_audit.py --class B00_Summary --curve-strict`.
- **Observed result:** `8 snapshots → CLEAN`. Subsequent body scene layout checks reported clean.

## 2026-10-25 — Resolved Remotion opening timeout
- With the Manim scenes built, the opening `BIDEA` (`BrutalistHesitantWriter`) failed after a `delayRender()` timeout.
- Ran `./art remotion-upgrade`; installation reported Remotion 4.0.538. A subsequent `./art run` generated BIDEA successfully, and the log showed 26/26 beats slotted.
- **Open caveat:** Prior rendered Remotion bookends were reused after the upgrade. CapCut postproduction was used later; only the author's full playback review can confirm the exact final transitions and credits.

## 2026-10-25 — Distinguished a slate false failure from the clean export
- The `./art run` review cut was about 202.2 seconds. Its GATE V report showed `frames=52 BLOCKER=52 MAJOR=0`, with all 52 failures classified as left-edge `edge-bleed`.
- The review contact sheet showed a small production slate/beat label on the left edge of every frame. This made the review slate unsuitable as the clean film and plausibly explained the repeated edge error.
- **Action planned:** Use `./art final` to create a clean cut and check that exact file using `final_frame_check.py --mp4 <clean-file>`, rather than applying the slate-gate result to the submitted file. First, GATE T required a separate B09 repair (next entry).

## 2026-10-25 — Fixed the one GATE T text/pixel overlap failure
- Initial `./art final` halted with `GATE T: FAIL (1 pixel beats, 0 sweep, 0 shape)`.
- `TYPECHECK.md` identified `B09` with a 100% overlap between detected blob bounding boxes. A folder illustration with internal tab was a plausible false text-overlap trigger.
- Changed B09's left prop from `'folder'` to `'interviews'`, regenerated `scenes.py`, backed up the previous B09 render, and reran the pipeline.
- **Observed result:** `GATE T: PASS`; clean cut again contained 26/26 beats at about 202.2 seconds. The following explicit clean-file GATE V run returned `frames=52 BLOCKER=0 MAJOR=0`. The old 52-blocker slate report was a real failed attempt, not a pass. This success is confirmed for the exported Brutalist cut, not automatically for any later edits.
- **Remaining visual note:** B07 was center-trimmed from approximately 2.7 s to 2.2 s; check whether any essential animation movement was lost.

## 2026-10-26 — Completed CapCut edit and personally recorded narration
- Edited the Brutalist film with **CapCut (Jianying)**, used **personally recorded English narration** in place of the Kokoro preview voice, and added **English subtitles** (author-confirmed). No AI voice clone is claimed for the final narration.
- Saved the edited MP4 in `final-output/`. This version measured **179.467029 seconds**, versus 202.2 seconds for the original Brutalist cut. The 26-beat QC mapping attempted B21 at 179.646 s, just beyond the edited endpoint, and correctly reported **incomplete / not passed**.
- The editing project was not provided for inspection; the exact trim list, subtitle-generation technique, and any supplementary media/music are not independently documented. The aim was to avoid instructor-themed toolkit credits/persona in the submitted version; only complete playback can verify the final sequence.

## 2026-10-26 — Prepared submission documentation
- Consolidated the brief, source scripts, workflow instructions, AI-use disclosure, build commands and the dated Frictional log into a downloadable package.
- **Not yet claimed at this stage:** Canvas submission, public publication, a matching GitHub commit, working UX validator or evaluated research performance. The padded post-edited MP4 was tested later; see the final QC entry below.

## 2026-10-26 — Investigated the edited video’s boundary failures
- Independently extracted 30 frames from the edited MP4 at roughly six-second intervals; `final_frame_check.py --frames-dir` reported **30 BLOCKERs (all `edge-bleed`)**. These were not counted as a successful QC.
- A separate 1%-crop diagnostic still produced **29 BLOCKERs and 21 MAJORs**, demonstrating the simple crop was not a fix.
- Pixel diagnostics found full-frame edge classifications on the original samples, and bottom-border classifications on 29/30 cropped samples. A **test-only** 86%-scaled image on a light background returned **30 sampled frames, 0 BLOCKER, 0 MAJOR**.
- Chose to preserve the artwork rather than crop away visuals. Created a new padded MP4 at 960×544 by scaling content to 826×468 and centering it on a `0xF3F1EB` background. The source was not overwritten.

## 2026-10-26 — Rechecked the padded final edited video
- The student exported `UX_Research_Insight_Validator_FINAL.mp4`; Terminal showed the file existed (~4.7 MB).
- Extracted 30 sample frames from **that new MP4**, then ran an independent `final_frame_check.py --frames-dir` QC. The supplied actual report states: **30 frames, BLOCKER 0, MAJOR 0**.
- A `zsh: no matches found` message arose from an attempted cleanup of files that did not exist yet. It did not prevent the following extraction or QC.
- The earlier 26-beat GATE T / GATE V reports still apply to the original Brutalist clean cut. The 30-frame independent QC applies to the padded final edited MP4. Neither report validates audio synchronization or the final narrator’s identity.

## Confirmed finishing facts and remaining verification boundaries
- **Confirmed by the author:** CapCut editing, personally recorded English narration, and English subtitles.
- **Still to verify from the author's final playback or editing project:** exact trim list, full-film viewing, subtitle correctness, soundtrack synchronization, use/licensing of any extra music or external assets, and exact duration of the padded final MP4.
- **Still pending:** GitHub repository URL and actual last commit hash after upload; Canvas submission date and archive name once submitted.

The 30-frame independent visual QC is not a sound-quality check or a full 26-beat Gate V rerun. No GitHub push, Canvas submission, working validator or quantitative evaluation result is asserted in this log.

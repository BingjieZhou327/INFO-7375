# UX Research Insight Validator — Final Project Pitch Film

**Author:** Bingjie Zhou  
**Course:** INFO 7375, Fall 2026  
**Target role:** UX Researcher / UX Designer  
**Film title:** *UX Research Insight Validator*  
**Artifact status:** Pitch film completed; the proposed research validation tool is **not yet implemented or evaluated**.

## What this film proposes
An AI-assisted UX research workflow that audits interview findings against original quotes, highlights overgeneralizations and overlooked minority perspectives, and asks how unreliable findings could affect design decisions. The film introduces the intended user, differentiators, scope, first runnable step, planned verification, concrete risks, and the student's motivation.

The interviews, reports, and interface illustrations in the pitch are **CONSTRUCTED** or **PROPOSED**. They are not evidence that the validator has been built or that real research participants were interviewed.

## Submission contents
- `UX_Research_Insight_Validator_FINAL.mp4` — final edited video; the author adds the MP4 from the Mac before zipping/submitting.
- `PROJECT-BRIEF.md` — seven required pitch questions and Exists Today / Will Exist.
- `beat_sheet.json` — final provided 26-beat production manifest, preserving measured durations and build statuses.
- `BUILD-PROMPT.md` — production prompts, commands, and rebuilding steps.
- `SOURCES.md` — references, asset licensing, and AI-use disclosure.
- `FRICTIONAL.md` — dated development observations and failures.
- `quality-reports/` — actual Brutalist clean-export GATE T/GATE V results, plus the independent 30-frame visual inspection of the final padded MP4; see `quality-reports/README.md` for each test’s scope.
- `SOURCE_FILES_FOR_REBUILD/` — source scripts referenced in the rebuilding instructions.

**Before submitting:** Add the actual `UX_Research_Insight_Validator_FINAL.mp4` beside this README. The current folder already contains the latest student-provided 26-beat `beat_sheet.json`, all three supplied QC reports, and the author-confirmed postproduction details. Review the video and check any separately licensed music or imported media before submission.

## Environment used during development (observed in local terminal logs)
- macOS, Terminal, Git 2.39.5, Homebrew 5.0.5.
- Python 3.13.9, Node.js 24.11.1, FFmpeg 9.0.2.
- Manim Community 0.20.1; Remotion upgraded to 4.0.538.
- Brutalist show-tell, with local Kokoro `af_bella` **temporary narration** for timing.
- No paid media services or API keys were used in the documented Brutalist build.

## Rebuild overview
1. Clone [Brutalist](https://github.com/nikbearbrown/brutalist.art) and run `./setup --install`; see the repository's own README, HOW-TO.md and show-tell SKILL.md.
2. Place `SOURCE_FILES_FOR_REBUILD/make_sheet.py`, `assemble_scenes.py`, and `scenes_body.py` in a project reel directory. Use the generated `beat_sheet.json` as the production manifest. Do **not** regenerate it after audio timing and build stamps have been added unless deliberately rebuilding from scratch.
3. Build scenes using `python3 assemble_scenes.py` (pastes Brutalist's local `iso_kit.py` into `scenes.py`), generate preview narration with `generate_audio_kokoro.py`, and render with Brutalist's `./art run` and `./art final` commands.
4. Review the clean cut. The student used **CapCut (Jianying)** for postproduction, replaced the temporary Kokoro preview narration with **personally recorded English speech**, and added **English subtitles**. The precise final editing timeline is **not** reproduced by this source tree because the CapCut project and raw narration recordings are not included.
5. Run applicable checks on the **actual final edited MP4** and preserve the original reports separately; an independent 30-frame sample from the newly padded edited MP4 has already been checked with no BLOCKER or MAJOR findings. See exact commands and known limitations in `BUILD-PROMPT.md`.

## Reproducibility boundary
The project folder documents source and steps but does **not** include restricted data, private conversations, credentials, or paid media accounts. The Brutalist toolkit itself is a separate external dependency. Exact output can vary with software versions and narration timing. The final hand-edited video cannot be reproduced bit-for-bit without its editing timeline and original narration audio; do not claim otherwise.

## Recorded quality and edited-cut scope
- Brutalist clean export: 26/26 beats, 202.2 s; GATE T PASS and 52-frame GATE V with 0 BLOCKER / 0 MAJOR.
- Edited-cut source before safe-margin re-encode: 179.467 s, 960×544 (from the student's `ffprobe` output). The edited timeline no longer aligns with the original beat-level inspection; its B21 sampling timestamp was beyond the cut length.
- Final submitted-file candidate: `UX_Research_Insight_Validator_FINAL.mp4`. FFmpeg resized the 960×544 edited cut to 826×468 inside a 960×544 light background, retaining the personally recorded narration and English subtitles from the CapCut edit. A **separate** visual inspection of 30 frames sampled from that newly generated MP4 returned 0 BLOCKER / 0 MAJOR. The exact padded-file duration and full-playback audio synchronization have **not** been independently measured or certified in these records.
- These final 30-frame samples are **not** the original full 26-beat Gate V and do not substitute for checking audio synchronization, caption accuracy, or reviewing the film in full. The manifest’s `voice=af_bella` and `caption_policy=none` refer to the **Brutalist preview**, not the final CapCut version.

## Submission
Canvas archive: `Zhou_Bingjie_INFO7375_FinalProjectFilm.zip`  
GitHub path: `fall-2026/bingjie-z/final-project-film/`  
**GitHub URL:** Add after uploading.  
**Final commit hash:** Add after your last commit.

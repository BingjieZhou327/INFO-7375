# Quality Reports — Actual Files and Scope

All reports in this directory originate in the submitted local production records; results are not inferred from an untested file.

| File | Subject | Actual result |
|---|---|---|
| `GATE-T-Brutalist-Clean.md` | Original 26-beat Brutalist clean export | PASS; 26 beats, 0 failures |
| `GATE-V-Brutalist-Clean.md` | Original unedited Brutalist clean MP4 | 52 sampled frames, 0 BLOCKER, 0 MAJOR |
| `GATE-V-Contact-Sheet.png` | Original clean export contact sheet | Reference image |
| `GATE-V-Final-Edited-Video.md` | Independent frame-directory QC on 30 frames sampled from the **padded final edited MP4** | 30 frames, 0 BLOCKER, 0 MAJOR |

The last row is **not a repeat of the complete beat-indexed GATE V**. After trimming, the edit was 179.467 seconds and the original beat-indexed checker attempted to read B21 at 179.646 seconds, beyond the edited cut. A separate independent frame-directory test was therefore performed. Initial independent checks on the unpadded edited cut failed with edge-bleed; those failures led to the 86%-scale padding and subsequent passing sample set.

These image checks do not test audio, synchronization, voice provenance, captions accuracy, or completeness of the full video. GATE T was not re-run against the edited version.

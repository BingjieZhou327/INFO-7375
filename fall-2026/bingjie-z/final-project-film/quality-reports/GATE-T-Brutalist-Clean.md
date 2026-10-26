# TYPECHECK.md — GATE T

Reel: `ux-research-insight-validator-pitch`  |  Checked: 2026-10-25T23:36  |  Overall: PASS  |  Beats checked: 26  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BIDEA | bookend | light | min-size §8.1: min text-run height 59px >= floor 41px | PASS | — |
| BDEFS | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B00 | manim | light | min-size §8.1: min text-run height 88px >= floor 41px | PASS | — |
| B01 | manim | light | min-size §8.1: min text-run height 88px >= floor 41px | PASS | — |
| B02 | manim | light | min-size §8.1: min text-run height 93px >= floor 41px | PASS | — |
| B03 | manim | light | min-size §8.1: min text-run height 88px >= floor 41px | PASS | — |
| B04 | manim | light | min-size §8.1: min text-run height 80px >= floor 41px | PASS | — |
| B05 | manim | light | min-size §8.1: min text-run height 75px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B06 | manim | light | min-size §8.1: min text-run height 85px >= floor 41px | PASS | — |
| B07 | manim | light | min-size §8.1: min text-run height 93px >= floor 41px | PASS | — |
| B08 | manim | light | min-size §8.1: min text-run height 388px >= floor 41px | PASS | — |
| B09 | manim | light | min-size §8.1: min text-run height 88px >= floor 41px | PASS | — |
| B10 | manim | light | min-size §8.1: min text-run height 93px >= floor 41px | PASS | — |
| B11 | manim | light | min-size §8.1: min text-run height 93px >= floor 41px | PASS | — |
| B12 | manim | light | min-size §8.1: min text-run height 88px >= floor 41px | PASS | — |
| B13 | manim | light | min-size §8.1: min text-run height 75px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B14 | manim | light | min-size §8.1: min text-run height 84px >= floor 41px | PASS | — |
| B15 | manim | light | min-size §8.1: min text-run height 88px >= floor 41px | PASS | — |
| B16 | manim | light | min-size §8.1: min text-run height 76px >= floor 41px | PASS | — |
| B17 | manim | light | min-size §8.1: min text-run height 88px >= floor 41px | PASS | — |
| B18 | manim | light | min-size §8.1: min text-run height 88px >= floor 41px | PASS | — |
| B19 | manim | light | min-size §8.1: min text-run height 93px >= floor 41px | PASS | — |
| B20 | manim | light | min-size §8.1: min text-run height 88px >= floor 41px | PASS | — |
| B21 | manim | light | min-size §8.1: min text-run height 93px >= floor 41px | PASS | — |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | bookend | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 26 | 0 |
| overflow §8.2 | 26 | 0 |
| contrast §8.3 | 26 | 0 |
| contrast-local §8.3b | 26 | 0 |
| bbox-overlap §8.6b | 26 | 0 |
| card-clip §8.13 | 26 | 0 |
| kerning §8.4 | 22 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*

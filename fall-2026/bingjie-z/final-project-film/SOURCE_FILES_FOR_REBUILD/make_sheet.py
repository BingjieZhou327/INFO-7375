#!/usr/bin/env python3
"""Generate a student-specific Brutalist show-tell beat_sheet.json.

Based on skills/make/show-tell/reference/example-make_sheet.py.
This generates the storyboard contract, NOT Manim scenes or a rendered video.
The content is a project PITCH; no implementation or study outcomes are asserted.
Temporary local Kokoro voice is for layout/timing only; the submitted film
must use the student's own narration.  No instructor persona or credit line.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "ux-research-insight-validator-pitch"
TITLE = "UX Research Insight Validator"
AUTHOR = "Bingjie Zhou"
VOICE = "af_bella"  # TEMPORARY preview audio only

# Each tuple: (narration, Python Manim class, scene description, motion timeline)
# Each shot is a separate scene. All research/example visuals are PROPOSED
# or CONSTRUCTED; they are NOT screenshots of a working product.
SECTIONS = [
    ("The problem", [
        ("AI can summarize user interviews in seconds. But a fluent summary is not necessarily a faithful one.",
         "B00_Summary", "A stack of fictional interview pages slides into a schematic AI box; a clean summary page comes out. Small label: CONSTRUCTED.",
         [(0.10, "pages enter"), (0.48, "summary emerges"), (0.75, "question mark arrives")]),
        ("It might exaggerate one comment, overlook a disagreement, or turn a possibility into a fact. For UX research, those mistakes matter because research findings can shape real design decisions.",
         "B01_Distortion", "One summary page incorrectly grows to cover two disagreeing quote cards, then an arrow carries it toward a design sketch. Labels: CLAIM, QUOTES.",
         [(0.10, "quote cards appear"), (0.35, "summary expands too far"), (0.72, "arrow moves to design sketch")]),
    ]),
    ("What I will build", [
        ("My proposed final project is UX Research Insight Validator: an AI-assisted workflow that checks research findings against their original interview evidence.",
         "B02_Validator", "One illustrated audit desk accepts a proposed finding and the original interview pages. Label: PROPOSED.",
         [(0.10, "audit desk arrives"), (0.48, "two source objects move into desk"), (0.78, "magnifier appears")]),
        ("I plan to build a small, reproducible Python-based workflow with structured outputs, sample reports, and tests. This is a proposal, not a working product yet.",
         "B03_Plan", "A proposed workflow grows from Python block to JSON report to test checklist; none is presented as running code. Label: PROPOSED.",
         [(0.12, "Python tile appears"), (0.42, "report page arrives"), (0.74, "test clipboard joins")]),
    ]),
    ("Value and alternatives", [
        ("Tools such as Dovetail and Looppanel already support AI-assisted research analysis, so generating themes alone would not be a meaningful difference.",
         "B04_Alternatives", "Two generic platform cards marked Dovetail and Looppanel are next to a stack of synthesized themes; neither card impersonates a real UI.",
         [(0.10, "two cards appear"), (0.52, "theme pages land")]),
        ("My focus will be narrower: auditing individual claims for missing support, overgeneralization, and minority perspectives that a summary may overlook.",
         "B05_Claims", "One claim card moves through three visible inspection gates: EVIDENCE, SCOPE, VOICES. A small dissenting quote remains visible. Label: PROPOSED.",
         [(0.10, "claim arrives"), (0.32, "evidence gate appears"), (0.54, "scope gate appears"), (0.76, "minority quote becomes visible")]),
        ("I will also connect questionable findings to possible design risks, rather than simply generating another polished summary.",
         "B06_DesignRisk", "A warning dot appears on a disputed finding; a branching arrow points toward a possible design decision. Label: PROPOSED.",
         [(0.13, "finding appears"), (0.43, "warning flag arrives"), (0.72, "risk branch draws")]),
    ]),
    ("Who uses it", [
        ("The main user will be a UX researcher.",
         "B07_Researcher", "A laptop/workbench and research pages assemble as a generic researcher workspace, without a real person portrait. Label: PROPOSED.",
         [(0.10, "workbench enters"), (0.55, "interview papers arrive")]),
        ("In the first minute, they will open a sample report, choose one finding, and see the original quotes, conflicting viewpoints, and any audit flags.",
         "B08_Report", "A CONSTRUCTED report shows one finding and linked source cards; a conflicting source turns to face the viewer and an audit flag appears.",
         [(0.08, "constructed report opens"), (0.35, "one finding selected"), (0.62, "conflicting quote surfaces"), (0.82, "flag appears")]),
        ("A hiring manager will be able to examine the same evidence, prompts, and tests in the repository.",
         "B09_Review", "A generic repository folder opens to reveal labeled evidence, prompt and test documents. Label: PLANNED.",
         [(0.14, "repo folder opens"), (0.48, "three documents lift"), (0.76, "source link draws")]),
    ]),
    ("Scope and first working step", [
        ("I will begin with three to five synthetic interviews.",
         "B10_Synthetic", "Three to five fictional paper interview cards fan out. Each paper has a visible CONSTRUCTED label.",
         [(0.12, "three cards arrive"), (0.60, "two more outlines arrive")]),
        ("The first runnable step will be simple: check whether a cited quotation actually appears in its source transcript, and return the source ID.",
         "B11_QuoteMatch", "An exact quote string is visually connected to the matching line on a constructed source page; then a source ID appears. Label: PROPOSED.",
         [(0.09, "quote appears"), (0.42, "matching line highlighted"), (0.75, "source ID appears")]),
        ("After that, I will add checks for distorted claims and overlooked perspectives, plus a short note on potential design impact.",
         "B12_FutureChecks", "Three proposed modules emerge beside the audit desk: DISTORTION, VOICES, IMPACT. One card advances to each module.",
         [(0.12, "distortion module"), (0.46, "voices module"), (0.76, "impact module")]),
        ("I will not build live transcription, a full dashboard, or an automatic design decision maker.",
         "B13_OutOfScope", "Three optional objects (microphone, dashboard, autopilot switch) move outside a dotted boundary marked OUT OF SCOPE.",
         [(0.11, "dotted boundary appears"), (0.48, "objects move out"), (0.79, "scope closes")]),
    ]),
    ("Skills, evaluation, and risk", [
        ("This project will demonstrate prompt contracts, source grounding, structured outputs, verification, and evaluation.",
         "B14_Skills", "Five labeled research/engineering elements connect as a single workflow, not a wall of text. Labels are limited to two or three terms. Label: PROPOSED.",
         [(0.10, "source page appears"), (0.43, "prompt contract and structured output assemble"), (0.75, "evaluation check appears")]),
        ("I plan to create roughly eight to twelve manually labeled test cases and compare basic AI findings with audited findings.",
         "B15_Evaluation", "A constructed test case joins two paths labeled BASELINE and AUDIT, ending at an illustrated comparison sheet. Label: PLANNED.",
         [(0.13, "test case appears"), (0.40, "two evaluation paths draw"), (0.74, "comparison sheet appears")]),
        ("A major risk is that the validator itself may hallucinate or flag reasonable interpretations as errors.",
         "B16_Risk", "A validator box incorrectly flags one reasonable interpretation; a caution marker appears. Label: HYPOTHETICAL.",
         [(0.12, "finding appears"), (0.47, "wrong flag appears"), (0.74, "caution pulse")]),
        ("Exact quote matching can verify citations, but judgments about meaning will need human review.",
         "B17_HumanReview", "One exact quote passes a string-match check while a separate interpretation is placed in a HUMAN REVIEW tray. Label: PROPOSED.",
         [(0.10, "citation check draws"), (0.43, "ambiguous claim rises"), (0.73, "human-review tray appears")]),
        ("I will record both detected mistakes and missed ones.",
         "B18_FailureLog", "A future evaluation log reveals two columns DETECTED and MISSED, with generic blank rows. Label: PLANNED.",
         [(0.10, "log opens"), (0.55, "two empty categories appear")]),
    ]),
    ("Why I chose it", [
        ("I chose this project because I want to work in UX research.",
         "B19_Motivation", "A simple road from university project papers toward a UX research role marker. No invented job offer or employer shown.",
         [(0.15, "project papers appear"), (0.56, "path draws to role")]),
        ("Through UX coursework and the Tonightly app concept, I have practiced thinking about user needs and design trade-offs.",
         "B20_Tonightly", "A constructed Tonightly concept card sits beside generic user-needs notes and design tradeoff arrows; not represented as a validated study.",
         [(0.12, "concept card appears"), (0.49, "needs notes arrive"), (0.78, "tradeoff arrows draw")]),
        ("Building reliable AI checks and systematic evaluations will be new learning for me. My goal is not to replace researchers, but to help them question AI-generated findings before those findings influence design.",
         "B21_Conclusion", "Audit workflow and human review table join in front of the design decision sketch; the final check mark is a plan, not a test result. Label: PROPOSED.",
         [(0.09, "audit objects join"), (0.42, "human review card enters"), (0.79, "question mark is preserved")]),
    ]),
]

SPARSE_REASON = (
    "Show-tell intentionally uses one isometric drawing per beat with short labels. "
    "This does not waive contrast, empty-frame, or edge-bleed checks."
)


def estimate(text):
    return round(len(text.split()) / 2.5, 1)  # estimate only; later measure audio


def body_beat(bid, narration, cls, visual_intent, cues, section):
    return {
        "beat_id": bid, "act": "show-tell", "section": section,
        "lane": "manim", "proof_gate": "SHOW", "narration_text": narration,
        "estimated_duration_s": estimate(narration), "voice": VOICE, "engine": "kokoro",
        "shot": {
            "type": "GRAPHIC", "source": "own", "visual_intent": visual_intent,
            "show": [{"at": t, "event": e} for t, e in cues],
            "manim": {"class": cls}, "motion_claim": visual_intent,
        },
        "qc": {"sparse_by_design": True, "sparse_reason": SPARSE_REASON},
    }


def remotion(bid, act, narration, pattern, props, visual_events, proof_gate="SHOW", **extra):
    b = {
        "beat_id": bid, "act": act, "lane": "bookend", "proof_gate": proof_gate,
        "narration_text": narration, "estimated_duration_s": estimate(narration),
        "voice": VOICE, "engine": "kokoro",
        "shot": {"type": "REMOTION", "source": "own", "show": visual_events,
                 "remotion": {"pattern": pattern, "props": props}},
    }
    b.update(extra)
    return b


def build():
    idea = remotion(
        "BIDEA", "proposal question",
        "Hi, I'm Bingjie Zhou. My project asks a simple question: when AI summarizes interviews, how can we verify its findings?",
        "BrutalistHesitantWriter",
        {"text": "How can AI summarize interviews?",
         "triggerWords": "summarize interviews", "replacementWords": "verify findings",
         "fontSize": 70, "charMs": 22, "hesitateBetween": 6,
         "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
         "seed": SLUG, "banner": ""},
        [{"at": 0.1, "event": "types the research question"},
         {"at": 0.6, "event": "corrects 'summarize interviews' to 'verify findings'"}],
        lead_silence_s=0.8,
        motion_claim="The question is corrected from summary generation to verification.",
        qc={"sparse_by_design": True, "sparse_reason": "Typed, corrected question is the action."},
    )
    defs = remotion(
        "BDEFS", "key terms",
        "Three terms: a finding is a research claim, evidence is what participants actually said, and an audit checks whether the claim follows from that evidence.",
        "ClaudeDefinitions",
        {"title": "Terms In This Film",
         "terms": [
             {"term": "finding", "meaning": "a research claim"},
             {"term": "evidence", "meaning": "what participants actually said"},
             {"term": "audit", "meaning": "checking whether a claim follows from evidence"},
         ], "folderLabel": AUTHOR},
        [{"at": 0.12, "event": "finding appears"},
         {"at": 0.50, "event": "evidence appears"},
         {"at": 0.79, "event": "audit appears"}], proof_gate="CARD",
        qc={"sparse_by_design": True, "sparse_reason": "Brief definitions card."},
    )
    body = []
    for sec_name, items in SECTIONS:
        for narration, cls, visual_intent, cues in items:
            body.append(body_beat(cls.split('_')[0], narration, cls, visual_intent, cues, sec_name))
    prompt = (
        "Before trusting an AI research finding, ask: which exact quotes support it, "
        "whose views might be missing, and what design decision could it influence?"
    )
    your_turn = remotion(
        "BHTF", "human review",
        "Before trusting an AI research finding, ask three questions. Which exact quotes support it? Whose views might be missing? And what design decision could it influence?",
        "ClaudeComposerAsk",
        {"greeting": "Your turn.", "topic": "UX RESEARCH · YOUR TURN",
         "segment": "Check a Finding", "command": prompt,
         "runningText": "check the evidence…",
         "output": ["Check source quotes.", "Look for missing perspectives."],
         "folderLabel": AUTHOR, "modelLabel": "", "effortLabel": ""},
        [{"at": 0.10, "event": "review question types"},
         {"at": 0.78, "event": "two checks appear"}],
    )
    outro = remotion(
        "BOUT", "outro",
        "UX Research Insight Validator. Final project pitch by Bingjie Zhou.",
        "ClaudeTitleOutro",
        {"title": TITLE, "slug": SLUG, "handle": AUTHOR, "subline": ""},
        [{"at": 0.0, "event": "project title and student attribution appear"}],
        kind="outro_voice", tail_silence_s=1.0,
    )
    beats = [idea, defs, *body, your_turn, outro]
    return {
        "metadata": {
            "slug": SLUG, "title": TITLE, "topic": "UX RESEARCH · EVIDENCE AUDIT",
            "skill": "show-tell", "style_preset": "show-tell",
            "channel": "student-pitch", "channel_title": AUTHOR,
            "persona": "Bingjie Zhou (student narration; Kokoro is preview only)",
            "voice": VOICE, "voice_kokoro": VOICE, "engine": "kokoro",
            "clock": "narration", "palette": "claude", "register": "Plain",
            "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
            "caption_policy": "none", "greeting_language": "English",
            "bookend_exempt": ["cold-open", "bvdt"],
            "bookend_exempt_reason": (
                "INFO 7375 student pitch: use a self-attributed hesitant-writer opener, "
                "not the toolkit host persona; no verdict card; own voice in final edit."
            ),
            "audience": "UX researchers, UX hiring managers, and INFO 7375 reviewers",
            "source_doc": "PROJECT-BRIEF.md; NARRATION-SCRIPT.md; SOURCES.md",
            "playlist": "INFO 7375 Final Project", "chapter_number": 0,
            "tags": ["UX research", "research validation", "source grounding", "evidence", "AI evaluation"],
            "development_status": "PROPOSED — no working validator or evaluation results yet",
            "student_film_note": "All interview visuals are constructed; do not present as field research.",
        },
        "beats": beats,
    }


def main():
    sheet = build()
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    # Complete spoken text includes the customized, student-branded bookends.
    sections = ["# Recording Script — UX Research Insight Validator", "", "Own voice for final submission. Synthetic/illustrative scenes are CONSTRUCTED.", ""]
    for b in sheet["beats"]:
        sections += [f"## {b['beat_id']} · {b.get('section', b['act'])}", "", b["narration_text"], ""]
    (HERE / "NARRATION-RECORDING.md").write_text("\n".join(sections) + "\n", encoding="utf-8")
    length = sum(b['estimated_duration_s'] for b in sheet['beats'])
    words = sum(len(b['narration_text'].split()) for b in sheet['beats'])
    print(f"Created beat_sheet.json and NARRATION-RECORDING.md")
    print(f"{len(sheet['beats'])} beats, {words} words, estimated {length:.1f} s ({length/60:.2f} min)")
    print("NOTE: Manim scenes.py and actual audio/video still need to be built and QC checked.")
    print("Do not rerun after generating Kokoro audio unless you plan to restore audio metadata.")


if __name__ == "__main__":
    main()

# Source-grounded review rubric

Apply the supplied task instruction before judging fluency. An output may read well and still fail. All examples here use **fictional sources** and AI-drafted reference decisions.

## Four scored dimensions

Each dimension is assigned **0–2** where sufficient source evidence exists:

| Dimension | 2 | 1 | 0 |
|---|---|---|---|
| **Grounding** | Every material claim is supported | Partly supported; important qualification missing | Material claim contradicts or exceeds evidence |
| **Instructions** | Fully meets requested format and task | Minor nonmaterial deviation | Violates an explicit important instruction |
| **Privacy** | No prohibited identifier disclosed | Unclear scope needing manual judgment | Identifier exposed contrary to requirement |
| **Completeness** | All necessary details included | Some relevant detail absent | Essential information missing or misleading |

Scores are decision aids, **not a calibrated model-quality metric**. Hard failures in material arithmetic, confidentiality, grounding or core instructions justify REJECT even if other dimensions score 2. A summed score never overrides a hard-failure decision.

## Verdicts and uncertainty

- **ACCEPT:** The proposed response meets the stated evidence and requirement in this fictional scenario.
- **REJECT:** A verifiable material error, requirement violation or privacy failure is shown. Record the contrary source and a correction.
- **INSUFFICIENT_EVIDENCE:** The source is inadequate to adjudicate the requested business fact; do not guess. No numerical score is assigned.

A reference case labelled INSUFFICIENT_EVIDENCE may contain a **good refusal to invent facts**. That label is about the state of the evidence, not a claim that the cautious response is bad.

## Paired comparison

Compare A and B against exactly the same source. Choose **A**, **B**, **TIE** (equally satisfactory), or **NEITHER** (both unacceptable). Record the decisive requirement, not the preferred tone. No reviewer agreement, model win rate or commercial benchmark is claimed.

## Provenance

These reference labels and rationales were drafted with AI. They are editable practice keys for personal review, not personally scored work attributed to Hans. Until a genuine independent pass is recorded, do not describe them as 30 completed human annotation tasks or quote agreement rates.

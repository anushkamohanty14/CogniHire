# CogniHire — Cognitive Ability–Driven Interview Preparation Platform

## Overview

CogniHire is a cognitive-first career intelligence system that combines:

* **Cognitive ability assessment (NCPT-style tasks)**
* **Resume-based skill extraction**
* **O*NET-aligned job matching**
* **AI-driven interview preparation**

The system evaluates users using **scientifically grounded cognitive tasks**, converts performance into standardized ability scores, and uses these to drive **job recommendations, skill gap analysis, and interview generation**.

---

## Core System Flow

User
→ Cognitive Tasks (generated dynamically)
→ Response + Reaction Time (RT) capture
→ Raw + Composite Scoring
→ Normalization (O*NET scale: 0–7)
→ Ability Vector
→ Skill Extraction (Resume)
→ Hybrid Recommendation Engine
→ Interview Generation + Feedback

---

## Implemented Phases (Current State)

### Phase 1 — O*NET Integration

* Job ability matrices
* Lexical job suggestion baseline

---

### Phase 2 — User Profiling

* Resume upload + parsing
* Manual skill input
* Profile normalization

---

### Phase 3 — Cognitive Ability Engine

* NCPT-style task framework
* Ability-specific task mapping:

  * Memory (digit span)
  * Attention (Stroop)
  * Speed (symbol search)
  * Closure (pattern completion)
  * Multitasking (dual-task)

---

### Phase 4 — Preference Matching

* Activity-based user preferences
* Job activity similarity computation

---

### Phase 5 — Reaction Time System

* Trial-level timing capture
* RT calculation (milliseconds)
* Uses: `performance.now()` (frontend)

---

### Phase 6 — Composite Scoring

* Combines:

  * Accuracy
  * Reaction time
* Task-specific scoring logic

---

### Phase 7 — Ability Normalization

* Z-score standardization
* Scaling to O*NET-like range (0–7)

---

## Cognitive System Design

### Generation Strategy

#### Rule-Based (Primary)

Used for:

* Memory
* Attention
* Perceptual speed
* Time sharing
* Speed of closure

#### LLM-Based (Selective)

Used for:

* Mathematical reasoning
* Problem sensitivity
* Written comprehension

---

### Why This Design

* Ensures **measurement validity**
* Enables **difficulty control**
* Prevents memorization
* Matches real cognitive testing systems

---

## Key Features

* Dynamic cognitive task generation (no static datasets)
* Reaction-time–aware scoring
* Ability vector construction
* O*NET-aligned ability scaling
* Hybrid recommendation system
* Interview question generation (AI-powered)

---

## Project Structure

For full architecture and module mapping:

* `docs/cognitive_ability_requirements.md`
* `PROJECT_STRUCTURE_PHASE2_ONWARDS.md`

---

## Running the API

Follow the setup and execution instructions defined in the project structure and API configuration.

Typical flow:

```bash
# Install dependencies
pip install -r requirements.txt

# Run API
uvicorn apps.api.src.main:app --reload
```

---

## Design Principles

* Cognitive-first architecture
* Deterministic task generation
* Separation of:

  * generation
  * scoring
  * normalization
* Minimal but effective use of AI

---

## Status

The system currently supports:

* End-to-end cognitive scoring pipeline
* Ability normalization
* Integration with job ability datasets

Next steps include:

* Full recommendation pipeline integration
* Interview simulation expansion
* Explainability and visualization layers

---

## References

System design aligns with the full SRS:
See `docs/` for detailed requirements and architecture documentation.

---


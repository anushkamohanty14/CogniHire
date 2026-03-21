# CogniHire

### AI-Powered Interview Preparation Platform with Cognitive Assessment

---

## Overview

CogniHire is an AI-powered interview preparation platform designed to help students and job seekers:

* understand their strengths and weaknesses
* identify skill gaps for target roles
* practice technical and behavioral interviews
* receive structured, actionable feedback

The platform combines:

* cognitive assessment (behavioral and working tendencies)
* resume-based skill extraction
* AI-generated interview questions
* performance analysis and feedback

The goal is to simulate real interview environments while providing personalized, data-driven preparation.

---

## Core Workflow

```text
User
│
├── Cognitive Assessment (Quiz + Tasks)
├── Resume Upload
│
↓
User Profile & Capability Analysis
│
├── Strengths & Weaknesses
├── Skill Gap Identification
│
↓
Interview System
├── Technical Questions (skill-based)
└── Behavioral Questions (cognitive-based)
│
↓
Practice + Feedback + Improvement
```

---

## Key Features

### Cognitive Assessment

* Evaluates:

  * attention
  * memory
  * problem-solving
  * multitasking

* Uses:

  * NCPT-style cognitive tasks
  * reaction-time–based evaluation
  * structured scoring system

---

### Resume Analysis

* Extracts:

  * skills
  * experience
  * education

* Builds a structured user skill profile

---

### User Profile Generation

Combines:

* cognitive results
* resume data

Outputs:

* strengths
* weaknesses
* capability profile

---

### Skill Gap Analysis

* Compares user profile with job requirements

* Identifies:

  * missing skills
  * readiness level

* Suggests improvement areas

---

### Interview System

* Generates:

  * technical questions (based on skills and gaps)
  * behavioral questions (based on cognitive profile)

* Supports:

  * text responses
  * voice responses

---

### Feedback and Improvement

Provides:

* technical accuracy feedback
* communication quality analysis
* improvement suggestions

---

## Cognitive System

### Measured Abilities

* Mathematical Reasoning
* Memorization
* Perceptual Speed
* Problem Sensitivity
* Selective Attention
* Speed of Closure
* Time Sharing
* Written Comprehension

---

### Task Design

| Ability       | Task Type          |
| ------------- | ------------------ |
| Memory        | Digit span         |
| Attention     | Stroop task        |
| Speed         | Symbol search      |
| Closure       | Pattern completion |
| Multitasking  | Dual-task          |
| Math          | Word problems      |
| Comprehension | Reading passages   |

---

### Scoring Pipeline

1. Response capture

   * accuracy
   * reaction time (RT)

2. Composite scoring

   * combines accuracy and speed

3. Normalization

   * z-score standardization
   * scaled to 0–7 (O*NET-aligned)

---

### Generation Strategy

**Rule-based (primary):**

* memory
* attention
* perceptual speed
* time sharing
* closure

**AI-based (selective):**

* mathematical reasoning
* problem sensitivity
* written comprehension

---

## Project Phases (Current Implementation)

* Phase 1: Cognitive task design and response capture (accuracy + reaction time)
* Phase 2: Resume parsing and structured skill extraction
* Phase 3: Composite scoring (accuracy and speed integration)
* Phase 4: Ability normalization and mapping to O*NET scale (0–7)
* Phase 5: User profile generation (cognitive + skill profile)
* Phase 6: Skill gap analysis against target job roles
* Phase 7: Interview question generation (technical + behavioral)

---

## Tech Stack

* Frontend: React / Next.js / Streamlit
* Backend: FastAPI (Python)
* Database: PostgreSQL / MongoDB
* AI/NLP: LLM APIs (Gemini / GPT)
* Processing: NumPy, NLP libraries

---

## Running the Project

```bash
pip install -r requirements.txt
uvicorn apps.api.src.main:app --reload
```

---

## Design Principles

* cognitive assessment supports interview preparation
* deterministic task generation for reliability
* minimal but effective use of AI
* modular and scalable architecture
* clear separation of:

  * assessment
  * profiling
  * interview system

---

## Status

Currently implemented:

* cognitive scoring pipeline
* reaction-time measurement
* user profiling
* resume parsing

Upcoming:

* full interview simulation flow
* advanced feedback system
* visualization dashboards

---

## Summary

CogniHire is a cognitive-informed interview preparation platform that adapts to how users think, perform, and improve.

---

## Documentation

* docs/cognitive_ability_requirements.md
* PROJECT_STRUCTURE_PHASE2_ONWARDS.md

---

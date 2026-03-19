# AI-Powered Candidate Evaluation System

## Overview
This project is an AI-powered candidate evaluation system that analyzes multiple resumes against a job description and generates structured hiring insights.

The system simulates a real-world hiring workflow by scoring, ranking, and explaining candidate suitability in a clear and practical format.

---

## Problem Statement
**Problem : Design an AI-powered candidate evaluation system**

---

## Features

- Upload Job Description and multiple resumes
- Evaluate candidates based on role requirements
- Generate:
  - Match Score (0–100)
  - Candidate Ranking
  - Matched Skills
  - Missing Skills
  - Strengths and Gaps
  - Final Recommendation (Strong Fit / Moderate Fit / Not Fit)
- Interactive UI to explore candidate details
- Structured output in CSV format

---

## System Workflow

1. Extract text from resumes (PDF)
2. Compare resume content with job description
3. Evaluate candidates using structured prompting (LLM-based logic)
4. Generate consistent outputs for each candidate
5. Rank candidates based on score
6. Display results through a Streamlit UI

---

## Tech Stack

- Python
- PyMuPDF (PDF text extraction)
- Pandas (data processing)
- Streamlit (UI/dashboard)
- ChatGPT (LLM-based evaluation)

---

## UI Demo

The Streamlit interface allows:
- Uploading job description and resumes
- Running screening process
- Viewing ranked candidates
- Exploring detailed candidate insights (strengths, gaps, reasoning)

---

## Output

The final output is stored in: screening_results.csv

This file contains:
- Ranked candidates
- Scores and recommendations
- Skill analysis
- Strengths and gaps

---

## Note on Implementation

Due to API and time constraints, the current version demonstrates the system using **precomputed evaluation results**.

However, the architecture is designed to support **fully automated real-time evaluation** using LLM APIs.

---

## Future Improvements

- Integrate live API-based evaluation for real-time screening
- Add weighted scoring (skills, projects, tools)
- Build recruiter dashboard with filtering and analytics
- Support bulk resume uploads and batch processing
- Integrate with Google Sheets / ATS systems

---

## How to Run

```bash
pip install streamlit pandas pymupdf
streamlit run app.py

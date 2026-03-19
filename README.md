# AI Resume Screening System

## Overview
This project is an AI-powered resume screening system that evaluates candidate resumes against a job description and generates structured hiring recommendations.

## Inputs
- Job Description (JD)
- Multiple resumes (PDF)

## Outputs
- Match score (0–100)
- Candidate ranking
- Matched and missing skills
- Key strengths and gaps
- Final recommendation (Strong Fit / Moderate Fit / Not Fit)

## Approach
- Extracted text from resumes using Python (PyMuPDF)
- Used structured prompting with an LLM to evaluate each resume
- Generated consistent JSON outputs for each candidate
- Compiled results into a ranked CSV file

## Tools Used
- Python
- PyMuPDF
- ChatGPT (LLM)
- Google Colab

## Output
See `screening_results.csv` for final ranked results.

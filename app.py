import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Resume Screening System", layout="wide")

st.title("AI Resume Screening System")
st.write("Upload the job description and candidate resumes, then run screening.")

jd_file = st.file_uploader("Upload Job Description (.txt)", type=["txt"])
resume_files = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)

RESULTS_FILE = "screening_results.csv"

def load_results():
    df = pd.read_csv(RESULTS_FILE)
    df.columns = [col.strip().title() for col in df.columns]
    return df

if "show_results" not in st.session_state:
    st.session_state.show_results = False

if st.button("Run Screening"):
    if jd_file is None or not resume_files:
        st.warning("Please upload both the job description and resumes.")
        st.session_state.show_results = False
    else:
        st.session_state.show_results = True

if st.session_state.show_results:
    df = load_results()

    st.subheader("Summary Results")
    summary_cols = [col for col in ["Rank", "Candidate", "Score", "Recommendation"] if col in df.columns]
    st.dataframe(df[summary_cols], use_container_width=True)

    st.subheader("Candidate Details")
    candidate_name = st.selectbox("Select a candidate", df["Candidate"].tolist())
    row = df[df["Candidate"] == candidate_name].iloc[0]

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Rank", row["Rank"])
        st.metric("Score", row["Score"])
        st.write("**Recommendation:**", row["Recommendation"])

        if "Matched Skills" in df.columns:
            st.write("**Matched Skills**")
            st.write(row["Matched Skills"])

        if "Missing Skills" in df.columns:
            st.write("**Missing Skills**")
            st.write(row["Missing Skills"])

    with c2:
        if "Strengths" in df.columns:
            st.write("**Strengths**")
            st.write(row["Strengths"])

        if "Gaps" in df.columns:
            st.write("**Gaps**")
            st.write(row["Gaps"])

        if "Reasoning" in df.columns:
            st.write("**Reasoning**")
            st.write(row["Reasoning"])
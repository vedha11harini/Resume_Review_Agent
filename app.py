import streamlit as st
from tools.speech_to_text import speech_to_text
from tools.pdf_parser import extract_text_from_pdf
from agents.resume_agent import analyze_resume
from tools.text_to_speech import text_to_speech
from tools.report_generator import generate_report

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Review Agent",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📄 AI Resume Review Agent")
st.write("Upload your resume and let AI analyze it using AI.")
st.divider()

# -----------------------------
# Upload Resume
# -----------------------------
resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)


# -----------------------------
# Analyze Button
# -----------------------------
if st.button("Analyze Resume"):

    if resume is None:
        st.error("Please upload a PDF Resume.")

    else:

        # -----------------------------
        # Extract Resume Text
        # -----------------------------
        with st.spinner("Reading Resume..."):
            resume_text = extract_text_from_pdf(resume)

        # -----------------------------
        # Analyze Resume
        # -----------------------------
        with st.spinner("Analyzing Resume..."):
            analysis = analyze_resume(resume_text)

        st.success("Resume uploaded successfully!")

        # -----------------------------
        # Error Handling
        # -----------------------------
        if "error" in analysis:

            st.error("Unable to parse Gemini response.")
            st.write(analysis["error"])

        else:

            # -----------------------------
            # Scores
            # -----------------------------
            st.header("📋 Resume Review Report")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Overall Resume Score",
                    analysis["overall_score"]
                )

            with col2:
                st.metric(
                    "ATS Score",
                    analysis["ats_score"]
                )

            # -----------------------------
            # Grammar
            # -----------------------------
            st.subheader("📝 Grammar Review")
            st.write(analysis["grammar_review"])

            # -----------------------------
            # Formatting
            # -----------------------------
            st.subheader("📄 Formatting Review")
            st.write(analysis["formatting_review"])

            # -----------------------------
            # Technical Skills
            # -----------------------------
            st.subheader("💻 Technical Skills")
            st.write(", ".join(analysis["technical_skills"]))

            # -----------------------------
            # Soft Skills
            # -----------------------------
            st.subheader("🤝 Soft Skills")
            st.write(", ".join(analysis["soft_skills"]))

            # -----------------------------
            # Missing Skills
            # -----------------------------
            st.subheader("❌ Missing Skills")
            st.write(", ".join(analysis["missing_skills"]))

            # -----------------------------
            # Missing Keywords
            # -----------------------------
            st.subheader("🔑 Missing Keywords")
            st.write(", ".join(analysis["missing_keywords"]))

            # -----------------------------
            # Professional Summary
            # -----------------------------
            st.subheader("📌 Professional Summary")
            st.write(analysis["professional_summary"])

            # -----------------------------
            # Improved Bullet Points
            # -----------------------------
            st.subheader("🚀 Improved Resume Bullet Points")

            for bullet in analysis["improved_bullet_points"]:
                st.markdown(f"- {bullet}")

            # -----------------------------
            # Recommendations
            # -----------------------------
            st.subheader("✅ Recommendations")

            for rec in analysis["recommendations"]:
                st.markdown(f"- {rec}")

            # -----------------------------
            # Voice Summary
            # -----------------------------
            st.subheader("🔊 Voice Summary")

            summary = f"""
            Your overall resume score is {analysis['overall_score']}.
            Your ATS score is {analysis['ats_score']}.
            Please review the recommendations to improve your resume.
            """

            voice_file = text_to_speech(summary)

            st.audio(voice_file)

            # -----------------------------
            # Generate PDF Report
            # -----------------------------
            pdf_path = generate_report(analysis)

            with open(pdf_path, "rb") as pdf_file:

                st.download_button(
                    label="📄 Download Resume Review Report",
                    data=pdf_file,
                    file_name="Resume_Report.pdf",
                    mime="application/pdf"
                )
                
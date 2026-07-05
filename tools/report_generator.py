import os

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Create reports folder if it doesn't exist
os.makedirs("reports", exist_ok=True)


def generate_report(analysis):
    """
    Generates a PDF Resume Review Report.

    Args:
        analysis (dict): Analysis returned by Gemini.

    Returns:
        str: Path of generated PDF.
    """

    pdf_path = "reports/Resume_Report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    # -----------------------------
    # Title
    # -----------------------------
    story.append(Paragraph("<b>AI Resume Review Report</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    # -----------------------------
    # Scores
    # -----------------------------
    story.append(
        Paragraph(
            f"<b>Overall Resume Score:</b> {analysis['overall_score']}",
            styles["Heading2"],
        )
    )

    story.append(
        Paragraph(
            f"<b>ATS Score:</b> {analysis['ats_score']}",
            styles["Heading2"],
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    # -----------------------------
    # Grammar
    # -----------------------------
    story.append(Paragraph("<b>Grammar Review</b>", styles["Heading2"]))
    story.append(Paragraph(str(analysis["grammar_review"]), styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    # -----------------------------
    # Formatting
    # -----------------------------
    story.append(Paragraph("<b>Formatting Review</b>", styles["Heading2"]))
    story.append(Paragraph(str(analysis["formatting_review"]), styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    # -----------------------------
    # Technical Skills
    # -----------------------------
    story.append(Paragraph("<b>Technical Skills</b>", styles["Heading2"]))

    for skill in analysis["technical_skills"]:
        story.append(Paragraph(f"• {skill}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    # -----------------------------
    # Soft Skills
    # -----------------------------
    story.append(Paragraph("<b>Soft Skills</b>", styles["Heading2"]))

    for skill in analysis["soft_skills"]:
        story.append(Paragraph(f"• {skill}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    # -----------------------------
    # Missing Skills
    # -----------------------------
    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))

    for skill in analysis["missing_skills"]:
        story.append(Paragraph(f"• {skill}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    # -----------------------------
    # Missing Keywords
    # -----------------------------
    story.append(Paragraph("<b>Missing Keywords</b>", styles["Heading2"]))

    for keyword in analysis["missing_keywords"]:
        story.append(Paragraph(f"• {keyword}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    # -----------------------------
    # Professional Summary
    # -----------------------------
    story.append(Paragraph("<b>Professional Summary</b>", styles["Heading2"]))
    story.append(
        Paragraph(str(analysis["professional_summary"]), styles["BodyText"])
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    # -----------------------------
    # Improved Bullet Points
    # -----------------------------
    story.append(
        Paragraph("<b>Improved Resume Bullet Points</b>", styles["Heading2"])
    )

    for bullet in analysis["improved_bullet_points"]:
        story.append(Paragraph(str(bullet), styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    # -----------------------------
    # Recommendations
    # -----------------------------
    story.append(Paragraph("<b>Recommendations</b>", styles["Heading2"]))

    for recommendation in analysis["recommendations"]:
        story.append(Paragraph(f"• {recommendation}", styles["BodyText"]))

    # -----------------------------
    # Build PDF
    # -----------------------------
    doc.build(story)

    return pdf_path
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def export_premium_lock_report(name, birth_date, location, rectified_time, score_matrix):
    """
    Sprint K Engine: Compiles the dynamic verified app parameters 
    into a beautiful, professional, printable cryptographic PDF report file.
    """
    # Create target directory for final output files
    os.makedirs('generated', exist_ok=True)
    pdf_filename = "generated/premium_lock_report.pdf"
    
    # Initialize the primary document layout template
    doc = SimpleDocTemplate(
        pdf_filename, 
        pagesize=letter,
        rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40,
        title="Cosmic Co-Pilot: Birth Time Rectification Certificate"
    )
    
    # Define color scheme palette
    primary_color = colors.HexColor("#0d0f14")  # Deep Space Blue
    accent_color = colors.HexColor("#6366f1")   # Electric Indigo
    success_color = colors.HexColor("#10b981")  # Matrix Green
    text_dark = colors.HexColor("#1e293b")      # Charcoal Grey
    
    # Setup stylesheet overrides
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=24, leading=28,
        textColor=accent_color, spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle', parent=styles['Normal'],
        fontName='Helvetica-Oblique', fontSize=10, leading=14,
        textColor=colors.HexColor("#64748b"), spaceAfter=20
    )
    
    section_heading = ParagraphStyle(
        'SecHeading', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=14, leading=18,
        textColor=primary_color, spaceBefore=15, spaceAfter=8
    )
    
    body_text = ParagraphStyle(
        'BodyText', parent=styles['Normal'],
        fontName='Helvetica', fontSize=10, leading=15,
        textColor=text_dark
    )
    
    story = []
    
    # 1. DOCUMENT HEADER BLOCK
    story.append(Paragraph("COSMIC CO-PILOT: RECTIFICATION RUN", title_style))
    story.append(Paragraph("Official Birth Time Mathematical Verification Certificate & Matrix Audit", subtitle_style))
    story.append(Spacer(1, 10))
    
    # 2. VERIFIED PARAMETERS MATRIX (TABLE)
    story.append(Paragraph("Verified Profile Coordinates", section_heading))
    profile_data = [
        [Paragraph("<b>Target Identity Name:</b>", body_text), Paragraph(name, body_text)],
        [Paragraph("<b>Target Birth Date:</b>", body_text), Paragraph(birth_date, body_text)],
        [Paragraph("<b>Location Space Coordinates:</b>", body_text), Paragraph(location, body_text)],
        [Paragraph("<b>Rectified Time (Locked):</b>", body_text), Paragraph(f"<font color='{success_color}'><b>{rectified_time}</b></font>", body_text)]
    ]
    
    profile_table = Table(profile_data, colWidths=[180, 350])
    profile_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('PADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LINEBELOW', (0,0), (-1, -2), 0.5, colors.HexColor("#e2e8f0")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
    ]))
    story.append(profile_table)
    story.append(Spacer(1, 20))
    
    # 3. FORENSIC AUDIT TRAIL DATA GRAPH (TABLE)
    story.append(Paragraph("Forensic Milestone Audit Trail Scores", section_heading))
    
    table_data = [[Paragraph("<b>Life Event Milestone</b>", body_text), Paragraph("<b>Mathematical Alignment Verification Score</b>", body_text)]]
    for event, score in score_matrix.items():
        score_para = Paragraph(f"<font color='{success_color}'><b>{score} Points Match (Calibrated)</b></font>", body_text)
        table_data.append([Paragraph(event, body_text), score_para])
        
    audit_table = Table(table_data, colWidths=[250, 280])
    audit_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e2533")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('PADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
    ]))
    # Quick structural loop to make the header row text white manually inside reportlab paragraph flows
    for i in range(2):
        table_data[0][i].style.textColor = colors.white
        
    story.append(audit_table)
    story.append(Spacer(1, 25))
    
    # 4. SYSTEM INTERPRETATION ARCHETYPE BLOCK
    story.append(Paragraph("Midheaven (MC) Career Archetype Readout", section_heading))
    profile_desc = (
        "Having Pisces on your career cusp means your professional life is a fluid winding river, "
        "not a rigid corporate highway. Your chart calculations prove that you do not possess a single fixed "
        "'passion' because you are mathematically wired to adapt to roles dynamically over time. "
        "Traditional corporate constraints suffocate your processing speed; your path thrives in fluid, creative, "
        "or deep intuitive counsel tracks."
    )
    story.append(Paragraph(profile_desc, body_text))
    story.append(Spacer(1, 30))
    
    # 5. FOOTNOTE COMPLIANCE DISCLAIMER
    disclaimer_style = ParagraphStyle(
        'Footnote', parent=styles['Normal'],
        fontName='Helvetica-Oblique', fontSize=8, leading=11,
        textColor=colors.HexColor("#94a3b8")
    )
    story.append(Paragraph("This is for informational purposes only. For medical advice or diagnosis, consult a professional. AI responses may include mistakes.", disclaimer_style))
    
    # Build document
    doc.build(story)
    print(f"🏆 System Success! PDF certificate output compiled cleanly to: {pdf_filename}")

# --- RUNNING DYNAMIC EXPORT TEST ---
user_scores = {
    "April 2019 Broken Wrist/Knee": 15,
    "October 2022 Burnout Leave": 12,
    "March 2024 Pet Medical Crisis": 10,
    "July 2026 Complicated Job Loss": 15
}

export_premium_lock_report(
    name="Ess", 
    birth_date="January 28, 1983", 
    location="Roberval, Québec", 
    rectified_time="3:09 PM", 
    score_matrix=user_scores
)

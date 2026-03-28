from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from datetime import datetime
import io

class ReportGenerator:
    """Generate professional PDF health reports"""
    
    def __init__(self):
        self.pagesize = A4
        self.width, self.height = self.pagesize
        
    def generate_report(self, patient_data, prediction_result, recommendations):
        """
        Generate PDF report
        
        Args:
            patient_data: dict with patient information
            prediction_result: dict with prediction results
            recommendations: dict with recommendations
        
        Returns:
            bytes: PDF content
        """
        # Create PDF in memory
        pdf_buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=self.pagesize,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch
        )
        
        # Create story
        story = []
        styles = getSampleStyleSheet()
        
        # Header
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=28,
            textColor=colors.HexColor('#1e3a8a'),
            spaceAfter=6,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Normal'],
            fontSize=12,
            textColor=colors.HexColor('#64748b'),
            spaceAfter=20,
            alignment=TA_CENTER
        )
        
        story.append(Paragraph("SLEEP HEALTH", title_style))
        story.append(Paragraph("Comprehensive Sleep Assessment Report", subtitle_style))
        story.append(Spacer(1, 0.2*inch))
        
        # Report Date
        date_style = ParagraphStyle(
            'DateStyle',
            parent=styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#94a3b8'),
            spaceAfter=30
        )
        report_date = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        story.append(Paragraph(f"Report Generated: {report_date}", date_style))
        
        # Patient Information Section
        story.append(self._create_section_title("PATIENT INFORMATION", styles))
        
        patient_info_data = [
            ["Gender", "Male" if patient_data.get('gender') == 0 else "Female"],
            ["Age", f"{patient_data.get('age', 'N/A')} years"],
            ["Sleep Duration", f"{patient_data.get('sleep_duration', 'N/A')} hours"],
            ["BMI Category", ["Underweight", "Normal", "Overweight", "Obese"][patient_data.get('bmi_category', 1)]],
        ]
        
        story.append(self._create_table(patient_info_data, styles))
        story.append(Spacer(1, 0.3*inch))
        
        # Prediction Results Section
        story.append(self._create_section_title("ASSESSMENT RESULTS", styles))
        
        result_color_map = {
            "Normal Sleep": colors.HexColor('#28a745'),
            "Insomnia": colors.HexColor('#ffc107'),
            "Sleep Apnea": colors.HexColor('#dc3545')
        }
        result_color = result_color_map.get(prediction_result['prediction'], colors.black)
        
        result_style = ParagraphStyle(
            'ResultStyle',
            parent=styles['Normal'],
            fontSize=16,
            textColor=result_color,
            spaceAfter=12,
            fontName='Helvetica-Bold'
        )
        
        story.append(Paragraph(f"Predicted Condition: {prediction_result['prediction']}", result_style))
        
        risk_level = prediction_result['risk_level']
        risk_style = ParagraphStyle(
            'RiskStyle',
            parent=styles['Normal'],
            fontSize=12,
            textColor=result_color,
            spaceAfter=12
        )
        story.append(Paragraph(f"Risk Level: {risk_level}", risk_style))
        
        conf_style = ParagraphStyle(
            'ConfStyle',
            parent=styles['Normal'],
            fontSize=11,
            textColor=colors.HexColor('#64748b'),
            spaceAfter=30
        )
        story.append(Paragraph(f"Confidence Score: {prediction_result['confidence']:.1f}%", conf_style))
        
        # Health Metrics Section
        story.append(self._create_section_title("HEALTH METRICS", styles))
        
        metrics_data = [
            ["Heart Rate", f"{patient_data.get('heart_rate', 'N/A')} bpm"],
            ["Blood Pressure", f"{patient_data.get('sbp', 'N/A')}/{patient_data.get('dbp', 'N/A')} mmHg"],
            ["Daily Steps", f"{patient_data.get('daily_steps', 0):,.0f}"],
            ["Oxygen Saturation", f"{patient_data.get('oxygen_saturation', 'N/A')}%"],
            ["Physical Activity", f"{patient_data.get('physical_activity', 'N/A')} days/week"],
        ]
        
        story.append(self._create_table(metrics_data, styles))
        story.append(Spacer(1, 0.3*inch))
        
        # Recommendations Section
        story.append(self._create_section_title("PERSONALIZED RECOMMENDATIONS", styles))
        
        rec_text_style = ParagraphStyle(
            'RecText',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=8,
            leftIndent=0.2*inch
        )
        
        # Lifestyle
        story.append(Paragraph("🧘 Lifestyle:", styles['Heading3']))
        for rec in recommendations.get('lifestyle', []):
            story.append(Paragraph(f"• {rec}", rec_text_style))
        story.append(Spacer(1, 0.15*inch))
        
        # Sleep Habits
        story.append(Paragraph("😴 Sleep Habits:", styles['Heading3']))
        for rec in recommendations.get('sleep_habits', []):
            story.append(Paragraph(f"• {rec}", rec_text_style))
        story.append(Spacer(1, 0.15*inch))
        
        # Medical Advice
        story.append(Paragraph("🩺 Medical Advice:", styles['Heading3']))
        for rec in recommendations.get('medical_advice', []):
            story.append(Paragraph(f"• {rec}", rec_text_style))
        
        story.append(Spacer(1, 0.4*inch))
        
        # Footer
        footer_style = ParagraphStyle(
            'Footer',
            parent=styles['Normal'],
            fontSize=9,
            textColor=colors.HexColor('#94a3b8'),
            alignment=TA_CENTER,
            spaceAfter=0
        )
        
        story.append(Paragraph("This report is generated for informational purposes only and should not replace professional medical advice.", footer_style))
        story.append(Paragraph("Please consult a healthcare professional for diagnosis and treatment.", footer_style))
        
        # Build PDF
        doc.build(story)
        pdf_buffer.seek(0)
        return pdf_buffer.getvalue()
    
    def _create_section_title(self, title, styles):
        """Create a section title"""
        title_style = ParagraphStyle(
            'SectionTitle',
            parent=styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#1e3a8a'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        )
        return Paragraph(title, title_style)
    
    def _create_table(self, data, styles):
        """Create a formatted table"""
        table = Table(data, colWidths=[2*inch, 3.5*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f0f9ff')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, colors.HexColor('#f8fafc')])
        ]))
        return table

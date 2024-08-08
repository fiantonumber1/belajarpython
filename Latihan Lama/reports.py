#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)
    penggayaan = getSampleStyleSheet()
    info_laporan = Paragraph(paragraph, penggayaan["Normal"])
    report_title = Paragraph(title, penggayaan["h1"])
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, info_laporan])

"""
Serviço de geração de relatórios PDF
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart
from io import BytesIO
from datetime import datetime
import os

class PDFReportService:
    """Serviço para geração de relatórios PDF profissionais"""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.custom_styles = self._create_custom_styles()
    
    def _create_custom_styles(self):
        """Criar estilos personalizados"""
        custom_styles = {}
        
        # Título principal
        custom_styles['Title'] = ParagraphStyle(
            'Title',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=1,  # Centro
            textColor=colors.HexColor('#2c3e50')
        )
        
        # Subtítulo
        custom_styles['Subtitle'] = ParagraphStyle(
            'Subtitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=20,
            textColor=colors.HexColor('#34495e')
        )
        
        # Texto normal com margem
        custom_styles['NormalIndent'] = ParagraphStyle(
            'NormalIndent',
            parent=self.styles['Normal'],
            leftIndent=20,
            spaceAfter=12
        )
        
        return custom_styles
    
    def generate_tnc_report(self, tncs, filters=None):
        """Gerar relatório de TNCs"""
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        # Conteúdo do relatório
        story = []
        
        # Cabeçalho
        story.append(Paragraph("Relatório de TNCs", self.custom_styles['Title']))
        story.append(Paragraph(f"Gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M')}", 
                              self.styles['Normal']))
        story.append(Spacer(1, 12))
        
        # Filtros aplicados
        if filters:
            story.append(Paragraph("Filtros Aplicados:", self.custom_styles['Subtitle']))
            for key, value in filters.items():
                if value:
                    story.append(Paragraph(f"• {key.title()}: {value}", self.custom_styles['NormalIndent']))
            story.append(Spacer(1, 20))
        
        # Resumo executivo
        story.append(Paragraph("Resumo Executivo", self.custom_styles['Subtitle']))
        
        total_tncs = len(tncs)
        valor_total = sum(float(tnc.valor or 0) for tnc in tncs)
        
        # Estatísticas por status
        stats_status = {}
        stats_gravidade = {}
        for tnc in tncs:
            stats_status[tnc.status] = stats_status.get(tnc.status, 0) + 1
            stats_gravidade[tnc.gravidade] = stats_gravidade.get(tnc.gravidade, 0) + 1
        
        resumo_data = [
            ['Indicador', 'Valor'],
            ['Total de TNCs', str(total_tncs)],
            ['Valor Total', f'R$ {valor_total:,.2f}'],
            ['TNCs Abertas', str(stats_status.get('Aberta', 0))],
            ['TNCs Em Reinspeção', str(stats_status.get('Em Reinspeção', 0))],
            ['TNCs Concluídas', str(stats_status.get('Concluída', 0))],
            ['TNCs Graves', str(stats_gravidade.get('Grave', 0))],
            ['TNCs Médias', str(stats_gravidade.get('Média', 0))],
            ['TNCs Leves', str(stats_gravidade.get('Leve', 0))],
        ]
        
        resumo_table = Table(resumo_data, colWidths=[3*inch, 2*inch])
        resumo_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(resumo_table)
        story.append(Spacer(1, 30))
        
        # Lista detalhada de TNCs
        if tncs:
            story.append(Paragraph("Detalhamento das TNCs", self.custom_styles['Subtitle']))
            
            # Cabeçalho da tabela
            tnc_data = [
                ['Nº', 'Empresa', 'Projeto', 'Gravidade', 'Status', 'Valor', 'Data Emissão']
            ]
            
            # Dados das TNCs
            for tnc in tncs:
                tnc_data.append([
                    tnc.numero_sequencia or '',
                    tnc.empresa.nome[:20] + '...' if len(tnc.empresa.nome) > 20 else tnc.empresa.nome,
                    tnc.projeto.nome[:15] + '...' if len(tnc.projeto.nome) > 15 else tnc.projeto.nome,
                    tnc.gravidade,
                    tnc.status,
                    f'R$ {float(tnc.valor or 0):,.2f}',
                    tnc.data_emissao.strftime('%d/%m/%Y')
                ])
            
            tnc_table = Table(tnc_data, colWidths=[0.8*inch, 1.5*inch, 1.2*inch, 0.8*inch, 1*inch, 1*inch, 1*inch])
            tnc_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))
            
            story.append(tnc_table)
        
        # Rodapé
        story.append(Spacer(1, 50))
        story.append(Paragraph("Relatório gerado pelo Sistema TNC Gestão", 
                              ParagraphStyle('Footer', 
                                           parent=self.styles['Normal'],
                                           fontSize=8,
                                           alignment=1,
                                           textColor=colors.grey)))
        
        # Gerar PDF
        doc.build(story)
        buffer.seek(0)
        
        return buffer
    
    def generate_dashboard_report(self, stats, charts_data):
        """Gerar relatório executivo do dashboard"""
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        
        story = []
        
        # Título
        story.append(Paragraph("Relatório Executivo - Dashboard TNC", self.custom_styles['Title']))
        story.append(Paragraph(f"Período: {datetime.now().strftime('%d/%m/%Y')}", self.styles['Normal']))
        story.append(Spacer(1, 30))
        
        # Indicadores principais
        story.append(Paragraph("Indicadores Principais", self.custom_styles['Subtitle']))
        
        kpi_data = [
            ['Indicador', 'Valor'],
            ['Total de TNCs', str(stats.get('total_tncs', 0))],
            ['TNCs Abertas', str(stats.get('tncs_abertas', 0))],
            ['TNCs em Reinspeção', str(stats.get('tncs_reinspeção', 0))],
            ['TNCs Concluídas', str(stats.get('tncs_concluidas', 0))],
            ['Valor Total', f"R$ {stats.get('valor_total', 0):,.2f}"],
            ['Total de Empresas', str(stats.get('total_empresas', 0))],
            ['Total de Projetos', str(stats.get('total_projetos', 0))],
        ]
        
        kpi_table = Table(kpi_data, colWidths=[3*inch, 2*inch])
        kpi_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e74c3c')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(kpi_table)
        story.append(Spacer(1, 30))
        
        doc.build(story)
        buffer.seek(0)
        
        return buffer
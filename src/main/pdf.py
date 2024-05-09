from fpdf import FPDF


class PDF(FPDF):
    pass
    
    def createPdf():
        pdf = PDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.output('test.pdf', 'F')
        
    def create(self):
        self.createPDF()


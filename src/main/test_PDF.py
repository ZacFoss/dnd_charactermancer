import unittest

from pdf import PDF


class testPDF(unittest.TestCase):
    
    def testCreatePDF(self):
        PDF.createPdf()
        
if __name__ == '__main__':
    unittest.main()
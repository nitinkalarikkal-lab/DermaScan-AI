from fpdf import FPDF
import re

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Dermascan AI - Team Contributions', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf(md_file, pdf_file):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            pdf.ln(5)
            continue
        
        # Headers
        if line.startswith('# '):
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, line[2:], ln=True)
            pdf.set_font("Arial", size=12)
        elif line.startswith('## '):
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(0, 10, line[3:], ln=True)
            pdf.set_font("Arial", size=12)
        elif line.startswith('### '):
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, line[4:], ln=True)
            pdf.set_font("Arial", size=12)
        
        # Bold text **text**
        elif '**' in line:
            parts = re.split(r'(\*\*.*?\*\*)', line)
            for part in parts:
                if part.startswith('**') and part.endswith('**'):
                    pdf.set_font("Arial", 'B', 12)
                    pdf.write(5, part[2:-2])
                else:
                    pdf.set_font("Arial", '', 12)
                    pdf.write(5, part)
            pdf.ln(5)
        
        # List items
        elif line.startswith('* ') or line.startswith('- '):
            pdf.set_font("Arial", '', 12)
            pdf.write(5, '  - ' + line[2:])
            pdf.ln(5)
            
        # Normal text
        else:
            pdf.set_font("Arial", '', 12)
            # Replace common unicode chars
            line = line.replace('\u2013', '-').replace('\u2014', '-').replace('\u2018', "'").replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
            # Force latin-1
            line = line.encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 5, line)

    pdf.output(pdf_file)
    print(f"PDF created: {pdf_file}")

if __name__ == "__main__":
    files = [
        ("CONTRIBUTIONS.md", "CONTRIBUTIONS.pdf"),
        ("ML_EXPLANATION.md", "ML_EXPLANATION.pdf"),
        ("VIVA_QA.md", "VIVA_QA.pdf")
    ]
    for md, pdf in files:
        try:
            create_pdf(md, pdf)
        except PermissionError:
            print(f"Skipped {pdf}: File is open or locked.")
        except Exception as e:
            print(f"Failed to create {pdf}: {e}")

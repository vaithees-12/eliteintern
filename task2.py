from fpdf import FPDF
from datetime import datetime

# Create PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "EliteTech Python Internship - Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def add_paragraph(self, text):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, text)
        self.ln()

# Initialize PDF
pdf = PDF()
pdf.add_page()

# Report content
pdf.add_section_title("Date")
pdf.add_paragraph(datetime.now().strftime("%d %B %Y"))

pdf.add_section_title("Task 1 Summary")
pdf.add_paragraph(
    "In Task 1, I integrated the CoinGecko cryptocurrency API using Python. "
    "The data was extracted, converted to a pandas DataFrame, and visualized using matplotlib "
    "to show the top 10 cryptocurrencies by market capitalization."
)

pdf.add_section_title("Tools Used")
pdf.add_paragraph(
    "- Python\n- requests\n- pandas\n- matplotlib\n- fpdf"
)

pdf.output("report.pdf")
print("✅ PDF report generated successfully.")

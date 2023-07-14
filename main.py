from fpdf import FPDF
import pandas as pd 

pdf = FPDF(orientation="P", unit="mm", format="A4")
# Sets PDF to portrait or landscape mode. Also, sets the unit for dimensions. 

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # Uses RGB colors
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1) 
    # align=aligns text on the left, right or middle of page, ln=break line, border=1 adds border
    pdf.line(10, 21, 200, 21)
    # Uses coordinates (x1, y1, x2, y2) to place the line

    for i in range(row['Pages'] - 1):
        # Repeats the loop based on the range
        pdf.add_page()

pdf.output("output.pdf") 
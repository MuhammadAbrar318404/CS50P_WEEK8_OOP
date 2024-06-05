from fpdf import FPDF

class PDF(FPDF):
    ...

def create_shirtificate(name):
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add header
    pdf.set_font("Arial", "B", 24)
    pdf.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")


    # Add the shirt image
    pdf.image("shirtificate.png", x=10, y=50, w=190)

    # Add the name on the shirt
    pdf.set_text_color(255, 255, 255)  # White color
    pdf.set_font("Arial", "B", 36)
    pdf.text(x=55, y=140, txt=name)

    # Output the PDF to a file
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    name = input("Enter your name: ")
    create_shirtificate(name+" took CS50")

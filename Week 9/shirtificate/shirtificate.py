# Importing the FPDF class
from fpdf import FPDF


# Defining a PDF class inherting form FPDF and overriding the header method.
class PDF(FPDF):
    def header(self):
        # Adding the shirt image and centering it.
        self.image("shirtificate.png", 10, 70, 190)
        # Setting the front for the header text.
        self.set_font("Times", "BU", 52)
        # Setting the draw color or outline color for the header text.
        self.set_draw_color(227, 3, 252)
        # Setting the text mode per https://py-pdf.github.io/fpdf2/TextStyling.html#text_mode
        with PDF.local_context(self, text_mode="FILL_STROKE", line_width=1):
            # Adding the header text using the .cell method.
            self.cell(0, 45, "CS50 Shirtificate", align="C")
        self.ln(20)


def main():
    # Prompting the user for input.
    name = input("Your Name: ")
    # Creating an instance of the PDF class.
    pdf = PDF()
    # Adding a new page to the PDF file.
    pdf.add_page()
    # Setting the font for the text on the shirt.
    pdf.set_font("Times", "B", 34)
    # Setting the font color to white.
    pdf.set_text_color(255, 255, 255)
    # Adding the inputted name and the rest of the text to the shirt, using the cell method.
    pdf.cell(0, 195, f"{name} took CS50", align="C")
    # Saving the PDF file with the specified name.
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

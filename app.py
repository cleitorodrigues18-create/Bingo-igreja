from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def gerar_cartelas():
    c = canvas.Canvas("cartelas.pdf", pagesize=letter)

    serie = "A"
    total = 500

    for i in range(1, total + 1):
        c.setFont("Helvetica-Bold", 16)
        c.drawString(180, 750, "BINGO BENEFICENTE")

        c.setFont("Helvetica", 12)
        c.drawString(200, 720, f"Série {serie}")
        c.drawString(180, 700, f"Cartela Nº {i:04}")

        # área cartela
        c.rect(100, 500, 400, 150)

        # canhoto destacável
        c.rect(100, 460, 400, 30)
        c.drawString(110, 470, f"Canhoto - Série {serie} Nº {i:04}")

        c.showPage()

    c.save()

gerar_cartelas()

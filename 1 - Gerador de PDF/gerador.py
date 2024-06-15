#TODOS OS COMENTARIOS A RESPEITO DESTE CÓDIGO
#ESTÁ NO ARQUIVO JUPITER (.IPYNB)

from fpdf import FPDF

descricao_projeto =input("Digite a descrição do projeto: ")
horas_previstas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da Hora trabalhada: ")
prazo_estimado = input("Digite o prazo estimado: ")

valor_total = int(horas_previstas) * int(valor_hora)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)

pdf.image("template.png", x=0, y=0)

pdf.text(115, 145, descricao_projeto)
pdf.text(115, 160, horas_previstas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo_estimado)

pdf.text(115, 205, str(valor_total))

pdf.output("Documento.pdf")
print("Documento gerado com sucesso!")
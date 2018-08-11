import docx2txt
import glob

PATH_ARTIGOS = r".\prontuarios_originais"
	
# Converter docx em txt
lista_arq_artigos = glob.glob(PATH_ARTIGOS + r"\*.docx")
for arq in lista_arq_artigos:
	text = docx2txt.process(arq)
	arq = open(arq + ".txt", 'w')
	try: 
		arq.write(text)
	except ValueError:
		print(arq)
	arq.close()

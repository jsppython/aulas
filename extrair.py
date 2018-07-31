import re
import docx2txt
import glob

PATH_ARTIGOS = r"D:\downloads\artigos"
KEYWORD = "flexão"

def extrair_frase(linha, palavra):
	frase = None
	padrao = r"[^\.\n]*\b" + palavra + r"\b[^\.\n]*[\.\n]"
	matches = re.search(padrao, linha, re.I)
	if matches:
		frase = matches.group(0)
	return frase
	
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

# Identificar os prontuários (arquivos) que referenciam artrose
lista_arq_texto = glob.glob(PATH_ARTIGOS + r"\*.txt")
lista_arq_keyword = []
for nome_arq in lista_arq_texto:
	texto = ""
	arq = open(nome_arq, 'r')
	texto = arq.read()
	arq.close()
	if KEYWORD in texto.lower():
		lista_arq_keyword.append(nome_arq)

linhas_resultado = []
		
# Extrair as frases que referenciam artrose
for nome_arq in lista_arq_keyword:
	arq = open(nome_arq, 'r')
	linhas = arq.readlines()
	arq.close()
	for linha in linhas:
		#print(linha)
		frase = extrair_frase(linha, KEYWORD) 
		if frase:
			print(frase + "\n\n")
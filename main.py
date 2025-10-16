from curriculo import gerar_html, salvar_html, coletar_dados

def main():
	nome, email, resumo, arq_exp, arq_hab = coletar_dados()
	html = gerar_html(nome, email, resumo, arq_exp, arq_hab)
	salvar_html(html)
	
if __name__ == "__main__":
	main()
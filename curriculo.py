def coletar_dados():
    nome = input("Nome: ")
    email = input("E-mail: ")
    resumo = input("Resumo: ")

    arq_exp = open("experiencias.txt", "w", encoding="utf-8")
    continuar = 's'
    while continuar == 's' or continuar == 'S':
        exp = input("Digite uma experiência: ")
        arq_exp.write(exp + "\n")
        continuar = input("Deseja adicionar outra experiência? [S/N] ")
    arq_exp.close()

    arq_hab = open("habilidades.txt", "w", encoding="utf-8")
    continuar = 's'
    while continuar == 's' or continuar == 'S':
        hab = input("Digite uma habilidade: ")
        arq_hab.write(hab + "\n")
        continuar = input("Deseja adicionar outra habilidade? [S/N] ")
    arq_hab.close()

    return nome, email, resumo, "experiencias.txt", "habilidades.txt"


def gerar_html(nome, email, resumo, arq_experiencias, arq_habilidades):
    foto = "foto.jpg"

    arq = open(arq_experiencias, "r", encoding="utf-8")
    experiencias = arq.readlines()
    arq.close()
    lista_exp = ""
    for e in experiencias:
        lista_exp += f"<li>{e.strip()}</li>"

    arq = open(arq_habilidades, "r", encoding="utf-8")
    habilidades = arq.readlines()
    arq.close()
    lista_hab = ""
    for h in habilidades:
        lista_hab += f"<li>{h.strip()}</li>"

        html = f"""
<html>
<head>
<meta charset="utf-8">
<title>Currículo de {nome}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="card">
        <header>
            <h1>{nome}</h1>
            <img src="images.jpg" alt="Foto de {nome}">
            <div class="meta">
                <span class="badge">{email}</span>
            </div>
        </header>

        <section>
            <h2>Resumo Profissional</h2>
            <p>{resumo}</p>
        </section>

        <section>
            <h2>Experiências</h2>
            <ul>{lista_exp}</ul>
        </section>

        <section>
            <h2>Habilidades</h2>
            <ul>{lista_hab}</ul>
        </section>

        <footer>
            Gerado automaticamente
        </footer>
    </div>
</body>
</html>
"""
    return html


def salvar_html(html):
    arq = open("curriculo.html", "w", encoding="utf-8")
    arq.write(html)
    arq.close()
    print("Currículo gerado: curriculo.html")

import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Dados das famílias
familia = {
    "regetz": {
        "email": "aldabrasilia@gmail.com",
        "familia": ["Mikael Regetz", "Isabelly Regetz", "Miguel Regetz", "Alda Oliveira"]
    },
    "zimmermann": {
        "email": "cassiabrasilia@gmail.com",
        "familia": ["Cássia Zimmermann", "Rosino Estevam", "Salomão Zimmermann", "Serena Zimmermann"]
    },
    
    "henrique": {
        "email": "alanna.bsb.df@gmail.com",
        "familia": ["Alanna Zimmermann", "Ericatia Zimmermann", "Fábio Henrique"]
    },

    "soares": {
        "email": "lindalvasoaresr@gmail.com",
        "familia": ["Carlos", "Samuel", "Lindalva"]
    },

    "cassia": {
        "email": "demetrio.pereira1968@gmail.com",
        "familia": ["Ericarla", "Demetrio", "Abraão"]
    },
}

pessoas = []
for sobrenome, dados in familia.items():
    for membro in dados["familia"]:
        pessoas.append((membro, sobrenome))

# Função para realizar o sorteio
def sorteio_entre_familias(pessoas):
    resultado = {}
    disponiveis = pessoas.copy()
    
    for pessoa, familia_pessoa in pessoas:
        # Tentar sortear alguém de uma família diferente
        candidatos = [p for p in disponiveis if p[1] != familia_pessoa]
        
        if not candidatos:
            # Se não houver candidatos, reiniciar o sorteio
            return sorteio_entre_familias(pessoas)
        
        sorteado = random.choice(candidatos)
        resultado[pessoa] = sorteado[0]
        disponiveis.remove(sorteado)
    
    return resultado

# Função para enviar email
def enviar_email(destinatario, assunto, corpo):
    remetente = ""
    senha = ""

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    msg.attach(MIMEText(corpo, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha)
        texto = msg.as_string()
        server.sendmail(remetente, destinatario, texto)
        server.quit()

        print(f"Email enviado para {destinatario}")
    except Exception as e:
        print(f"Falha ao enviar email para {destinatario}: {e}")

# Executar o sorteio
resultado_sorteio = sorteio_entre_familias(pessoas)

# Preparar e enviar emails para cada família
for sobrenome, dados in familia.items():
    corpo_email = "Resultado do sorteio:\n\n"   
    for pessoa in dados["familia"]:
        sorteado = resultado_sorteio[str(pessoa)]
        corpo_email += f"{pessoa} tirou {sorteado}\n"

    print(corpo_email)
    #enviar_email(dados["email"], "Resultado do Sorteio de Natal", corpo_email)

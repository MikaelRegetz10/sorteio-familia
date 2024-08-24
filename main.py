import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Tuple, List, Dict
import settings.setting as settings


def lista_pessoas_e_familia(familia: dict) -> List[Tuple[str, str]]:
    pessoas = [] # (nome pessoas, familia)
    for sobrenome, dados in familia.items():
        for membro in dados["familia"]:
            pessoas.append((membro, sobrenome))
    return pessoas


def sorteio_entre_familias(pessoas: list) -> Dict[str,str]:
    resultado = {}
    disponiveis = pessoas.copy()
    
    for pessoa, familia_pessoa in pessoas:
        candidatos = [p for p in disponiveis if p[1] != familia_pessoa]
        
        if not candidatos:
            return sorteio_entre_familias(pessoas)
        
        sorteado = random.choice(candidatos)
        resultado[pessoa] = sorteado[0]
        disponiveis.remove(sorteado)
    return resultado


def enviar_email(destinatario: str, assunto: str, corpo: str) -> None:
    remetente = settings.EMAIL
    senha = settings.SENHA

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


def sorteio_main(familia: dict) -> Dict[str, bool]:
    try:
        print(familia)
        pessoas = lista_pessoas_e_familia(familia)
        resultado_sorteio = sorteio_entre_familias(pessoas)

        for sobrenome, dados in familia.items():
            corpo_email = "Olá, obrigado por escolher nosso site para o sorteio!\n\nSeguem os resultados do nosso sorteio:\n\n"
            for pessoa in dados["familia"]:
                sorteado = resultado_sorteio[str(pessoa)]
                corpo_email += f"• {pessoa} tirou {sorteado}\n"

            enviar_email(dados["email"], "Resultado do Sorteio", corpo_email)

        return {"status": True}

    except Exception as e:
        print(f"Erro: {e}")
        return {"status": False}
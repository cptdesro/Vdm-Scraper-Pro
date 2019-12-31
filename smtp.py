import smtplib
import ssl
from datetime import datetime
from socket import gaierror


def productionServerStart(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    login = "vdmscraperpro@gmail.com"
    sentTo = "julien.desrochers11@gmail.com"
    password = input("Type your password and press enter: ")
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(login, password)
        server.sendmail(login, sentTo, message)

    except (gaierror, ConnectionRefusedError):
        print('Impossible de se connecter au serveur. Mauvais paramètres de connexion?')
    except smtplib.SMTPServerDisconnected:
        print('Impossible de se connecter au serveur. Utilisateur / mot de passe incorrect?')
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
    else:
        print('Message envoyé.\nDe ' + login + '\nÀ ' + sentTo)
    finally:
        server.quit()


def debugServerStart(message):
    sender_email = "from@example.com"
    receiver_email = "mailtrap@example.com"
    smtp_server = "localhost"
    port = 1025
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.sendmail(sender_email, receiver_email, message)
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
    else:
        print('Message envoyé.\nDe ' + sender_email + '\nÀ ' + receiver_email)


def sendEmail():
    now = datetime.now()
    message = """\
    Subject: Nouveaux postes disponibles

    %s

    Il y a de nouveaux postes TI disponibles sur le site de la ville de MTLL.

    https://ville.montreal.qc.ca/mtl-ti/

    ---
    VdmScraperPro
    Copyright - 2020
     """ % (now.strftime("%d-%m-%Y, %H:%M:%S"))

    # productionServerStart(message)
    debugServerStart(message)

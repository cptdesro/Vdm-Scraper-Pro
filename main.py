from smtplib import SMTP
import requests, bs4
import smtplib
from socket import gaierror


def main():
    print("Début du processus")

    # variables
    websiteUrl = "https://ville.montreal.qc.ca/mtl-ti/"
    lookingForHtmlId = "#listing .narrow .end-post-text"  # Le div: "Il n'y a pas de poste à combler pour le moment."

    responseTextHtml = pingWebsite(websiteUrl)

    print("\n -------------------------- \n -------------------------- \n")
    if isHtmlElementPresent(responseTextHtml, lookingForHtmlId):
        print("Il n'y a pas d'emploi disponible pour l'instant. \nLe processus sera relancé plus tard.")
        sendEmail()

    else:
        print("Il y a des emplois disponible")
        sendEmail()


def sendEmail():
    sender_email = "from@example.com"
    receiver_email = "mailtrap@example.com"
    message = """\
    Subject: Nouveaux postes disponibles

    Il y a de nouveaux postes TI disponibles sur le site de la ville de MTLL.
    
    https://ville.montreal.qc.ca/mtl-ti/
    
    ---
    VdmScraperPro
    Copyright - 2020
     """

    # productionServerStart(sender_email, receiver_email, message)
    debuggServerStart(sender_email, receiver_email, message)


def productionServerStart(sender_email, receiver_email, message):
    # TODO
    smtp_server = ""
    port = 0
    login = ""
    password = ""

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(login, password)
            server.sendmail(sender_email, receiver_email, message)

    except (gaierror, ConnectionRefusedError):
        print('Impossible de se connecter au serveur. Mauvais paramètres de connexion?')
    except smtplib.SMTPServerDisconnected:
        print('Impossible de se connecter au serveur. Utilisateur / mot de passe incorrect?')
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
    else:
        print('Message envoyé.\nDe ' + sender_email + '\nÀ ' + receiver_email)
    finally:
        server.quit()


def debuggServerStart(sender_email, receiver_email, message):
    smtp_server = "localhost"
    port = 1025
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.sendmail(sender_email, receiver_email, message)
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
    else:
        print('Message envoyé.\nDe ' + sender_email + '\nÀ ' + receiver_email)


def isHtmlElementPresent(html, htmlElementToSearch):
    htmlStructure = bs4.BeautifulSoup(html)
    noJobAvailableHtmlTag = htmlStructure.select(htmlElementToSearch)

    return len(noJobAvailableHtmlTag) > 0


def pingWebsite(websiteUrl):
    res = requests.get(websiteUrl)
    res.raise_for_status()

    return res.text


main()





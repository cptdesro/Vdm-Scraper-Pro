import time, getpass
from utils import getCurrentTime
import scraper, smtp
URL_TO_FETCH = "https://ville.montreal.qc.ca/mtl-ti/"
HTML_ID_TO_TARGET = "#listing .narrow .end-post-text"  # Le div: "Il n'y a pas de poste à combler pour le moment."


def main():
    today = getCurrentTime()
    print("------------------------------"
          "------------------------------\n"
          "Début du processus - %s" % (today.strftime("%d-%m-%Y, %H:%M:%S")))
    password = getpass.getpass("Inscrire le mot de passe Marcel: ")

    # REPEAT_AFTER = 43200  # 12 hours
    REPEAT_AFTER = 10  # 12 hours

    now = time.time()
    repeatAfter = now + REPEAT_AFTER

    while 1:
        if time.time() >= repeatAfter:
            print("LETS PING - %s" % (getCurrentTime().strftime("%d-%m-%Y, %H:%M:%S")))

            responseTextHtml = scraper.pingWebsite(URL_TO_FETCH)

            if scraper.isHtmlElementPresent(responseTextHtml, HTML_ID_TO_TARGET):
                print("Il n'y a pas d'emploi disponible pour l'instant.\n"
                      "Le processus sera relancé dans %s secondes." % REPEAT_AFTER)
                smtp.sendEmail(password)
            else:
                print("Il y a des emplois disponibles!")
                # smtp.sendEmail(password)
            repeatAfter = time.time() + REPEAT_AFTER  # repeat again in X seconds


main()





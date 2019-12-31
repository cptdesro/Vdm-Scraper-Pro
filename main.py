import scraper
import smtp

URL_TO_FETCH = "https://ville.montreal.qc.ca/mtl-ti/"
HTML_ID_TO_TARGET = "#listing .narrow .end-post-text"  # Le div: "Il n'y a pas de poste à combler pour le moment."


def main():
    print("Début du processus")
    responseTextHtml = scraper.pingWebsite(URL_TO_FETCH)

    print("\n -------------------------- \n -------------------------- \n")
    if scraper.isHtmlElementPresent(responseTextHtml, HTML_ID_TO_TARGET):
        print("Il n'y a pas d'emploi disponible pour l'instant. \nLe processus sera relancé plus tard.")
        smtp.sendEmail()

    else:
        print("Il y a des emplois disponible")
        smtp.sendEmail()


main()





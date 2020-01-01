import bs4
import requests


def isHtmlElementPresent(html, htmlElementToSearch):
    htmlStructure = bs4.BeautifulSoup(html, features="html.parser")
    noJobAvailableHtmlTag = htmlStructure.select(htmlElementToSearch)

    return len(noJobAvailableHtmlTag) > 0


def pingWebsite(websiteUrl):
    res = requests.get(websiteUrl)
    res.raise_for_status()

    return res.text

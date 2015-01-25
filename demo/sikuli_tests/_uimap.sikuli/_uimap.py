########################################################
# UI map for XYZ
########################################################
from sikuli import *
########################################################

class Google:
    searchBar = Pattern("searchBar-1.png").similar(0.80)
    telerikTab= "telerikTab.png"
    imagesTab = "images.png"
    telerikImage = "telerikImage.png"
    copy = "copy.png"
    adrressBar = "adrressBar.png"
    spaste = "spaste.png"

class Cities:
    oslo = "oslo.png"
    coppenhagen = "coppenhagen.png"
    stockholm = "stockholm.png"
    washington = "washington.png"
    seoul = "seoul.png"
    rome = "rome.png"
    madrid = "madrid.png"

class Countries:
    italy = "italy.png"
    sweden = "sweden.png"
    norway = "norway.png"
    spain = "spain.png"
    USA = "usa.png"
    southKorea = "soutKorea.png"
    denmark = "denmark.png"

class CitiesInCountries:
    romeItaly = "romeD.png"
    madridSpain = "madridD.png"
    seoulKorea = "seoulD.png"
    washingtonUsa = "washingtonD.png"
    coppenhagenDenmark = "coppenhagenD.png"
    stockholmSweden = "stockholmD.png"
    osloNorway = "osloD.png"

class Calculator:
    seven = "seven.png"
    five = "five.png"
    plus = "plus.png"
    minus = "minus.png"
    divide = "divide.png"
    multiply ="multiply.png"
    equals = "equals.png"
    thirtyFive = "thirtyFive.png"
    two = "two.png"
    twelve ="twelve.png"
    onePointFour = "onePointFour.png"
class Tabs:
    closeButton = "close.png"
    chrome = Pattern("chrome.png").similar(0.56)
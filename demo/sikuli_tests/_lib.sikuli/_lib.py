from sikuli import *
import HTMLTestRunner
bdLibPath = os.path.abspath(sys.argv[0] + "..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _uimap import *

def RunBrowserToUrl(browser,toUrl):
    #TestAction("Start " +browser +" "+toUrl)
    sleep(0.5)
    type("d",KEY_WIN); sleep(1)
    type("r", KEY_WIN); sleep(1)
    type(browser+" "); sleep(1)
    type(toUrl); sleep(1)
    type(Key.ENTER)
    
def CalculateAndVerify(firstMember, secondMember, operation, expected):
    sleep(0.5)
    type("d",KEY_WIN); sleep(1)
    type("r", KEY_WIN); sleep(1)
    type("calc"); sleep(1)
    type(Key.ENTER)
    click(firstMember)
    click(operation)
    click(secondMember)
    click(Calculator.equals)
    wait(expected,2)
    
def HighlightRegion(x,y,width,height):
    regLeft = Region(x,y,width,height)
    regLeft.highlight(5)
    regRight = Region(x+650,y,width,height)
    regRight.highlight(5)
    
def test_001_NavigateToTap(self):
        RunBrowserToUrl("chrome","http://google.com")
        wait(Google.searchBar,4)
        type(Google.searchBar,"Telerik Academy")
        wait(Google.telerikTab)
               
def test_002_DragAndDropCapitals(self):
        RunBrowserToUrl("chrome","http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
        dragDrop(Cities.oslo,Countries.norway)
        dragDrop(Cities.coppenhagen,Countries.denmark)
        dragDrop(Cities.rome,Countries.italy)
        dragDrop(Cities.madrid,Countries.spain)
        dragDrop(Cities.seoul,Countries.southKorea)
        dragDrop(Cities.washington,Countries.USA)
        dragDrop(Cities.stockholm,Countries.sweden)
        wait(CitiesInCountries.romeItaly)
        wait(CitiesInCountries.madridSpain)
        wait(CitiesInCountries.stockholmSweden)
        wait(CitiesInCountries.osloNorway)
        wait(CitiesInCountries.washingtonUsa)
        wait(CitiesInCountries.seoulKorea)
        wait(CitiesInCountries.coppenhagenDenmark)  

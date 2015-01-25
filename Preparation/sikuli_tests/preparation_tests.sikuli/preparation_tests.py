import unittest
bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *

    
class SmokeTests(unittest.TestCase):
    #def test_001_Google(self):
    #    RunBrowserToUrl("chrome","http://google.bg")
    #    type(Google.search_Input,"Telerik Academy")
    #    type(Key.ENTER)
    #    click(Google.images_Tab)
    #    rightClick(Google.selected_Image)
    #    click(Google.contextMenu_Option)
    #    click(Google.address_Bar)
    #    link=Env.getClipboard()
    #    paste(link)
    #    type(Key.ENTER)
    #
    def test_002_FindTheDifferences(self):
        RunBrowserToUrl("chrome","http://content.screencast.com/users/AsyaGeorgieva/folders/Jing/media/f9c85f8b-3b5a-4c33-b2bf-34d09b0c691b/2013-07-14_1547.png")
        #wait(Google.pictures,3)
        #click(Google.pictures)
        sleep(5)
        HighlightRegion(135,80,25,25)
        HighlightRegion(145,120,25,25)
        HighlightRegion(355,475,25,25)
        HighlightRegion(350,503,25,25)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)    


    outfile = open("report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report' )
    runner.run(suite)
    outfile.close()


import unittest
bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *
from _uimap import*

    
class SmokeTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass    

        
    def tests_003_CalculatorOperations(selfself):
        RunBrowserToUrl('chrome','http://google.bg') 
        type(Google.searchBar,'Telerik academy')
        type(Key.ENTER)
        click(Google.imagesTab)
        rightClick(Google.telerikImage)
        click(Google.copy)
        rightClick(Google.adrressBar)
        click(Google.spaste)
        type(Key.ENTER)
           

             
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
    
    
    outfile = open("report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report' )
    runner.run(suite)
    outfile.close()


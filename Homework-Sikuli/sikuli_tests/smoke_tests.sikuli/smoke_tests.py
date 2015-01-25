import unittest
bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *

    
class SmokeTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass    
    
    def test_001_NavigateToTap(self):
        RunBrowserToUrl("chrome","http://platform.telerik.com")
        wait(BS.button_CreateWorkspace,30)
    
    def test_002_CreateWorkspace(self):
        click(BS.button_CreateWorkspace)
        wait(BS.button_DoCreateWorkspace,10)
        type(BS.label_WorkspaceName,"TestProject")
        click(BS.button_DoCreateWorkspace)
        wait(BS.button_CreateABProject,10)
        click(BS.button_CreateABProject)
             
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
    
    
    outfile = open("report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report' )
    runner.run(suite)
    outfile.close()


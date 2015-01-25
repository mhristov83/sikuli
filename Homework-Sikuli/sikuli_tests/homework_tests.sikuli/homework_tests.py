import unittest
bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *

    
class SmokeTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass    
    def test_001_Google(self):
        RunBrowserToUrl("chrome","http://google.com")
        type(Google.search_Input, "Telerik Academy")
        type(Key.ENTER)
        wait(Google.telerik_Result_Div)

    def test_002_DragAndDrop(self):
        RunBrowserToUrl("chrome","http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
        dragDrop(DragAndDrop.oslo,DragAndDrop.norway)
        dragDrop(DragAndDrop.copenhagen,DragAndDrop.denmark)
        dragDrop(DragAndDrop.madrid,DragAndDrop.spain)
        dragDrop(DragAndDrop.stockholm,DragAndDrop.sweden)
        dragDrop(DragAndDrop.washington, DragAndDrop.usa)
        dragDrop(DragAndDrop.seoul,DragAndDrop.southKorea)
        dragDrop(DragAndDrop.rome, DragAndDrop.italy)
        wait(DragAndDrop.norwayOslo)
        wait(DragAndDrop.italyRome)
        wait(DragAndDrop.spainMadrid)
        wait(DragAndDrop.swedenStockholm)
        wait(DragAndDrop.usaWashington)
        wait(DragAndDrop.southKoreaSeoul)
        wait(DragAndDrop.denmarkCopenhagen)

    def test_003_MinimizeAll(self):
        while (exists(Google.minimize_Button)):
            click(Google.minimize_Button)

    def test_004_SkypeMessage(self):
        if exists(Skype.skype_OnScreen) is None:
            click(Skype.skype_Icon)
        click(Skype.friend_Name)
        wait(5)
        for i in range(1):
            type(Skype.message_Input,"taka got li ti e, a?!")
            type(Key.ENTER)

    def test_004_FacebookMessages(self):
        RunBrowserToUrl("chrome","https://facebook.com")
        click(Facebook.messages_Button)
        wait(Facebook.newMessage_Button,3)
        click(Facebook.newMessage_Button)
        type(Facebook.search_Input,"Asya Georgieva")
        type(Key.ENTER)
        wait(Facebook.assertRightPerson_Field)
        type(Facebook.message_Input,"I tuka tormoz za teb")
        type(Key.ENTER)
        type(Facebook.message_Input,"She spra na vreme shot si levskar!")
        type(Key.ENTER)

    def test_005_Calculator(self):
        StartCalculator()
        CalculateAndVerify(Calculator.button_7,Calculator.button_8,Calculator.button_plus,Calculator.result_field_sum)
        CalculateAndVerify(Calculator.button_7,Calculator.button_8,Calculator.button_minus,Calculator.result_field_subtract)
        CalculateAndVerify(Calculator.button_7,Calculator.button_8,Calculator.button_multiply,Calculator.result_field_multiply)
        CalculateAndVerify(Calculator.button_7,Calculator.button_8,Calculator.button_divide,Calculator.result_field_divide)
        CalculateAndVerify(Calculator.button_0,Calculator.button_0,Calculator.button_divide,Calculator.result_field_divideByZero)
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)    


    outfile = open("report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report' )
    runner.run(suite)
    outfile.close()


########################################################
# UI map for XYZ
########################################################
from sikuli import *
########################################################

class BS:
    button_CreateWorkspace="button_CreateWorkspace.png"
    button_DoCreateWorkspace="button_DoCreateWorkspace.png"
    label_WorkspaceName=Pattern("label_WorkspaceName.png").targetOffset(0,28)
    button_CreateABProject="button_CreateABProject.png"

class Google:
    search_Input = "1414754015818.png"
    telerik_Result_Div = "1414754137073.png"
    minimize_Button = Pattern("1414758934864.png").similar(0.78).targetOffset(-36,3)

class DragAndDrop:
    oslo = "1414756509844.png"
    madrid = "1414756525597.png"
    stockholm = "1414756532180.png"
    washington = "1414756537956.png"
    seoul ="1414756547717.png"
    rome ="1414756553253.png"
    copenhagen ="1414756559302.png"
    norway ="1414756707006.png"
    sweden ="1414756716043.png"
    usa="1414756721932.png"
    spain="1414756729123.png"
    southKorea="1414756734669.png"
    denmark="1414756741860.png"
    italy="1414756746957.png"
    italyRome="1414756774572.png"
    denmarkCopenhagen="1414756781396.png"
    swedenStockholm="1414756789667.png"
    norwayOslo="1414756795470.png"
    usaWashington="1414756800818.png"
    southKoreaSeoul="1414756805827.png"
    spainMadrid = "1414756811357.png"

class Skype:
    skype_Icon = "1414763592916.png"
    skype_OnScreen = "1414763644096.png"
    friend_Name = "1414765560202.png"
    message_Input = "1414763925862.png"

class Facebook:
    messages_Button = "1414765050739.png"
    newMessage_Button = "1414767979760.png"
    search_Input = "1414765114507.png"
    message_Input = "1414765699448.png"
    assertRightPerson_Field = "1414940479908.png"

class Calculator:
    button_ce ="1414769953384.png"
    button_0="1414769838457.png"
    button_7 = "1414769850633.png"
    button_8 = "1414770145586.png"
    button_plus="1414769868017.png"
    button_minus="1414769875985.png"
    button_multiply="1414769887120.png"
    button_divide="1414769894688.png"
    button_equals="1414769899201.png"
    result_field_sum="1414769926999.png"
    result_field_subtract="1414769975056.png"
    result_field_multiply="1414769999409.png"
    result_field_divide="1414770111920.png"
    result_field_divideByZero="1414770132521.png"

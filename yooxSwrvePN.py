import csv
import datetime
Settings.AutoDetectKeyboardLayout = False
popup("Make sure the content is saved as \\Downloads\\pn.csv before proceeding!")
templateName = input("Please enter the Yoox Template Name to Copy:")
templateName = "".join(templateName.split())
campaignName = input("Please enter the Campaign Name:")
campaignName = "".join(campaignName.split())
campaignPhase = select("Please select the Campaign Phase:", options = ("Exploration", "Broadcast"))
linkURL = input("Please enter the Deeplink URL:")
linkURL = "".join(linkURL.split()).replace("\"", "").replace("COUNTRY", "${user.country_shop|fallback=\"us\"}").replace("GENDERLETTER", "${user.gender_short|fallback=\"w\"}").replace("GENDERFULL", "${user.gender_full|fallback=\"women\"}")
tp = linkURL[linkURL.index("tp=") + len("tp="):].split("&")[0]
iosSpecific = input("Please enter the iOS specific media (leave blank for \"NO\"):")
audienceCountry = input("Please enter the Audience (country_shop is):")
#audienceFraudster = input("Please enter the Audience (FRAUDSTER does not contain):")
#audienceFraudster = audienceFraudster.replace(" or ", ", ")
scheduleDate = input("Please enter the Schedule Date:")
scheduleDate = "".join(scheduleDate.split())
scheduleDate = datetime.datetime.strptime(scheduleDate, '%d/%m/%Y').strftime("%b %d,%Y")
scheduleTime = input("Please enter the Schedule Time:").lower()
hour = scheduleTime.split(':')[0]
min = scheduleTime.split(':')[1].split(" ")[0]
if min == "00":
    min = "0"
ampm = scheduleTime.split(' ')[1]

variantList = []

with open("C:\\Users\\gantoniou\\Downloads\\pn.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None)  
    for row in reader:
        if not "".join(row[1]).strip():
            continue
        else:
            variantList.append(row[1].decode("utf-8"))

variantNum = len(variantList)

if campaignPhase == "Broadcast":
    if variantNum == 3:
        pFactor = 4
    if variantNum == 4:
        pFactor = 3
    if variantNum == 5:
        pFactor = 2
    variantContent = variantList[:-1]
    variantContent = [variant for variant in variantContent for i in range(pFactor)]
    variantContent.append(variantList[-1])
    variantNum = len(variantContent)
else: 
    variantContent = variantList

click("1631691197455.png")
sleep(0.2)
click(Pattern("1631691235418.png").targetOffset(16,0))
type("a", KeyModifier.CTRL)
type(Key.BACKSPACE)
paste(templateName)
sleep(1)
wait("1631691587025.png")
click(Pattern("1631699439910.png").similar(0.90).targetOffset(0,33))
sleep(0.2)
click("1631699482999.png")
wait(Pattern("1631699581633.png").similar(0.60),60)
sleep(0.2)
click("1634800915307.png")
wait(Pattern("1634127149521.png").exact(),10)
click(Pattern("1634127149521.png").exact())
wait("1634212518149.png",10)
type("a", KeyModifier.CTRL)
type(Key.BACKSPACE)
paste(campaignName)
click("1634801053079.png")
type("a", KeyModifier.CTRL)
type(Key.BACKSPACE)
paste("tp_" + tp)
click(Pattern("1637075248357.png").similar(0.80))
sleep(0.2)
click("1631692530961.png")
#wait(Pattern("1634127179427.png").exact(),10)
#click(Pattern("1634127179427.png").exact())
#wait("1634212696357.png",10)
#if not exists("1634213042223.png",0.2):
#    sleep(0.2)
#    click(Pattern("1634212871052.png").exact().targetOffset(125,-25))
#    sleep(0.2)
#    click(Pattern("1634212871052.png").exact().targetOffset(-125,25))
#    sleep(0.2)
#click("1631692530961.png")
#wait(Pattern("1634127470603.png").exact(),10)
#click(Pattern("1634127470603.png").exact())
#wait("1634213161537.png",10)
#if not exists(Pattern("1634213232091.png").exact(),0.2):
#    click("1631698341731.png")
#    sleep(0.2)
#    click(Pattern("1631698387855.png").similar(0.90))
#    sleep(0.2)
#if not exists("1634801345410.png",0.2):
#    click("1634801262107.png")
#    type("a", KeyModifier.CTRL)
#    type(Key.BACKSPACE)
#    type("2")
#    click(Pattern("1634213392939.png").exact())
#    sleep(0.1)
#    click("1631698517389.png")
#    sleep(0.1)
#click("1631692530961.png")
wait("1634127673527.png",10)
click("1634127673527.png")
# create 1st variant
wait(Pattern("1634213541596.png").exact(),10)
click(Pattern("1638364225273.png").targetOffset(-47,30))
type("a", KeyModifier.CTRL)
type(Key.BACKSPACE)
paste(variantContent[0])
sleep(0.2)
if iosSpecific:
    click(Pattern("1637148316686.png").targetOffset(-25,0))
    sleep(0.2)
    click(Pattern("1637148372581.png").targetOffset(-75,0))
    type("a", KeyModifier.CTRL)
    type(Key.BACKSPACE)
    paste(iosSpecific)
    click("1637148579278.png")
    tab = 4
else:
    click(Pattern("1637148316686.png").targetOffset(5,0))
    tab = 3
sleep(0.2)
if not exists(Pattern("1634213779049.png").exact(),0.2):
    click(Pattern("1634213834859.png").exact().targetOffset(0,15))
    sleep(0.2)
    click(Pattern("1634127903571.png").exact())
    sleep(0.2)
#if not exists("1634801608746.png",0.2):
#    click(Pattern("1634214491245.png").exact())
#    type(Key.PAGE_DOWN)
#sleep(0.2)
#click(Pattern("1634801608746.png").targetOffset(-35,-70))
#sleep(0.2)
#click(Pattern("1637223114088.png").exact().targetOffset(-24,16))
for i in range(tab):
    type(Key.TAB)
type("a", KeyModifier.CTRL)
type(Key.BACKSPACE)
paste(linkURL)
type(Key.TAB)
type("a", KeyModifier.CTRL)
type(Key.BACKSPACE)
paste(linkURL)
sleep(0.2)
#click(Pattern("1634214491245.png").exact())
type(Key.TAB)
type(Key.PAGE_UP)
# create the rest of the variants
click("1634806625327.png")
wait("1634806963650.png",10)
for i in range(1,variantNum):
    wait(Pattern("1634806671106.png").similar(0.64),5)
    click(Pattern("1638364225273.png").targetOffset(-47,30))
    type("a", KeyModifier.CTRL)
    type(Key.BACKSPACE)
    paste(variantContent[i])
    if i < variantNum - 1:
        click(Pattern("1634807183865.png").targetOffset(-2,5))
click("1631692530961.png")
# audience setup
wait("1634811940398.png",10)
click("1634811956942.png")
wait("1634811998346.png",5)
# delete unused filters
click(Pattern("1634813772764.png").targetOffset(594,-2))
wait("1634813864538.png",5)
click(Pattern("1634813864538.png").targetOffset(0,45))
click(Pattern("1634813958642.png").targetOffset(592,0))
wait("1634813864538.png",5)
click(Pattern("1634813864538.png").targetOffset(0,45))
click(Pattern("1634814118903.png").targetOffset(593,0))
wait("1634813864538.png",5)
click(Pattern("1634813864538.png").targetOffset(0,45))
click(Pattern("1634814938079.png").targetOffset(593,0))
wait("1634813864538.png",5)
click(Pattern("1634813864538.png").targetOffset(0,45))
click(Pattern("1634815072964.png").targetOffset(593,0))
wait("1634813864538.png",5)
click(Pattern("1634813864538.png").targetOffset(0,45))
sleep(0.2)
click(Pattern("1634812166475.png").targetOffset(560,0))
wait("1634812262699.png",5)
click("1634812262699.png")
while not exists("1637079484347.png",0.2):
    type(Key.BACKSPACE)
paste(audienceCountry)
sleep(0.2)
click("1634812657859.png")
sleep(0.2)
#click(Pattern("1634812777240.png").targetOffset(560,-2))
#wait("1634812885113.png",5)
#click(Pattern("1634812885113.png").targetOffset(280,0))
#sleep(0.1)
#while not exists("1637079586584.png",0.2):
#    type(Key.BACKSPACE)
#paste(audienceFraudster)
#sleep(0.2)
#click("1634813689378.png")
click("1634815517509.png")
# set up schedule
wait(Pattern("1637079926458.png").exact(),10)
click(Pattern("1637079926458.png").exact())
wait("1637081189220.png",10)
click(Pattern("1637082450821.png").exact().targetOffset(-65,4))
type(hour)
click(Pattern("1637082580217.png").exact().targetOffset(3,1))
type(min)
click(Pattern("1637082612798.png").exact().targetOffset(59,0))
type(ampm)
sleep(0.2)
click(Pattern("1637081189220.png").targetOffset(-161,0))
type("a", KeyModifier.CTRL)
paste(scheduleDate)
click("1634815517509.png")
popup("Configuration READY!")

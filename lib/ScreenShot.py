import datetime,threading,pyautogui



def takeScreenShot(intervel):
    threading.Timer(intervel,takeScreenShot,args=[intervel]).start()
    current = datetime.datetime.now()
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'{current.date()}_{str(current.time()).replace(":","-")}.png')

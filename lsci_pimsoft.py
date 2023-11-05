import pyautogui, os, time

def kill_process(process_name):
    os.system("taskkill /f /im " + process_name)

def to_desktop():
    pyautogui.hotkey('win', 'd')

def is_running(process_name):
    import psutil
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            return True
    return False

def open_program(iconpath):
    if is_running("PIMSoft.exe"):
        kill_process("PIMSoft.exe")
    elif pyautogui.locateCenterOnScreen(iconpath) == None:
        to_desktop()
    pyautogui.click(pyautogui.locateCenterOnScreen(iconpath),
                    button='left', clicks=2, interval=0.25)

def handle_client(client, servermsg):
    if servermsg == "marker":
        client.send('marker'.encode("utf-8"))
    elif servermsg == "accepted":
        pass
    else:
        print(f"Received:{servermsg}")
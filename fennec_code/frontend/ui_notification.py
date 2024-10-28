#temp notification boxes, need to be re-designed
import ctypes
import logging

log_file = 'Fennec_Logs.log'

logging.basicConfig(
filename=log_file,
level=logging.DEBUG,
format='%(asctime)s %(levelname)s: %(message)s'
)

def conn_alert():
    try:
        logging.info("conn_alert function called successfully")
        WIN_TOPMOST = 0x40000
        windowTitle = "Connection Alert"
        message = "A remote connection program has been detected and stopped. You're safe, but you may be a victim of a scam."

        # display a message box; execution will stop here until user acknowledges
        ctypes.windll.user32.MessageBoxExW(None, message, windowTitle, WIN_TOPMOST)
    except Exception as e:
        logging.error("something went wrong! Here's the error: {e}")

def paused_alert():
    WIN_TOPMOST = 0x40000
    windowTitle = "Monitoring Paused Alert"
    message = "RCA monitoring has been paused! We highly recommend unpausing."

    # display a message box; execution will stop here until user acknowledges
    ctypes.windll.user32.MessageBoxExW(None, message, windowTitle, WIN_TOPMOST)

def unpaused_alert():

    WIN_TOPMOST = 0x40000
    windowTitle = "Monitoring Unpaused"
    message = "Monitoring has resumed! You are now safe from remote connection attempts :)"

    # display a message box; execution will stop here until user acknowledges
    ctypes.windll.user32.MessageBoxExW(None, message, windowTitle, WIN_TOPMOST)

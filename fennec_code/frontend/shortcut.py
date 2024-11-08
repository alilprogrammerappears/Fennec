import os
import winshell
from win32com.client import Dispatch
import logging
import pythoncom
import sys

# Set up log file
log_file = 'Fennec_Logs.log'

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def check_and_create_shortcut():

    #initialize COM library
    pythoncom.CoInitialize()

    # Define the shortcut name and target file
    shortcut_name = "Fennec"
    script_file = "ui_home.py"

    # Path to icon file
    icon_file = "shortcut_icon.ico"
    
    # Get the absolute path of the script file
    current_directory = os.path.abspath(os.path.dirname(__file__))
    script_path = os.path.join(current_directory, script_file)
    icon_path = os.path.join(current_directory, icon_file)

    # Get python executable and use pythonw so it doesn't open a terminal
    python_executable = sys.executable
    pythonw_executable = python_executable.replace('python.exe', 'pythonw.exe')
    
    if not os.path.isfile(pythonw_executable):
        # Fallback if pythonw.exe is not in the same directory
        pythonw_executable = 'pythonw'
    
    # Define the path to the Start Menu
    startmenu_path = winshell.start_menu()
    shortcut_path = os.path.join(startmenu_path, f"{shortcut_name}.lnk")
    
    # Check if the shortcut already exists otherwise create it
    try:
        if os.path.exists(shortcut_path):
            logging.info(f"Shortcut '{shortcut_name}' already exists.")
        else:
            logging.info(f"Creating shortcut '{shortcut_name}'...")
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.Targetpath = pythonw_executable
            shortcut.Arguments = script_path
            shortcut.WorkingDirectory = current_directory
            shortcut.IconLocation = icon_path
            shortcut.save()
            logging.info(f"Shortcut '{shortcut_name}' created successfully.")
    except Exception as e:
        logging.error(f"Something went wrong! Here's the error info: {e}")
    finally:
        pythoncom.CoUninitialize()
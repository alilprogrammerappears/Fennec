# Some processes require elevated privileges to be terminated.
# This file checks if it is running with admin privileges and if not,
# tries to restart itself with privileges.

import ctypes
import sys
import os
import logging

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if is_admin():
        return True

    try:
        # Relaunch the program with admin rights and add a flag
        params = ' '.join([os.path.abspath(sys.argv[0])] + sys.argv[1:] + ["--elevated"])
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1)
        logging.info("re-launching Fennec with admin privileges")
        return True
    except Exception as e:
        logging.error("Failed to elevate process: {e}")
        return False

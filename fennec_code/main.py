import logging
import sys
import threading
from elevate import is_admin, run_as_admin
from port_blocking import block_all_ports, block_single_port
from process_blocking import monitor_process




def start_up():

    # Set up logging
    log_file = 'Fennec_Logs.log'

    logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s'
    
    )
    # Check if in admin mode. If not, restart as admin
    if not is_admin() and "--elevated" not in sys.argv:
        logging.info(f"Attempting to restart with administrative privileges...")
        if run_as_admin():
            logging.info(f"Restarted with administrative privileges.")
            logging.info("Hello World :)")
            sys.exit(0)  # Terminate the current process to restart as admin
        else:
            logging.error(f"Failed to restart with administrative privileges.")
            sys.exit(1)


def run_bkg_script():
    # change script_running flag (state_manager) somehow
    # new thread: shortcut
    port_thread = threading.Thread(target=block_all_ports)
    process_thread = threading.Thread(target=monitor_process)

    port_thread.start()
    logging.info("port thread started")
    process_thread.start()
    logging.info("process thread started")

    port_thread.join()
    logging.info("port thread stopped")
    process_thread.join()
    logging.info("process thread stopped")


    # To quickly unblock all ports, uncomment the following:
    """ logging.info(f"Unblocking all ports")
    unblock_ports_thread = threading.Thread(target=unblock_all_ports)
    unblock_ports_thread.start()
    unblock_ports_thread.join() """


if __name__ == '__main__':

    start_up()
    run_bkg_script()



""" 
    - multiprocessing option (use queue for communication). Maybe
    - start up flag option - put shortcut code into a wrapper script, use a flag property to specify
        whether main.py has been executed via the shortcut or via start up. Then just put it in
        a big ol if/elif statement.
    - if monitoring isn't running and the shortcut is executed, have one process call the monitoring function
        and one handle the UI and share the stateManager instance between the two.

    - two boolean flags: running = whether or not the process_script is running
                         is_shortcut = whether or not the script was executed via the shortcut

    def start_up:
        initialize logging
        check privileges

    def run_bkg_script():
        
        change running_flag (state_manager) = 1
        start shortcut thread
        start port_blocking thread
        start process_blocking thread
    
    def run_ui_script():
        
        if bkg_script is !running (running_flag)
            call run_bkg_script:
        else

        


    

    if __name__ == '__main__':
    
        create instance of state_manager
        if (running as script):
            call def start_up
            call def run_bkg_script
        elif (running shortcut):
            call def start_up
            call def run_ui_script


 """
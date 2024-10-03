import time
import logs
import random
import sys
import formatter
import difflib
import textwrap

def password_protected():
    password = 342588
    while True:
        time.sleep(2)
        user_input = input("Please input password to access additional files: \n")
        try:
            user_input = int(user_input)
            if user_input != password:
                print("INCORRECT PASSWORD\n")
            else:
                print("Password accepted.\n")
                return True
        except ValueError:
            print("ERROR: Input not recognized.\n")
            
def restore_files():
    print("\nAttempting to restore files...\n")
    time.sleep(4)
    print("Files restored:")
    time.sleep(1)
    print("Captain Log1")
    time.sleep(1)
    print("Captain Log2")
    time.sleep(1)
    print("Captain Log3")
    time.sleep(1)
    print("Captain Log4")
    time.sleep(1)
    print("Defrost Log\n")
    time.sleep(2)

def fuzzy_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        closest_match = difflib.get_close_matches(user_input, valid_options, n=1, cutoff=0.6)
        if closest_match:
            return closest_match[0]
        else:
            print(f"ERROR: Input '{user_input}' not recognized. Please try again.")

def restoring_additional_files():
    random.seed(time.time())
    
    progress = 0
    bar_width = 50 
    
    while progress < 100:
        increment = random.randint(1, 15)
        
        # Ensure we don't exceed 100% progress
        if progress + increment > 100:
            increment = 100 - progress  # Adjust increment to exactly reach 100
        
        progress += increment
        
        # Calculate the position of the progress bar based on the current percentage
        pos = bar_width * progress // 100 
        
        # Print the progress bar at the exact percentage
        sys.stdout.write("\rRestoring... [")
        for i in range(bar_width):
            if i < pos:
                sys.stdout.write("=") 
            elif i == pos:
                sys.stdout.write(">") 
            else:
                sys.stdout.write(" ")
        sys.stdout.write(f"] {progress}%")
        sys.stdout.flush()
        
        time.sleep(0.3)
    
    print("\nPreparing restored file...")
    

def scrape_data():
    random.seed(time.time())
    
    progress = 0
    bar_width = 50
    
    while progress < 100:
        increment = random.randint(1, 15)
        
        if progress + increment > 100:
            increment = 100 - progress
            
        progress += increment
        pos = bar_width * progress // 100
        
        sys.stdout.write("\rScraping data... [")
        for i in range(bar_width):
            if i < pos:
                sys.stdout.write("=")
            elif i == pos:
                sys.stdout.write(">")
            else:
                sys.stdout.write(" ")
        sys.stdout.write(f"] {progress}%")
        sys.stdout.flush()
        
        time.sleep(0.25)
    print()

# Function to access Captain Logs functions
def accessLogs():
    captain_logs = logs.CaptainLogs()
    valid_commands = [
        "access captain log1",
        "access captain log2",
        "access captain log3",
        "access captain log4",
        "access defrost log",
        "back"
    ]
    accessed_logs = set()
    
    input_lower = ""
    while (input_lower != "back"):
        time.sleep(2)
        user_input = input("Which file would you like to access? [Type 'access captain log1', 'access captain log2', etc.]\n").strip().lower()
        
        #fuzzy matching
        closest_matches = difflib.get_close_matches(user_input, valid_commands, n=1, cutoff=0.6)
        
        if closest_matches:
            input_lower = closest_matches[0]
        
        if input_lower == "access captain log1":
            captain_logs.captainLog1()
            accessed_logs.add("captain log1")
        elif input_lower == "access captain log2":
            captain_logs.captainLog2()
            accessed_logs.add("captain log2")
        elif input_lower == "access captain log3":
            captain_logs.captainLog3()
            accessed_logs.add("access captain log3")
        elif input_lower == "access captain log4":
            captain_logs.captainLog4()
            accessed_logs.add("access captain log4")
        elif input_lower == "access defrost log":
            captain_logs.defrostLog()
            accessed_logs.add("access defrost log")
        elif input_lower == "back":
            print("Returning to the previous menu...")
            return
        else:
            print(f"ERROR: Input {user_input} not recognized.\n")
            print("Please input 'access and the log you would like to access.\n")
        if accessed_logs == {"captain log1", "captain log2", "captain log3", "captain log4", "crew log"}:
            print("\nYou have accessed all captain's logs. Type 'back' to exit.")

# Accesses Mattis Logs functions in logs.py        
def restoreCassieLogs():
    mattis_logs = logs.MattisLogs()
    print("Attempting to restore files...\n")
    time.sleep(2)

    # Loop for Mattis Log98 (No password required)
    while True:
        user_input = input("Mattis Log98 ready for access. Type 'Access Mattis Log98' to open the file.\n").strip().lower()
        
        if user_input == "access mattis log98":
            mattis_logs.mattisLog98()  # Call the correct function to display Mattis Log98
            time.sleep(3)
            print("Additional files intact. These files are password protected.\n")
            
            # Mark Log98 as accessed
            accessed_logs = {"access mattis log98"}  # Initialize accessed logs tracking
            break  # Break out of the loop after accessing Mattis Log98
        else:
            print(f"ERROR: Input '{user_input}' not recognized. Please type 'Access Mattis Log98'.") 

    # Once Mattis Log98 is accessed, ask for password to unlock remaining logs
    password_granted = password_protected()

    if password_granted:
        # Print "RESTORED FILES:" and list all Mattis logs
        restored_files_list = textwrap.dedent("""
        Mattis Log00
        Mattis Log03
        Mattis Log07
        Mattis Log09
        Mattis Log20
        Mattis Log24
        Mattis Log37
        Mattis Log44
        Mattis Log49
        Mattis Log70
        """)

        # Format and print the restored files using `type_text_blank_format`
        formatter.type_text_blank_format("RESTORED FILES:", delay=30)
        formatter.type_text_blank_format(restored_files_list, delay=30)
    
    # Define the list of logs that need to be accessed before unlocking Mattis Log99 and Mattis Log100
    prerequisite_logs = {
        "access mattis log00",
        "access mattis log03",
        "access mattis log07",
        "access mattis log09",
        "access mattis log20",
        "access mattis log24",
        "access mattis log37",
        "access mattis log44",
        "access mattis log49",
        "access mattis log70"
    }

    valid_commands = list(prerequisite_logs)
    
    restored_files = False

    while True:
        if not prerequisite_logs:
            handle_mattis_log99(mattis_logs, accessed_logs)
            handle_mattis_log100(mattis_logs, accessed_logs)
            break  # Exit the loop and the function when all logs are accessed

        user_input = input("Type the log name to open the file. [EX: Type 'Access Mattis Log00' to open Mattis Log00]: \n").strip().lower()
        closest_matches = difflib.get_close_matches(user_input, valid_commands, n=1, cutoff=0.6)

        if closest_matches:
            matched_command = closest_matches[0]

            if password_granted:
                if not restored_files:
                    time.sleep(2)
                    restoring_additional_files()  # Restore additional files
                    restored_files = True
                
                time.sleep(2)
                if matched_command not in accessed_logs:  # Only access the log if not already accessed
                    logs_access(matched_command, accessed_logs)  # Access the log
                    
                    # Remove the log from prerequisite logs once accessed
                    prerequisite_logs.discard(matched_command)
                    
                    # Remove accessed log from the displayed list
                    log_name = matched_command.replace("access", "").title().strip()
                    log_name = log_name.replace("Mattislog", "Mattis Log")
                    restored_files_list = restored_files_list.replace(log_name, "")
                    restored_files_list = '\n'.join([line for line in restored_files_list.splitlines() if line.strip()])  # Clean up empty lines
                    
                    # Display remaining unaccessed logs using `type_text_blank_format`
                    if restored_files_list:
                        formatter.type_text_blank_format("FILES NOT YET ACCESSED:", delay=30)
                        formatter.type_text_blank_format(restored_files_list, delay=30)
                    else:
                        formatter.type_text_blank_format("", delay=30)
                else:
                    print(f"Log '{matched_command}' has already been accessed.\n")
        else:
            print(f"ERROR: Input '{user_input}' not recognized. Please try again.\n")

def logs_access(command, accessed_logs):
    """Function to access specific Mattis logs"""
    mattis_logs = logs.MattisLogs()

    if command == "access mattis log00":
        mattis_logs.mattisLog00()
        accessed_logs.add("access mattis log00")
    elif command == "access mattis log03":
        restoring_additional_files()
        mattis_logs.mattisLog03()
        accessed_logs.add("access mattis log03")
    elif command == "access mattis log07":
        restoring_additional_files()
        mattis_logs.mattisLog07()
        accessed_logs.add("access mattis log07")
    elif command == "access mattis log09":
        restoring_additional_files()
        mattis_logs.mattisLog09()
        accessed_logs.add("access mattis log09")
    elif command == "access mattis log20":
        restoring_additional_files()
        mattis_logs.mattisLog20()
        accessed_logs.add("access mattis log20")
    elif command == "access mattis log24":
        restoring_additional_files()
        mattis_logs.mattisLog24()
        accessed_logs.add("access mattis log24")
    elif command == "access mattis log37":
        restoring_additional_files()
        mattis_logs.mattisLog37()
        accessed_logs.add("access mattis log37")
    elif command == "access mattis log44":
        restoring_additional_files()
        mattis_logs.mattisLog44()
        accessed_logs.add("access mattis log44")
    elif command == "access mattis log49":
        restoring_additional_files()
        mattis_logs.mattisLog49()
        accessed_logs.add("access mattis log49")
    elif command == "access mattis log70":
        restoring_additional_files()
        mattis_logs.mattisLog70()
        accessed_logs.add("access mattis log70")


def handle_mattis_log99(mattis_logs, accessed_logs):
    time.sleep(1.5)
    restoring_additional_files()
    time.sleep(2)
    print("Error preparing restored file...")
    time.sleep(2)
    print("Analyzing...")
    time.sleep(3)
    print("Large amounts of corrupted data.")
    time.sleep(2)
    print("**WARNING: POSSIBLE MALTECH DETECTED**")
    user_input = input("Proceed? [Yes/No]: ").lower()
    if user_input in ['yes', 'y', 'n', 'no']:
        time.sleep(2)
        mattis_logs.mattisLog99()
    accessed_logs.add("access mattis log99")


def handle_mattis_log100(mattis_logs, accessed_logs):
    time.sleep(1.5)
    mattis_logs.mattisLog100()
    time.sleep(5)
    restoring_additional_files()
    time.sleep(2)
    print("Error preparing restored file...")
    time.sleep(2)
    print("Analyzing...")
    time.sleep(3)
    print("Large amounts of corrupted data.")
    time.sleep(2)
    print("**WARNING: POSSIBLE MALTECH DETECTED**")
    user_input = input("Proceed? [Yes/No]: ").lower()
    if user_input in ['yes', 'y', 'n', 'no']:
        time.sleep(2)
        print("Accessing LogCASSIE")
        time.sleep(2)
        mattis_logs.logCassie()
    accessed_logs.add("access mattis log100")

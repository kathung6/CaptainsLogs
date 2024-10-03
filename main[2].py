import time
import functions
import sys

def main():
    time.sleep(1)
    print("Connecting to foreign system...")
    time.sleep(3)
    print("System not recognized. Attempting to decrypt...")
    time.sleep(3)
    print("System not encrypted.")
    time.sleep(2)
    print("Analysis: System is operating on an alien standardization that is not recognized.\n")
    time.sleep(1)
    print("Attempting to translate...")
    time.sleep(3)
    print("System Translated.")
    time.sleep(1)
    print("Connection established.\n")
    time.sleep(2)

    valid_commands = ["scrape data"]
    command = functions.fuzzy_input("Data found on local drive. Type 'scrape data' to continue: ", valid_commands)

    if command == "scrape data":
        time.sleep(2)
        functions.scrape_data()
        time.sleep(2)
        print("Data scraped.")
        time.sleep(2)
        print("Analysis: 100% of files are corrupted and/or inaccessable...")
        time.sleep(2)
        
        valid_responses = ["yes", "y"]
        restore_input = functions.fuzzy_input("Attempt to restore corrupted files? Type 'Yes' to continue: ", valid_responses)
    
        if restore_input in ["yes", "y"]:
            time.sleep(2)
            functions.restore_files()
            functions.accessLogs()
        else:
            print("Files restoration aborted. \nExiting terminal\n")
            sys.exit(0)
        
        # Further analysis after scraping
        time.sleep(1)
        print("Data analyzed for frequent keywords.\n")
        time.sleep(1.5)
        print("'Cassie' is mentioned in over a dozen personal logs.\n")
        time.sleep(1.5)

        # Ask if they want to restore Cassie logs
        cassie_input = functions.fuzzy_input("Attempt to restore this file? Type 'Yes' to continue: ", valid_responses)
    
        if cassie_input in ["yes", "y"]:
            functions.restoreCassieLogs()
            time.sleep(3)
            #functions.handle_mattis_log99()
            #time.sleep(5)
            #functions.handle_mattis_log100()
            #time.sleep(2)
        else:
            print("File recovery attempt terminated.\nExiting terminal.\n")
            sys.exit(0)
        time.sleep(10)
        print("No more recoverable files. Initiating self-destruct sequence.\n")

        # Self-destruct countdown
        for i in range(10, -1, -1):
            print(i)
            time.sleep(1)

        print("Goodbye")
        sys.exit(0)  # Exit the program with status code 0


if __name__ == "__main__":
    main()

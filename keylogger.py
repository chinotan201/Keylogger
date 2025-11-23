# keylogger_simulator.py
import time
from datetime import datetime
import sys
from termcolor import colored

log_file = "keystrokes.log"
max_log_size = 10000
is_logging = False

def log_key(key):
    """Log a simulated key press for educational purposes"""
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(log_file, "a+") as f:
            f.write(f"{key} [{timestamp}]\n")
    except Exception as e:
        print(f"Error logging key: {e}")

def simulate_typing():
    """Simulate typing for testing logging functionality"""
    print(colored("Simulating key presses for testing...", "blue"))
    sample_keys = ["a", "b", "Enter", "Space", "Backspace", "Shift"]
    for key in sample_keys:
        log_key(key)
        time.sleep(0.5)
    print(colored(f"Simulation complete. Data saved to {log_file}", "green"))

def main():
    print(colored("\n⚠️ WARNING ⚠️", "red"))
    print("This tool is for educational purposes only. Logs simulated input.")
    
    while True:
        print("\nOptions:")
        print("1. Simulate typing")
        print("2. View logs")
        print("3. Exit")
        choice = input("\nChoose option (1-3): ")
        
        if choice == "1":
            simulate_typing()
        elif choice == "2":
            try:
                with open(log_file, "r") as f:
                    print("\n" + "="*50)
                    print(colored("LOG CONTENTS", "yellow"))
                    print("="*50)
                    print(f.read())
                    print("="*50)
            except FileNotFoundError:
                print(colored("No logs found", "red"))
        elif choice == "3":
            print(colored("Exiting...", "magenta"))
            sys.exit()
        else:
            print(colored("Invalid choice", "red"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\nInterrupted", "red"))
    except Exception as e:
        print(colored(f"\nError: {e}", "red"))

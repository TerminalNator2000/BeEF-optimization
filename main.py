
# main.py
import payload_generator
import social_engineering
import session_hijacking
import keylogger
import database_logger
import threading

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

def display_menu():
    print("\nChoose an action:")
    print("1. Generate Payload")
    print("2. Launch Social Engineering Attack")
    print("3. Attempt Session Hijacking")
    print("4. Start Keylogging")
    print("5. Exit")

def main():
    database_logger.create_database()  # Ensure the database is set up
    
    while True:
        display_menu()
        choice = input("Enter choice (1-5): ")
        
        if choice == "1":
            generate_payload_module()
        elif choice == "2":
            social_engineering_module()
        elif choice == "3":
            session_hijacking_module()
        elif choice == "4":
            keylogging_module()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()


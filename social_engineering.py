# social_engineering.py
import random

def generate_phishing_link(site_name):
    fake_domain = f"{site_name}-{random.randint(1000, 9999)}.com"
    return f"http://{fake_domain}"

if __name__ == "__main__":
    # Sample usage
    site_name = "facebook"
    phishing_link = generate_phishing_link(site_name)
    print(f"Generated phishing link: {phishing_link}")

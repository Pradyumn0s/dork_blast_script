import webbrowser
import time
import random
from termcolor import colored
from cryptography.fernet import Fernet
import os

# Encryption key for security
key = b'YOUR_SECRET_KEY'  # Replace this with a generated key
cipher_suite = Fernet(key)

# Function to encrypt script code
def encrypt_script():
    with open(__file__, 'rb') as file:
        encrypted = cipher_suite.encrypt(file.read())
    with open('encrypted_script.py', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Domain input (with domain check)
valid_domains = ["luminpdf.com", "acceptmission.com", "graphenedb.com", "bugcrowd.com", "gofrugal.com"]
domain = input(colored("Enter the target domain (e.g. luminpdf.com): ", 'cyan')).strip()

if domain not in valid_domains:
    print(colored(f"Invalid domain entered: {domain}. Please choose from: {valid_domain}", 'red'))
    exit()

# Your personal information (Pradyumn and X.com link)
personal_info = f"Script created by Pradyumn. Follow me at: https://x.com/pradyumnTiwari0?t=q1SFPLeF_r0aon3OSd23IA&s=09"

# Core sensitive keywords
keywords = [
    "password", "username", "apikey", "api_key", "access_token", "private_key", "ssh_key",
    "db_password", "ftp_password", "email", "user_credentials", "auth_token", "secret_token",
    "jwt_token", "smtp_password", "PGPASSWORD", "client_secret", "token_secret", "vault_key"
]import webbrowser
import time
import random
from termcolor import colored
from cryptography.fernet import Fernet
import os

# Encryption key for security
key = b'YOUR_SECRET_KEY'  # Replace this with a generated key
cipher_suite = Fernet(key)

# Function to encrypt script code
def encrypt_script():
    with open(__file__, 'rb') as file:
        encrypted = cipher_suite.encrypt(file.read())
    with open('encrypted_script.py', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Domain input (with domain check)
valid_domains = ["luminpdf.com", "acceptmission.com", "graphenedb.com", "bugcrowd.com", "gofrugal.com"]
domain = input(colored("Enter the target domain (e.g. luminpdf.com): ", 'cyan')).strip()

if domain not in valid_domains:
    print(colored(f"Invalid domain entered: {domain}. Please choose from: {valid_domains}", 'red'))
    exit()

# Your personal information (Pradyumn and X.com link)
personal_info = f"Script created by Pradyumn. Follow me at: https://x.com/pradyumnTiwari0?t=q1SFPLeF_r0aon3OSd23IA&s=09"

# Core sensitive keywords
keywords = [
    "password", "username", "apikey", "api_key", "access_token", "private_key", "ssh_key",
    "db_password", "ftp_password", "email", "user_credentials", "auth_token", "secret_token",
    "jwt_token", "smtp_password", "PGPASSWORD", "client_secret", "token_secret", "vault_key"
]

# Google dork templates
google_templates = [
    f'site:{domain} intext:"{key}"',
    f'site:{domain} inurl:{key}',
    f'site:{domain} intitle:"index of" "{key}"',
    f'site:{domain} filetype:txt "{key}"',
    f'site:{domain} filetype:log "{key}"',
    f'site:{domain} filetype:env "{key}"',
    f'site:{domain} filetype:sql "{key}"',
    f'site:{domain} filetype:json "{key}"',
    f'site:{domain} filetype:conf "{key}"',
    f'site:{domain} filetype:ini "{key}"',
]

# GitHub dork templates
github_templates = [
    f'site:github.com "{domain}" "{key}"',
    f'site:github.com "{domain}" in:file "{key}"',
    f'site:github.com "{domain}" in:readme "{key}"',
    f'site:github.com "{domain}" in:path "{key}"',
    f'site:github.com "{domain}" filename:.env "{key}"',
]

# Combine dorks
def generate_dorks():
    dorks = []
    for key in keywords:
        for template in google_templates + github_templates:
            dorks.append(template.replace("{key}", key))
    random.shuffle(dorks)
    return dorks

# Open tabs in batches
def open_dorks(dorks, batch_size=25, delay=5):
    print(colored(f"\nStarting dorking for domain: {domain}...", 'yellow'))
    for i in range(0, len(dorks), batch_size):
        batch = dorks[i:i+batch_size]
        print(colored(f"\nOpening batch {i//batch_size + 1} ({len(batch)} dorks)...", 'green'))
        for dork in batch:
            url = "https://www.google.com/search?q=" + dork
            webbrowser.open(url)
        time.sleep(delay)

# Main execution
if __name__ == "__main__":
    print(colored(f"\n{personal_info}", 'magenta'))
    all_dorks = generate_dorks()
    open_dorks(all_dorks, batch_size=25, delay=10)
import webbrowser
import time
import random
from termcolor import colored
from cryptography.fernet import Fernet
import os

# Encryption key for security
key = b'YOUR_SECRET_KEY'  # Replace this with a generated key
cipher_suite = Fernet(key)

# Function to encrypt script code
def encrypt_script():
    with open(__file__, 'rb') as file:
        encrypted = cipher_suite.encrypt(file.read())
    with open('encrypted_script.py', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Domain input (with domain check)
valid_domains = ["luminpdf.com", "acceptmission.com", "graphenedb.com", "bugcrowd.com", "gofrugal.com"]
domain = input(colored("Enter the target domain (e.g. luminpdf.com): ", 'cyan')).strip()

if domain not in valid_domains:
    print(colored(f"Invalid domain entered: {domain}. Please choose from: {valid_domains}", 'red'))
    exit()

# Your personal information (Pradyumn and X.com link)
personal_info = f"Script created by Pradyumn. Follow me at: https://x.com/pradyumnTiwari0?t=q1SFPLeF_r0aon3OSd23IA&s=09"

# Core sensitive keywords
keywords = [
    "password", "username", "apikey", "api_key", "access_token", "private_key", "ssh_key",
    "db_password", "ftp_password", "email", "user_credentials", "auth_token", "secret_token",
    "jwt_token", "smtp_password", "PGPASSWORD", "client_secret", "token_secret", "vault_key"
]

# Google dork templates
google_templates = [
    f'site:{domain} intext:"{key}"',
    f'site:{domain} inurl:{key}',
    f'site:{domain} intitle:"index of" "{key}"',
    f'site:{domain} filetype:txt "{key}"',
    f'site:{domain} filetype:log "{key}"',
    f'site:{domain} filetype:env "{key}"',
    f'site:{domain} filetype:sql "{key}"',
    f'site:{domain} filetype:json "{key}"',
    f'site:{domain} filetype:conf "{key}"',
    f'site:{domain} filetype:ini "{key}"',
]

# GitHub dork templates
github_templates = [
    f'site:github.com "{domain}" "{key}"',
    f'site:github.com "{domain}" in:file "{key}"',
    f'site:github.com "{domain}" in:readme "{key}"',
    f'site:github.com "{domain}" in:path "{key}"',
    f'site:github.com "{domain}" filename:.env "{key}"',
]

# Combine dorks
def generate_dorks():
    dorks = []
    for key in keywords:
        for template in google_templates + github_templates:
            dorks.append(template.replace("{key}", key))
    random.shuffle(dorks)
    return dorks

# Open tabs in batches
def open_dorks(dorks, batch_size=25, delay=5):
    print(colored(f"\nStarting dorking for domain: {domain}...", 'yellow'))
    for i in range(0, len(dorks), batch_size):
        batch = dorks[i:i+batch_size]
        print(colored(f"\nOpening batch {i//batch_size + 1} ({len(batch)} dorks)...", 'green'))
        for dork in batch:
            url = "https://www.google.com/search?q=" + dork
            webbrowser.open(url)
        time.sleep(delay)

# Main execution
if __name__ == "__main__":
    print(colored(f"\n{personal_info}", 'magenta'))
    all_dorks = generate_dorks()
    open_dorks(all_dorks, batch_size=25, delay=10)


# Google dork templates
google_templates = [
    f'site:{domain} intext:"{key}"',
    f'site:{domain} inurl:{key}',
    f'site:{domain} intitle:"index of" "{key}"',
    f'site:{domain} filetype:txt "{key}"',
    f'site:{domain} filetype:log "{key}"',
    f'site:{domain} filetype:env "{key}"',
    f'site:{domain} filetype:sql "{key}"',
    f'site:{domain} filetype:json "{key}"',
    f'site:{domain} filetype:conf "{key}"',
    f'site:{domain} filetype:ini "{key}"',
]

# GitHub dork templates
github_templates = [
    f'site:github.com "{domain}" "{key}"',
    f'site:github.com "{domain}" in:file "{key}"',
    f'site:github.com "{domain}" in:readme "{key}"',
    f'site:github.com "{domain}" in:path "{key}"',
    f'site:github.com "{domain}" filename:.env "{key}"',
]

# Combine dorks
def generate_dorks():
    dorks = []
    for key in keywords:
        for template in google_templates + github_templates:
            dorks.append(template.replace("{key}", key))
    random.shuffle(dorks)
    return dorks

# Open tabs in batches
def open_dorks(dorks, batch_size=25, delay=5):
    print(colored(f"\nStarting dorking for domain: {domain}...", 'yellow'))
    for i in range(0, len(dorks), batch_size):
        batch = dorks[i:i+batch_size]
        print(colored(f"\nOpening batch {i//batch_size + 1} ({len(batch)} dorks)...", 'green'))
        for dork in batch:
            url = "https://www.google.com/search?q=" + dork
            webbrowser.open(url)
        time.sleep(delay)

# Main execution
if __name__ == "__main__":
    print(colored(f"\n{personal_info}", 'magenta'))
    all_dorks = generate_dorks()
    open_dorks(all_dorks, batch_size=25, delay=10)

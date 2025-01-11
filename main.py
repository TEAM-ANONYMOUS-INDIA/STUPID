import requests
import socket
import threading
import os
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Wordlist file paths
PORT_LIST = "ports_common.txt"
SQL_PAYLOADS = "sql_injection_payloads.txt"
PASSWORD_LIST = "passwords_common.txt"
XSS_PAYLOADS = "xss_payloads.txt"
DIRECTORY_LIST = "directories_common.txt"
SUBDOMAIN_LIST = "subdomains_common.txt"
USERNAMES_LIST = "usernames_common.txt"

# ================================ PORT SCANNER ================================ #
def load_ports():
    with open(PORT_LIST, "r") as file:
        ports = [line.strip() for line in file.readlines()]
    return ports

def port_scan(target_ip):
    open_ports = []
    ports = load_ports()
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, int(port)))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass
    print(Fore.GREEN + f"Open ports: {open_ports}")

# ================================ SQL INJECTION TESTER ================================ #
def sql_injection_test(url):
    with open(SQL_PAYLOADS, "r") as file:
        payloads = [line.strip() for line in file.readlines()]
    for payload in payloads:
        test_url = url + payload
        response = requests.get(test_url)
        if "error" in response.text:
            print(Fore.RED + f"Vulnerable to SQL Injection: {test_url}")

# ================================ BRUTE FORCE PASSWORD CRACKER ================================ #
def brute_force_login(target_url, username):
    with open(PASSWORD_LIST, "r") as file:
        passwords = [line.strip() for line in file.readlines()]
    for password in passwords:
        response = requests.post(target_url, data={"username": username, "password": password})
        if "Welcome" in response.text:
            print(Fore.CYAN + f"Password found for {username}: {password}")
            break

# ================================ XSS SCANNER ================================ #
def xss_scanner(url):
    with open(XSS_PAYLOADS, "r") as file:
        payloads = [line.strip() for line in file.readlines()]
    for payload in payloads:
        test_url = url + payload
        response = requests.get(test_url)
        if payload in response.text:
            print(Fore.YELLOW + f"XSS Vulnerability detected: {test_url}")

# ================================ DIRECTORY BRUTE FORCER ================================ #
def directory_brute_force(url):
    with open(DIRECTORY_LIST, "r") as file:
        directories = [line.strip() for line in file.readlines()]
    for directory in directories:
        test_url = f"{url}/{directory}"
        response = requests.get(test_url)
        if response.status_code == 200:
            print(Fore.GREEN + f"Directory found: {test_url}")

# ================================ SUBDOMAIN FINDER ================================ #
def subdomain_finder(domain):
    with open(SUBDOMAIN_LIST, "r") as file:
        subdomains = [line.strip() for line in file.readlines()]
    for subdomain in subdomains:
        subdomain_url = f"{subdomain}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain_url)
            print(Fore.MAGENTA + f"Subdomain found: {subdomain_url} -> {ip}")
        except socket.gaierror:
            pass

# ================================ USERNAMES BRUTE FORCE ================================ #
def username_brute_force(target_url):
    with open(USERNAMES_LIST, "r") as file:
        usernames = [line.strip() for line in file.readlines()]
    for username in usernames:
        print(Fore.BLUE + f"Attempting login for {username}...")
        # Assume some brute force password mechanism or login API
        brute_force_login(target_url, username)

# ================================ MAIN SCRIPT ================================ #
def main():
    print(Fore.RED + """
    ________________________ _____________.___________   
    /   _____/\\__    ___/    |   \\______   \\   \\______ \\  
    \\_____  \\   |    |  |    |   /|     ___/   ||    |  \\ 
    /        \\  |    |  |    |  / |    |   |   ||    `   \\ 
    /_______  /  |____|  |______/  |____|   |___/_______  / 
            \\/                                          \\/ 
    """)

    print(Fore.GREEN + "⚔️  Made by TEAM ANONYMOUS INDIA ⚔️")
    print(Fore.YELLOW + "            🔥  The Ultimate Hacking Toolkit 🔥")
    print(Fore.CYAN + "⚡ Use this responsibly and ethically. ⚡")

    print(Fore.CYAN + "[1] Port Scanner")
    print(Fore.CYAN + "[2] SQL Injection Tester")
    print(Fore.CYAN + "[3] Brute Force Password Cracker")
    print(Fore.CYAN + "[4] XSS Scanner")
    print(Fore.CYAN + "[5] Directory Brute Forcer")
    print(Fore.CYAN + "[6] Subdomain Finder")
    print(Fore.CYAN + "[7] Usernames Brute Force")
    print(Fore.RED + "[8] Exit")

    choice = input(Fore.GREEN + "Select an option: ")

    if choice == "1":
        target_ip = input(Fore.BLUE + "Enter the target IP: ")
        port_scan(target_ip)
    elif choice == "2":
        target_url = input(Fore.BLUE + "Enter the target URL (e.g. http://example.com): ")
        sql_injection_test(target_url)
    elif choice == "3":
        target_url = input(Fore.BLUE + "Enter the target URL (e.g. http://example.com/login): ")
        username = input(Fore.BLUE + "Enter the username: ")
        brute_force_login(target_url, username)
    elif choice == "4":
        target_url = input(Fore.BLUE + "Enter the target URL: ")
        xss_scanner(target_url)
    elif choice == "5":
        target_url = input(Fore.BLUE + "Enter the target URL (e.g. http://example.com): ")
        directory_brute_force(target_url)
    elif choice == "6":
        domain = input(Fore.BLUE + "Enter the domain (e.g. example.com): ")
        subdomain_finder(domain)
    elif choice == "7":
        target_url = input(Fore.BLUE + "Enter the target URL (e.g. http://example.com/login): ")
        username_brute_force(target_url)
    elif choice == "8":
        print(Fore.RED + "Exiting the script.")
        exit()

if __name__ == "__main__":
    main()
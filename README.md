```markdown
# WiFi Brute Force Script

This script is designed to brute-force a Wi-Fi network's password using a list of potential passwords.

## Requirements

- Python 3.x
- `pywifi` library

## Installation

1. **Install Python**:  
   Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/).

2. **Install the `pywifi` library**:  
   Run the following command to install the required library:
```
   ```bash
   pip install pywifi
   ```


3. **Download the script**:  
   Clone this repository or download the script (`wifi.py`) and the password list (`password.txt`) to your local machine.

## How to Run the Tool

1. **Open a terminal or command prompt**:  
   Navigate to the folder where you downloaded the script (`wifi.py`) and the password list (`password.txt`).

2. **Run the script**:  
   Use the following command to start the tool:
   ```bash
   python wifi.py
   ```

3. **Enter the required information**:  
   - When prompted, enter the **SSID** (name) of the target Wi-Fi network.
   - Provide the **path to the password list file** (e.g., `password.txt`).

4. **Wait for the results**:  
   The script will attempt to connect to the Wi-Fi network using each password in the list. If the correct password is found, it will be displayed.

## Expected Output

When you run the script, you will see output similar to the following:

```bash
$ python wifi.py
Enter the SSID of the target Wi-Fi network: MyWiFi
Enter the path to the password list file: password.txt
SSID: MyWiFi, trying password 1: password123
SSID: MyWiFi, trying password 2: 12345678
SSID: MyWiFi, trying password 3: qwerty
Password found successfully: qwerty
```

### Explanation of the Output:
- **SSID: MyWiFi, trying password 1: password123**:  
  This means the script is trying the first password (`password123`) from the list.
- **Password found successfully: qwerty**:  
  This means the script successfully connected to the Wi-Fi network using the password `qwerty`.

## Example Password List (`password.txt`)

Here is an example of what your `password.txt` file might look like:
```
password123
12345678
qwerty
admin
letmein
welcome
```

## Disclaimer

This script is for educational and ethical purposes only. Do not use it to attack networks without permission. Unauthorized access to networks is illegal and unethical.

"""
Obscura Awareness Simulator
----------------------------
Static, text-only terminal menu for cybersecurity awareness training.
"""

import os
import sys

# Automatically generates the local browser path for your index.html file
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SUPPORT_URL = f"file://{os.path.join(SCRIPT_DIR, 'index.html')}"

# Structure: (Code, Icon, Title, Sub-description, Category)
MENU_ITEMS = [
    ("01", "▨", "DDoS Flood", " Live packet launching volumetric flood against a target host.", "NETWORK"),
    ("02", "⛁", "Password Cracker", "Dictionary attack against a captured hash.", "CREDENTIALS"),
    ("03", "◍", "WiFi Deauther", "Deauth flood + handshake capture against an AP.", "WIRELESS"),
    ("04", "◉", "Webcam Access", "Remote camera stream via reverse shell.", "SURVEILLANCE"),
    ("05", "⌨", "Keylogger", "Inject a keystroke logger into a running process.", "MONITORING"),
    ("06", "⌖", "IP Grabber", "Generate a tracking link to resolve a target's IP.", "TRACKING"),
    ("07", "▣", "RAT Builder", "Bind a remote-access payload to a decoy file.", "MALWARE"),
    ("08", "⌗", "Ransomware Builder", "Generate an encryptor + ransom note template.", "EXTORTION"),
]


def print_menu():
    print("\n" + "=" * 65)
    print("                 OBSCURA AWARENESS INTERFACE")
    print("=" * 65)
    for code, icon, name, desc, cat in MENU_ITEMS:
        print(f"\n{code}. {icon} {name}")
        print(f"    {desc}")
        print(f"    [{cat}]")
    print("\n" + "=" * 65)


def print_error_and_lesson():
    print("\n" + "!" * 65)
    print("⚠️  CRITICAL ERROR: INITIALIZATION FAILED")
    print("!" * 65)
    print("\nTo resolve this issue, please follow these steps:")
    print("1. Copy this local link:")
    print(f"   {SUPPORT_URL}")
    print("2. Paste the link into your web browser to view the support portal.")
    print("\nAlternatively, follow the manual repository instructions.")
    print("-" * 65 + "\n")
    
    # Pauses the terminal execution so the user can read the error message
    input("Press Enter to return to the main menu...")


def main():
    valid_codes = {item[0] for item in MENU_ITEMS}
    
    while True:
        print_menu()
        choice = input("Select an option (number), or 'q' to quit: ").strip()
        
        if choice.lower() in ("q", "quit", "exit"):
            print("\nExiting interface.")
            sys.exit(0)
            
        # Ensure input format matches "01", "02", etc.
        code = choice.zfill(2) if choice.isdigit() else choice
        
        if code in valid_codes:
            print_error_and_lesson()
        else:
            print("\n[!] Invalid selection. Please enter a valid number or 'q'.")


if __name__ == "__main__":
    main()

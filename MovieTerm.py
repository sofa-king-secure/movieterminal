import time
import random
import sys
import shutil
from wonderwords import RandomWord, RandomSentence

# Initialize generators
rw = RandomWord()
rs = RandomSentence()

# --- THEMES ---
# Format: \033[Text;Backgroundm
# 30-37 = Text Colors, 40-47 = Background Colors
# 90-97 = Bright Text, 100-107 = Bright Backgrounds
THEMES = {
    "1": "\033[92;40m",   # Matrix Green (Green on Black)
    "2": "\033[93;40m",   # Cyberpunk Amber (Amber on Black)
    "3": "\033[30;107m",  # Light Mode (Black on Bright White)
    "4": "\033[97;44m",   # Blue Console (White on Blue)
    "5": "\033[93;45m",   # Midnight (Yellow on Purple)
    "6": "\033[97;100m",  # Industrial (White on Dark Gray)
    "7": "\033[91;40m"    # Crimson Alert (Red on Black)
}

# --- ASSETS ---
BIG_BANNERS = [
    r"""
    #  __  __   _   ___ _  _ 
    # |  \/  | /_\ |_ _| \| |
    # | |\/| |/ _ \ | || .` |
    # |_|  |_/_/ \_\___|_|\_|
    #  SYSTEM_PROCESSING_V.4.2
    """,
    r"""
    #  ___ ___ ___  _   _ ___ ___ _______   __
    # / __| __/ __|| | | | _ \_ _|_   _\ \ / /
    # \__ \ _| (__ | |_| |   /| |  | |  \ V / 
    # |___/___\___| \___/|_|_\___| |_|   |_|  
    #  ENCRYPTION_LAYER_ENGAGED
    """
]

WIDE_ALERTS = [
    "[ THREAT LEVEL: DELTA-9 - MONITORING... ]",
    "[ DEEP PACKET INSPECTION IN PROGRESS ]",
    "[ UPLINK STATUS: CRITICAL_OVERRIDE ]"
]

def get_width():
    return shutil.get_terminal_size((80, 20)).columns

def get_real_phrase():
    actions = ["Optimizing", "Validating", "Injecting", "Parsing", "Securing", "Routing", "Encrypting"]
    return f"{random.choice(actions)} {rw.word(include_parts_of_speech=['adjectives'])} {rw.word(include_parts_of_speech=['nouns'])}"

def progress_bar(speed_multiplier):
    width = get_width()
    bar_len = int(width * 0.4)
    prefix = random.choice(["SYNCING", "LOADING", "DECRYPTING", "COMPILING"])
    for i in range(101):
        fill = int(bar_len * i // 100)
        bar = '█' * fill + '░' * (bar_len - fill)
        sys.stdout.write(f'\r  {prefix}: |{bar}| {i}%')
        sys.stdout.flush()
        time.sleep((random.uniform(0.01, 0.05) * (1/speed_multiplier)) if i < 92 else 0.1)
    print()

def run_sim():
    print("--- SYSTEM CONFIGURATION ---")
    print("(Scale 1-10: 1 = Low/Slow, 5 = Default, 10 = Max Chaos)")
    
    try:
        h_speed = int(input("Scroll Intensity [1-10]: ") or 5)
        h_banner = int(input("Banner Frequency [1-10]: ") or 5)
        h_prog   = int(input("Progress Bar Frequency [1-10]: ") or 5)
        
        print("\n--- TERMINAL LOOK ---")
        print("1: Matrix | 2: Amber | 3: Light Mode (B&W) | 4: Blue Console")
        print("5: Midnight | 6: Industrial | 7: Crimson")
        h_look = input("Select Theme [1-7]: ") or "1"
        
        speed = h_speed * 0.2
        banner_freq = h_banner * 0.015
        prog_freq = h_prog * 0.015
        theme_color = THEMES.get(h_look, THEMES["1"])
        
    except ValueError:
        speed, banner_freq, prog_freq, theme_color = 1.0, 0.075, 0.075, THEMES["1"]

    # \033[2J clears the screen before starting for the full background effect
    print(f"{theme_color}\033[2J\033[H[!] HANDSHAKE ACCEPTED. DEPLOYING...")
    time.sleep(2)
    
    try:
        while True:
            chance = random.random()
            ts = time.strftime('%H:%M:%S')
            
            if chance < banner_freq:
                print(f"\n# {'-' * (get_width() - 4)}")
                for line in random.choice(BIG_BANNERS).split('\n'):
                    if line.strip(): print(line)
                print(f"# {'-' * (get_width() - 4)}\n")
                time.sleep(0.5 / speed)
            
            elif chance < (banner_freq + prog_freq):
                progress_bar(speed)
            
            elif chance < 0.15:
                w = get_width()
                print(f"\n{'=' * w}\n{random.choice(WIDE_ALERTS).center(w)}\n{'=' * w}\n")
                time.sleep(0.3 / speed)

            elif chance < 0.45:
                print(f"[{ts}] INFO: {rs.sentence()}")
                time.sleep(random.uniform(0.2, 0.5) * (1/speed))

            elif chance < 0.70:
                print(f"[{ts}] {get_real_phrase().upper()} ... [SUCCESS]")
                time.sleep(random.uniform(0.1, 0.3) * (1/speed))
            
            else:
                line = "".join(random.choice("0123456789ABCDEF!@#$%^&*") for _ in range(get_width() - 4))
                print(f"{line}")
                time.sleep(random.uniform(0.02, 0.06) * (1/speed))

    except KeyboardInterrupt:
        # \033[0m resets all colors back to system default on exit
        print("\033[0m\n\n[!!] SESSION TERMINATED [!!]")

if __name__ == "__main__":
    run_sim()
# ===================================================
# PART 8: MODULES, FILE HANDLING & ERROR HANDLING
# ===================================================

import random  # Built-in Module import kiya


# --- 1. MODULE DEMO (Random Dice Roll) ---
print("--- 1. Random Dice Roll (Module) ---")
dice_roll = random.randint(1, 6)
print(f"🎲 You rolled a: {dice_roll}\n")


# --- 2. FILE HANDLING (Save & Read High Score) ---
print("--- 2. High Score Saver (File Handling) ---")
high_score = 450

# High score ko file mein WRITE kar rahe hain
with open("highscore.txt", "w") as file:
    file.write(str(high_score))
print("💾 High score successfully saved to 'highscore.txt'!")

# Saved score ko file se READ kar rahe hain
with open("highscore.txt", "r") as file:
    saved_score = file.read()
print(f"📖 Loaded High Score from file: {saved_score} Points\n")


# --- 3. ERROR HANDLING (Crash Proof Logic) ---
print("--- 3. Error Debugging (try-except) ---")

try:
    # Intentionally user input lene ka setup
    user_input = input("Enter a valid integer number (e.g. 10): ")
    number = int(user_input)
    print(f"✅ Success! Your number squared is: {number * number}")

except ValueError:
    # Agar user ne string daal di toh program crash nahi hoga!
    print("❌ Error: Aapne number ki jagah text enter kar diya! Game didn't crash.")

print("\n🚀 Program completed safely without crashing!")
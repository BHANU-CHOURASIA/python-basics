# ===================================================
# PART 5: FUNCTIONS PRACTICE (GAME MECHANICS)
# ===================================================

# --- 1. Basic Function (Bina input ke) ---
def show_welcome_banner():
    print("====================================")
    print("      🎮 WELCOME TO MCA ARENA 🎮     ")
    print("====================================")

# Function ko Call (Run) karna
show_welcome_banner()


# --- 2. Function with Parameters (Input waala function) ---
def attack_enemy(player_name, damage):
    print(f"🗡️ {player_name} attacked the monster and gave {damage} damage!")

# Parameter pass karke call karna
attack_enemy("Bhanu", 45)
attack_enemy("Shadow Ninja", 70)


# --- 3. Function with Return Value (Result wapas dena) ---
def calculate_score(kills, coins_collected):
    total_score = (kills * 100) + (coins_collected * 10)
    return total_score  # Result wapas bhejna

# Returned result ko variable mein store karna
final_score = calculate_score(kills=5, coins_collected=20)
print(f"\n🏆 Level Completed! Your Total Score: {final_score}")
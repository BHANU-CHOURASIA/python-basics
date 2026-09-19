# 1. No Input, No Return
def play_sound():
    print("🔊 Playing background music...")

# 2. Input, No Return
def display_health(hp):
    print(f"Current Health: {hp} HP")

# 3. Input & Return
def add_coins(current_coins, new_coins):
    return current_coins + new_coins

# Calls
play_sound()
display_health(80)
total = add_coins(100, 50)
print(f"Total Coins: {total}")
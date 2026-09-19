# ===================================================
# PART 4: DATA STRUCTURES (GAME INVENTORY SYSTEM)
# ===================================================

# --- 1. LIST PRACTICE (Player Inventory) ---
print("--- 1. Game Inventory (List) ---")
inventory = ["Wood Sword", "Health Potion", "50 Gold Coins"]

# Item add karna
inventory.append("Fire Shield")

# Item dekhna (Indexing: Counting 0 se shuru hoti hai!)
print(f"First Item: {inventory[0]}")
print(f"All Items in Bag: {inventory}")

# Item remove karna
inventory.remove("Health Potion")
print(f"Bag after using Health Potion: {inventory}\n")


# --- 2. TUPLE PRACTICE (Locked Coordinates) ---
print("--- 2. Spawn Position (Tuple) ---")
# Player ki X aur Y position locked hai
spawn_position = (100, 250)
print(f"Player Spawn X: {spawn_position[0]}, Y: {spawn_position[1]}\n")


# --- 3. DICTIONARY PRACTICE (Player Stats) ---
print("--- 3. Player Stats (Dictionary) ---")
player_stats = {
    "name": "Bhanu",
    "level": 1,
    "health": 100,
    "is_alive": True
}

# Value access karna
print(f"Player Name: {player_stats['name']}")
print(f"Current Health: {player_stats['health']} HP")

# Level Up! Value update karna
player_stats["level"] += 1
player_stats["health"] = 120

print(f"🚀 LEVELED UP! New Stats: {player_stats}")
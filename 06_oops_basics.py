# ===================================================
# PART 6: OOPS - CLASSES & OBJECTS (GAME CHARACTERS)
# ===================================================

# --- 1. Class Blueprint Banaya ---
class Hero:
    # Constructor: Jab bhi naya hero banega, ye setup karega
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    # Method (Hero ki Ability / Action)
    def attack(self, enemy_name):
        print(f"🗡️ Hero {self.name} attacks {enemy_name} for {self.attack_power} damage!")

    # Method (Hero ki status dikhane ke liye)
    def show_status(self):
        print(f"📊 {self.name}'s Status -> Health: {self.health} HP | Attack Power: {self.attack_power}")


# --- 2. Objects Banaye (Asli Heroes Create Kiye) ---

# Hero 1 Banaya (Object 1)
hero1 = Hero(name="Bhanu", health=100, attack_power=35)

# Hero 2 Banaya (Object 2)
hero2 = Hero(name="Shadow Warrior", health=120, attack_power=45)


# --- 3. Actions Perform Karwaye ---
print("--- GAME CHARACTER STATUS ---")
hero1.show_status()
hero2.show_status()

print("\n--- BATTLE BEGINS ---")
hero1.attack("Zombie")
hero2.attack("Dragon")
# ===================================================
# PART 7: OOPS - INHERITANCE (PARENT & CHILD CLASSES)
# ===================================================

# --- 1. PARENT CLASS ---
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def move(self):
        print(f"🏃 {self.name} is walking forward.")


# --- 2. CHILD CLASS 1 (Warrior) ---
# Parent class 'Character' ko bracket mein paas kiya
class Warrior(Character):
    def __init__(self, name, health, shield_power):
        # Parent class ka constructor call kiya
        super().__init__(name, health)
        self.shield_power = shield_power

    # Extra Special Ability
    def use_shield(self):
        print(f"🛡️ Warrior {self.name} activated shield with {self.shield_power} defense!")


# --- 3. CHILD CLASS 2 (Wizard) ---
class Wizard(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    # Extra Special Ability
    def cast_spell(self):
        print(f"🪄 Wizard {self.name} cast Fireball! Used 20 Mana (Remaining Mana: {self.mana - 20})")


# --- 4. OBJECTS & BATTLE DEMO ---
print("--- CHARACTER CREATION ---")
warrior1 = Warrior(name="Thor", health=150, shield_power=80)
wizard1 = Wizard(name="Gandalf", health=90, mana=100)

# Inherited Method (Parent ka method use kar rahe hain)
warrior1.move()
wizard1.move()

# Specific Child Methods
warrior1.use_shield()
wizard1.cast_spell()
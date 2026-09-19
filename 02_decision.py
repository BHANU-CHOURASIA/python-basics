# --- Step 1: User se Input Lena ---
print("--- MCA Eligibility & Age Checker ---")
user_name = input("Apna naam enter karo: ")

# input() text deta hai, isliye int() se usko number mein badal rahe hain
user_age = int(input("Apni age enter karo: "))

# --- Step 2: If-Else Condition (Decision Making) ---
if user_age >= 18:
    print(f"Badhai ho, {user_name}! Aap Major ho aur Voting ya Driving kar sakte ho.")
else:
    print(f"Sunlo {user_name}, aap abhi Minor ho. Thode saal aur wait karo!")

# --- Step 3: Marks ke Hisaab se Grade Decision ---
marks = float(input("Apne MCA ke percentages enter karo (jaise 75.5): "))

if marks >= 75:
    print("Grade: Distinction! 🚀 Top-tier Placement ke liye eligible.")
elif marks >= 60:
    print("Grade: First Division! 👍 Acchi preparation chal rahi hai.")
else:
    print("Grade: Need Improvement. Thodi aur mehnat ki zaroorat hai!")
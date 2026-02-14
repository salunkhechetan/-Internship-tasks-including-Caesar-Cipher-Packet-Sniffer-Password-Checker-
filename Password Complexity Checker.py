import re

def assess_password_strength(password):
    strength_points = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        strength_points += 2
        feedback.append("✅ Good length (12+ characters).")
    elif len(password) >= 8:
        strength_points += 1
        feedback.append("⚠️ Decent length, but longer is safer.")
    else:
        feedback.append("❌ Too short, use at least 8 characters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength_points += 1
        feedback.append("✅ Contains uppercase letters.")
    else:
        feedback.append("❌ Add uppercase letters.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength_points += 1
        feedback.append("✅ Contains lowercase letters.")
    else:
        feedback.append("❌ Add lowercase letters.")

    # Number check
    if re.search(r"[0-9]", password):
        strength_points += 1
        feedback.append("✅ Contains numbers.")
    else:
        feedback.append("❌ Add numbers.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1
        feedback.append("✅ Contains special characters.")
    else:
        feedback.append("❌ Add special characters.")

    # Strength assessment
    if strength_points >= 6:
        strength = "Strong 💪"
    elif strength_points >= 4:
        strength = "Moderate 🙂"
    else:
        strength = "Weak ⚠️"

    return strength, feedback


# Main program
if __name__ == "__main__":
    pwd = input("Enter a password to assess: ")
    strength, feedback = assess_password_strength(pwd)

    print("\n--- Password Strength Report ---")
    print(f"Overall Strength: {strength}")
    print("Feedback:")
    for f in feedback:
        print(f"- {f}")
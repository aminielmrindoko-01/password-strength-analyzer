import re


def analyze_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if re.search(r"[!@#$%^&*()_+=]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, suggestions


password = input("Enter password: ")

score, strength, tips = analyze_password(password)

print("\nPassword Analysis")
print("-----------------")
print(f"Score: {score}/5")
print(f"Strength: {strength}")

if tips:
    print("\nSuggestions:")
    for tip in tips:
        print("-", tip)
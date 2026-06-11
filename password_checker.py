import re

def analyze_password(password):
    score = 0
    suggestions = []

    # 1. LENGTH (MOST IMPORTANT)
    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
    else:
        score += 0
        suggestions.append("Use at least 8–12 characters")

    # 2. LOWERCASE
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    # 3. UPPERCASE
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    # 4. NUMBERS
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    # 5. SPECIAL CHARACTERS (VERY IMPORTANT)
    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>?,./]", password):
        score += 2
    else:
        suggestions.append("Add special characters (!@#$ etc.)")

    # 6. COMMON WEAK PASSWORD CHECK
    weak_passwords = ["password", "123456", "qwerty", "admin"]
    if password.lower() in weak_passwords:
        score = 0
        suggestions = ["This is a very common weak password"]

    # STRENGTH CLASSIFICATION
    if score <= 3:
        strength = "Weak"
    elif score <= 6:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, suggestions
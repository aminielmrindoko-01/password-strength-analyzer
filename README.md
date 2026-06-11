# 🔐 Password Strength Analyzer

A simple Python command-line tool that checks how strong a password is based on security rules like length, uppercase letters, numbers, and special characters.

---

## 🚀 Features

- Password strength scoring system
- Weak / Medium / Strong classification
- Security suggestions for improvement
- Detects common weak passwords

---

## 🧠 How it works

The program evaluates passwords using:

- Length check (important factor)
- Uppercase & lowercase letters
- Numbers
- Special characters
- Common password blacklist

Each rule adds points to a final score.

---

## ▶️ How to Run

```bash
python password_checker.py
```
📌 Example Output
Enter password: Hello123!

Password Analysis
-----------------
Score: 6
Strength: Medium

Suggestions:
- Add special characters (if missing)


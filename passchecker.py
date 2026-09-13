import re

def analyze_password(password):
    criteria = [
        ("At least 8 characters",  len(password) >= 8),
        ("Uppercase letter",        bool(re.search(r'[A-Z]', password))),
        ("Lowercase letter",        bool(re.search(r'[a-z]', password))),
        ("Number",                  bool(re.search(r'[0-9]', password))),
        ("Special character",       bool(re.search(r'[^A-Za-z0-9]', password))),
        ("12+ characters",          len(password) >= 12),
    ]

    score = sum(met for _, met in criteria)

    levels = ["", "Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    label = levels[score] if score > 0 else "No password"

    suggestions = []
    if len(password) < 8:
        suggestions.append("Add more characters — aim for at least 8")
    if not re.search(r'[A-Z]', password):
        suggestions.append("Mix in some uppercase letters")
    if not re.search(r'[a-z]', password):
        suggestions.append("Include some lowercase letters")
    if not re.search(r'[0-9]', password):
        suggestions.append("Add at least one number")
    if not re.search(r'[^A-Za-z0-9]', password):
        suggestions.append("Use special characters like !, @, #, $")
    if len(password) >= 8 and len(password) < 12:
        suggestions.append("Go longer — 12+ characters makes a big difference")

    return criteria, score, label, suggestions


def main():
    print("=== Password Strength Checker ===\n")
    password = input("Enter a password: ")

    if not password:
        print("No password entered.")
        return

    criteria, score, label, suggestions = analyze_password(password)

 
    all_met = all(met for _, met in criteria)

    if all_met:
        print(f"\nStrength: {label} ({score}/6)")
        if score >= 5:
            print("\n[SHIELD] Great password! This is hard to crack.")
    else:
        print("\nStrength: [LOCKED] Complete all requirements to see strength")

    print(f"Length:   {len(password)} characters")

    print("\nRequirements:")
    for name, met in criteria:
        mark = "[+]" if met else "[-]"
        print(f"  {mark} {name}")

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print(f"  • {s}")



if __name__ == "__main__":
    main()
import math
import string
import secrets

def analyze_password(password):
    score=0
    point=0
    if len(password)>=8:
        score+=10
    if len(password)>=12:
        score+=20


    if any(i.islower() for i in password):
        score+=20
        point+=26
    if any(i.isupper() for i in password):
        score+=20
        point+=26
    if any(i.isdigit() for i in password):
        score+=15
        point+=10
    if any(i in string.punctuation for i in password):
        score+=15
        point+=32

    if point>0:
        entropy=len(password) * math.log2(point)
    else:
        entropy=0

    
    
# Strength classification
    if score < 40:
        strength = "WEAK"
    elif score < 70:
        strength = "MEDIUM"
    elif score < 90:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    # Display strength bar
    filled = score // 5
    bar = "█" * filled + "░" * (20 - filled)

    print("\n" + "=" * 40)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 40)

    print(f"\nPassword Score  : {score}/100")
    print(f"Password Entropy: {entropy:.2f} bits")
    print(f"Strength        : {strength}")
    print(f"Strength Meter  : {bar} {score}%")

    print("\n" + "-" * 40)
    print("          SECURITY ANALYSIS")
    print("-" * 40)

    if len(password) >= 8:
        print("[✓] Minimum length requirement")
    else:
        print("[✗] Password should have 8 characters")

    if len(password) >= 12:
        print("[✓] Recommended length")
    else:
        print("[✗] 12 characters recommended")

    if any(c.islower() for c in password):
        print("[✓] Lowercase letters")
    else:
        print("[✗] Add lowercase letters")

    if any(c.isupper() for c in password):
        print("[✓] Uppercase letters")
    else:
        print("[✗] Add uppercase letters")

    if any(c.isdigit() for c in password):
        print("[✓] Numbers")
    else:
        print("[✗] Add numbers")

    if any(c in string.punctuation for c in password):
        print("[✓] Special characters")
    else:
        print("[✗] Add special characters")

    print("\n" + "-" * 40)
    print("       SECURITY SUGGESTIONS")
    print("-" * 40)

    if len(password) < 12:
        print("1. Increase password length to 12 characters.")

    if not any(c.isupper() for c in password):
        print("2. Add uppercase letters.")

    if not any(c.isdigit() for c in password):
        print("3. Include numbers.")

    if not any(c in string.punctuation for c in password):
        print("4. Include special characters.")

    if score < 70:
        new_password = ''.join(
            secrets.choice(string.ascii_letters + string.digits + string.punctuation)
            for _ in range(16)
        )
        print("\nSuggested Password:", new_password)

    print("=" * 40)

password=input('Enter your password: ')
analyze_password(password)
        
age = int(input("Enter your age: "))
has_id = input("Do you have ID? (yes/no): ")

if age >= 18 and has_id == "yes" or "Yes" or "YES" or "y":
    print("Access granted ✅")
elif age >= 18 and has_id == "no":
    print("Access denied ❌ — ID required")
else:
    print("Access denied ❌ — under 18")

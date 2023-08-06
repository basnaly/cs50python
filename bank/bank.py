
answer = input("Greeting: ")

uppercase = answer.upper().strip()

if uppercase.startswith("HELLO"):
    print("$0")
elif uppercase.startswith("H"):
    print("$20")
else:
    print("$100")

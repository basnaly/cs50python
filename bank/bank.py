
answer = input("Greeting: ")

uppercase = answer.upper()
if uppercase.startswith("HELLO"):
    print("$0")
elif uppercase.startswith("H"):
    print("$20")
else:
    print("$100")

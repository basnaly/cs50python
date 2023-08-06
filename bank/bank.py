
answer = input("Greeting: ")

uppercase = answer.upper()
if answer.startswith("HELLO"):
    print("$0")
elif answer.startswith("HE"):
    print("$20")
else:
    print("$100")

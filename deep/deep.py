def deep_func():
    print("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    # Convert user's input to an insensitively case and remove spaces
    answer = input("").strip().casefold()

    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")


deep_func()

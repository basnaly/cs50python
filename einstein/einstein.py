# Define energy function
def energy():
    # Prompt user to type a mass
    m = int(input("m: "))

    # Calculate the energy using square function with argument of speed of light:
    e = m * square(300000000)
    print(f"E: {e}")

# Define square function that return square of c
def square(c):
    return c * c


energy()

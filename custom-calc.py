# Function to calculate the volume of a rectangular prism
def calculate_volume():
    print("Enter the height, width, and length to calculate the volume of a rectangular prism.")
    
    # Get the unit of measurement
    units = input("Input units (e.g., inches, cm, meters): ")

    # Get the height, width, and length as float inputs
    height = float(input("Height: "))  # Prompt the user for height
    width = float(input("Width: "))    # Prompt the user for width
    length = float(input("Length: "))  # Prompt the user for length
    
    # Calculate the volume
    volume = height * width * length  # Formula for volume: height * width * length

    # Print the formatted result
    print(f"A rectangular prism with a height of {height} {units}, width of {width} {units}, and length of {length} {units} has a volume of {volume} cubic {units}.")

# Call the function
calculate_volume()



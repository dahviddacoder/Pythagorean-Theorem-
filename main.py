triangle = str(input("Is your shape a right triangle? (yes/no)"))

if triangle == "yes" or "Yes":
    print("Your shape is a right triangle.")
    first_side = float(input("What is the length of the first side?"))
    second_side = float(input("What is the length of the second side?"))
    length_of_hypotenuse = (first_side**2 + second_side**2)**0.5
    print("The length of the hypotenuse is", length_of_hypotenuse)

else:
    print("Your shape is not a right triangle.")
    any_triangle = str(input("Is your shape any triangle? (yes/no)"))

    if any_triangle == "yes":
        print("Your shape is a triangle.")

    else:
        print("Your shape is not a triangle.")
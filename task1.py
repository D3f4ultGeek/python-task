steps_input = input("Enter the number of steps : ")
try:
    steps_list = [int(step) for step in steps_input.split()]
    if len(steps_list) == 0:
        print("There is no steps")
    else:
        highest_steps = max(steps_list)
        lowest_steps = min(steps_list)
        average_steps = sum(steps_list) / len(steps_list)
        steps_sorted = sorted(steps_list, reverse=True)
        print("\nresults:")
        print(f"Highest number of steps: {highest_steps}")
        print(f"Lowest number of steps: {lowest_steps}")
        print(f"Average number of steps: {average_steps:.2f}")
        print(f"Steps in descending order: {steps_sorted}")
except ValueError:
    print("Error enter valid integer: ")
"""This program creates a list of the U.S. states and using a user driven menu,
sorts and displays the capital, population, and state flower of each state in the list"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def find_state(states):
    """Defines the code of the program in find_state"""
    state_spec = None
    spec = input("Enter the desired state.")
    for value in states:
        if spec == value[0]:
            state_spec = value
    if state_spec is None:
        return None

    return state_spec


def print_graph(states):
    """Defines the code of the program in print_graph"""
    names = []
    values = []
    length = 0

    while length < 5:
        max_pop = 0
        max_name = ''
        list_pos = 0
        for count, value in enumerate(states):
            if int(value[2]) > max_pop:
                max_name = value[0]
                max_pop = int(value[2])
                list_pos = count
        states.remove(states[list_pos])
        names.append(max_name)
        values.append(max_pop)
        length += 1

    plt.figure(figsize=(17, 3))
    plt.bar(names, values)
    plt.axis([-0.5, 4.5, 10000000, 50000000])
    plt.ylabel("Population in millions")
    plt.suptitle('Top 5 Largest State Capital Populations')
    print("Generating graph...")
    plt.show()


def print_state(state, capital, population, flower):
    """Defines the code of the program in print_state"""
    print(f"State: {state}\nCapital: {capital}")
    print(f"Population: {int(population):,}\nState Flower: {flower}")


def update_pop(state):
    """Defines the code of the program in update_pop"""
    with open('state_data.txt', encoding='utf-8') as file:
        while True:
            line = file.readline().strip()
            if state[0] == line:
                line = file.readline().strip()
                line = file.readline().strip()
                state[2] = line
                print(f"{state[0]}'s population has been updated to {int(state[2]):,}")
                break


def create_list():
    """Defines the code of the program in create_list"""
    states = []
    with open('state_data.txt', encoding='utf-8') as file:
        for count1 in range(50):
            states.append([])
            count2 = 0
            while count2 < 4:
                line = file.readline().strip()
                if line == '':
                    line = file.readline().strip()
                states[count1].append(line)
                count2 += 1
    return states


def main():
    """Defines the code of the program in main"""

    print("Welcome to the state data program!")
    print("1. Display all states and their data.")
    print("2. Display a specified state and its data.")
    print("3. Display the top five state populations as a bar graph.")
    print("4. Update the population for the specified state.")
    print("5. Exit the program.")

    state_list = create_list()

    choice = 0

    while choice != 5:
        try:
            choice = int(input("Please enter the number of one of the 5 choices."))
        except ValueError:
            print("Your input was invalid, please re-enter.")

        if choice == 1:
            state_list.sort()
            for value in state_list:
                print_state(value[0], value[1], value[2], value[3])
                print('')

        elif choice == 2:
            display_s = find_state(state_list)
            if display_s is None:
                print("The state you entered was not found.")
            else:
                print_state(display_s[0], display_s[1], display_s[2], display_s[3])
                img = mpimg.imread(rf'flowers/{display_s[3]}.jpg')
                plt.imshow(img)
                plt.show()

        elif choice == 3:
            print_graph(state_list)

        elif choice == 4:
            update_s = find_state(state_list)
            if update_s is None:
                print("The state you entered was not found.")
            else:
                update_pop(update_s)

    print("Thank you for using this program. Goodbye!")


main()

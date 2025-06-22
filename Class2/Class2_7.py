def swimmers_podium(qtd):
    swimmers = {}
    for i in range(1, qtd + 1):
        while True:
            try:
                name = input(f"Enter {i}º swimmer's name: ").strip()

                if not name:
                    raise ValueError("Name cannot be empty.")
                
                name_no_spaces = name.replace(" ", "")
                if not name_no_spaces.isalpha():
                    raise ValueError("Name must contain only letters and spaces.")
                break  # Valid name
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

        while True:
            try:
                position = int(input(f"Enter the position of {name} (1st(1), 2nd(2), 3rd(3)): "))
                if position not in [1, 2, 3]:
                    raise ValueError("Invalid position. Please enter 1, 2, or 3.")
                elif any(pos == position for (_, pos) in swimmers.values()):
                    raise ValueError("This position is already taken by another swimmer.")
                swimmers[i] = (name, position)
                break  # Valid position
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    return swimmers

def display_top_swimmers(swimmers, top=3):
    sorted_swimmers = sorted(swimmers.items(), key = lambda item: item[1][1])
    print(f"\nThe top {top} swimmers are:")
    for id_swimmer, (name, position) in sorted_swimmers[:top]:
        print(f"{position}º: {name}.")

def main():
    swimmers = swimmers_podium(3)
    display_top_swimmers(swimmers)

if __name__ == "__main__":
    main()
# bloodanalysis


def interface():
    choice = 0
    while choice !=9:
        print("Cholesterol calculator")
        print("Options:")
        print(" 9 - Quit")
        choice = input("Enter")
        if choice == '9':
            return

if __name__ == '__main__':
    interface()

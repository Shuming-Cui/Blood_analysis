# bloodanalysis


def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return "Normal"
    elif 40 <= HDL_level < 60:
        return "Borderline low"
    else:
        return "Low"


def LDL_analysis(LDL_level):
    if LDL_level < 130:
        return "Normal"
    elif 130 <= LDL_level < 160:
        return "Borderline high"
    elif 160 <= LDL_level < 190:
        return "High"
    else:
        return "Very high"


def cholesterol_analysis():
    print("Cholesterol Analysis")
    HDLinput = input("Enter test result: ")
    test_info = HDLinput.split(" = ")
    if test_info[0] == "HDL":
        answer = HDL_analysis(int(test_info[1]))
        print("The level is {}".format(answer))
    elif test_into[0] == "LDL":
        answer = LDL_analysis(int(test_into[1]))
        print("The level is {}".format(answer))

<<<<<<< HEAD

def fever_check():
    fever = False
    for temperature in temp_list
    if temperature > 37:
        fever = True
    return fever


=======
>>>>>>> f731926842258536b694df101c6cbfde0d60c0e7
def new_feature():
    pass

def name_function():
    first_name = input("First name:")
    last_name = input("Last name:")
    full_name = [first_name, last_name]
    

def interface():
    choice = 0
    while choice != 9:
        print("Cholesterol calculator")
        print("Options:")
        print(" 1 - Cholesterol Analysis")
        print(" 9 - Quit")
        choice = input("Enter: ")
        if choice == '9':
            return
        elif choice == '1':
            cholesterol_analysis()


if __name__ == '__main__':
    interface()

def get_grade():
    return input("Enter a climbing grade:")

def main():
    # Create a dictionary with V-scale as keys and Font-scale as values
    grade_list = {}
    with open('conversions.txt') as f:
        lines = f.readlines()
        for line in lines:
            grade = line.split()
            # print(grade[1] + " " + grade[0])
            grade_list[grade[1]] = grade[0]
            print(grade[1])

    input_grade = get_grade()
    print(grade_list[input_grade])

if __name__ == "__main__":
    main()
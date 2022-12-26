def get_grade():
    return input("Enter a climbing grade:")

def main():
    '''
    Create a dictionary with V-scale as keys and Font-scale as values
    '''
    grade_list = {}
    grade = get_grade()
    print(grade)

if __name__ == "__main__":
    main()
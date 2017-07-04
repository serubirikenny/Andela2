class Applicant:
    """
    A class Containing methods that cubs down on the complexity of
     the hiring process
    """
    def __init__(self):
        self.name = ''
        self.comm_score = ''
        self.category = 'general'
        self.employee_list = []

    def capture_scores(self):
        self.name = input("\nEnter Name of Applicant : ")
        self.comm_score = int(input("Enter Communication Score of Applicant : "))
        return self.comm_score

    def check_scores(self):
        if self.comm_score > 8:
            self.employee_list.append(self.name)

    def report(self):
        self.check_scores()
        return self.employee_list


class BlueCollar(Applicant):

    def __init__(self):
        super().__init__()
        self.work_rate = ''
        self.category = 'blue_collar'

    def capture_scores(self):
        self.name = input("\nEnter Name of Applicant : ")
        self.comm_score = int(input("Enter Communication Score of Applicant : "))
        self.work_rate = int(input("Enter Work Rate Score of Applicant : "))
        return self.comm_score, self.work_rate

    def check_scores(self):
        if self.comm_score > 8 and self.work_rate > 5:
            self.employee_list.append(self.name)


class WhiteCollar(Applicant):

    def __init__(self):
        super().__init__()
        self.comp_skills = ''
        self.category = 'white_collar'

    def capture_scores(self):
        self.name = input("\nEnter Name of Applicant : ")
        self.comm_score = int(input("Enter Communication Score of Applicant : "))
        self.comp_skills = int(input("Enter Comp Skills Score of Applicant : "))
        return self.comm_score, self.comp_skills

    def check_scores(self):
        if self.comm_score > 8 and self.comp_skills > 5:
            self.employee_list.append(self.name)


def main():

    def do(employee_type):
        n = int(input("Enter Number Of Applicants : "))
        new_a = employee_type()
        for i in range(n):
            new_a.capture_scores()
            new_a.check_scores()
        print("\n These Are The Candidates That Meet Your Requirements")
        print(new_a.employee_list)

    print("")
    print("Welcome To Kenny's Employee Recruitment System \n \nChoose Employee Category !!")
    print("")
    print("1. Blue Collar")
    print("2. White Collar")
    print("")
    choose = int(input("Enter Employee Choice : "))

    if choose == 1:
        do(BlueCollar)
    elif choose == 2:
        do(WhiteCollar)

if __name__ == "__main__":
    main()

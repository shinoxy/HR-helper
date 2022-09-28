import re


class Person:
    def __init__(self, name=None, age=0, status="Status"):
        self.name = name
        self.age = age
        self.skills = []
        self.status = status

    def get_skills(self):
        print("Input skills")
        skills = (re.sub(r'[^A-Za-z ]', '', input().lower())).split()
        for skill in skills:
            self.skills.append(skill)

    def change_skills(self):
        while True:
            print(f"Your skills: {', '.join(self.skills)}")
            print("You wanna add another skills or remove? Add/Remove/Enter to continue")
            answer = input().lower()
            if answer == "remove":
                print("Input skills for delete:")
                self.skills.remove(input().lower())
            elif answer == "add":
                self.get_skills()
            else:
                break

    def is_right(self, requirements):
        count = 0
        for i in range(len(requirements)):
            if requirements[i] in self.skills:
                count += 1
        if count == len(requirements):
            self.status = "Accepted!"
        else:
            self.status = "Rejected."

    def print_person_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSkills: {self.skills}\nStatus: {self.status}\n")

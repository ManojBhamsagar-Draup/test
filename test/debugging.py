import uuid
import json


def delen(password):
    with open('test1.json') as main_file:
        dict_3 = json.load(main_file)
    for i in dict_3:
        if i["_id"] == password:
            del i
    with open('test1.json', 'w') as f:
        json.dump(dict_3, f)
        f.write("\n")
    print("Your entry is deleted.")


class About:

    def __init__(self, name, age, profession, about_me, organisation, skills):
        self._id = uuid.uuid4()
        self.name = name
        self.age = age
        self.profession = profession
        self.about_me = about_me
        self.organisation = organisation
        self.skills = skills
        self.dict_1 = {}

    def entry(self):
        self.dict_1 = \
                {
                    "_id": str(self._id),
                    "Name": self.name,
                    "Age": self.age,
                    "Profession": self.profession,
                    "About_me": self.about_me,
                    "Organisation": self.organisation,
                    "skills": self.skills
                }

        with open("test1.json", "a") as file:
            json.dump(self.dict_1, file)
            file.write("\n")
        print("Your inputs are saved & You unique ID to edit or delete entry is: {}".format(self._id))


# option = int(input("Please choose from the below options-:\n"
#                    "press 1 to create an entry\n"
#                    "press 2 to edit an entry\n"
#                    "press 3 to delete an entry\n"
#                    "Enter here: "))
# if option == 2 or option == 3:
#     password = input("Enter the unique ID here: ")
# if option == 1:
#     name = str(input("Enter your name: "))
#     age = int(input("Enter your age: "))
#     profession = str(input("Enter your profession: "))
#     about_me = input("Enter about you: ")
#     organisation = input("Enter the name of your organisation: ")
#     skills = input("Enter your skills: ")
#     details = About(name, age, profession, about_me, organisation, skills)
#     About.entry(details)
# elif option == 3:
#     delen(password)


if __name__=="__main__":
    delen(password="56e3b692-81af-4ec4-86e6-94a416d759e1")


class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(
            f"Congratulations on the new addition to the family! Meet {kwargs['name']}."
        )

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member["age"] >= 18
        return False

    def family_presentation(self):
        print(f"{self.last_name} family members:")
        for member in self.members:
            print(f"- {member['name']}")


class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] >= 18:
                    print(f"{name}'s power is {member['power']}.")
                else:
                    raise Exception(
                        f"{name} is not over 18 years old and cannot use their power."
                    )
        else:
            print(f"{name} is not a member of the family.")

    def incredible_presentation(self):
        super().family_presentation()
        print("Incredible family members:")
        for member in self.members:
            print(f"- {member['incredible_name']}, who can {member['power']}.")


members = [
    {"name": "Michael", "age": 35, "gender": "Male", "is_child": False},
    {"name": "Sarah", "age": 32, "gender": "Female", "is_child": False},
]
incredible_members = [
    {
        "name": "Michael",
        "age": 35,
        "gender": "Male",
        "is_child": False,
        "power": "fly",
        "incredible_name": "MikeFly",
    },
    {
        "name": "Sarah",
        "age": 32,
        "gender": "Female",
        "is_child": False,
        "power": "read minds",
        "incredible_name": "SuperWoman",
    },
]

fam = Family("Smith", members)
incredibles = TheIncredibles("Parr", incredible_members)

fam.family_presentation()

incredibles.incredible_presentation()

incredibles.born(
    name="Baby Jack",
    age=0,
    gender="Male",
    is_child=True,
    power="Unknown Power",
    incredible_name="Unknown",
)

incredibles.incredible_presentation()
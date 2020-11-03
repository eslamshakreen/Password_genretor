import random

ra = random


class PasswordGenerator:
    print("welcome to Eslam password generator The password can be between 1 to 20 characters")
    try:
        upper_case = int(input("how many uppercase you want: "))
        lower_case = int(input("how many lowercase you want: "))
        number = int(input("how many number you want: "))
        Special_characters = int(input("how many special characters you want: "))
    except ValueError:
        print("pleas inter a number")
        quit()

    def __init__(self):
        self.password_list = []
        self.liter = ["a", "b", "c", "d", "e",
                      "f", "g", "h", "i", "j",
                      "k", "l", "m", "n", "o",
                      "p", "q", "r", "s", "t",
                      "u", "v", "w", "x", "y",
                      "z"]
        self.special_characters_list = ['~', ':', "'", '+', '[',
                                        '@', '^', '{', '%', '(',
                                        '-', '"', '*', '|', ',',
                                        '&', '<', '`', '}', '.',
                                        '_', '=', ']', '!', '>',
                                        ';', '?', '#', '$', ')',
                                        '/']
        self.up = []
        self.pass_str = ""

    def __str__(self):
        return "Tis class generate a random password"

    def capital_liter(self):
        for c in self.liter:
            self.up.append(c.upper())

        [self.password_list.append(ra.choice(self.up)) for usless in range(PasswordGenerator.upper_case)]
        return self.password_list

    def random_number(self):
        [self.password_list.append(str(ra.randrange(0, 9))) for usless in range(PasswordGenerator.number)]
        return self.password_list

    def random_liter(self):
        [self.password_list.append(ra.choice(self.liter)) for usless in range(PasswordGenerator.lower_case)]
        return self.password_list

    def special_characters(self):

        [self.password_list.append(ra.choice(self.special_characters_list))
         for usless in range(PasswordGenerator.Special_characters)]
        return self.password_list

    def generate_password(self):
        self.capital_liter(), self.random_number(), self.random_liter(), self.special_characters()
        ra.shuffle(self.password_list)
        for password in self.password_list:
            self.pass_str += password
        if 0 < len(self.pass_str) <= 20:
            return f"your password is: {self.pass_str}"
        else:
            return "pleas inter the length of password you want"


ps = PasswordGenerator()
print(ps.generate_password())

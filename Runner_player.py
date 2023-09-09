class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __str__(self):
        return f"{self.name}___{self.speed}"


with open("runner_name.txt") as f:
    text = f.readlines()

# for name in text:
#     person = name.strip().split(" ")[0]
#     speed = name.strip().split(" ")[1]
#     # speed = int(speed)
#     person = Runner(person, speed)
#     print(name.strip().split(" "))

# print(person)

rnr_john_10 = Runner("john", 10)
rnr_jack_8 = Runner("jack", 8)
rnr_james_6 = Runner("james", 6)
rnr_oliver_9 = Runner("oliver", 9)

print(rnr_james_6)

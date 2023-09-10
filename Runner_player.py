import random
import time

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.location = 0

    def __str__(self):
        return f"{self.name}___{self.speed}"

    def step(self):
        rnd = random.uniform(0, 1)
        # rnd = random.choice([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1])
        self.location += rnd*self.speed

    def get_location(self):
        return self.location



with open("runner_name.txt") as f:
    text = f.readlines()
# runners = {}
# rnr_john_10 = Runner("john", 10)
# rnr_jack_8 = Runner("jack", 8)
# rnr_james_6 = Runner("james", 6)
# rnr_oliver_9 = Runner("oliver", 9)

# rnr_list = [rnr_john_10,rnr_jack_8,rnr_james_6,rnr_oliver_9]
runners = []

with open('runner_name.txt') as file:
    text = file.readlines()
    for line in text:
        name, speed = line.strip().split(' ')
        runners.append(Runner(name, float(speed)))


end_line = 10
winner = None



while True:
    for runner in runners:
        runner.step()
        location = runner.get_location()
        print(f"{runner.name}: {'-' * int(location)}")
        time.sleep(0.5)
        
        if location >= end_line:
            winner = runner
            break
    
    if winner:
        break


print(f"The winner is {winner.name}!")

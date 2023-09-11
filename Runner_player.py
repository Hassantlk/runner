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
        self.location += rnd*self.speed

    def get_location(self):
        return self.location

runners = []

with open('runner_name.txt') as file:
    text = file.readlines()
    for line in text:
        name, speed = line.strip().split(' ')
        runners.append(Runner(name, float(speed)))

end_line = 10
winner = None

with open('runner.log', 'w') as file:
    file.write("Starting \n")

with open('runner.log', 'a') as file:
    step=0
    while True:
        for runner in runners:
            runner.step()
            location = runner.get_location()
            print(f"{runner.name}: {'-' * int(location)}")
            file.write(f"[{step}: {runner.name}]: {runner.get_location()}\n") 
            time.sleep(0.5)

            
            if location >= end_line:
                winner = runner
                break
        step +=1
                    


        if winner:
            break




print(f"The winner is {winner.name}!")

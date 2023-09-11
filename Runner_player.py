import random
import time
import logging
import sys

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

logging.basicConfig(filename='sample.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='[%Y-%m-%d %I:%M:%S %p]')
# logging.basicConfig(handlers=[logging.FileHandler("handeler.log"),logging.StreamHandler(sys.stdout)], level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s',
#                     datefmt='[%Y-%m-%d %I:%M:%S %p]')

logging.info("Starting...")

step=0
while True:
    for runner in runners:
        runner.step()
        location = runner.get_location()
        print(f"{runner.name}: {'-' * int(location)}")
        logging.info(f"\t[{step}: {runner.name}]: {runner.get_location()}")
        time.sleep(0.5)

        if location >= end_line:
            winner = runner
            # if winner.get_location() != 10:
            #     logging.debug("it more than 10 and should be 10 -- FIXME--")
            break
    step +=1
                


    if winner:
        logging.info(f"\t\tWinner is: {runner.name} AT {runner.get_location()}")
        break




print(f"The winner is {winner.name}!")

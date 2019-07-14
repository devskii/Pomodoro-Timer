"""
Pomodoro Timer
Version 1.0

PomodoroTimer.py
Written by Spencer Michalski
July 13, 2019

A simple productivity tool based on the Pomodoro Technique.
"""

import logging, time, datetime

""" Set up logging """
LOG_FILENAME = 'PomodoroTimer.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)


""" Return a timestamp string """
def nowStr():
    return str(datetime.datetime.now())


""" Start a 25-minute Pomodoro, returning a completion status """
def startPomodoro(taskName):
    msg = nowStr() + ": Pomodoro started. Task: " + taskName
    print(msg)
    logging.debug(msg)

    # Time loop for 25 minutes
    minute = 0
    while minute < 25:
        try:
            time.sleep(60)
        except KeyboardInterrupt:
            interrupt_str = nowStr() + ": Task interrupted after " + str(minute) + " minutes. "
            print(interrupt_str)
            interrupt_reason = input("What is the reason for your interruption? ")
            log_interruption_str = interrupt_str + "Task: " + taskName + ". Interruption reason: " + interrupt_reason
            logging.debug(log_interruption_str)
            return "n"
        minute += 1
        print(str(minute) + " Minutes")
    completeStr = nowStr() + ": Pomodoro completed. Task: " + taskName
    print(completeStr)
    logging.debug(completeStr)
    accomplished = input("Did you accomplish your task? (y/n): ")
    return accomplished


print("Welcome to PomodoroTimer 1.0\n")


# Cycle through Pomodoros, continually allowing the user to work until they Ctrl-C to exit the program.
taskName = input("What is your task? ")
while True:
    taskAccomplished = startPomodoro(taskName)
    print("Get up, stretch, and take a 5 minute break!")
    sameTask = "n"
    if taskAccomplished == "y":
        accomplishedStr = "Task accomplished: " + taskName
        logging.debug(accomplishedStr)
        print("Good job!")
    else:
        sameTask = input("Would you like to continue working on this task? (y/n): ")
        if sameTask != "y":
            taskName = input("\nWhat is your next task? ")

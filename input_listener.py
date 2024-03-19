import time

import gui_display


def start(gui_display_thread):
    print("!--- INPUT LISTENER THREAD STARTED ---!")

    want_to_enter_more_coordinates = True

    time.sleep(1)

    while want_to_enter_more_coordinates:
        print("<<<Entering a new coordinate>>>")
        print("Please enter the X-Value of a new coordinate:")
        x = int(input())
        print("Please enter the y-Value of a new coordinate:")
        y = int(input())

        gui_display.add_coordinate(x, y, 'black')

        answer_valid = False
        while not answer_valid:
            print("Do you wish to enter another coordinate? (Y/N)")
            answer = input()

            if answer == "Y":
                answer_valid = True
            elif answer == "N":
                answer_valid = True
                want_to_enter_more_coordinates = False
            else:
                print("Invalid Input. Please enter Y for Yes or N for No")

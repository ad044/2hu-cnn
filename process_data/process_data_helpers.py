from collections import Counter
from random import shuffle
import cv2
import numpy as np
import os
import pandas as pd

def get_moves(data):

    forward = []
    backward = []
    left = []
    right = []
    forward_and_left = []
    forward_and_right = []
    backward_and_left = []
    backward_and_right = []
    no_input = []

    for entry in data:
        img = entry[0]
        choice = entry[1]

        if choice == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
            forward.append([img, choice])
        elif choice == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
            backward.append([img, choice])
        elif choice == [0, 0, 1, 0, 0, 0, 0, 0, 0]:
            left.append([img, choice])
        elif choice == [0, 0, 0, 1, 0, 0, 0, 0, 0]:
            right.append([img, choice])
        elif choice == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
            forward_and_left.append([img, choice])
        elif choice == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
            forward_and_right.append([img, choice])
        elif choice == [0, 0, 0, 0, 0, 0, 1, 0, 0]:
            backward_and_left.append([img, choice])
        elif choice == [0, 0, 0, 0, 0, 0, 0, 1, 0]:
            backward_and_right.append([img, choice])
        else:
            no_input.append([img, choice])

    moves = [forward, backward, left, right, forward_and_right,
             forward_and_left, backward_and_left, backward_and_right, no_input]

    return moves


def get_limit(move_list):
    move_sizes = []
    for move in move_list:
        move_sizes.append(len(move))
    return min(move_sizes)


def balance(move_list, limit):
    balanced_data = []
    for move in move_list:
        if len(move) > limit:
            move = move[:limit]
            balanced_data.append(move)
        else:
            balanced_data.append(move)
    return balanced_data

# replays the data with opencv and shows keys (for visualization)
def replay(data):
    for entry in data:
        img = entry[0]
        choice = entry[1]
        cv2.imshow('window', img)
        print(choice)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def check_val_of_data_file(starting_value):
    while True:
        file_name = './training_data-v{}.npy'.format(starting_value)

        if os.path.isfile(file_name):
            print('File exists at index', starting_value,
                  'moving to index', starting_value + 1)
            starting_value += 1
        else:
            print('Saving at index', starting_value)
            break

    return file_name

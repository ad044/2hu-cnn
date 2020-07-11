from PIL import Image
from Xlib import display, X
import cv2
import keyboard
import numpy as np
import os
import time

# getting keyboard input when gathering data

forward = [1, 0, 0, 0, 0, 0, 0, 0, 0]
backward = [0, 1, 0, 0, 0, 0, 0, 0, 0]
left = [0, 0, 1, 0, 0, 0, 0, 0, 0]
right = [0, 0, 0, 1, 0, 0, 0, 0, 0]
forward_and_left = [0, 0, 0, 0, 1, 0, 0, 0, 0]
forward_and_right = [0, 0, 0, 0, 0, 1, 0, 0, 0]
backward_and_left = [0, 0, 0, 0, 0, 0, 1, 0, 0]
backward_and_right = [0, 0, 0, 0, 0, 0, 0, 1, 0]
no_input = [0, 0, 0, 0, 0, 0, 0, 0, 1]


def check_keys():
    current = []
    try:
        if keyboard.is_pressed('p'):
            current.append('p')

        if keyboard.is_pressed('left'):
            current.append('left')
            if keyboard.is_pressed('up'):
                current.append('up')
            if keyboard.is_pressed('down'):
                current.append('down')

        elif keyboard.is_pressed('up'):
            current.append('up')
            if keyboard.is_pressed('left'):
                current.append('left')
            if keyboard.is_pressed('right'):
                current.append('right')

        elif keyboard.is_pressed('right'):
            current.append('right')
            if keyboard.is_pressed('up'):
                current.append('up')
            if keyboard.is_pressed('down'):
                current.append('down')

        elif keyboard.is_pressed('down'):
            current.append('down')
            if keyboard.is_pressed('left'):
                current.append('left')
            if keyboard.is_pressed('right'):
                current.append('right')
    except:
        pass
    return current


def keys_to_vector(keys):
    output = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if 'up' in keys and 'left' in keys:
        output = forward_and_left
    elif 'up' in keys and 'right' in keys:
        output = forward_and_right
    elif 'down' in keys and 'left' in keys:
        output = backward_and_left
    elif 'down' in keys and 'right' in keys:
        output = backward_and_right
    elif 'up' in keys:
        output = forward
    elif 'down' in keys:
        output = backward
    elif 'left' in keys:
        output = left
    elif 'right' in keys:
        output = right
    else:
        output = no_input

    return output

# image related functions


# take image and process it on X11

dsp = display.Display()
root = dsp.screen().root
# location of the window and the size of it
abs_x, abs_y, width, height = 50, 50, 575, 674


def take_and_process_img():
    raw_img = root.get_image(
        abs_x, abs_y, width, height, X.ZPixmap, 0xffffffff)
    raw_img_to_numpy = np.array(Image.frombytes(
        "RGB", (width, height), raw_img.data, "raw", "BGRX"))

    resized_img = cv2.resize(raw_img_to_numpy, (80, 94))
    final_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
    return final_img

def show_img(image):
    cv2.imshow('window', image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

# random useful functions


def countdown(seconds):
    for i in list(range(seconds))[::-1]:
        print(i + 1)
        time.sleep(1)


def check_val_of_data_file(starting_value):
    while True:
        file_name = './training_data-{}.npy'.format(starting_value)

        if os.path.isfile(file_name):
            print('File exists at index', starting_value,
                  'moving to index', starting_value + 1)
            starting_value += 1
        else:
            print('Starting at index', starting_value)
            break

    return starting_value, file_name



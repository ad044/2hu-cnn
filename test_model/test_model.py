import test_model_helpers as helpers
from keras.models import load_model
import cv2
import numpy as np
import time

MODEL_NAME = './th-xception-9-epochs-model'
model = load_model(MODEL_NAME)


def main():
    helpers.countdown(4)
    abs_x, abs_y, width, height = 50, 50, 650, 800

    resized_x = 80
    resized_y = 94

    paused = False

    while True:
        if not paused:
            screen = helpers.grab_screen(region=(abs_x, abs_y, width, height))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

            screen = cv2.resize(screen, (resized_x, resized_y))

#            cv2.imshow('window',screen)
#            if cv2.waitKey(25) & 0xFF == ord('q'):
#                cv2.destroyAllWindows()
#                break

            prediction = model.predict(screen.reshape(1, resized_x, resized_y, 3))[0]

            print(prediction)

            move_choice = np.argmax(prediction)

            if move_choice == 0:
                print('forward')
                helpers.move_forward()
            elif move_choice == 1:
                print('backward')
                helpers.move_backward()
            elif move_choice == 2:
                print('left')
                helpers.move_left()
            elif move_choice == 3:
                print('right')
                helpers.move_right()
            elif move_choice == 4:
                print('forward and left')
                helpers.move_forward_and_left()
            elif move_choice == 5:
                print('forward and right')
                helpers.move_forward_and_right()
            elif move_choice == 6:
                print('backward and left')
                helpers.move_backward_and_left()
            elif move_choice == 7:
                print('backward and right')
                helpers.move_backward_and_right()
            elif move_choice == 8:
                print('no move')
                helpers.move_no_input()

        keys = helpers.key_check()

        if 'p' in keys:
            if paused:
                paused = False
                print("Unpaused")
                time.sleep(1)
            else:
                paused = True
                print("Paused!")
                helpers.move_no_input()
                time.sleep(1)


if __name__ == "__main__":
    main()

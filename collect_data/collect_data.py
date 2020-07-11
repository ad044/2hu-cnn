import collect_data_helpers as helpers
import numpy as np
import time

starting_value, file_name = helpers.check_val_of_data_file(1)


def main(starting_value, file_name):
    data_path = './'

    training_data = []

    last_time = time.time()

    paused = False

    helpers.countdown(3)
    while True:
        if not paused:
            final_img = helpers.take_and_process_img()

            keys = helpers.check_keys()
            keys_to_vector = helpers.keys_to_vector(keys)

            training_data.append([final_img, keys_to_vector])

            print(keys)
            print('Loop took {} seconds'.format(time.time() - last_time))

            last_time = time.time()

            #helpers.show_img(final_img)

            if len(training_data) == 5000:
                np.save(file_name, training_data)
                training_data = []
                starting_value += 1
                file_name = data_path + \
                    'training_data-{}.npy'.format(starting_value)

        keys = helpers.check_keys()
        if 'p' in keys:
            if paused:
                paused = False
                print('Unpaused')
                time.sleep(1)
            else:
                print('Pausing')
                paused = True
                time.sleep(1)


if __name__ == '__main__':
    main(starting_value, file_name)

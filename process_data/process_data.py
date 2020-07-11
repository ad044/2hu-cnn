import process_data_helpers as helpers
import os
import numpy as np
from random import shuffle

data_path = '../collect_data/'

def combine_past_datasets():
    combined_data = []
    for file in os.listdir('.'):
        if file.endswith('.npy'):
            data = np.load('./' + file, allow_pickle=True)
            for entry in data:
                combined_data.append(entry)
    np.save('./combined_data-v2.npy', combined_data)

def main(path):
    final_data = []
    for file in os.listdir(data_path):
        if file.endswith('.npy'):
            train_data = np.load(data_path + file, allow_pickle=True)

            shuffle(train_data)

            move_list = helpers.get_moves(train_data)

            limit = helpers.get_limit(move_list)

            print(limit)

            # there are some stages where i don't press one key at all,
            # we ignore data like this to avoid high bias towards certain actions
            if limit == 0:
                continue
            else:
                balanced_data = helpers.balance(move_list, limit)

                summed_balanced_data = []
                for entry in balanced_data:
                    summed_balanced_data += entry

                shuffle(summed_balanced_data)

                final_data += summed_balanced_data

    shuffle(final_data)

    file_name = helpers.check_val_of_data_file(1)
    np.save(file_name, final_data)

if __name__ == "__main__":
    #main(data_path)
    combine_past_datasets()


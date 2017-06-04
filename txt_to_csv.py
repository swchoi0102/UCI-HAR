import os


def main():

    file_names = ["X_test.txt", "X_train.txt", "y_test.txt", "y_train.txt"]

    for file in file_names:
        with open(os.path.join("..", "data", file)) as f:
            lines = f.readlines()

        with open(os.path.join("..", "data", file.split(".")[0] + '.csv'), 'wb') as f:
            for line in lines:
                f.write(','.join(line.split()) + "\n")

if __name__ == "__main__":
    main()
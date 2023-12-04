import pathlib
import csv

CONFIG_DIR_NAME="config"
TEST_DATA_FILE_NAME="test-data.csv"

TEST_DATA_FILE=pathlib.Path(__file__).resolve().parent.parent.joinpath(CONFIG_DIR_NAME).joinpath(TEST_DATA_FILE_NAME)
def read_data():
    with open(TEST_DATA_FILE) as file:
        reader=csv.reader(file)
        # skipping header
        # next(reader)
        return [tuple(row) for row in reader]

read_data()
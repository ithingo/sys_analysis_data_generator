import sys
import csv
import random

DEFAULT_FILENAME = 'data.txt'
PARAMS_DELIMITER = ":"
VALUES_DELIMITER = ","

COUNT_KEY = 'PEOPLE'


def run():
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = DEFAULT_FILENAME
    finally:
        process_file(file_name)


def process_file(file_name=DEFAULT_FILENAME):
    with open(file_name, "r") as file:
        if file.mode == "r":
            content = file.readlines()
            params = {}
            for line in content:
                params_setter(line.strip(), params)
            result = generate_data(params)

            generate_csv(result, params.keys())


def params_setter(params_line: str, result):
    params = params_line.split(PARAMS_DELIMITER)
    value = params[1].split(VALUES_DELIMITER)

    if isinstance(value, list) and len(value) == 1:
        value = value[0]
    else:
        value = list(map(strip_param, value))
    result[params[0].strip().upper()] = value


def generate_data(params):
    iterations = int(params[COUNT_KEY])
    del params[COUNT_KEY]

    data_string_array = []

    for x in range(0, iterations):
        result = []

        for key, value in params.items():
            if key == COUNT_KEY:
                del params[key]
            if isinstance(value, list):
                result.append(random.choice(value))
            else:
                result += value
        data_string_array.append(result)
    return data_string_array


def generate_csv(generated_data, header_keys):
    with open('output.csv', "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header_keys)
        line_count = 1

        for line in generated_data:
            writer.writerow(line)
            line_count += 1
        print("processed {0} lines".format(line_count))


def strip_param(param: str): return param.strip()


if __name__ == "__main__":
    run()
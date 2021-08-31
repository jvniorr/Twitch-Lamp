import ast

filename = 'data.txt'


def read_file():
    with open(filename) as f:
        d = f.read()
    data = ast.literal_eval(d)
    return data


def dictionary_with_back():
    dic = read_file()
    dic['Back'] = 'back'
    return dic


def write_file(dictionary):
    with open(filename, 'w') as data:
        data.write(str(dictionary))


def delete_element(streamer):
    data = read_file()
    del data[streamer]
    write_file(data)


def add_element(streamer, color):
    data = read_file()
    data[streamer] = color
    write_file(data)


def dict_keys_to_list():
    dic = read_file()
    keys = list(dic.keys())
    return keys

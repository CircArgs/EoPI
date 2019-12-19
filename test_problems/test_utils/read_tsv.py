"""ensure you only use this if you know your test data does not consist of anything malicious"""


from dataclasses import dataclass


def __interpret(s: str) -> object:
    try:
        return eval(s)
    except:
        return s


def read_tsv(path: str, schema):
    """
    Description: 
        utility for reading testing data from a tsv

    Args:
        path: os path to tsv to read
        schema (dataclass): a class of python 3.7+ @dataclass defining the structure of a line of tab separated data
    

    """
    with open(path) as file:
        data = file.read()
    data = data.split("\n")
    data = [row for row in data if row]
    ret = [None] * len(data)
    for line_number, line in enumerate(data):
        cols = line.split("\t")
        cols = [__interpret(c) for c in cols]
        ret[line_number] = schema(*cols)
    return ret

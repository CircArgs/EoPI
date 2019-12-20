"""ensure you only use this if you know your test data does not consist of anything malicious"""


from dataclasses import dataclass
import os


def __interpret(s: str) -> object:
    try:
        return eval(s)
    except:
        return s


def read_tsv(tsv: str, schema):
    """
    Description: 
        utility for reading testing data from a tsv

    Args:
        tsv: name of test data tsv i.e. 4_1.tsv
        schema (dataclass): a class of python 3.7+ @dataclass defining the structure of a line of tab separated data
    

    """

    with open(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "test_data",
            tsv,
        )
    ) as file:
        data = file.read()
    data = data.split("\n")
    data = [row for row in data if row]
    ret = [None] * len(data)
    for line_number, line in enumerate(data):
        cols = line.split("\t")
        cols = [__interpret(c) for c in cols]
        ret[line_number] = schema(*cols)
    return ret

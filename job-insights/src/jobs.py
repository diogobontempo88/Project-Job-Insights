from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        list = [row for row in csv.DictReader(file)]
    return list

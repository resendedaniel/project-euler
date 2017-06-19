import pandas as pd
import os
import urllib


def get_file(file):
    if not os.path.isfile('data/' + file):
        files = {
            'p022_names.txt': 'https://projecteuler.net/project/resources/p022_names.txt'
        }

        downloaded_file = urllib.URLopener()
        downloaded_file.retrieve(files[file], 'data/' + file)

    data = open('data/' + file).read()
    data = data.replace('"', '')
    data = data.split(',')
    return data

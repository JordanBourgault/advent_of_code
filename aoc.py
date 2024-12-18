import argparse
import os
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-y', '--year', help='Specify year to fetch', type=int)
parser.add_argument('-d', '--day', help='Specify day to fetch', type=int)
args = parser.parse_args()
session = open('session').read()


_, top_level_dirs, _ = next(os.walk('./'))
years = sorted([int(year) for year in top_level_dirs if year.isnumeric()])
year_to_process = args.year or years[-1]
if not year_to_process in years:
    os.mkdir(year_to_process)
os.chdir(f'./{year_to_process}')


_, days_dirs, _ = next(os.walk(f'./'))
days = sorted([int(day[3:]) for day in days_dirs if day[:3] == 'day'])
if days[-1] >= 24:
    raise Exception('AoC is finished for the specified year :(')
day_to_process = (args.day or days[-1]) + 1
os.mkdir(f'./day{day_to_process}')
os.chdir(f'./day{day_to_process}')

with open(f'day{day_to_process}.py', 'w') as f:
    str_to_write = f'with open("{year_to_process}/day{day_to_process}/input.txt") as f:\n    pass'
    f.write(str_to_write)


with open('input.txt', 'w') as f:
    res = requests.get(f'https://adventofcode.com/{year_to_process}/day/{day_to_process}/input', cookies={'session': session})
    f.write(res.content.decode())

with open('input_test.txt', 'w') as f:
    pass

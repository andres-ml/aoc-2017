import sys
import subprocess

if len(sys.argv) < 3 :
    print('Usage: python3 solve.py <day> <part> [path/to/input.txt]')
    print('Input file defaults to input.txt file inside that day\'s folder')
    exit(0)

day = sys.argv[1]
part = sys.argv[2]
filename = './day{day}/input.txt'.format(day=day) if len(sys.argv) == 3 else sys.argv[3]

subprocess.call("python3 ./day{day}/main-{part}.py < {filename}".format(day=day, part=part, filename=filename), shell=True)

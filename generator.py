import sys
import os
import shutil

argv = sys.argv

# -----------------------------------------------------
# CONSTANTS
# -----------------------------------------------------
CONTESTS = {
    'ABC': 'beginner-contest',
}
ABS_FILE = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_FILE)
USAGE = 'USAGE: python {} contest-name contest-num'.format(argv[0])
FILES = {
    'A.py': '',
    'B.py': '',
    'C.py': '',
    'D.py': '',
    'README.md': '',
}
FILES['README.md'] = '''# AtCoder Beginner Contest {contest_num}

## A

TODO: not implemeted

## B

TODO: not implemented

## C

TODO: not implemented

## D

TODO:notimplemented
'''


# -----------------------------------------------------
# VALIDATE ARGUMENTS
# -----------------------------------------------------
if len(argv) != 3:
    print(USAGE)
    sys.exit(1)

contest = argv[1].upper()
if contest not in CONTESTS:
    print(USAGE)
    print('invalid contest name. belows are allowed:')
    for contest_name in CONTESTS:
        print('\t- {}'.format(contest_name))
    sys.exit(1)

# -----------------------------------------------------
# MAIN LOGIC
# -----------------------------------------------------

# create contest dir if not exists
contest_dir = os.path.join(BASE_DIR, CONTESTS[contest])
if not os.path.exists(contest_dir):
    os.mkdir(contest_dir)

# create contest-num dir if not exists
try:
    contest_num = argv[2]
    contest_num_dir = os.path.join(contest_dir, contest_num)
    if not os.path.exists(contest_num_dir):
        os.mkdir(contest_num_dir)
except Exception as e:
    print('cannot create {}'.format(contest_num_dir))
    print(e)
    try:
        shutil.rmtree(contest_dir)
    except:
        pass
    sys.exit(1)


# correct contents of README.md
FILES['README.md'] = FILES['README.md'].format(contest_num=contest_num)

# create files if not exists
try:
    for filename, content in FILES.items():
        filepath = os.path.join(contest_num_dir, filename)
        if os.path.exists(filepath):
            print('{} exists, so skip it.'.format(filepath))
            continue
        with open(filepath, 'w') as f:
            f.write(content)
        print('{} is created.'.format(filepath))
except Exception as e:
    print('cannot create {}'.format(filename))
    print(e)
    try:
        shutil.rmtree(contest_dir)
    except:
        pass
    sys.exit(1)

print('successfully created.')

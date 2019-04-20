#! /usr/bin/env python3
import sys
import os
import shutil

argv = sys.argv

# -----------------------------------------------------
# CONSTANTS
# -----------------------------------------------------

# common variables
ABS_FILE = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_FILE)
LANGUAGES = {
    'python': {
        'extension': 'py',
    },
}

# AtCoder's perticular variables
CONTESTS = {
    'ABC': {
        'dirname': 'beginner',
        'files': ['A', 'B', 'C', 'D'],
        'contest_name': 'AtCoder Beginner Contest',
    },
    'AGC': {
        'dirname': 'grand',
        'files': ['A', 'B', 'C', 'D', 'E', 'F'],
        'contest_name': 'AtCoder Grand Contest',
    },
    'S8P': {
        'dirname': 's8p',
        'files': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        'contest_name': 'square869120Contest',
    },
    'T1': {
        'dirname': 'tenka1',
        'files': ['A', 'B', 'C', 'D', 'E', 'F'],
        'contest_name': 'Tenka1 Programing Contest',
    }
}
README_TEMPLATE = '''# {contest_name} {contest_num}

{contents}
'''
PROBLEM = '''## {problem}

TODO: not implemented
'''

# error messages
USAGE = 'USAGE: python {} contest-name contest-num [language]'.format(argv[0])
INVALID_CONTEST_NAME = ''''{contest_name}' is invalid contest name. belows are allowed:
{allowed_contests}
'''.format(
    contest_name='{contest_name}',
    allowed_contests='\n'.join(map(lambda x: '\t- ' + x, CONTESTS))
)
INVALID_LANGUAGE = ''''{language_name}' is invalid language name. belows are allowed:
{allowed_languages}
'''.format(
    language_name='{language_name}',
    allowed_languages=' '.join(map(lambda x: '\t- ' + x, LANGUAGES))
)


# -----------------------------------------------------
# VALIDATE ARGUMENTS
# -----------------------------------------------------
if len(argv) < 3:
    print(USAGE)
    sys.exit(1)

# argv[1] is contest name
contest_name = argv[1].upper()
if contest_name not in CONTESTS:
    print(USAGE)
    print(INVALID_CONTEST_NAME.format(contest_name=contest_name))
    sys.exit(1)

# argv[2] is contest number
contest_num = argv[2]

# argv[3] is used language. this is OPTIONAL
if len(argv) == 4:
    language_name = argv[3].lower()
    if language_name not in LANGUAGES:
        print(INVALID_LANGUAGE.format(language_name=language_name))
        sys.exit(1)

    language = LANGUAGES[language_name]
else:
    language = LANGUAGES['python']


# -----------------------------------------------------
# MAIN LOGIC
# -----------------------------------------------------

contest_info = CONTESTS[contest_name]

# create contest dir if not exists
contest_dir = os.path.join(BASE_DIR, contest_info['dirname'])
if not os.path.exists(contest_dir):
    os.mkdir(contest_dir)

# create contest-num dir if not exists
try:
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
readme = README_TEMPLATE.format(
    contest_name=contest_info['contest_name'],
    contest_num=contest_num,
    contents='\n'.join(
        map(lambda x: PROBLEM.format(problem=x), contest_info['files']))
)


def write_files_if_not_exists(dirname: str, filename: str, content: str = ''):
    '''指定されたディレクトリ直下に `filename` が存在しない時に限り、指定された内容のファイルを作成します。
    :param dirname: ディレクトリ
    :param filename: ファイル名
    :param content: ファイルの内容
    '''
    filepath = os.path.join(dirname, filename)
    if os.path.exists(filepath):
        print('{} exists, so skip it.'.format(filepath))
        return

    with open(filepath, 'w') as f:
        f.write(content)
    print('{} is successfully created.'.format(filepath))


# create files if not exists
try:
    # problem files
    for filename in contest_info['files']:
        write_files_if_not_exists(
            contest_num_dir, filename + '.' + language['extension'])

    # README.md
    write_files_if_not_exists(
        contest_num_dir, 'README.md', readme)
except Exception as e:
    print('cannot create {}'.format(filename))
    print(e)
    try:
        shutil.rmtree(contest_dir)
    except:
        pass
    sys.exit(1)

print('successfully created.')

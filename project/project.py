import argparse
from create import create
from edit import edit
from finish import finish


def main():
    # Accept argument of mode with 3 options:
    parser = argparse.ArgumentParser(description='Process one of three arguments')
    parser.add_argument('-m', '--mode', help='Select one of three modes: create, edit or finish', type=str)
    args = parser.parse_args()

    if is_create(args.mode):
        create()
    elif is_edit(args.mode):
        edit()
    elif is_finish(args.mode):
        finish()
    else:
        print('Not supported option. Select one of three modes: create, edit or finish.')


def is_create(mode):
    return mode == 'create'


def is_edit(mode):
    return mode == 'edit'


def is_finish(mode):
    return mode == 'finish'


if __name__ == '__main__':
    main()

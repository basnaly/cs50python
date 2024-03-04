import argparse

from create import create
from edit import edit
from finish import finish


def main():
    # Create cli, that include mode and 3 options:
    parser = argparse.ArgumentParser(description='Process one of three arguments')
    parser.add_argument('-m', '--mode', help='Select one of three modes: create, edit or finish', type=str)
    args = parser.parse_args()

    if args.mode == 'create':
        create()
    elif args.mode == 'edit':
        edit()
    elif args.mode == 'finish':
        finish()
    else:
        print('Not supported option. Select one of three modes: create, edit or finish.')


main()

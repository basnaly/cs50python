import argparse

from create import create


def main():
    parser = argparse.ArgumentParser(description='Process one of three arguments')
    parser.add_argument('-m', '--mode', help='Select one of three modes: create, edit or finish', type=str)
    args = parser.parse_args()

    if args.mode == 'create':
        create()
    elif args.mode == 'edit':
        print('Edit')
    elif args.mode == 'finish':
        print('Finish')
    else:
        print('Not supported option. Select one of three modes: create, edit or finish.')


# if __name__ == '__main__':
main()

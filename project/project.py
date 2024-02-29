import argparse


def main():
    parser = argparse.ArgumentParser(description="Procee one of three")
    parser.add_argument('-m', '--mode', help="number of times to meow", type=str)
    args = parser.parse_args()




if __name__ == '__main__':
    main()

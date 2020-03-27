import argparse


def main(number: int, distance: int):
    print(number, distance)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", dest="number", type=int)
    parser.add_argument("-s", dest="distance", type=int)
    args = parser.parse_args()
    args_number = args.number
    args_distance = args.distance
    if args_number is None or args_distance is None:
        print("use --help")
    else:
        main(args_number, args_distance)

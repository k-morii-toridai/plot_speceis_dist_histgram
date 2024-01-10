import argparse

parser = argparse.ArgumentParser(description='This script takes two arguments: arg1 and arg2.',
                                 usage='%(prog)s <arg1> <arg2> \
                                 \nexample: python3 %(prog)s NH_dist_1d_list.npy 5')
parser.add_argument('arg1', help='npy_file_name')
parser.add_argument('arg2', help='figsize')
args = parser.parse_args()
print(args.arg1)
print(args.arg2)

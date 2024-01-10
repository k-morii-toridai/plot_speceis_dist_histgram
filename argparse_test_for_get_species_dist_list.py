import argparse

parser = argparse.ArgumentParser(description='This script takes two arguments: arg1, arg2 and arg3.',
                                 usage='%(prog)s <arg1> <arg2> <arg3> \
                                 \nexample: python3 %(prog)s P H P_H_existed_poscar_folder_path_list.npy')

parser.add_argument('arg1', help='central_atom_symbol')
parser.add_argument('arg2', help='neighboring_atom_symbol')
parser.add_argument('arg3', help='npy_file_name')

args = parser.parse_args()

print(args.arg1)
print(args.arg2)
print(args.arg3)

import argparse
import itertools
from multiprocessing import Pool, cpu_count

import numpy as np
from tqdm import tqdm

from package_file_conversion.nnlist2df import nnlist2df


def flatten_func(list_2dim):
    return list(itertools.chain.from_iterable(list_2dim))


def get_CO_bond_dist_list(nnlist_path='sample_test_files/POSCAR.nnlist'):
    df_nnlist = nnlist2df(nnlist_path)
    df_nnlist_C_O = df_nnlist[df_nnlist.apply(lambda row: (row['central_atom_symbol'] == central_atom_symbol) and (row['neighboring_atom_symbol'] == neighboring_atom_symbol), axis=1)]
    CO_bond_dist_list = df_nnlist_C_O['rel_distance'].tolist()
    return CO_bond_dist_list


# コマンドライン引数を受け取る
parser = argparse.ArgumentParser(description='This script takes two arguments: arg1, arg2 and arg3.',
                                 usage='%(prog)s <arg1> <arg2> <arg3> \
                                 \nexample: python3 %(prog)s P H P_H_existed_poscar_folder_path_list.npy')
parser.add_argument('arg1', help='central_atom_symbol')
parser.add_argument('arg2', help='neighboring_atom_symbol')
parser.add_argument('arg3', help='npy_file_name')
args = parser.parse_args()
central_atom_symbol = args.arg1
neighboring_atom_symbol = args.arg2
# print(f"type(args.arg1): {type(args.arg1)}", f"args.arg1: {args.arg1}")
# print(f"type(args.arg2): {type(args.arg2)}", f"args.arg2: {args.arg2}")

# 元素種C, Oを含むPOSCARファイルパスリストをload
C_O_existed_poscar_folder_path_list = np.load(f'../get_some_speceis_existed_poscar_path_list/{args.arg3}', allow_pickle=True)
# CO結合間距離を抽出したいnnlist_5/POSCAR.nnlistのパスリストを作成
C_O_existed_nnlist_5_path_list = [str(folder_p) + '/nnlist_5/POSCAR.nnlist' for folder_p in C_O_existed_poscar_folder_path_list]

# 並列化して処理
try:
    p = Pool(cpu_count() - 1)
    CO_bond_dist_2d_list = list(tqdm(p.imap(get_CO_bond_dist_list, C_O_existed_nnlist_5_path_list), total=len(C_O_existed_nnlist_5_path_list)))
    # flatten
    CO_bond_dist_1d_list = flatten_func(CO_bond_dist_2d_list)
finally:
    p.close()
    p.join()

# 抽出したCO結合間距離の1Dリストをを.npy形式で保存
np.save(f'{args.arg1}_{args.arg2}_dist_1d_list.npy', np.array(CO_bond_dist_1d_list))

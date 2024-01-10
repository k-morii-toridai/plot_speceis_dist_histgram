import os
import sys
import argparse

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


elements = {
    "H": "Hydrogen",
    "Li": "Lithium",
    "Be": "Beryllium",
    "B": "Boron",
    "C": "Carbon",
    "N": "Nitrogen",
    "O": "Oxygen",
    "F": "Fluorine",
    "Na": "Sodium",
    "Mg": "Magnesium",
    "Al": "Aluminium",
    "Si": "Silicon",
    "P": "Phosphorus",
    "S": "Sulfur",
    "Cl": "Chlorine",
    "K": "Potassium",
    "Ca": "Calcium",
    "Sc": "Scandium",
    "Ti": "Titanium",
    "V": "Vanadium",
    "Cr": "Chromium",
    "Mn": "Manganese",
    "Fe": "Iron",
    "Co": "Cobalt",
    "Ni": "Nickel",
    "Cu": "Copper",
    "Zn": "Zinc",
    "Ga": "Gallium",
    "Ge": "Germanium",
    "As": "Arsenic",
    "Se": "Selenium",
    "Br": "Bromine",
    "Rb": "Rubidium",
    "Sr": "Strontium",
    "Y": "Yttrium",
    "Zr": "Zirconium",
    "Nb": "Niobium",
    "Mo": "Molybdenum",
    "Tc": "Technetium",
    "Ru": "Ruthenium",
    "Rh": "Rhodium",
    "Pd": "Palladium",
    "Ag": "Silver",
    "Cd": "Cadmium",
    "In": "Indium",
    "Sn": "Tin",
    "Sb": "Antimony",
    "Te": "Tellurium",
    "I": "Iodine",
}


def mk_fig_histgram(array, figsize, xmax):
    """
    This func() makes a figure of histgram about distance between some species.
    
    Usage:
    ------
    mk_fig_histgram(some_speceis_dist_1d_list_loaded, figsize=5, xmax=2.0)
    
    Parameters:
    -----------
    array: ndarray 
    figsize: int or float
    xmax: int or float
    
    Outputs:
    --------
    figures: .png(dpi=100, 200, 300), .eps, .pdf
    """
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(figsize, figsize))
    sns.histplot(array[array <= xmax], 
                 ax=axes, 
                 label=f'{elements[central_atom_symbol]}-{elements[neighboring_atom_symbol]} distance',
                 color='lightgray', 
                 # alpha=0.4,
                 edgecolor=None,)
    # タイトルの設定
    if figsize == 5:
        fontsize = 10
    if figsize == 6:
        fontsize = 12
    axes.set_title(f'Histgram of distances between {elements[central_atom_symbol]} and {elements[neighboring_atom_symbol]} under {xmax}Å',
                   y=1.05, 
                   fontsize=fontsize,)
    # 軸ラベルの設定
    axes.set_xlabel('Distance(Å)', fontsize=15)
    axes.set_ylabel('Count', fontsize=15)
    axes.xaxis.set_label_coords(0.5, -0.08)  # x軸ラベルの位置を調整
    axes.yaxis.set_label_coords(-0.11, 0.5)  # y軸ラベルの位置を調整
    # x軸の範囲設定
    axes.set_xlim(right=xmax)
    # y軸を指数表示
    axes.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))
    # 凡例の設定
    axes.legend(loc='upper left',bbox_to_anchor=(0.01, 0.99))  # 凡例を表示
    # save
    f_name = f'figure/{central_atom_symbol}{neighboring_atom_symbol}/under{xmax}/size_{figsize}_{figsize}/'
    None if os.path.exists(f_name) else os.makedirs(f_name)
    # fig.savefig(f'{f_name}/Histgram_of_carbon-oxygen_bond_distances', format='png')
    fig.savefig(f'{f_name}/Histgram_of_{elements[central_atom_symbol]}-{elements[neighboring_atom_symbol]}_bond_distances_under{xmax}_300dpi_s{figsize}.png', dpi=300)
    fig.savefig(f'{f_name}/Histgram_of_{elements[central_atom_symbol]}-{elements[neighboring_atom_symbol]}_bond_distances_under{xmax}_200dpi_s{figsize}.png', dpi=200)
    fig.savefig(f'{f_name}/Histgram_of_{elements[central_atom_symbol]}-{elements[neighboring_atom_symbol]}_bond_distances_under{xmax}_100dpi_s{figsize}.png', dpi=100)
    # fig.savefig(f'{f_name}/Histgram_of_carbon-oxygen_bond_distances', format='pdf')
    fig.savefig(f'{f_name}/Histgram_of_{elements[central_atom_symbol]}-{elements[neighboring_atom_symbol]}_bond_distances_under{xmax}_s{figsize}.pdf')
    # .eps形式で保存
    fig.savefig(f'{f_name}/Histgram_of_{elements[central_atom_symbol]}-{elements[neighboring_atom_symbol]}_bond_distances_under{xmax}_s{figsize}.eps')
    # show
    plt.show()


# 直書き
npy_file_name = 'PH_dist_1d_list.npy'
central_atom_symbol = npy_file_name[0]
neighboring_atom_symbol = npy_file_name[1]

some_speceis_dist_1d_list_loaded = np.load(npy_file_name, allow_pickle=True)


# コマンドライン引数として受け取る
parser = argparse.ArgumentParser(description='This script takes two arguments: arg1, arg2 and arg3.',
                                 usage='%(prog)s <arg1> <arg2> <arg3> \
                                 \nexample: python3 %(prog)s NH_dist_1d_list.npy 5 2.0')
parser.add_argument('arg1', help='npy_file_name')
parser.add_argument('arg2', help='figsize')
parser.add_argument('arg3', help='xmax')
args = parser.parse_args()

npy_file_name = args.arg1
figsize = args.arg2
xmax = args.arg3
central_atom_symbol = npy_file_name.split('_')[0]
neighboring_atom_symbol = npy_file_name.split('_')[1]
print(f"central_atom_symbol: {central_atom_symbol}")
print(f"neighboring_atom_symbol: {neighboring_atom_symbol}")


some_speceis_dist_1d_list_loaded = np.load(npy_file_name, allow_pickle=True)
mk_fig_histgram(some_speceis_dist_1d_list_loaded, figsize=figsize, xmax=xmax)

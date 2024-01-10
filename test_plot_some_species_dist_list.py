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


def mk_fig_histgram(array, figsize=6):

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(figsize, figsize))
    sns.histplot(array, 
                 ax=axes, 
                 label=f'{elements[central_atom_symbol]}-{elements[neighboring_atom_symbol]} distance',
                 color='lightgray', 
                 # alpha=0.4,
                 edgecolor=None,)
    # タイトルの設定
    if figsize == 5:
        fontsize = 11
    if figsize == 6:
        fontsize = 15
    axes.set_title(f'Histgram of distances between {elements[central_atom_symbol]} and {elements[neighboring_atom_symbol]}',
                   y=1.05, 
                   fontsize=fontsize,)
    # 軸ラベルの設定
    axes.set_xlabel('Distance(Å)', fontsize=15)
    axes.set_ylabel('Count', fontsize=15)
    axes.xaxis.set_label_coords(0.5, -0.08)  # x軸ラベルの位置を調整
    axes.yaxis.set_label_coords(-0.11, 0.5)  # y軸ラベルの位置を調整
    # x軸の範囲設定
    axes.set_xlim(right=5)
    # y軸を指数表示
    axes.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))
    # 凡例の設定
    axes.legend(loc='upper left',bbox_to_anchor=(0.01, 0.99))  # 凡例を表示
    # save
    f_name = f'figure/{central_atom_symbol}{neighboring_atom_symbol}/under500pm/size_{figsize}_{figsize}/'
    None if os.path.exists(f_name) else os.makedirs(f_name)
    # fig.savefig(f'{f_name}/Histgram_of_carbon-oxygen_bond_distances', format='png')
    fig.savefig(f'{f_name}/Histgram_of_{elements[central_atom_symbol]}-{elements[neighboring_atom_symbol]}_bond_distances_300dpi_s{figsize}.png', dpi=300)
    fig.savefig(f'{f_name}/Histgram_of_{elements[central_atom_symbol]}-{elements[neighboring_atom_symbol]}_bond_distances_200dpi_s{figsize}.png', dpi=200)
    fig.savefig(f'{f_name}/Histgram_of_{elements[central_atom_symbol]}-{elements[neighboring_atom_symbol]}_bond_distances_100dpi_s{figsize}.png', dpi=100)
    # fig.savefig(f'{f_name}/Histgram_of_carbon-oxygen_bond_distances', format='pdf')
    fig.savefig(f'{f_name}/Histgram_of_{elements[central_atom_symbol]}-{elements[neighboring_atom_symbol]}_bond_distances_s{figsize}.pdf')
    # .eps形式で保存
    fig.savefig(f'{f_name}/Histgram_of_{elements[central_atom_symbol]}-{elements[neighboring_atom_symbol]}_bond_distances_s{figsize}.eps')


parser = argparse.ArgumentParser(description='This script takes two arguments: arg1 and arg2.',
                                 usage='%(prog)s <arg1> <arg2> \
                                 \nexample: python3 %(prog)s NH_dist_1d_list.npy 5')
parser.add_argument('arg1', help='npy_file_name')
parser.add_argument('arg2', help='figsize')
args = parser.parse_args()
npy_file_name = args.arg1
figsize = args.arg2
central_atom_symbol = npy_file_name[0]
neighboring_atom_symbol = npy_file_name[1]
print(f"central_atom_symbol: {central_atom_symbol}")
print(f"neighboring_atom_symbol: {neighboring_atom_symbol}")


# npy_file_name = 'PH_dist_1d_list.npy'
# central_atom_symbol = npy_file_name[0]
# neighboring_atom_symbol = npy_file_name[1]


# make a histgram of CO-bond distances under 5Å
CO_bond_dist_1d_list_loaded = np.load(npy_file_name, allow_pickle=True)
mk_fig_histgram(array=CO_bond_dist_1d_list_loaded, figsize=figsize)
print(f"A histgram of CO-bond distances under 5Å was made \n\
and saved at figure/under500pm/size_{figsize}_{figsize}/")

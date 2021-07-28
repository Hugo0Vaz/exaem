#==============================================================================#
#   _____  ____ _  ___ _ __ ___
# _/ _ \ \/ / _` |/ _ \ '_ ` _ \     seleciona quais coloboradores podem ter
# |  __/>  < (_| |  __/ | | | | |    os email removidos e feito backup.
#  \___/_/\_\__,_|\___|_| |_| |_|
#
# Autor: Hugo Vaz - hugo.martins@kot.com.br
#==============================================================================#

import re

# arquivos de entrada dos emails
ea_file = './emails_ativos.txt'
a_file = './colaboradores_ativos.txt'
ex_file = './emails_exececoes.txt'
b_file = './backup_realizado.txt'
o_file = './output.txt'


def load_list(input_file):

    input_set = set()

    with open(input_file, 'r') as file:
        for line in file:
            line = re.sub(' +', '', line)
            input_set.add(line)

    return input_set


def dump_list(output_set):

    with open(o_file, 'w') as file:

        for item in output_set:
            print(item)
            file.write(item)


if __name__ == '__main__':

    ea_set = load_list(ea_file)
    a_set = load_list(a_file)
    ex_set = load_list(ex_file)
    b_set = load_list(b_file)

    o_set = set()

    for i in ea_set:
        if i not in a_set and i not in ex_set and i not in b_set:
            o_set.add(i)

    dump_list(o_set)

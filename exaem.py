#==============================================================================#
#   _____  ____ _  ___ _ __ ___
# _/ _ \ \/ / _` |/ _ \ '_ ` _ \     seleciona emails que estão disponíveis
# |  __/>  < (_| |  __/ | | | | |    para backup e exclusão.
#  \___/_/\_\__,_|\___|_| |_| |_|
#     EXclude Available EMails
#
# Autor: Hugo Vaz - hugo.martins@kot.com.br
#==============================================================================#

import re
import pandas as pd

def rm_nan(input_list):
    a = []
    for i in input_list:
        if type(i) != float:
            a.append(i)
    return a

def rm_space(input_list):
    a = []
    for i in input_list:
        a.append(re.sub(' +', '', i))

    return a

def get_data(input_file):
    
    data = pd.read_csv(input_file)
    
    colab_ativos = data['Colaboradores Ativos'].tolist()
    colab_desl = data['Colaboradores Desligados'].tolist()
    email_ativos = data['Emails Ativos Task'].tolist()
    emails_exc = data['Emails Exceções'].tolist()
    backup = data['Backup Realizados'].tolist()

    colab_ativos = rm_nan(colab_ativos)
    colab_desl = rm_nan(colab_desl)
    email_ativos = rm_nan(email_ativos)
    emails_exc = rm_nan(emails_exc)
    backup = rm_nan(backup)
   
    colab_ativos = rm_space(colab_ativos)
    colab_desl = rm_space(colab_desl)
    email_ativos = rm_space(email_ativos)
    emails_exc = rm_space(emails_exc)
    backup = rm_space(backup)

    return colab_ativos, colab_desl, email_ativos, emails_exc, backup
   
def dump_list(output_list, output_file):
    with open(output_file, 'w') as file:

        for item in output_list:
            file.write(item+'\n')


if __name__ == '__main__':

    a_set, d_set, ea_set, ex_set, b_set = get_data('./Controle Backup Emails.csv')
    
    o_set = set()

    for i in ea_set:
        if i not in a_set and i not in ex_set and i not in b_set:
            o_set.add(i)

    dump_list(o_set, 'backupTODO.txt')

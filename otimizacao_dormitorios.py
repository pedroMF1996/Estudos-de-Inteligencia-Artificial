# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:51:00 2019

@author: PEDROMARTINSFALLEIRO
"""

import otimizacao_voos as ov

dormitorios = ['São Paulo', 'Flamengo', 'Coritiba', 'Cruzeiro', 'Fortaleza']

preferencias=[('Amanda',    ('Cruzeiro', 'Coritiba')),
              ('Pedro',     ('São Paulo', 'Fortaleza')),
              ('Marcos',    ('Flamengo', 'São Paulo')),
              ('Priscila',  ('São Paulo', 'Fortaleza')),
              ('Jessica',   ('Flamengo', 'Cruzeiro')), 
              ('Paulo',     ('Coritiba', 'Fortaleza')), 
              ('Fred',      ('Fortaleza', 'Flamengo')), 
              ('Suzana',    ('Cruzeiro', 'Coritiba')), 
              ('Laura',     ('Cruzeiro', 'Coritiba')), 
              ('Ricardo',   ('Coritiba', 'Flamengo'))]

# [1, 0, 2, 0, 0, 0]
# (0,9), (0,8), (0,7)...(0,0)
dominio = [(0, (len(dormitorios) * 2) - i - 1) for i in range(0, len(dormitorios) * 2)] 

def imprimir_solucao(solucao):
    vagas = []
    for i in range(len(dormitorios)):
        vagas += [i, i]
    for i in range(len(solucao)):
        atual = solucao[i]
        dormitorio = dormitorios[vagas[atual]]
        print(preferencias[i][0], dormitorio)
        del vagas[atual]
      
imprimir_solucao([6,1,2,1,2,0,2,2,0,0])


def Funcao_Custo(solucao):
    custo = 0
    vagas = [0,0,1,1,2,2,3,3,4,4]
    for i in range(len(solucao)):
        atual = solucao[i]
        dormitorio = dormitorios[vagas[atual]]
        preferencia = preferencias[i][1]
        if preferencia[0] == dormitorio:
            custo = custo + 0
        elif preferencia[1] == dormitorio:
            custo = custo + 1
        else:
            custo = custo + 3
        del vagas[atual]
    return custo

Funcao_Custo([6,1,2,1,2,0,2,2,0,0])

solucao_randomica = ov.pesqisa_randomica(dominio, Funcao_Custo)
custo_randomica = Funcao_Custo(solucao_randomica)
imprimir_solucao(solucao_randomica)
print('\n\n')

solucao_subida_encosta = ov.subida_encosta(dominio, Funcao_Custo)
custo_subida_encosta = Funcao_Custo(solucao_subida_encosta)
imprimir_solucao(solucao_subida_encosta)  
print('\n\n')

solucao_tempera = ov.Tempera_Simulada(dominio, Funcao_Custo)
custo_tempera = Funcao_Custo(solucao_tempera)
imprimir_solucao(solucao_tempera) 
print('\n\n')

solucao_genetico = ov.genetico(dominio, Funcao_Custo)
custo_genetico = Funcao_Custo(solucao_genetico)
imprimir_solucao(solucao_genetico)     

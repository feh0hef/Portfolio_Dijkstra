import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path

dir = r'C:\Users\fehhe\OneDrive\Área de Trabalho\study\Projeto CR' #Diretorio
vertices_temp = pd.read_excel(os.path.join(dir, 'Arestas Portfólios.xlsx')) #VERTICES.xlsx
arestas_temp1 = pd.read_excel(os.path.join(dir, 'Vertices Portfólios.xlsx'), sheet_name=0) #ARESTAS CR.xlsx
arestas_temp2 = pd.read_excel(os.path.join(dir, 'Vertices Portfólios.xlsx'), sheet_name=1)
arestas_temp3 = pd.read_excel(os.path.join(dir, 'Vertices Portfólios.xlsx'), sheet_name=2)
arestas_temp4 = pd.read_excel(os.path.join(dir, 'Vertices Portfólios.xlsx'), sheet_name=3)

arestas_temp1 = arestas_temp1.iloc[:,[0, 1]]
arestas_temp2 = arestas_temp2.iloc[:,[0, 1]]
arestas_temp3 = arestas_temp3.iloc[:,[0, 1]]
arestas_temp4 = arestas_temp4.iloc[:,[0,1]]

def portfolios_inicio():
    """ Gerar o grafo """
    list_arestas1 = arestas_temp1.values.tolist()

    G1 = nx.Graph()

    for i, j in list_arestas1:
        G1.add_edge(i, j)

    arcos = [('1', '3'),
    ('1', '4'),
    ('1', '5'),
    ('1', '6'),
    ('1', '7'),
    ('1', '8'),
    ('1', '9'),
    ('1', '10'),
    ('1', '11'),
    ('1', '12'),
    ('1', '13'),
    ('1', '14'),
    ('1', '15'),
    ('1', '16'),
    ('1', '17'),
    ('2', '18'),
    ('2', '19'),
    ('2', '20'),
    ('2', '21'),
    ('2', '22'),
    ('2', '23'),
    ('2', '24'),
    ('2', '25'),
    ('2', '26'),
    ('2', '27'),
    ('2', '28'),
    ('2', '29'),
    ('2', '30'),
    ('2', '31'),
    ('2', '32')]


    corA = [('1', '3'),
    ('1', '4'), 
    ('1', '5'),
    ('1', '6'),
    ('1', '7'),
    ('1', '8'),
    ('1', '9'),
    ('1', '10'),
    ('1', '11'),
    ('1', '12'),
    ('1', '13'),
    ('1', '14'),
    ('1', '15'),
    ('1', '16'),
    ('1', '17')]

    cor_dos_arcos = []
    for arco in arcos:
        if arco in corA:
            cor_dos_arcos.append("red")
        else:
            cor_dos_arcos.append("black")


    nx.draw_circular(G1, edgecolors=cor_dos_arcos, node_color='white', node_size=300)

def portfolios_tempo2():

    """ Gerar o grafo """
    list_arestas2 = arestas_temp2.values.tolist()

    G2 = nx.Graph()

    for i, j in list_arestas2:
        G2.add_edge(i, j)

    arcos = [('1', '3'),
    ('1', '4'),
    ('1', '5'),
    ('1', '6'),
    ('1', '7'),
    ('1', '8'),
    ('1', '9'),
    ('1', '10'),
    ('1', '11'),
    ('1', '12'),
    ('1', '13'),
    ('1', '14'),
    ('1', '15'),
    ('1', '16'),
    ('1', '17'),
    ('1', '18'),
    ('1', '19'),
    ('1', '20'),
    ('1', '21'),
    ('1', '22'),
    ('2', '23'),
    ('2', '24'),
    ('2', '25'),
    ('2', '26'),
    ('2', '27'),
    ('2', '28'),
    ('2', '29'),
    ('2', '30'),
    ('2', '31'),
    ('2', '32')]


    corA = [('1', '3'),
    ('1', '4'), 
    ('1', '5'),
    ('1', '6'),
    ('1', '7'),
    ('1', '8'),
    ('1', '9'),
    ('1', '10'),
    ('1', '11'),
    ('1', '12'),
    ('1', '13'),
    ('1', '14'),
    ('1', '15'),
    ('1', '16'),
    ('1', '17'),
    ('1', '18'),
    ('1', '19'),
    ('1', '20'),
    ('1', '21'),
    ('1', '22')]

    cor_dos_arcos = []
    for arco in arcos:
        if arco in corA:
            cor_dos_arcos.append("red")
        else:
            cor_dos_arcos.append("black")


    nx.draw_circular(G2, edgecolors=cor_dos_arcos, node_color='white', node_size=300)

def portfolios_temp3():
    """ Gerar o grafo """
    list_arestas3 = arestas_temp3.values.tolist()

    G1 = nx.Graph()

    for i, j in list_arestas3:
        G1.add_edge(i, j)

    arcos = [('1', '3'),
    ('1', '4'),
    ('1', '5'),
    ('1', '6'),
    ('1', '7'),
    ('1', '8'),
    ('1', '9'),
    ('1', '10'),
    ('1', '11'),
    ('1', '12'),
    ('1', '13'),
    ('1', '14'),
    ('1', '15'),
    ('1', '16'),
    ('1', '17'),
    ('2', '18'),
    ('2', '19'),
    ('2', '20'),
    ('2', '21'),
    ('2', '22'),
    ('2', '23'),
    ('2', '24'),
    ('2', '25'),
    ('2', '26'),
    ('2', '27'),
    ('2', '28'),
    ('2', '29'),
    ('2', '30'),
    ('2', '31'),
    ('2', '32')]


    corA = [('1', '3'),
    ('1', '4'), 
    ('1', '5'),
    ('1', '6'),
    ('1', '7'),
    ('1', '8'),
    ('1', '9'),
    ('1', '10'),
    ('1', '11'),
    ('1', '12'),
    ('1', '13'),
    ('1', '14'),
    ('1', '15'),
    ('1', '16'),
    ('1', '17')]

    cor_dos_arcos = []
    for arco in arcos:
        if arco in corA:
            cor_dos_arcos.append("red")
        else:
            cor_dos_arcos.append("black")


    nx.draw_circular(G1, edgecolors=cor_dos_arcos, node_color='white', node_size=300)

def portfolios_temp4():
    """ Gerar o grafo """
    list_arestas4 = arestas_temp4.values.tolist()

    G1 = nx.Graph()

    for i, j in list_arestas4:
        G1.add_edge(i, j)

    arcos = [('1', '3'),
    ('1', '4'),
    ('1', '5'),
    ('1', '6'),
    ('1', '7'),
    ('1', '8'),
    ('1', '9'),
    ('1', '10'),
    ('1', '11'),
    ('1', '12'),
    ('2', '13'),
    ('2', '14'),
    ('2', '15'),
    ('2', '16'),
    ('2', '17'),
    ('2', '18'),
    ('2', '19'),
    ('2', '20'),
    ('2', '21'),
    ('2', '22'),
    ('2', '23'),
    ('2', '24'),
    ('2', '25'),
    ('2', '26'),
    ('2', '27'),
    ('2', '28'),
    ('2', '29'),
    ('2', '30'),
    ('2', '31'),
    ('2', '32')]


    corA = [('1', '3'),
    ('1', '4'), 
    ('1', '5'),
    ('1', '6'),
    ('1', '7'),
    ('1', '8'),
    ('1', '9'),
    ('1', '10'),
    ('1', '11'),
    ('1', '12')]

    cor_dos_arcos = []
    for arco in arcos:
        if arco in corA:
            cor_dos_arcos.append("red")
        else:
            cor_dos_arcos.append("black")


    nx.draw_circular(G1, edgecolors=cor_dos_arcos, node_color='white', node_size=300)

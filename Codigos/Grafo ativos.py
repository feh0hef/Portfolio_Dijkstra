import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path

def dados_origem(arquivo_aresta=str, arquivo_vertices=str):
    dir = r'C:\Users\fehhe\OneDrive\Área de Trabalho\study\Projeto CR' #Diretorio
    vertices = pd.read_excel(os.path.join(dir, 'VERTICES.xlsx')) #VERTICES.xlsx
    arestas = pd.read_excel(os.path.join(dir, 'ARESTAS CR.xlsx')) #ARESTAS CR.xlsx
    arestas['peso corrigido'] = np.around(arestas['Weights'] + 1, 2) #mudar intervalo de -1 a 1 para 0 a 2
    arestas = arestas.iloc[:,[0,1,4]] #Selecionar as colunas que serão usadas 

    #Grafo
    list_arestas = arestas.values.tolist()
    return list_arestas

def gerar_grafo():
    """ Gerar o grafo """

    list_arestas = dados_origem()

    G = nx.Graph()

    for i, j, v in list_arestas:
        G.add_edge(i, j, weight=v)

    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 1]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 1]
    return G, elarge, esmall
    
def caminho_minimo_portA():
    """ Traçar o grafo de caminhos minimos do portfólio A """

    G, elarge, esmall = gerar_grafo()

    arcos_caminho = [(1.0, 8.0), (2.0, 6.0), (2.0, 13.0),(7.0, 8.0), (8.0, 6.0), (8.0,9.0), (8.0, 13.0), (8.0,14.0), (8.0, 12.0), (8.0, 15.0)]

    cor_dos_arcos = []
    for arco in esmall:
        if arco in arcos_caminho:
            cor_dos_arcos.append("red")
        else:
            cor_dos_arcos.append("black")

    pos = nx.spring_layout(G,k=5.5, seed=7, scale=2)  # positions for all nodes - seed for reproducibility

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=300, node_color='white', edgecolors='black')

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=0.5)
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=0.5, alpha=0.5, edge_color=cor_dos_arcos 
    )

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=5)
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=5)

    ax = plt.gca()
    ax.margins(0.03)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def caminho_minimo_portB():
    """ Traçar o grafo de caminhos minimos do portfólio B """

    G, elarge, esmall = gerar_grafo()
         
    arcos_caminho = [(2.0, 6.0), (2.0, 13.0), (2.0, 15.0), (4.0, 6.0),(5.0, 12.0), (8.0, 6.0), (8.0, 11.0), (8.0, 15.0), (8.0, 12.0), (20.0, 13.0)]

    cor_dos_arcos = []
    for arco in esmall:
        if arco in arcos_caminho:
            cor_dos_arcos.append("red")
        else:
            cor_dos_arcos.append("black")

    pos = nx.spring_layout(G,k=5.5, seed=7, scale=2)  # positions for all nodes - seed for reproducibility

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=300, node_color='white', edgecolors='black')

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=0.5)
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=0.5, alpha=0.5, edge_color=cor_dos_arcos 
    )

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=5)
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=5)

    ax = plt.gca()
    ax.margins(0.03)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
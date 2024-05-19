import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo: listas de importadores e exportadores
importadores = ['EUA', 'China', 'Alemanha', 'Japão']
exportadores = ['China', 'EUA', 'Alemanha', 'Japão']

# Criação do DataFrame
data = {
    'Importadores': importadores,
    'Exportadores': exportadores
}
df = pd.DataFrame(data)

# Adiciona a coluna 'Brasil' para centralizar
df['Brasil'] = ['Brasil'] * len(importadores)

# Visualização do DataFrame
print(df)

# Função para plotar gráfico bipartido
def plot_bipartite_graph(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Adicionando as linhas
    for i in range(len(df)):
        ax.plot([0, 1, 2], [i, i, i], 'ro-', color='gray')
        ax.text(0, i, df['Importadores'][i], ha='right', va='center', fontsize=12)
        ax.text(1, i, df['Brasil'][i], ha='center', va='center', fontsize=12, fontweight='bold')
        ax.text(2, i, df['Exportadores'][i], ha='left', va='center', fontsize=12)

    # Configuração dos eixos
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, len(df) - 0.5)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(['Importadores', 'Brasil', 'Exportadores'])
    ax.set_yticks([])

    plt.title('Relação de Importadores e Exportadores do Brasil')
    plt.show()

# Plotando o gráfico bipartido
plot_bipartite_graph(df)


import matplotlib.pyplot as plt


capitais = [
    'São Paulo', 'Rio de Janeiro', 'Brasília', 'Fortaleza', 'Salvador',
    'Belo Horizonte', 'Manaus', 'Curitiba', 'Recife', 'Goiânia',
    'Porto Alegre', 'Belém', 'São Luís', 'Maceió', 'Campo Grande',
    'Teresina', 'João Pessoa', 'Natal', 'Cuiabá', 'Aracaju',
    'Florianópolis', 'Porto Velho', 'Macapá', 'Boa Vista',
    'Rio Branco', 'Vitória', 'Palmas'
]
populacao_2022 = [
    11451245, 6211423, 2817068, 2428708, 2417678,
    2315560, 2063547, 1773733, 1488920, 1437237,
    1332833, 1303375, 1037775, 957916, 897938,
    866300, 833932, 751300, 650912, 602757,
    537213, 460413, 442933, 413486, 364756,
    322869, 302692
]


regioes = {
    'São Paulo': 'Sudeste', 'Rio de Janeiro': 'Sudeste', 'Belo Horizonte': 'Sudeste', 'Vitória': 'Sudeste',
    'Brasília': 'Centro-Oeste', 'Goiânia': 'Centro-Oeste', 'Campo Grande': 'Centro-Oeste', 'Cuiabá': 'Centro-Oeste',
    'Manaus': 'Norte', 'Belém': 'Norte', 'Porto Velho': 'Norte', 'Boa Vista': 'Norte', 'Macapá': 'Norte', 'Palmas': 'Norte',
    'Fortaleza': 'Nordeste', 'Salvador': 'Nordeste', 'Recife': 'Nordeste', 'São Luís': 'Nordeste', 'Maceió': 'Nordeste', 'Aracaju': 'Nordeste', 'Teresina': 'Nordeste', 'João Pessoa': 'Nordeste', 'Natal': 'Nordeste',
    'Curitiba': 'Sul', 'Porto Alegre': 'Sul', 'Florianópolis': 'Sul', 'Rio Branco': 'Norte'
}


populacao_por_regiao = {}
for capital, populacao in zip(capitais, populacao_2022):
    regiao = regioes[capital]
    if regiao not in populacao_por_regiao:
        populacao_por_regiao[regiao] = populacao
    else:
        populacao_por_regiao[regiao] += populacao


plt.figure(figsize=(10, 8))
plt.pie(populacao_por_regiao.values(), labels=populacao_por_regiao.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Distribuição da População Brasileira por Região em 2022')
plt.axis('equal')  

plt.show()

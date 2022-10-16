# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
# Apenas os 5 primeiros colocados
# Os últimos 4 colocados
# Uma lista com os times em ordem alfabética
# Em que posição na tabela está o time do internacional

tabelaBrasileirao = ('Palmeiras', 'Atlético MG', 'Corinthians', 'Internacional',
                     'Fluminense', 'Athletico PR', 'Flamengo', 'Bragantino', 
                     'São Paulo', 'Santos', 'Botafogo', 'Avaí', 
                     'Goiás', 'Ceará SC', 'Cuiabá', 'Coritiba', 
                     'América MG', 'Atlético GO', 'Fortaleza', 'Juventude')

print(f'\nOs 5 primeiros colados são: {tabelaBrasileirao[:5]}')
print(f'\nOs últimos 4 colocados são: {tabelaBrasileirao[16:]}')
print(f'\nOs times em ordem alfabética: {sorted(tabelaBrasileirao)}')
print('\nPosição atual do Internacional: {}º colocado\n'.format(tabelaBrasileirao.index('Internacional') + 1))

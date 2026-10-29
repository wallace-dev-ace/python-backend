from random import randint, shuffle
from time import sleep
pilotos = {'Verstappen': 'Red Bull',
        'Hadjar': 'Red Bull',
        'Antonelli': 'Mercedes',
        'Russel': 'Mercedes',
        'Leclerc': 'Ferrari',
        'Hamilton': 'Ferrari',
        'Norris': 'Mclaren',
        'Piastri': 'Mclaren',
        'Alonso': 'Aston Martin',
        'Stroll': 'Aston Martin',
        'Gasly': 'Alpine',
        'Colapinto': 'Alpine',
        'Albon': 'Williams',
        'Sainz': 'Williams',
        'Ocon': 'Haas',
        'Bearmen': 'Haas',
        'Hülkenberg': 'Audi',
        'Bortoleto': 'Audi',
        'Lindblad': 'RB visa',
        'Lawson': 'RB visa'}
times = set(pilotos.values())

def pontos(posicao):
        if posicao == 1: return 25
        elif posicao == 2: return 18
        elif posicao == 3: return 15
        elif posicao == 4: return 12
        elif posicao == 5: return 10
        elif posicao == 6: return 8
        elif posicao == 7: return 6
        elif posicao == 8: return 4
        elif posicao == 9: return 2
        else: return 1

piloto_pontos = {piloto: 0 for piloto in pilotos }
team_pontos = {team: 0 for team in times}

ncorridas = 22

for corridas in range(1, ncorridas +1):
        sleep(1)
        print(f'\nCorrida {corridas}:\n')
        shufflepiloto = list(pilotos.keys())
        shuffle(shufflepiloto)


        for posicao, piloto in enumerate(shufflepiloto[:10], start=1):
                pontos_ganhos = pontos(posicao)
                piloto_pontos[piloto]+=pontos_ganhos
                team_pontos[pilotos[piloto]]+=pontos_ganhos
                print(f'{posicao}° {piloto}: {pontos_ganhos} pontos')


def sort_pontos(data):
        items=list(data.items())
        for i in range(len(items)):
                for j in range(i+1, len(items)):
                        if items[i][1]<items[j][1]:
                                items[i], items[j]=items[j], items[i]
        return items


final_pilotos = sort_pontos(piloto_pontos)
print('\nClassificação Final do Campeonato de Pilotos\n')
for posicao, (pilotos,pontos) in enumerate(final_pilotos, start=1):
        print(f'{posicao}. {pilotos}: {pontos} pontos')



final_team = sort_pontos(team_pontos)
print('\n Classificação Fnal do Campeonato de Construtores\n')
for posicao, (team, pontos) in enumerate(final_team, start=1):
        print(f'{posicao}. {team}: {pontos} pontos')
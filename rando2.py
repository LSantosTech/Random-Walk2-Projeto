import random

def random_walk_2(n):
    """ Retorna as coordenadas depois que 'n' andar quarteirões."""
    x, y = 0, 0
    for u in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

number_of_walks = 20000

for walk_length in range(1, 31):
    no_transport = 0 # Sem transporte se o numero de passos for 4 ou menores que 4
    for u in range(number_of_walks):
        (x, y) =  random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance < 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length,
    " / % of no transport = ", 100*no_transport_percentage)
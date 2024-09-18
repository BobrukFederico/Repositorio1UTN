def torres_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 desde {origen} hasta {destino}")
    else:
        torres_hanoi(n-1, origen, auxiliar, destino)
        print(f"Mover disco {n} desde {origen} hasta {destino}")
        torres_hanoi(n-1, auxiliar, destino, origen)

torres_hanoi(3, 'A', 'C', 'B')

        
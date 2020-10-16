import Posisi


def Z_Function(Player, N):
    if (Player.noPlayer == 1):
        M = Posisi.Posisi(N - 1, N - 1)
    else:
        M = Posisi.Posisi(0, 0)
    sum = 0
    for Pion in Player.arrayPion:
        sum -= Pion.currentPosition.euclidean(M)
    return sum
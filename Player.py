
import numpy as np
import Pion


class Player:
    """
    class untuk agen
    Terdiri dari pion-pion dalam board
    """

    def __init__(self, noPlayer):
        self.noPlayer = noPlayer
        self.arrayPion = []

        def addPion(Pion):
            # masukan harus tipe bentukan Pion
            self.arrayPion.append(Pion)

        def movePion(pionId, posisi):
            # masukkan harus berupa tipe bentukkan posisi
            for pion in self.arrayPion:
                if pion.pionId == pionId:
                    pion.currentPosition = posisi
                    break

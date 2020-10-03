class Pion:
    """
    class untuk tiap pion yang ada
    pionId = identifikasi untuk memudahkan nanti dalam menggerakkan pion
    """

    def __init__(self, pionId, currentPosition, startPosition):
        self.pionId = pionId
        self.currentPosition = currentPosition
        self.startPosition = startPosition

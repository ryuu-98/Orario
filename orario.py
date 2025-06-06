class Orario:
    def __init__(self, ore, minuti, secondi):   #COSTRUTTORE

        if ore < 0 or ore > 23:
            raise ValueError("Ore must be 0..23")

        if minuti < 0 or minuti > 59:
            raise ValueError("Minuti must be 0..59")

        if secondi < 0 or secondi > 59:
            raise ValueError("Secondi must be 0..59")

        self.ore = ore
        self.minuti = minuti
        self.secondi = secondi

    def __str__(self):              #METODI MAGICI __NOME__
        return f"{str(self.ore).zfill(2)}:{str(self.minuti).zfill(2)}:{str(self.secondi).zfill(2)}"

    def __repr__(self):
        return f"{str(self.ore).zfill(2)}:{str(self.minuti).zfill(2)}:{str(self.secondi).zfill(2)}"

    def aggiungi_ore(self, ora_a):
        self.ore += ora_a

        if self.ore > 23:
            self.ore = self.ore % 24

    def aggiugi_minuti(self, min_a):
        self.minuti += min_a

        if self.minuti > 59:
            ore_da_aggiungere = self.minuti // 60
            self.minuti = self.minuti % 60

        self.aggiungi_ore(ore_da_aggiungere)

    def aggiungi_secondi(self, sec):
        secondi_attuali = self.converti_in_secondi()

        secondi_attuali += sec
        secondi_attuali %= 86400

        self.ore = secondi_attuali // 3600
        self.minuti = (secondi_attuali % 3600) // 60
        self.secondi = secondi_attuali % 60

    def converti_in_secondi(self):
        return self.secondi + self.minuti * 60 + self.ore * 3600

    def __eq__(self, other):
        return (self.ore, self.minuti, self.secondi) == (other.ore, other.minuti, other.secondi)

    def __lt__(self, other):
        return (self.ore, self.minuti, self.secondi) < (other.ore, other.minuti, other.secondi)

    def __gt__(self, other):
        return (self.ore, self.minuti, self.secondi) > (other.ore, other.minuti, other.secondi)

    def differenza_orari(self, orario_2):

        if orario_2.converti_in_secondi() >= self.converti_in_secondi():
            differenza_sec = orario_2.converti_in_secondi() - self.converti_in_secondi()
        else:
            differenza_sec = (86400 - self.converti_in_secondi()) + orario_2.converti_in_secondi()

        return differenza_sec


if __name__ == "__main__":

    o = Orario(10, 27, 40)

    print(o)
import pytest

from orario import Orario

@pytest.fixture
def orario():
    return Orario(10, 30, 50)

def test_creazione_orario(orario):
    assert orario.ore == 10
    assert orario.minuti == 30
    assert orario.secondi == 50

def test_creazione_orario_ora_non_valida(orario):
    with pytest.raises(ValueError):
        o = Orario(27,30,40)

def test_creazione_orario_minuti_non_validi(orario):
    with pytest.raises(ValueError):
        o = Orario(23,80,40)

def test_creazione_orario_secondi_non_validi(orario):
    with pytest.raises(ValueError):
        o = Orario(10, 30, 70)

def test_str(orario):
    assert str(orario) == "10:30:50"

def test_str2():
    o = Orario(8,10,50)
    assert str(o) == "08:10:50"

def test_str3():
    o = Orario(15, 1, 6)
    assert str(o) == "15:01:06"

def test_aggiungi_ore(orario):
    orario.aggiungi_ore(10)
    # assert orario.ore == 20
    assert str(orario) == "20:30:50"

def test_aggiungi_ore_eccesso(orario):
    orario.aggiungi_ore(16)
    # assert orario.ore == 20
    assert str(orario) == "02:30:50"

def test_aggiungi_ore_eccesso2(orario):
    orario.aggiungi_ore(18)
    # assert orario.ore == 20
    assert str(orario) == "04:30:50"

def test_aggiungi_secondi(orario):
    orario.aggiungi_secondi(1000)
    assert str(orario) == "10:47:30"

def test_aggiungi_secondi_2(orario):
    orario.aggiungi_secondi(100000)
    assert str(orario) == "14:17:30"

def test_aggiungi_minuti(orario):
    orario.aggiugi_minuti(1000)
    assert str(orario) == "03:10:50"

def test_orari_simili(orario):
    o2 = Orario(10, 30, 50)
    assert orario == o2

def test_orario_maggiore(orario):
    o2 = Orario(9, 56, 15)
    assert orario > o2

def test_orario_minore(orario):
    o2 = Orario(11, 25, 58)
    assert orario < o2

def test_differenza_orari(orario):
    o2 = Orario(10,36,50)
    assert orario.differenza_orari(o2) == 360

def test_differenza_orari_2(orario):
    o2 = Orario(9, 21, 11)
    assert orario.differenza_orari(o2) == 82221
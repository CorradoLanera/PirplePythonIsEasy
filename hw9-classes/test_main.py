from main import Veicle

def test_veicle():
    v = Veicle()
    assert isinstance(v, Veicle)
    assert v.Make is None
    assert v.Model is None
    assert v.Year is None
    assert v.Weight is None
    assert v.NeedsMaintenance is False
    assert v.TripsSinceMaintenance == 0

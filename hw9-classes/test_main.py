# -*- coding: utf-8 -*-
from main import Vehicle


def test_Vehicle_exists_with_expected_default():
    v = Vehicle()
    assert isinstance(v, Vehicle)
    assert v.Make is None
    assert v.Model is None
    assert v.Year is None
    assert v.Weight is None
    assert v.NeedsMaintenance is False
    assert v.TripsSinceMaintenance == 0


def test_Vehicle_can_set_main_attributes():
    v = Vehicle()

    v.setMake("Fiat")
    v.setModel("Punto")
    v.setYear("2000")
    v.setWeight(1000)

    assert v.Make == "Fiat"
    assert v.Model == "Punto"
    assert v.Year == "2000"
    assert v.Weight == 1000

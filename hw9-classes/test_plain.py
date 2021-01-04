# -*- coding: utf-8 -*-
from main import Vehicle, Planes


def test_Planes_exists_and_are_Vehicle():
    p = Planes()
    assert isinstance(p, (Planes, Vehicle))


def test_Planes_have_Fly_and_Land_methods_working():
    p = Planes()
    assert p.isFlying is False
    p.Fly()
    assert p.isFlying is True
    p.Land()
    assert p.isFlying is False


def test_switcing_isFlying_from_True_to_False_increment_TripsSinceMaintenance():
    p = Planes()
    assert p.TripsSinceMaintenance == 0
    assert p.NeedsMaintenance is False
    p.Fly()
    assert p.TripsSinceMaintenance == 0
    assert p.NeedsMaintenance is False
    p.Land()
    assert p.TripsSinceMaintenance == 1
    assert p.NeedsMaintenance is False


def test_switcing_isFlying_from_False_to_False_not_increment_TripsSinceMaintenance():
    p = Planes()
    p.Land()
    assert p.TripsSinceMaintenance == 0
    p.Fly()
    p.Land()
    p.Land()
    assert p.TripsSinceMaintenance == 1


def test_switcing_isFlying_more_than_100_times_turns_on_NeedsMaintenance():
    p = Planes()
    assert p.NeedsMaintenance is False
    p.Fly()
    p.Land()
    assert p.TripsSinceMaintenance == 1
    assert p.NeedsMaintenance is False
    for i in range(99):
        p.Fly()
        p.Land()
    assert p.TripsSinceMaintenance == 100
    assert p.NeedsMaintenance is False
    p.Fly()
    p.Land()
    assert p.TripsSinceMaintenance == 101
    assert p.NeedsMaintenance is True

def test_Repair_works():
    p = Planes()
    for i in range(101):
        p.Fly()
        p.Land()
    p.Repair()
    assert p.TripsSinceMaintenance == 0
    assert p.NeedsMaintenance is False

def test_rideBy_method_works():
    p = Planes()
    assert p.TripsSinceMaintenance == 0
    p.rideBy(15)
    assert p.TripsSinceMaintenance == 15
    p.rideBy(2)
    assert p.TripsSinceMaintenance == 17

def test_Fly_when_NeedsMaintenance_is_True_returns_False():
    p = Planes()
    p.rideBy(101)
    assert p.Fly() is False


# -*- coding: utf-8 -*-
from main import Vehicle, Cars


def test_Cars_exists_and_are_Vehicle():
    c = Cars()
    assert isinstance(c, (Cars, Vehicle))


def test_Cars_have_Drive_and_Stop_methods_working():
    c = Cars()
    assert c.isDriving is False
    c.Drive()
    assert c.isDriving is True
    c.Stop()
    assert c.isDriving is False


def test_switcing_isDriving_from_True_to_False_increment_TripsSinceMaintenance():
    c = Cars()
    assert c.TripsSinceMaintenance == 0
    assert c.NeedsMaintenance is False
    c.Drive()
    assert c.TripsSinceMaintenance == 0
    assert c.NeedsMaintenance is False
    c.Stop()
    assert c.TripsSinceMaintenance == 1
    assert c.NeedsMaintenance is False


def test_switcing_isDriving_from_False_to_False_not_increment_TripsSinceMaintenance():
    c = Cars()
    c.Stop()
    assert c.TripsSinceMaintenance == 0
    c.Drive()
    c.Stop()
    c.Stop()
    assert c.TripsSinceMaintenance == 1


def test_switcing_isDriving_more_than_100_times_turns_on_NeedsMaintenance():
    c = Cars()
    assert c.NeedsMaintenance is False
    c.Drive()
    c.Stop()
    assert c.TripsSinceMaintenance == 1
    assert c.NeedsMaintenance is False
    for i in range(99):
        c.Drive()
        c.Stop()
    assert c.TripsSinceMaintenance == 100
    assert c.NeedsMaintenance is False
    c.Drive()
    c.Stop()
    assert c.TripsSinceMaintenance == 101
    assert c.NeedsMaintenance is True

def test_Repair_works():
    c = Cars()
    for i in range(101):
        c.Drive()
        c.Stop()
    c.Repair()
    assert c.TripsSinceMaintenance == 0
    assert c.NeedsMaintenance is False

def test_rideBy_method_works():
    c = Cars()
    assert c.TripsSinceMaintenance == 0
    c.rideBy(15)
    assert c.TripsSinceMaintenance == 15
    c.rideBy(2)
    assert c.TripsSinceMaintenance == 17

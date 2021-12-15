#!/usr/bin/env/ python

import pytest
from mock import patch
from plan_handler import cha_cha_handler, clap_handler, left_handler, back_handler, one_hop_handler, right_foot_handler, left_foot_handler, circle_handler

@patch('plan_handler.last_moves', [])
def test_cha_cha_handler_true(mocker):
    mocker.patch('plan_handler.move_circle', return_value=True)

    res = cha_cha_handler("we're gonna get funky", None)

    assert res == True

@patch('plan_handler.last_moves', [])
def test_cha_cha_handler_false(mocker):
    mocker.patch('plan_handler.move_circle', return_value=True)

    res = cha_cha_handler("NO", None)

    assert res == False

@patch('plan_handler.last_moves', [])
def test_clap_handler_true(mocker):
    mocker.patch('plan_handler.move_forward', return_value=True)

    res = clap_handler("clap clap clap", None)

    assert res == True

@patch('plan_handler.last_moves', [])
def test_clap_handler_false(mocker):
    mocker.patch('plan_handler.move_forward', return_value=True)

    res = clap_handler("NO", None)

    assert res == False

@patch('plan_handler.last_moves', [])
def test_left_handler_true(mocker):
    mocker.patch('plan_handler.move_left', return_value=True)

    res = left_handler("to the left", None)

    assert res == True

@patch('plan_handler.last_moves', [])
def test_left_handler_false(mocker):
    mocker.patch('plan_handler.move_left', return_value=True)

    res = left_handler("NO", None)

    assert res == False

@patch('plan_handler.last_moves', [])
def test_back_handler_true(mocker):
    mocker.patch('plan_handler.move_forward', return_value=True)

    res = back_handler("take it back", None)

    assert res == True

@patch('plan_handler.last_moves', [])
def test_back_handler_false(mocker):
    mocker.patch('plan_handler.move_forward', return_value=True)

    res = back_handler("NO", None)

    assert res == False

@patch('plan_handler.last_moves', [])
def test_one_hop_handler_true(mocker):
    mocker.patch('plan_handler.move_forward', return_value=True)

    res = one_hop_handler("one hop this time", None)

    assert res == True

@patch('plan_handler.last_moves', [])
def test_one_hop_handler_false(mocker):
    mocker.patch('plan_handler.move_forward', return_value=True)

    res = one_hop_handler("NO", None)

    assert res == False

@patch('plan_handler.last_moves', [])
def test_right_foot_handler_true(mocker):
    mocker.patch('plan_handler.move_right', return_value=True)

    res = right_foot_handler("right foot", None)

    assert res == True

@patch('plan_handler.last_moves', [])
def test_right_foot_handler_false(mocker):
    mocker.patch('plan_handler.move_right', return_value=True)

    res = right_foot_handler("NO", None)

    assert res == False

@patch('plan_handler.last_moves', [])
def test_left_foot_handler_true(mocker):
    mocker.patch('plan_handler.move_left', return_value=True)

    res = left_foot_handler("left foot", None)

    assert res == True

@patch('plan_handler.last_moves', [])
def test_left_foot_handler_false(mocker):
    mocker.patch('plan_handler.move_left', return_value=True)

    res = left_foot_handler("NO", None)

    assert res == False

@patch('plan_handler.last_moves', [])
def test_circle_handler_true(mocker):
    mocker.patch('plan_handler.move_circle', return_value=True)

    res = circle_handler("turn it out", None)

    assert res == True

@patch('plan_handler.last_moves', [])
def test_circle_handler_false(mocker):
    mocker.patch('plan_handler.move_circle', return_value=True)

    res = circle_handler("NO", None)

    assert res == False

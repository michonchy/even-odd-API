import json

import pytest

from even_odd import app

def test_number_check():
    assert app.number_check(1) == "odd"


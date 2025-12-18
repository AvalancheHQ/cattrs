import pytest

from cattrs import BaseConverter, Converter


@pytest.mark.parametrize("converter_cls", [BaseConverter, Converter])
@pytest.mark.codspeed_benchmark
def test_unstructure_int(converter_cls):
    c = converter_cls()

    c.unstructure(5)


@pytest.mark.parametrize("converter_cls", [BaseConverter, Converter])
@pytest.mark.codspeed_benchmark
def test_unstructure_float(converter_cls):
    c = converter_cls()

    c.unstructure(15.0)

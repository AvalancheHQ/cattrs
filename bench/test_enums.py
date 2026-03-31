from enum import Enum, IntEnum, StrEnum

import pytest

from cattrs import BaseConverter, Converter
from cattrs.preconf.msgspec import MsgspecJsonConverter
from cattrs.preconf.orjson import OrjsonConverter


class SimpleEnum(Enum):
    FIRST = "first"
    SECOND = "second"
    THIRD = "third"


class SimpleIntEnum(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3


class SimpleStrEnum(StrEnum):
    ALPHA = "alpha"
    BETA = "beta"
    GAMMA = "gamma"


@pytest.mark.parametrize("converter_cls", [BaseConverter, Converter, MsgspecJsonConverter, OrjsonConverter])
@pytest.mark.codspeed_benchmark
def test_unstructure_simple_enum(converter_cls):
    """Benchmark unstructuring a simple enum."""
    c = converter_cls()
    c.unstructure(SimpleEnum.FIRST)


@pytest.mark.parametrize("converter_cls", [BaseConverter, Converter, MsgspecJsonConverter, OrjsonConverter])
@pytest.mark.codspeed_benchmark
def test_structure_simple_enum(converter_cls):
    """Benchmark structuring a simple enum."""
    c = converter_cls()
    c.structure("first", SimpleEnum)


@pytest.mark.parametrize("converter_cls", [BaseConverter, Converter, MsgspecJsonConverter, OrjsonConverter])
@pytest.mark.codspeed_benchmark
def test_unstructure_simple_int_enum(converter_cls):
    """Benchmark unstructuring a simple IntEnum."""
    c = converter_cls()
    c.unstructure(SimpleIntEnum.ONE)


@pytest.mark.parametrize("converter_cls", [BaseConverter, Converter, MsgspecJsonConverter, OrjsonConverter])
@pytest.mark.codspeed_benchmark
def test_structure_simple_int_enum(converter_cls):
    """Benchmark structuring a simple IntEnum."""
    c = converter_cls()
    c.structure(1, SimpleIntEnum)


@pytest.mark.parametrize("converter_cls", [BaseConverter, Converter, MsgspecJsonConverter, OrjsonConverter])
@pytest.mark.codspeed_benchmark
def test_unstructure_simple_str_enum(converter_cls):
    """Benchmark unstructuring a simple StrEnum."""
    c = converter_cls()
    c.unstructure(SimpleStrEnum.ALPHA)


@pytest.mark.parametrize("converter_cls", [BaseConverter, Converter, MsgspecJsonConverter, OrjsonConverter])
@pytest.mark.codspeed_benchmark
def test_structure_simple_str_enum(converter_cls):
    """Benchmark structuring a simple StrEnum."""
    c = converter_cls()
    c.structure("alpha", SimpleStrEnum)


"""Test Home Assistant remote methods and classes."""
import pytest

from homeassistant import core
from homeassistant.helpers.json import JSONEncoder
from homeassistant.util import dt as dt_util


def test_json_encoder(hass):
    """Test the JSON Encoder."""
    ha_json_enc = JSONEncoder()
    state = core.State("test.test", "hello")

    # Test serializing a datetime
    now = dt_util.utcnow()
    assert ha_json_enc.default(now) == now.isoformat()

    # Test serializing a set()
    data = {"milk", "beer"}
    assert sorted(ha_json_enc.default(data)) == sorted(list(data))

    # Test serializing an object which implements as_dict
    assert ha_json_enc.default(state) == state.as_dict()

    # Default method raises TypeError if non HA object
    with pytest.raises(TypeError):
        ha_json_enc.default(1)

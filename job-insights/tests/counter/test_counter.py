import json
from unittest.mock import mock_open, patch
from src.counter import count_ocurrences


word = {"result": "A Tribo é uma coisa"}


def test_counter():
    with patch("builtins.open", mock_open(read_data=json.dumps(word))):
        assert count_ocurrences("path", "a") == 3
        

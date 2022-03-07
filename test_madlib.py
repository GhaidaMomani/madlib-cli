import pytest

from madlib import read_template, parse_template, merge, empty_template,  handle_IO, write_file


def test_read_template_returns_stripped_string():
    actual = read_template("assets/template2.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected



import pytest

from libnix.exception.nix_error import NixError

from cli.tag import tag


def test_tag_list_no_tag(capsys):
    tag.tag("nixconfig", ["list"])

    _out, _err = capsys.readouterr()

    assert "tag1" in _out, "'tag1' should be in output"
    assert "tag2" in _out, "'tag2' should be in output"
    assert "tag3" in _out, "'tag3' should be in output"
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)

import pytest

from libnix.exception.nix_error import NixError

from cli.tag import tag


def test_tag_no_command(capsys):
    with pytest.raises(NixError) as _excinfo:
        tag.tag("nixconfig", [])

    _out, _err = capsys.readouterr()
    assert "Missing tag command" in str(_excinfo.value), "exception doesn't contain expected string"
    assert "usage: nixconfig tag" in _out, "StdOut doesn't contain expected string"
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_script_bad_command(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        tag.tag("nixconfig", ["badcommand"])

    _out, _err = capsys.readouterr()

    assert "2" in str(_excinfo.value), "Exception doesn't contain expected string"
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "invalid choice" in _err, "StdErr doesn't contain expected string"

import pytest

from libnix.exception.nix_error import NixError

from cli.script import script


def test_script_no_command(capsys):
    with pytest.raises(NixError) as _excinfo:
        script.script("nixconfig", [])

    _out, _err = capsys.readouterr()
    assert "Missing script command" in str(_excinfo.value), "exception doesn't contain expected string"
    assert "usage: nixconfig script" in _out, "StdOut doesn't contain expected string"
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_script_bad_command(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        script.script("nixconfig", ["asdf"])

    _out, _err = capsys.readouterr()

    assert "2" in str(_excinfo.value), "Exception doesn't contain expected string"
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "invalid choice" in _err, "StdErr doesn't contain expected string"

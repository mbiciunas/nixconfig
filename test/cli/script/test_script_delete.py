import pytest

from libnix.exception.nix_error import NixError

from cli.script import script


def test_script_delete_no_script(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        script.script("nixconfig", ["delete"])

    _out, _err = capsys.readouterr()

    assert "2" in str(_excinfo.value), "Exception doesn't contain expected string"
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "the following arguments are required: name" in _err, "StdErr doesn't contain expected string"


def test_script_delete_bad_script(capsys):
    with pytest.raises(NixError) as _excinfo:
        script.script("nixconfig", ["delete", "badscript"])

    _out, _err = capsys.readouterr()

    assert "Unable to find script: badscript" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)

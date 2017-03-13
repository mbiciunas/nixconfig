import pytest

from libnix.exception.nix_error import NixError

from cli.script import script


def test_script_list_no_tag(capsys):
    script.script("nixconfig", ["list"])

    _out, _err = capsys.readouterr()

    assert "script1" in _out, "'script1' should be in output"
    assert "script2" in _out, "'script2' should be in output"
    assert "script3" in _out, "'script3' should be in output"
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_script_list_bad_tag(capsys):
    with pytest.raises(NixError) as _excinfo:
        script.script("nixconfig", ["list", "badtag"])

    _out, _err = capsys.readouterr()

    assert "Unknown tags" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_script_list_good_tag(capsys):
    script.script("nixconfig", ["list", "tag1"])
    _out, _err = capsys.readouterr()

    assert "script1" in _out, "'script1' should be in output"
    assert "script2" in _out, "'script2' should be in output"
    assert "script3" not in _out, "'script3' should be in output"
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)

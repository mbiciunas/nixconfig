import pytest

from libnix.exception.nix_error import NixError

from cli.script import script


def test_script_rename_no_script(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        script.script("nixconfig", ["rename"])

    _out, _err = capsys.readouterr()

    assert _excinfo.value.code is 2, "Incorrect exit code.  Should be 2, received {}".format(_excinfo.value.code)
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "the following arguments are required: name, name_new" in _err, "StdErr doesn't contain expected string"


def test_script_rename_one_script(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        script.script("nixconfig", ["rename", "script1"])

    _out, _err = capsys.readouterr()

    assert _excinfo.value.code is 2, "Incorrect exit code.  Should be 2, received {}".format(_excinfo.value.code)
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "the following arguments are required: name_new" in _err, "StdErr doesn't contain expected string"


def test_script_rename_bad_script(capsys):
    with pytest.raises(NixError) as _excinfo:
        script.script("nixconfig", ["rename", "badscript", "newscript"])

    _out, _err = capsys.readouterr()

    assert "Unable to find script: badscript" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_script_rename_to_exist_script(capsys):
    with pytest.raises(NixError) as _excinfo:
        script.script("nixconfig", ["rename", "badscript", "script1"])

    _out, _err = capsys.readouterr()

    assert "New script name is already used: script1" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_script_rename_same(capsys):
    with pytest.raises(NixError) as _excinfo:
        script.script("nixconfig", ["rename", "script1", "script1"])

    _out, _err = capsys.readouterr()

    assert "Old and new script names are the same: script1" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_script_rename_good_script(capsys):
    script.script("nixconfig", ["rename", "script1", "newscript"])

    _out, _err = capsys.readouterr()

    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)

    script.script("nixconfig", ["rename", "newscript", "script1"])

    _out, _err = capsys.readouterr()

    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)

import pytest

from libnix.exception.nix_error import NixError

from cli.script import script


def test_script_create_no_script(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        script.script("nixconfig", ["create"])

    _out, _err = capsys.readouterr()

    assert "2" in str(_excinfo.value), "Exception doesn't contain expected string"
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "the following arguments are required: name, desc, tags" in _err, "StdErr doesn't contain expected string"


def test_script_create_no_desc_no_tag(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        script.script("nixconfig", ["create", "newscript"])

    _out, _err = capsys.readouterr()

    assert "2" in str(_excinfo.value), "Exception doesn't contain expected string"
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "the following arguments are required: desc, tags" in _err, "StdErr doesn't contain expected string"


def test_script_create_existing_script(capsys):
    with pytest.raises(NixError) as _excinfo:
        script.script("nixconfig", ["create", "script1", "new script", "tag3"])

    _out, _err = capsys.readouterr()

    assert "Script already exists: script1" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_script_create_bad_tag(capsys):
    with pytest.raises(NixError) as _excinfo:
        script.script("nixconfig", ["create", "script1", "new script", "badtag"])

    _out, _err = capsys.readouterr()

    assert "Unknown tags: badtag" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)

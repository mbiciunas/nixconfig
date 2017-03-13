import pytest

from libnix.exception.nix_error import NixError

from cli.script_tag import script_tag


def test_script_tag_list_no_script(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        script_tag.script_tag("nixconfig", ["list"])

    _out, _err = capsys.readouterr()

    assert "2" in str(_excinfo.value), "Exception doesn't contain expected string"
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "the following arguments are required: script" in _err, "StdErr doesn't contain expected string"


def test_script_tag_list_bad_script(capsys):
    with pytest.raises(NixError) as _excinfo:
        script_tag.script_tag("nixconfig", ["list", "badscript"])

    _out, _err = capsys.readouterr()

    assert "Unable to find script: badscript" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_script_tag_list_good_script(capsys):
    script_tag.script_tag("nixconfig", ["list", "script1"])
    _out, _err = capsys.readouterr()

    assert "tag1" in _out, "'tag1' should be in output"
    assert "tag2" in _out, "'tag2' should be in output"
    assert "tag3" not in _out, "'tag3' should not be in output"
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)

import pytest

from libnix.exception.nix_error import NixError

from cli.tag import tag


def test_tag_delete_no_tag(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        tag.tag("nixconfig", ["delete"])

    _out, _err = capsys.readouterr()

    assert "2" in str(_excinfo.value), "Exception doesn't contain expected string"
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "the following arguments are required: tag" in _err, "StdErr doesn't contain expected string"


def test_tag_delete_invalid_tag(capsys):
    with pytest.raises(NixError) as _excinfo:
        tag.tag("nixconfig", ["delete", "badtag"])

    _out, _err = capsys.readouterr()

    assert "Unknown tag: badtag" in str(_excinfo.value)
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_tag_delete_in_use_tag(capsys):
    with pytest.raises(NixError) as _excinfo:
        tag.tag("nixconfig", ["delete", "tag1"])

    _out, _err = capsys.readouterr()

    assert "Unable to delete tag: tag1 while attached to scripts" in str(_excinfo.value)
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)

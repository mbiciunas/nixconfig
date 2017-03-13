import pytest

from libnix.exception.nix_error import NixError

from cli.tag import tag


def test_tag_create_no_tag(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        tag.tag("nixconfig", ["create"])

    _out, _err = capsys.readouterr()

    assert "2" in str(_excinfo.value), "Exception doesn't contain expected string"
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "the following arguments are required: tag, desc" in _err, "StdErr doesn't contain expected string"


def test_tag_create_no_desc(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        tag.tag("nixconfig", ["create", "newtag"])

    _out, _err = capsys.readouterr()

    assert "2" in str(_excinfo.value), "Exception doesn't contain expected string"
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "the following arguments are required: desc" in _err, "StdErr doesn't contain expected string"


def test_tag_create_existing_tag(capsys):
    with pytest.raises(NixError) as _excinfo:
        tag.tag("nixconfig", ["create", "tag1", "new tag"])

    _out, _err = capsys.readouterr()

    assert "Tag already exists: tag1" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)

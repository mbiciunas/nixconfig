import pytest

from libnix.exception.nix_error import NixError

from cli.tag import tag


def test_tag_rename_no_tag(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        tag.tag("nixconfig", ["rename"])

    _out, _err = capsys.readouterr()

    assert "2" in str(_excinfo.value), "Exception doesn't contain expected string"
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "the following arguments are required: tag, tag_new" in _err, "StdErr doesn't contain expected string"


def test_tag_rename_one_tag(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        tag.tag("nixconfig", ["rename", "tag1"])

    _out, _err = capsys.readouterr()

    assert "2" in str(_excinfo.value), "Exception doesn't contain expected string"
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "the following arguments are required: tag_new" in _err, "StdErr doesn't contain expected string"


def test_tag_rename_bad_tag(capsys):
    with pytest.raises(NixError) as _excinfo:
        tag.tag("nixconfig", ["rename", "badtag", "new tag"])

    _out, _err = capsys.readouterr()

    assert "Unknown tag: badtag" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_tag_rename_to_exist_tag(capsys):
    with pytest.raises(NixError) as _excinfo:
        tag.tag("nixconfig", ["rename", "tag1", "tag2"])

    _out, _err = capsys.readouterr()

    assert "New tag already exists: tag2" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_tag_rename_same(capsys):
    with pytest.raises(NixError) as _excinfo:
        tag.tag("nixconfig", ["rename", "tag1", "tag1"])

    _out, _err = capsys.readouterr()

    assert "Original and new tag names are the same: tag1" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_tag_rename_good_tag(capsys):
    tag.tag("nixconfig", ["rename", "tag1", "newtag"])

    _out, _err = capsys.readouterr()

    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)

    tag.tag("nixconfig", ["rename", "newtag", "tag1"])

    _out, _err = capsys.readouterr()

    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)

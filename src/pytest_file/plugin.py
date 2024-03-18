"""Main entrypoint for the pytest-file plugin."""

import uuid
from pathlib import Path

import pytest
from _pytest.fixtures import FixtureRequest


@pytest.fixture(scope="function")
def tmp_file_path(
    request: FixtureRequest, tmp_path: Path, tmp_file_name: str, tmp_file_content: str
) -> Path:
    """The path of the newly created tmp file."""
    tmp_file_path: Path = getattr(request, "param", tmp_path / tmp_file_name)
    tmp_file_path.write_text(tmp_file_content)
    return tmp_file_path


@pytest.fixture(scope="function")
def tmp_file_name(
    request: FixtureRequest, tmp_file_stem: str, tmp_file_extension: str
) -> str:
    """The file name that will be used in tmp_file_path."""
    return getattr(
        request, "param", ".".join([tmp_file_stem, tmp_file_extension.lstrip(".")])
    )


@pytest.fixture(scope="function")
def tmp_file_stem(request: FixtureRequest) -> str:
    """The file stem that will be used in tmp_file_name."""
    return getattr(request, "param", uuid.uuid4())


@pytest.fixture(scope="function")
def tmp_file_extension(request: FixtureRequest) -> str:
    """The file extension that will be used in tmp_file_name."""
    return getattr(request, "param", ".txt")


@pytest.fixture(scope="function")
def tmp_file_content(request: FixtureRequest) -> str:
    """The content that will be written in tmp_file_path."""
    return getattr(request, "param", uuid.uuid4())


@pytest.fixture(scope="function")
def tmp_file_content_path(request: FixtureRequest) -> Path:
    """The path to retrieve content from for tmp_file_content."""
    return getattr(request, "param", Path())

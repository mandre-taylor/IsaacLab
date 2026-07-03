# Copyright (c) 2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Shared pytest configuration for repository tests."""

import sys
from collections.abc import Generator
from pathlib import Path

import pytest

_TOOLS_DIR = Path(__file__).resolve().parent / "tools"
if _TOOLS_DIR.is_dir() and str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from testmon_subprocess_coverage import (  # noqa: E402, F401
    pytest_runtest_makereport,
    pytest_runtest_setup,
    pytest_runtest_teardown,
    pytest_sessionfinish,
    pytest_sessionstart,
)


@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> Generator[None, None, None]:
    """Keep tests marked ``always`` selected when Testmon filters the collection."""
    always_items = [item for item in items if item.get_closest_marker("always")]
    yield

    if config.getoption("testmon_forceselect", default=False):
        selected = set(items)
        items.extend(item for item in always_items if item not in selected)

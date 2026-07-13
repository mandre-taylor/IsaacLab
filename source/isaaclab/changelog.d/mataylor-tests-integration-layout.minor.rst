Changed
^^^^^^^

* Moved installation CI tests from ``source/isaaclab/test/install_ci/`` to
  ``tests/integration/install_ci/`` to clearly separate integration and
  installation tests from unit tests. Updated :mod:`tools.run_install_ci`,
  CI actions, and the Dockerfile entrypoint to reference the new location.
  The ``tests/integration/install_ci/`` suite retains its own ``pytest.ini``
  and ``conftest.py`` and is unchanged in behaviour.

* Declared ``torch``, ``warp-lang``, and ``scipy`` as explicit dependencies in
  ``source/isaaclab/config/extension.toml`` and ``scipy`` in
  ``source/isaaclab/pyproject.toml``. These packages were already used in
  production code and unit tests but were undeclared, making them silent
  transitive dependencies.

* Added a testing guideline to ``AGENTS.md`` requiring unit tests to only
  import packages declared in the package's ``config/extension.toml``; tests
  that need unlisted packages must either declare the dependency or be
  reclassified as integration tests.

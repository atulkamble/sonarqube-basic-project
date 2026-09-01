# test_app.py
# ============================================================
# SonarQube Coverage Practice
#
# Only selected functions are tested intentionally.
# Other functions remain uncovered.
# ============================================================

from app import add, divide


def test_add():
    assert add(10, 5) == 15


def test_divide():
    assert divide(10, 5) == 2

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
サンプルテス
"""

import re
from acme.semver import Semver
import pytest

class TestSemver():
    @pytest.mark.parametrize(['major', 'minor', 'patch', 'expected'], [
        (1, 4, 2, 1),
        (2, 5, 3, 2),
    ])
    def test_major(self, major, minor, patch, expected):
        semver = Semver(major, minor, patch)
        actual = semver.major

        assert expected == actual

    def test_semver142_minor4(self):

        semver = Semver(1, 4, 2)
        actual = semver.minor

        assert 4 == actual

    def test_semver142_patch2(self):

        semver = Semver(1, 4, 2)
        actual = semver.patch

        assert 2 == actual

    def test_semver142_str142(self):

        semver = Semver(1, 4, 2)
        actual = semver.to_string()

        assert actual == "1.4.2"


    def test_semver253_str253(self):

        semver = Semver(2, 5, 3)
        actual = semver.to_string()

        assert actual == "2.5.3"

    def test_semver142_eq_semver142(self):
        semver1 = Semver(1, 4, 2)
        semver2 = Semver(1, 4, 2)

        actual = semver1.equals(semver2)
        assert actual == True

    def test_semver142_eq_semver253(self):
        semver1 = Semver(1, 4, 2)
        semver2 = Semver(2, 5, 3)

        actual = semver1.equals(semver2)
        assert actual == False

    def test_bad_major_minus1(self):
        with pytest.raises(ValueError):
            semver1 = Semver(-1, 4, 2)

    def test_bad_minor_minus(self):
        with pytest.raises(ValueError):
            semver1 = Semver(1, -4, 2)

    def test_bad_patch_minus(self):
        with pytest.raises(ValueError):
            semver1 = Semver(1, 4, -2)

    def test_major_string(self):
        with pytest.raises(TypeError):
            semver = Semver("a", 4, 2)

    def test_minor_string(self):
        with pytest.raises(TypeError):
            semver = Semver(1, "a", 2)

    def test_patch_string(self):
        with pytest.raises(TypeError):
            semver = Semver(1, 4, "a")

    def test_update_patch_142(self):
        semver = Semver(1, 4, 2)
        actual = semver.upgrade_patch()

        expected = Semver(1, 4, 3)

        assert actual.equals(expected)

    def test_update_minor_142(self):
        semver = Semver(1, 4, 2)
        actual = semver.upgrade_minor()

        expected = Semver(1, 5, 0)

        assert actual.equals(expected)

    def test_update_major_142(self):
        semver = Semver(1, 4, 2)
        actual = semver.upgrade_major()

        expected = Semver(2, 0, 0)

        assert actual.equals(expected)

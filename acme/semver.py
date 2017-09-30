#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Semver():

    def __init__(self, major, minor, patch):

        args = [major, minor, patch]

        for arg in args:

            if(arg < 0):
                raise ValueError("minus is bad!")

            if type(arg) is not int:
                raise TypeError

        self.major = major
        self.minor = minor
        self.patch = patch

    def to_string(self):
        ret = str(self.major) + "." + str(self.minor) + "." + str(self.patch)
        return ret

    def equals(self, semver):
        return semver.to_string() == self.to_string()

    def upgrade_patch(self):
        upgraded = Semver(self.major, self.minor, self.patch + 1)

        return upgraded

    def upgrade_minor(self):
        upgraded = Semver(self.major, self.minor + 1, 0)

        return upgraded

    def upgrade_major(self):
        upgraded = Semver(self.major + 1, 0, 0)

        return upgraded
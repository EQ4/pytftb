#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jaidev <jaidev@newton>
#
# Distributed under terms of the MIT license.

"""Base class for tests."""

import unittest
import numpy as np
from scipy import angle


class TestBase(unittest.TestCase):

    def assert_is_linear(self, signal, decimals=5):
        """Assert that the signal is linear."""
        derivative = np.diff(signal)
        derivative = np.around(derivative, decimals)
        self.assertEqual(np.unique(derivative).shape[0], 1)

    def assert_is_analytic(self, signal, amlaw=None):
        """Assert that signal is analytic."""
        omega = angle(signal)
        if amlaw is not None:
            recons = np.exp(1j * omega) * amlaw
        else:
            recons = np.exp(1j * omega)
        real_identical = np.allclose(np.real(recons), np.real(signal))
        imag_identical = np.allclose(np.imag(recons), np.imag(signal))
        if not (imag_identical and real_identical):
            raise AssertionError("Signal is not analytic.")

    def assert_is_concave(self, signal):
        second_derivative = np.diff(np.diff(signal))
        if not np.all(second_derivative < 0):
            raise AssertionError("Signal is not concave.")

    def assert_is_convex(self, signal):
        second_derivative = np.diff(np.diff(signal))
        if not np.all(second_derivative > 0):
            raise AssertionError("Signal is not convex.")

    def assert_is_monotonic_increasing(self, signal):
        derivative = np.diff(signal)
        if not np.all(derivative >= 0):
            raise AssertionError("Signal is not monotonically increasing.")

    def assert_is_monotonic_decreasing(self, signal):
        derivative = np.diff(signal)
        if not np.all(derivative <= 0):
            raise AssertionError("Signal is not monotonically decreasing.")

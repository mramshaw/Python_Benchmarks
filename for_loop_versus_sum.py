#!/usr/bin/env python

# pylint: disable=C0103

"""Compare 'for loop' performance versus 'sum' performance."""

import gc

import benchmark


class Benchmark_For_loop(benchmark.Benchmark):
    """Benchmark 'for loop'."""

    each = 1000  # allows for differing number of runs

    def setUp(self):
        """Define the number of benchmarks to perform."""
        self.size = 25000

    def test_for_loop(self):
        """Sum with a 'for' loop."""
        total = 0
        for i in xrange(self.size):
            total += i
        assert total == 312487500
        return total


class Benchmark_Sum_with_xrange(benchmark.Benchmark):
    """Benchmark 'for loop'."""

    each = 1000  # allows for differing number of runs

    def setUp(self):
        """Define the number of benchmarks to perform."""
        self.size = 25000

    def test_sum_with_xrange(self):
        """Sum with built-in sum and range."""
        total = sum(xrange(self.size))
        assert total == 312487500
        return total


if __name__ == '__main__':
    gc.disable()
    benchmark.main(each=50000, format="markdown", numberFormat="%.4g")

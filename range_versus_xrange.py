#!/usr/bin/env python

# pylint: disable=C0103

"""Compare range performance versus xrange performance."""

import gc

import benchmark


class Benchmark_Range(benchmark.Benchmark):
    """Benchmark range allocation."""

    each = 100  # allows for differing number of runs

    def setUp(self):
        """Define the number of benchmarks to perform."""
        self.size = 25000

    def test_range(self):
        """Allocate the specified number of tuples."""
        for _ in range(self.size):
            _ = (j for j in range(1, 100))


class Benchmark_Xrange(benchmark.Benchmark):
    """Benchmark xrange allocation."""

    each = 100  # allows for differing number of runs

    def setUp(self):
        """Define the number of benchmarks to perform."""
        self.size = 25000

    def test_xrange(self):
        """Allocate the specified number of tuples."""
        for _ in xrange(self.size):
            _ = (j for j in xrange(1, 100))


if __name__ == '__main__':
    gc.disable()
    benchmark.main(each=500, format="markdown", numberFormat="%.4g")

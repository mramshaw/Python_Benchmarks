#!/usr/bin/env python

"""Compare tuple performance versus list performance."""

import benchmark


class Benchmark_Tuple(benchmark.Benchmark):
    """Benchmark tuple allocation."""

    each = 100  # allows for differing number of runs

    def setUp(self):
        """Define the number of benchmarks to perform."""
        self.size = 25000

    def test_tuple(self):
        """Allocate the specified number of tuples."""
        for _ in xrange(self.size):
            _ = (j for j in xrange(1, 100))


class Benchmark_List(benchmark.Benchmark):
    """Benchmark list allocation."""

    each = 100  # allows for differing number of runs

    def setUp(self):
        """Define the number of benchmarks to perform."""
        self.size = 25000

    def test_list(self):
        """Allocate the specified number of lists."""
        for _ in xrange(self.size):
            _ = [j for j in xrange(1, 100)]


if __name__ == '__main__':
    benchmark.main(each=500, format="markdown", numberFormat="%.4g")

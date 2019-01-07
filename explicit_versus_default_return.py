#!/usr/bin/env python

"""Compare explicit return performance versus default return performance."""

import benchmark


class Benchmark_Explicit_Return(benchmark.Benchmark):
    """Benchmark explicit return."""

    each = 1000  # allows for differing number of runs

    def setUp(self):
        """Define the number of benchmarks to perform."""
        self.size = 25000

    def test_explicit_return(self):
        """Allocate the specified number of explicit return calls."""
        for _ in range(self.size):
            self.explicit_return(1)

    def explicit_return(self, dummy):
        # Add a circular assigmnet so the compiler does not optimize away this function call
        x = dummy
        dummy = x
        return None


class Benchmark_Default_Return(benchmark.Benchmark):
    """Benchmark default return."""

    each = 1000  # allows for differing number of runs

    def setUp(self):
        """Define the number of benchmarks to perform."""
        self.size = 25000

    def test_default_return(self):
        """Perform the specified number of default return calls."""
        for _ in xrange(self.size):
            self.default_return(1)

    def default_return(self, dummy):
        # Add a circular assigmnet so the compiler does not optimize away this function call
        x = dummy
        dummy = x


if __name__ == '__main__':
    benchmark.main(each=5000, format="markdown", numberFormat="%.4g")

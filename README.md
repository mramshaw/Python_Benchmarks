# Python_Benchmarks

test out some general Python memes

## Rationale

A lot of things are stated in Python writings.

Lets test some of these assumptions.

We will use the Python [benchmark](http://pypi.org/project/benchmark/) package.

[It looks a little old, but as long as it does what's expected, that should be fine.]

There are performance-related alternatives to Python such as Cython, etc.

## To Run

Run the various tests as described below.

#### List versus Tuple

Type <kbd>python list_versus_tuple.py</kbd> as follows:

```bash
$ python list_versus_tuple.py

Benchmark Report
================

Benchmark List
--------------

name | rank | runs |    mean |      sd | timesBaseline
-----|------|------|---------|---------|--------------
list |    1 |  100 | 0.06516 | 0.00227 |           1.0

Benchmark Tuple
---------------

 name | rank | runs |     mean |        sd | timesBaseline
------|------|------|----------|-----------|--------------
tuple |    1 |  100 | 0.009221 | 0.0004186 |           1.0

Each of the above 200 runs were run in random, non-consecutive order by
`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.12
Linux-4.4.0-141-generic-x86_64 on 2019-01-06 19:06:14.

$
```

#### Range versus Xrange

Type <kbd>python range_versus_xrange.py</kbd> as follows:

```bash
$ python range_versus_xrange.py

Benchmark Report
================

Benchmark Range
---------------

 name | rank | runs |    mean |       sd | timesBaseline
------|------|------|---------|----------|--------------
range |    1 |  100 | 0.01897 | 0.001786 |           1.0

Benchmark Xrange
----------------

  name | rank | runs |    mean |       sd | timesBaseline
-------|------|------|---------|----------|--------------
xrange |    1 |  100 | 0.00911 | 3.19e-05 |           1.0

Each of the above 200 runs were run in random, non-consecutive order by
`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.12
Linux-4.4.0-141-generic-x86_64 on 2019-01-06 19:11:46.

owner@G30AB:~/Documents/Python/Python_Benchmarks$
```

## Conclusion

As is generally stated, `tuples` are in fact significantly faster than `lists`.

In addition to other supposed benefits, `xrange` siginificantly out-performs `range`
(at least for Python 2).

## Versions

* Python __2.7.12__

* benchmark __0.1.5__

## To Do

- [x] Ensure code conforms to `pylint`, `pycodestyle` and `pydocstyle` (at least as far as `benchmark` permits)
- [x] Add test for `range` versus `xrange`
- [ ] Add some more benchmarks

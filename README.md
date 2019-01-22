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

$
```

#### Explicit function return versus Default function return

Type <kbd>python explicit_versus_default_return.py</kbd> as follows:

```bash
$ python explicit_versus_default_return.py

Benchmark Report
================

Benchmark Default Return
------------------------

          name | rank | runs |     mean |        sd | timesBaseline
---------------|------|------|----------|-----------|--------------
default return |    1 | 1000 | 0.002304 | 1.142e-05 |           1.0

Benchmark Explicit Return
-------------------------

           name | rank | runs |    mean |        sd | timesBaseline
----------------|------|------|---------|-----------|--------------
explicit return |    1 | 1000 | 0.00233 | 0.0002527 |           1.0

Each of the above 2000 runs were run in random, non-consecutive order by
`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.12
Linux-4.4.0-141-generic-x86_64 on 2019-01-07 18:09:31.


$
```
## Conclusion

As is generally stated, `tuples` are in fact significantly faster than `lists`.

[Note that tuples and lists are not interchangeable - lists are mutable whereas
 tuples are immutable (cannot be changed after their initial allocation). But
 for many uses - such as ___value objects___ - tuples are fine.]

In addition to other benefits (such as avoiding memory errors), `xrange`
significantly outperforms `range` (at least for Python 2).

In terms of performance, an explicit function return is pretty much the same
thing as a defaulted function return (the timing differences are really too
close to call).

## Versions

* Python __2.7.12__

* benchmark __0.1.5__

## To Do

- [x] Ensure code conforms to `pylint`, `pycodestyle` and `pydocstyle` (at least as far as `benchmark` permits)
- [x] Add test for `range` versus `xrange`
- [x] Add test for Explicit function return versus Default function return
- [ ] Find an alternative for Python 3; also memory profiling
- [ ] Add some more benchmarks

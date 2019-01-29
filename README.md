# Python_Benchmarks

[![Known Vulnerabilities](http://snyk.io/test/github/mramshaw/Python_Benchmarks/badge.svg?style=plastic&targetFile=requirements.txt)](http://snyk.io/test/github/mramshaw/Python_Benchmarks?style=plastic&targetFile=requirements.txt)

test out some general Python memes

The contents are as follows:

* [Rationale](#rationale)
* [Premature Optimization](#premature-optimization)
* [Memory Profiling](#memory-profiling)
* [Garbage Collection](#garbage-collection)
    * [With the default behaviour (GC under runtime control)](#with-the-default-behaviour-gc-under-runtime-control)
    * [With GC disabled](#with-gc-disabled)
    * [Difference](#difference)
* [To Run](#to-run)
    * [List versus Tuple](#list-versus-tuple)
    * [Range versus Xrange](#range-versus-xrange)
    * [Explicit function return versus Default function return](#explicit-function-return-versus-default-function-return)
    * [For loop summation versus Sum function](#for-loop-summation-versus-sum-function)
* [Conclusion](#conclusion)
* [Versions](#versions)
* [To Do](#to-do)

## Rationale

A lot of things are stated in Python writings.

Lets test some of these assumptions.

We will use the Python [benchmark](http://pypi.org/project/benchmark/) package.

[It looks a little old, but as long as it does what's expected, that should be fine.]

There are performance-related alternatives to Python such as Cython, etc.

But perhaps the ___best___ strategy is to not run performance-critical code in Python.

## Premature Optimization

> We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.

[Sir Charles Antony Richard Hoare FRS FREng](http://en.wikipedia.org/wiki/Tony_Hoare)

My personal feeling is that the time to start optimizing is when you have identified a performance problem.

[Wikipedia has it that Tony Hoare invented __quicksort__ in 1959/1960, so the next time you are asked at an interview
 to whiteboard a sort algorithm you might ask them why they are asking you to reinvent the wheel. And a stone-age wheel
 at that. Reference the [DRY principle](http://en.wikipedia.org/wiki/Don't_repeat_yourself) for bonus points.]

## Memory Profiling

Simply profiling run time (without factoring in memory usage) is not a very useful statistic.

However, memory profiling in Python is not always easy or very precise, as the Python interpreter handles memory management.

There are effective performance optimizations (such as enabling a JIT compiler with [numba](http://numba.pydata.org/)).

In general, my experience has been that benchmarking with JIT compilers is unreliable.

Even a good optimizing compiler can make comparative benchmarking troublesome.

## Garbage Collection

Garbage Collection is controlled by the Python runtime - however, the random nature of
GC can give rise to unexpected slowdowns at inopportune times. So we will take a leaf
from the [timeit code](http://github.com/python/cpython/blob/3.7/Lib/timeit.py) and
disable GC while our benchmarks are running.

This will probably result in a more useful graph of memory usage, as no memory should
be reclaimed while our benchmarks are being run.

Interestingly, this simple optimization results in an immediate improvement in our
benchmark run times.

#### With the default behaviour (GC under runtime control)

```bash
$ python list_versus_tuple.py

Benchmark Report
================

Benchmark List
--------------

name | rank | runs |    mean |     sd | timesBaseline
-----|------|------|---------|--------|--------------
list |    1 |  100 | 0.06922 | 0.0126 |           1.0

Benchmark Tuple
---------------

 name | rank | runs |     mean |        sd | timesBaseline
------|------|------|----------|-----------|--------------
tuple |    1 |  100 | 0.009339 | 1.175e-05 |           1.0

Each of the above 200 runs were run in random, non-consecutive order by
`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.12
Linux-4.4.0-141-generic-x86_64 on 2019-01-29 16:05:14.

$
```

Mean __0.06922__ and Std. Dev. __0.0126__, Mean __0.009339__ and Std. Dev. __1.175e-05__.

#### With GC disabled

```bash
$ python list_versus_tuple.py

Benchmark Report
================

Benchmark List
--------------

name | rank | runs |    mean |       sd | timesBaseline
-----|------|------|---------|----------|--------------
list |    1 |  100 | 0.06467 | 0.003457 |           1.0

Benchmark Tuple
---------------

 name | rank | runs |    mean |        sd | timesBaseline
------|------|------|---------|-----------|--------------
tuple |    1 |  100 | 0.00926 | 0.0007694 |           1.0

Each of the above 200 runs were run in random, non-consecutive order by
`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.12
Linux-4.4.0-141-generic-x86_64 on 2019-01-29 16:06:05.

$
```

Mean __0.06467__ and Std. Dev. __0.003457__, Mean __0.00926__ and Std. Dev. __0.0007694__.

#### Difference

Test | Before / After | Mean | Std. Dev. | Mean | Std. Dev. | Results
---- | -------------- | ---- | --------- | ---- | --------- | -------
List versus Tuple | Usual GC | 0.06922 | 0.0126 | 0.009339 | 1.175e-05
List versus Tuple | GC Off | 0.06467 | 0.003457 | 0.00926 | 0.0007694 | Slight decrease in both exection times; increase in entropy in both cases
Range versus Xrange | Usual GC | 0.01832 | 0.0001215 | 0.009139 | 6.165e-05
Range versus Xrange | GC Off | 0.01963 | 0.0002059 | 0.009128 | 6.597e-05 | Slight increase in `range` execution time; no change in in `xrange` execution time
Explicit return versus Default return | Usual GC | 0.003286 | 2.28e-05 | 0.003344 | 0.0002187
Explicit return versus Default return | GC Off | 0.00336 | 6.077e-05 | 0.003483 | 0.0001302 | Slight increase in both execution times; entropy moot
For loop summation versus Sum function | Usual GC | 0.0006326 | 8.786e-05 | 0.0001356 | 8.84e-07
For loop summation versus Sum function | GC Off | 0.0006081 | 1.367e-05 | 0.0001352 | 2.186e-06 | Slight increase `for loop` execution time; slight increase in `sum` entropy

I am reading the Standard Deviation of the results as a measure of execution entropy.

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

#### For loop summation versus Sum function

Type <kbd>python for_loop_versus_sum.py</kbd> as follows:

```bash
$ python for_loop_versus_sum.py

Benchmark Report
================

Benchmark For loop
------------------

    name | rank | runs |      mean |        sd | timesBaseline
---------|------|------|-----------|-----------|--------------
for loop |    1 | 1000 | 0.0005747 | 3.312e-06 |           1.0

Benchmark Sum with xrange
-------------------------

           name | rank | runs |      mean |        sd | timesBaseline
----------------|------|------|-----------|-----------|--------------
sum with xrange |    1 | 1000 | 0.0001355 | 1.347e-06 |           1.0

Each of the above 2000 runs were run in random, non-consecutive order by
`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.12
Linux-4.4.0-141-generic-x86_64 on 2019-01-25 21:34:59.

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

Using the `sum` primitive is more efficient and less error-prone (being fewer
lines of code) than a `for` loop.

## Versions

* Python __2.7.12__

* benchmark __0.1.5__

## To Do

- [x] Ensure code conforms to `pylint`, `pycodestyle` and `pydocstyle`
- [x] Add `pylint` exemptions for `benchmark` coding standards
- [x] Disable Garbage Collection for duration of benchmarks
- [x] Add test for `range` versus `xrange`
- [x] Add test for Explicit function return versus Default function return
- [x] Add test for For loop versus Sum
- [x] Add a Snyk.io vulnerability scan badge
- [ ] Find an alternative for Python 3; also memory profiling
- [ ] Add some more benchmarks

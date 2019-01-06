# Python_Benchmarks

test out some general Python memes

## Rationale

A lot of things are stated in Python writings.

Lets test some of these assumptions.

We will use the Python [benchmark](http://pypi.org/project/benchmark/) package.

[It looks a little old, but as long as it does what's expected, that should be fine.]

There are performance-related alternatives to Python such as Cython, etc.

## To Run

Type <kbd>python benchmarks.py</kbd> as follows:

```bash
$ python benchmarks.py 

Benchmark Report
================

Benchmark List
--------------

name | rank | runs |    mean |       sd | timesBaseline
-----|------|------|---------|----------|--------------
list |    1 |  100 | 0.07345 | 0.000233 |           1.0

Benchmark Tuple
---------------

 name | rank | runs |    mean |        sd | timesBaseline
------|------|------|---------|-----------|--------------
tuple |    1 |  100 | 0.01828 | 0.0001126 |           1.0

Each of the above 200 runs were run in random, non-consecutive order by
`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.12
Linux-4.4.0-141-generic-x86_64 on 2019-01-06 18:06:12.

$
```

[Currently only tests `tuple` versus `List` performance.]

## Conclusion

As is generally stated, `tuples` are in fact significantly faster than `lists`.

## Versions

* Python __2.7.12__

* benchmark __0.1.5__

## To Do

- [x] Ensure code conforms to `pylint`, `pycodestyle` and `pydocstyle` (at least as far as `benchmark` permits)
- [ ] Add some more benchmarks

# Poisson-Solver

Simple test program which solve the Poisson equation on a grid using a parallel implementation of the Gauss-seidel method. The
code is written in modern fortran and supports multithreading or GPU offloading via directives.

Directives have been written in both openACC and openMP.

The following spack install options with select which implementation is used and whether gpu support is built.

```
spack install poisson-solver@main+openmp       # for threaded version using openMP directives
spack install poisson-solver@main+openacc      # for threaded version using openACC directives
spack install poisson-solver@main+gpu+openmp   # for GPU version using openMP directives
spack install poisson-solver@main+gpu+openacc  # for GPU version using openACC directives
```

## Supported Compilers

* `nvfortran`
* `gfortran >= version 11`

## Usage

From the top-level directory of the repository, you can run the benchmarks with

```sh
reframe -c benchmarks/apps/poisson-solver -r --performance-report -S spack_spec='poisson-solver@main+openmp'
```

To select the number of threads use the `-S num_threads=4` option

```sh
reframe -c benchmarks/apps/poisson-solver -r --performance-report -S num_threads=4 -S spack_spec='poisson-solver@main+openmp'
```

<!-- ## Filtering the benchmarks -->

<!-- By default all benchmarks will be run. You can run individual benchmarks with the -->
<!-- [`--tag`](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#cmdoption-0) option: -->

<!-- * `scaling` to run scaling benchmarks -->

<!-- Examples: -->

<!-- ```sh -->
<!-- reframe -c benchmarks/apps/poisson-solver -r --performance-report --tag single-node -->
<!-- ``` -->

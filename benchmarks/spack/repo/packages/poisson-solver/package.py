# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PoissonSolver(CMakePackage):
    """Parallel test code written by Tom Meltzer for testing offloading
    directives.

    Supports GPU offloading and threading with either openMP or openACC.
    """

    homepage = "https://github.com/TomMelt/Poisson-Solver"
    git = "https://github.com/TomMelt/Poisson-Solver.git"

    maintainers = ["TomMelt"]

    version("main", branch="main")

    variant("usegs", default=True, description="enable use of parallel Gauss-Seidel method")
    variant("openmp", default=True, description="enable use of openMP directives")
    variant("openacc", default=False, description="enable use of openACC directives")
    variant("gpu", default=False, description="enable GPU offloading via directives")

    executables = [r"solver"]

    conflicts("+openacc", when="+openmp")

    depends_on("cmake@3.20:", type="build")
    depends_on("lapack", when="~usegs")

    def cmake_args(self):

        spec = self.spec

        args = [
                f"-D CMAKE_C_COMPILER={spack_cc}",
                f"-D CMAKE_Fortran_COMPILER={spack_fc}",
                ]

        if "+usegs" in spec:
            args.append("-D USEGS=ON")

        if "+openacc" in spec:
            args.append("-D USEACC=ON")

        if "+gpu" in spec:
            args.append("-D USEGPU=ON")

        print("args = \n", args)

        return args

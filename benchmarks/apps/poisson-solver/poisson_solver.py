import os.path as path
import reframe as rfm
import reframe.utility.sanity as sn
from benchmarks.modules.utils import SpackTest


@rfm.simple_test
class Poisson(SpackTest):

    descr = 'Base class for poisson-solver'
    valid_systems = ['*']
    valid_prog_environs = ['default']
    time_limit = '0d0h1m0s'
    spack_spec = 'poisson-solver'
    executable = 'solver'
    executable_opts = ['200 100000']

    num_threads = variable(int, value=0)
    N = variable(int, value=200)
    max_iter = variable(int, value=100000)

    reference = {
            '*': {
                'diagonlization': (200, None, None, 'seconds'),
                },
            }

    @run_after('setup')
    def set_job_script_variables(self):

        proc_info = self.current_partition.processor
        if (self.num_threads == 0):
            self.num_threads = proc_info.num_cpus

        self.executable_opts = [f'{self.N} {self.max_iter}']

        self.env_vars['OMP_NUM_THREADS'] = self.num_threads
        self.env_vars['OMP_PLACES'] = 'cores'

    @run_before('compile')
    def setup_build_system(self):
        self.spack_spec = self.spack_spec
        self.build_system.specs = [self.spack_spec]

    @sanity_function
    def validate_successful_run(self):
        return sn.assert_found(r'finished', self.stdout)

    @performance_function('seconds', perf_key='walltime')
    def extract_elapsed_time(self):
        return sn.extractsingle(r'time \(s\) =\s+(\S+)\s', self.stdout, 1, float)

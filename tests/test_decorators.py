import unittest
from time import sleep

from os import getcwd
from sys import path
path.append(getcwd())

from imports.my_decorators import *


class Test_Decorators(unittest.TestCase):


    def test_count_executions(self):
        
        @count_executions_of(return_executions=True)
        def execution_dummy():
            pass

        for i in range(1, 20):
            void, executions = execution_dummy()
            self.assertEqual(executions, i)


    def test_exit_after(self):
        
        @exit_after(1)
        def slow_dummy():
            sleep(2)
            return 'this should not be returned'

        @exit_after(1)
        def fast_dummy():
            sleep(0.1)
            return 'this should be returned'

        with self.assertRaises(KeyboardInterrupt):
            slow_dummy()
        
        ret = fast_dummy()
        self.assertEqual(ret, 'this should be returned')


    def test_timer(self):
        
        @timer(return_time=True)
        def timer_dummy():
            sleep(1)

        for i in range(2):
            void, elapsed = timer_dummy()
            self.assertAlmostEqual(1, elapsed, places=2)


    def test_recursive_timer(self):
        
        @recursive_timer
        def recursive_dummy(depth=2):
            if depth:
                sleep(1)
                return recursive_dummy(depth-1)
            else:
                return None
        
        recursive_dummy.return_time = True
        void, elapsed = recursive_dummy()
        
        self.assertAlmostEqual(2, elapsed, places=2)


if __name__ == '__main__':
    unittest.main()
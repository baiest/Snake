from unittest import TestLoader, TestSuite, TextTestRunner
from InicializacionTest import InicializacionTest
from ViewTest import ViewTest

def suite(modules):
    suite = TestSuite()
    for module in modules:
        suite.addTest(TestLoader().loadTestsFromTestCase(module))

    return suite

if __name__ == '__main__':
    pool_test = suite([
        InicializacionTest,
        ViewTest
    ])
    runner = TextTestRunner(verbosity=2)
    dir(runner.run(pool_test))
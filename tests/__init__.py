import random
import time
import unittest


def unique_id(name):
    """
    Generate a unique ID that includes the given name,
    a timestamp and a random number. This helps when running
    integration tests in parallel that must create remote
    resources.
    """
    return f'{name}-{int(time.time())}-{random.randint(0, 10000)}'

if __name__ == '__main__':
    suite = unittest.TestLoader().discover('.', pattern = "test*.py")
    unittest.TextTestRunner(verbosity=2).run(suite)
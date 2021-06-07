import unittest
from unittest.main import main
from check_hostname import checkhostname

class TestCheckHostname(unittest.TestCase):

    def test_checkhostname(self):
        self.assertEqual(checkhostname('foo'), 'UNKNOWN')
        self.assertEqual(checkhostname('cont-0m03-0004d'), 'EliteDesk 800 G1 USDT')
        self.assertEqual(checkhostname('CONT-0M03-0004D'), 'EliteDesk 800 G1 USDT')
        self.assertEqual(checkhostname('CONT0M030004d'), 'UNKNOWN')

if __name__ == '__main__':
    unittest.main()

import unittest
from letsbank import Transaction

class TransactionTest(unittest.TestCase):

    def test_note(self):
        # note must be < 255 characters:
        Transaction(note="x" * 255)
        self.assertRaises(ValueError, Transaction, note="x" * 256)


if __name__=="__main__":
    unittest.main()

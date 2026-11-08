import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import check

def row(h, enc, method=""):
    return {"host": h, "encrypted": enc, "method": method}

class TestEncryption(unittest.TestCase):
    def test_encrypted(self):
        self.assertEqual(check([row("PC-1", "yes", "BitLocker")])[0][2], "ENCRYPTED")
    def test_method_unknown(self):
        self.assertEqual(check([row("PC-1", "yes", "")])[0][2], "METHOD UNKNOWN")
    def test_not_encrypted(self):
        self.assertEqual(check([row("PC-1", "no", "")])[0][2], "NOT ENCRYPTED")
    def test_not_encrypted_first(self):
        r = check([row("A", "yes", "BitLocker"), row("B", "no", "")])
        self.assertEqual(r[0][0], "B")

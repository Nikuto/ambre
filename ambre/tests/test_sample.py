from . import TestCaseApi

class TestToto(TestCaseApi):
    def test_toto(self):
        """Test to ensure everything is running well"""
        self.assertEqual('bite', 'bite')

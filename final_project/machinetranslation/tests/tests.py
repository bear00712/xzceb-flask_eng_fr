import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishtoFrench(unittest.TestCase): 
    def test_englishToFrench(self):         
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')   
        self.assertEqual(englishToFrench(''), '')

class TestFrenchtoEnglish(unittest.TestCase): 
    def test_frenchToEnglish(self): 
        
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')    
        self.assertEqual(frenchToEnglish(''), '')

unittest.main()





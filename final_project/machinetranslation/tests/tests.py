import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishtoFrench(unittest.TestCase): 
    def test_englishToFrench(self):         
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')   
class TestEnglishtoFrench2(unittest.TestCase): 
    def test_englishToFrench(self):         
        self.assertNotEqual(englishToFrench('Hello'), 'Bonjouro') 

class TestFrenchtoEnglish(unittest.TestCase): 
    def test_frenchToEnglish(self):         
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')    
class TestFrenchtoEnglish2(unittest.TestCase): 
    def test_frenchToEnglish(self):         
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Helloo')  

unittest.main()





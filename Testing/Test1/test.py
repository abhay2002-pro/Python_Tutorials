import unittest
import main


class TestMain(unittest.TestCase):

    def setUp(self):
        print('about to test a function')

    def test_do_stuff1(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 50)

    def test_do_stuff2(self):
        test_param = 'sssks'
        result = main.do_stuff(test_param)
        self.assertEqual(isinstance(result,ValueError), True)
        self.assertTrue(isinstance(result,ValueError))
    
    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertTrue(result, 'please enter a number')

    def tearDown(self):
        print('cleaning up')
if __name__ == '__main__':
    unittest.main()

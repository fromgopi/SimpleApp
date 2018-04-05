import unittest
import app

class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.testApp = app.app.test_client()
        self.testApp.testing = True

    def testPage(self):
        home = self.testApp.get('/')
        self.assertIn('Home Page', str(home.data))


if __name__ == "__main__":
    unittest.main()
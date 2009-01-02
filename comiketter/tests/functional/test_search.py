from comiketter.tests import *

class TestSearchController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='search'))
        # Test response...

import unittest
from relaty import Relaty
import io


class TestRelaty(unittest.TestCase):

    def test_yaml_is_loaded_correctly(self):
        document = """
        title: Un título
        """
        relat = Relaty(document)

        # Assert the story is a dict
        self.assertIsInstance(relat.story, dict)

    def test_story_should_have_a_title_attribute(self):
        document = """
        otro: otro 
        """

        self.assertRaises(AttributeError, Relaty, document)

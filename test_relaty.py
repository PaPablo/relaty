import unittest

from relaty import Relat


class TestRelaty(unittest.TestCase):

    def setUp(self):
        super()

        document = """
        title: A title
        screens:
            - Hello, how are you?
            - These are two screens
        options:
            - title: option 1
              screens:
                - option 1 screen 1
                - option 1 screen 2
              options:
                - title: option 1.1
                  screens:
                    - option 1.1 screen 1
                    - option 1.1 screen 2
                    - FIN
                - title: option 1.2
                  screens:
                    - option 1.2 screen 1
                    - option 1.2 screen 2
                  options:
                    - title: option 1.2.1
                      screens:
                        - option 1.2.1 screen 1
                        - option 1.2.1 screen 2
                        - FIN
                    - title: option 1.2.2
                      screens:
                        - option 1.2.2 screen 1
                        - option 1.2.2 screen 2
                        - FIN
            - title: Option 2
              screens:
                - option 2 screen 1
                - option 2 screen 2
                - FIN
        """

        self.relat = Relat(document)
        self.story = self.relat.story

    def test_story_should_have_a_title(self):
        document = """
        otro:otro
        """
        self.assertRaises(TypeError, Relat, document)

    def test_screens_are_created_correctly(self):

        # Screens are created correctly
        self.assertEqual(len(self.story.screens), 2)

    def test_options_are_created_correctly(self):
        self.assertEqual(len(self.story.options), 2)

    def test_cant_create_relat_with_invalidid_options(self):
        failed_document = """
        no: tienen
        sentido: estos
        cosos: no?
        """

        self.assertRaises(TypeError, Relat, failed_document)

    def test_relat_has_correct_number_of_endings(self):
        expected_endings = 4
        actual_endings = self.relat.get_number_endings

        self.assertEqual(expected_endings, actual_endings)

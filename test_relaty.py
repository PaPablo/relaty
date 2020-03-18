import unittest
from yaml import safe_load

from components.relat import Relat, Story


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

        converted_document = safe_load(document)
        self.relat_from_document = Relat.create_from_document(
            converted_document)
        self.story_from_document = self.relat_from_document.story

        relat_title = "A test Relat"
        self.empty_relat = Relat(title=relat_title)

    def test_story_should_have_a_title(self):
        document = """
        otro:otro
        """
        self.assertRaises(TypeError, Relat.create_from_document, document)

    def test_screens_are_created_correctly(self):

        # Screens are created correctly
        self.assertEqual(len(self.story_from_document.screens), 2)

    def test_options_are_created_correctly(self):
        self.assertEqual(len(self.story_from_document.options), 2)

    def test_cant_create_relat_with_invalidid_options(self):
        failed_document = """
        no: tienen
        sentido: estos
        cosos: no?
        """

        self.assertRaises(
            TypeError, Relat.create_from_document, failed_document)

    def test_relat_has_correct_number_of_endings(self):
        expected_endings = 4
        actual_endings = self.relat_from_document.get_number_endings

        self.assertEqual(expected_endings, actual_endings)

    def test_can_create_empty_relat(self):
        self.assertEqual(self.empty_relat.title, "A test Relat")

    def test_a_screens_can_be_added_to_story(self):
        screens = [
            "Screen 1",
            "Screen 2"
        ]

        for screen in screens:
            self.empty_relat.add_screen(screen)

        self.assertEqual(len(self.empty_relat.screens), 2)

        for actual, expected in zip(screens, self.empty_relat.screens):
            self.assertEqual(actual, expected)

    def test_an_option_can_be_added_to_relat(self):
        self.empty_relat.add_screen("A screen")

        self.empty_relat.add_option(
            Story(
                title="Option 1"
            )
        )

        # Test the option was added
        self.assertEqual(
            len(self.empty_relat.options),
            1
        )

        # Test the added option has the given title
        self.assertEqual(
            self.empty_relat.options[0].title,
            "Option 1"
        )

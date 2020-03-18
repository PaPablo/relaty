from components.story import Story


class Relat():

    story: Story

    def __init__(self, title, *args, **kwargs):
        self.story = Story(title)

    @classmethod
    def create_from_document(cls, document):
        story = Story(**document)

        instance = cls(story.title)
        instance.story = story

        return instance

    @property
    def get_number_endings(self):
        """Get the number of endings of the story
        """
        return self.story.get_number_endings

    @property
    def title(self):
        return self.story.title

    @property
    def screens(self):
        return self.story.screens

    @property
    def options(self):
        return self.story.options

    def add_screen(self, screen: str):
        self.story.add_screen(screen)

    def add_option(self, option: Story):
        self.story.add_option(option)

    def play(self):
        self.story.play()

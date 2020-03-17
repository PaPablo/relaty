import yaml
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

    def play(self):
        self.story.play()

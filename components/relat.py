import yaml
from components.story import Story


class Relat():

    story: Story

    def __init__(self, stream, *args, **kwargs):
        loaded_yaml = yaml.safe_load(stream)
        self.story = Story(**loaded_yaml)

    @property
    def get_number_endings(self):
        """Get the number of endings of the story
        """
        return self.story.get_number_endings

    def play(self):
        self.story.play()

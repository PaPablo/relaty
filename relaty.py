import yaml
import typing


class Story():
    title: str

    def __init__(self, title: str):
        self.title = title


class Relaty():

    story: typing.Dict

    def __init__(self, stream, *args, **kwargs):
        self.story = yaml.safe_load(stream)

        if not 'title' in self.story.keys():
            raise AttributeError('I need a title')

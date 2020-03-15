import yaml
import typing


class Story():
    title: str
    screens: typing.List[str]
    options: typing.Union[typing.List['Story'], None]

    def __init__(
            self,
            title: str,
            screens: typing.List[str],
            options: typing.Union[typing.List[typing.Dict], None] = None,
    ):

        self.title = title
        self.screens = screens

        if options is not None:
            self.options = [Story(**option) for option in options]
        else:
            self.options = options

    @property
    def get_number_endings(self):
        if self.options is None:
            return 1
        else:
            return sum([option.get_number_endings for option in self.options])


class Relaty():

    story: Story

    def __init__(self, stream, *args, **kwargs):
        loaded_yaml = yaml.safe_load(stream)

        self.story = Story(**loaded_yaml)

    @property
    def get_number_endings(self):
        return self.story.get_number_endings

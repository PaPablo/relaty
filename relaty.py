import yaml
import typing
import click


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
        """Get the number of endings of the Story
        """
        if self.options is None:
            return 1
        else:
            return sum([option.get_number_endings for option in self.options])

    def display_options(self):
        if self.options is None:
            return

        for number, option in enumerate(self.options):
            print(f'{number+1} - {option.title}')

        try:
            option_number = int(input("Input option number: "))

            if option_number < 1 or option_number > len(self.options):
                raise ValueError

            return option_number
        except ValueError:
            print("The input wasn't valid, try again")
            self.display_options()

    def play(self):
        # Print title
        print(self.title)

        # Print each screen
        for s in self.screens:
            print(s)
            input("Print any key to continue...")

        option_number = self.display_options()

        self.options[option_number-1].play()


class Relaty():

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


@click.group()
def relaty():
    pass


@click.command(help="Play a story")
@click.argument("story_path")
def play(story_path):
    file = open(story_path)
    relat = Relaty(file)

    relat.play()


relaty.add_command(play)

if __name__ == "__main__":
    relaty()

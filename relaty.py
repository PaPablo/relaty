import click
from relat import Relat


@click.group()
def relaty():
    pass


@click.command(help="Play a story")
@click.argument("story_path")
def play(story_path):
    file = open(story_path)
    relat = Relat(file)

    relat.play()


relaty.add_command(play)

if __name__ == "__main__":
    relaty()

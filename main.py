import yaml
from pprint import pprint

def main():
    with open('story.yml') as story:
        story = yaml.load(story)

        pprint(story)

if __name__ == "__main__":
    main()
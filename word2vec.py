"""Text conversion to word2vec and associated helpers."""


class Word2Vec:
    """Generation of work2vec for words in a paragraph."""

    def reduce_paragraph(self, paragraph: str) -> dict:
        """Split words in paragraph to individual words in dict."""
        paragraph = paragraph.strip('“').strip('”').strip(',').strip('.')
        word_list = paragraph.split(' ')
        word_dict = {}
        for i, word in enumerate(word_list):
            word_dict[i] = word

        return word_dict


if __name__ == '__main__':
    word2vec = Word2Vec()
    word2vec.reduce_paragraph(
        "“I’ll go in first to check it out”, Ar said. He squeezed under the door and found"
        " piles of boxes there. The space was tightly packed, without much space to move."
        " “Come ladies.” He peeked back out and helped Celeste in as she couldn’t reach"
        " down without letting go of her handhold. They all sat with their knees pulled"
        " towards their chests, cramped, but they were finally able to take a breather."
        " “These spurious bumps are rather uncomfortable, ladies”, said Ar after a few"
        " minutes of turns and halts. “I’m going to take a quick look to see where we"
        " are.” He lay on his stomach and poked his head out under the door and perceived"
        " an unfamiliar street, with sparse traffic but appeared to be closer to the"
        " centre of town. “Let’s see if I can work out our position from the sun and the"
        " street signs. Westbrooke, we’re no longer heading towards the East Gate. That’s"
        " not good. Hey guys, there’s a man with a hat and trenchcoat at the street"
        " corner. I think he just saw me. He looked like one of ‘them’”. Celeste looked"
        " bewildered, yet Christie was rather calm and composed."
    )


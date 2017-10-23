from nltk.corpus import wordnet as wn
import nltk
import random

try:
    # Check to see if data already exists
    nltk.data.find('corpora/wordnet')
    print('Wordnet data found at ' + str(nltk.data.path[len(nltk.data.path) - 1]))
except LookupError:
    # if data doesn't exist, download it
    print('Wordnet data needs to be downloaded...')
    nltk.download('wordnet')

# dictionary to hold parts of speech by abbreviations
POS = {
    'v': 'verbs',
    'a': 'adjectives',
    'n': 'nouns',
    'r': 'adverbs'
}

# a dictionary to hold lists of words, indexed by part of speech
pos_lists = {
    'nouns': [],
    'verbs': [],
    'adjectives': [],
    'adverbs': []
}


# strips underscores from multi-word phrases
def strip_underscores(word):
    temp = word.name().split('_')
    temp_word = ''
    for x in temp:
        if x != temp[-1]:
            temp_word += x + ' '
        else:
            temp_word += x
    return temp_word


def pop_pos_lists():
    """
    populates each list in the parts of speech dictionary
    """
    for key in POS:
        count = 0
        for ss in list(wn.all_synsets(key)):
            for element in ss.lemmas():
                count += 1
                if '_' in element.name():
                    temp_word = strip_underscores(element)
                    pos_lists[POS[key]].append(temp_word)
                else:
                    pos_lists[POS[key]].append(element.name())
        print(str(count) + ' ' + POS[key] + ' loaded...')


def get_rand_of_type(pos_list):
    """
    gets a random word from the given list
    :param pos_list:
    :return a word:
    """
    return pos_list[random.randrange(len(pos_list))]


def beat_model():
    """
        poem is of form:
            adjective noun verb
            verb noun verb
            adverb noun verb
    :return: beat string
    """
    poem = '' \
           + get_rand_of_type(pos_lists['adjectives']).capitalize() \
           + ' ' + get_rand_of_type(pos_lists['nouns']) \
           + ' ' + get_rand_of_type(pos_lists['verbs']) + '\n'

    poem += get_rand_of_type(pos_lists['verbs']).capitalize() + ' ' \
            + 'the ' + get_rand_of_type(pos_lists['nouns']) + ' ' \
            + get_rand_of_type(pos_lists['verbs']) + '\n'

    poem += get_rand_of_type(pos_lists['nouns']).capitalize() + ', ' \
            + get_rand_of_type(pos_lists['nouns']) + ' ' \
            + get_rand_of_type(pos_lists['verbs']) + '.\n'

    return poem


def setup():
    print('Loading dictionaries...')
    pop_pos_lists()


def display_poem():
    print('\nHere\'s your beat poem:\n')
    print(beat_model())


if __name__ == "__main__":
    setup()
    display_poem()

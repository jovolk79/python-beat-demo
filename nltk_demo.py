from nltk.corpus import wordnet as wn
import nltk
import random

try:
    # Check to see if data already exists
    nltk.data.find('corpora/wordnet')
    print('Wordnet data found at ' + str(nltk.data.path[len(nltk.data.path)-1]))
except LookupError:
    # if data doesn't exist, download it
    print('Wordnet data needs to be downloaded...')
    nltk.download('wordnet')

# dictionary to hold parts of speech by abbreviations
"""
POS = {
    'v': 'verb',
    'a': 'adjective',
    'n': 'noun',
    'r': 'adverb'
}
"""

nouns = []
verbs = []
adjectives = []
adverbs = []

verbose = True

def strip_underscores(elts):
    temp = elts.name().split('_')
    temp_word = ''
    for x in temp:
        if x != temp[-1]:
            temp_word += x + ' '
        else:
            temp_word += x
    return temp_word


def pop_nouns():
    count = 0
    for ss in list(wn.all_synsets('n')):
        for elts in ss.lemmas():
            count += 1
            # print(elts.name())
            if '_' in elts.name():
                temp_word = strip_underscores(elts)
                nouns.append(temp_word)
            else:
                nouns.append(elts.name())
    print(str(count) + ' nouns loaded.')


def pop_verbs():
    count = 0
    for ss in list(wn.all_synsets('v')):
        count += 1
        for elts in ss.lemmas():
            # print(elts.name())
            if '_' in elts.name():
                temp_word = strip_underscores(elts)
                verbs.append(temp_word)
            else:
                verbs.append(elts.name())
    print(str(count) + ' verbs loaded.')


def pop_adj():
    count = 0
    for ss in list(wn.all_synsets('a')):
        count += 1
        for elts in ss.lemmas():
            if '_' in elts.name():
                adjectives.append(strip_underscores(elts))
            else:
                adjectives.append(elts.name())
    print(str(count) + ' adjectives loaded')


def pop_adverbs():
    count = 0
    for ss in list(wn.all_synsets('r')):
        for elts in ss.lemmas():
            count += 1
            if '_' in elts.name():
                adverbs.append(strip_underscores(elts))
            else:
                adverbs.append(elts.name())
    print(str(count) + ' adverbs loaded.')


def setup():
    print('Loading dictionaries...')
    pop_adverbs()
    pop_adj()
    pop_nouns()
    pop_verbs()


def get_rand_of_type(pos_list):
    this_list = pos_list
    return this_list[random.randrange(len(this_list))]


def beat_model():
    """
        poem is of form:
            adjective noun verb
            verb noun verb
            adverb noun verb
    :return: beat string
    """
    poem = '' \
           + get_rand_of_type(adjectives).capitalize() \
           + ' ' + get_rand_of_type(nouns) \
           + ' ' + get_rand_of_type(verbs) + '\n'

    poem += get_rand_of_type(verbs).capitalize() + ' ' \
            + 'the ' + get_rand_of_type(nouns) + ' ' \
            + get_rand_of_type(verbs) + '\n'

    poem += get_rand_of_type(nouns).capitalize() + ', ' \
            + get_rand_of_type(nouns) + ' ' \
            + get_rand_of_type(verbs) + '.\n'

    return poem


def display_poem():
    print('\nHere\'s your beat poem:\n')
    print(beat_model())

if __name__ == "__main__":

    setup()
    display_poem()
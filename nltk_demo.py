from nltk.corpus import wordnet as wn

import nltk

import random

from nltk.corpus import stopwords as sw

#nltk.download('wordnet')

# dictionary to hold parts of speech abbreviations
POS = {
        'v': 'verb',
        'a': 'adjective',
        'n': 'noun',
        'r': 'adverb'
        }


nouns = []
verbs = []
adjectives = []
adverbs = []


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

    for ss in list(wn.all_synsets('n')):
        for elts in ss.lemmas():
            # print(elts.name())
            if '_' in elts.name():
                temp_word = strip_underscores(elts)
                nouns.append(temp_word)
            else:
                nouns.append(elts.name())





def pop_verbs():

    for ss in list(wn.all_synsets('v')):
        for elts in ss.lemmas():
            #print(elts.name())
            if '_' in elts.name():
                temp_word = strip_underscores(elts)
                verbs.append(temp_word)
            else:
                verbs.append(elts.name())


def pop_adj():

    for ss in list(wn.all_synsets('a')):
        for elts in ss.lemmas():
            if '_' in elts.name():
                adjectives.append(strip_underscores(elts))
            else:
                adjectives.append(elts.name())

def pop_adverbs():

    for ss in list(wn.all_synsets('r')):
        for elts in ss.lemmas():
            if '_' in elts.name():
                adverbs.append(strip_underscores(elts))
            else:
                adverbs.append(elts.name())


def get_rand_of_type(pos_list):
    this_list = pos_list
    return this_list[random.randrange(len(this_list))]

# list_of_english_stopwords = sw.words('english')

# print(sw.words('english'))

# print(len(list_of_english_stopwords))

# print(list_of_english_stopwords[random.randrange(len(list_of_english_stopwords))])


def beat_model():
    """
        poem is of form:
            adjective noun verb
            verb noun verb
            adverb noun verb
    :return: beat string
    """
    poem = ''\
           + get_rand_of_type(adjectives).capitalize() \
           + ' ' + get_rand_of_type(nouns) \
           + ' ' + get_rand_of_type(verbs) + '\n'

    poem += get_rand_of_type(verbs).capitalize() + ' ' \
            + 'the ' + get_rand_of_type(nouns) + ' ' \
            + get_rand_of_type(verbs) + '\n'

    poem += get_rand_of_type(nouns).capitalize() + ', ' \
            + get_rand_of_type(nouns) + ' —' \
            + get_rand_of_type(verbs) + '.\n'

    return poem


pop_nouns()
pop_verbs()
pop_adj()
pop_adverbs()

print('Num verbs: ' + str(len(verbs)))
print('Num nouns: ' + str(len(nouns)))
print('Num adj: '   + str(len(adjectives)))
print('Num adv: '   + str(len(adverbs)))
print(verbs[random.randrange(len(verbs))])
print(get_rand_of_type(nouns) + '\n\n')

print(beat_model())





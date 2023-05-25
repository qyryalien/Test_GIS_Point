import re
from collections import Counter

paragraph = [
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
]


def word_frequency(paragraph):
    treated_string = ' '.join(paragraph).lower()
    treated_string = re.sub(r'[.,"\'-?:!;]', '', treated_string)
    treated_string = treated_string.split()
    result = dict(Counter(treated_string))
    return result


frequency = word_frequency(paragraph)
print(frequency)

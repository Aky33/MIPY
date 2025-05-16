import math
from .alphabet import alphabet
from .get_bigrams import get_bigrams
from .transition_matrix import transition_matrix

def plausibility(text, TM_ref):
    bigrams_obs = get_bigrams(text)
    TM_obs = transition_matrix(bigrams_obs, alphabet)
    likelihood = 0

    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            likelihood += math.log(TM_ref[i][j]) * TM_obs[i][j]

    return likelihood
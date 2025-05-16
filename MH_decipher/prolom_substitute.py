#alphabet- obsahuje abecedu písmen, např. list 
#TM_ref – referenční relatinví matice bigramů /přechodů sestavená z nějakého textu který není zašifrovaný (např. knihy) 
#iter – počet iterací algoritmu 
#start_key  - dává uzivatel ale pokud ho nedá vygenerujte náhodně počáteční klíč pro prolomení šifry. 
#Text – zašifrovaný text se kterým pracujeme 

from .alphabet import alphabet
from .substitute_decrypt import substitute_decrypt
from .plausibility import plausibility
import random

def prolom_substitute(text, TM_ref, iter, start_key):
    current_key = start_key
    decrypted_current = substitute_decrypt(text, current_key)
    p_current = plausibility(decrypted_current, TM_ref)

    for i in range(iter):
        candidate_key = current_key #copy?
        indices = randomsFromArray(2, alphabet)
        swap(candidate_key, indices[0], indices[1])

        decrypted_candidate = substitute_decrypt(text, candidate_key)
        p_candidate = plausibility(decrypted_candidate, TM_ref)

        q = p_candidate / p_current

        if q > 1:
            current_key = candidate_key
            p_current = p_candidate
        elif random.uniform(0, 1) < 0.01:
            current_key = candidate_key
            p_current = p_candidate

        if (i % 50) == 0:
            print('Iteration ', i, ' log plausibility: ', p_current)

    best_decrypted_text = substitute_decrypt(text, current_key)
    return current_key, best_decrypted_text, p_current

def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def randomsFromArray(number, array):
    randoms = []
    for i in range(number):
        randoms[i] = random.choice(array)

    return randoms
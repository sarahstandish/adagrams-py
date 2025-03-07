
import random
# Wave 1

def draw_letters():
    LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
    # Transforming LETTER_POOL dictionary into a list
    all_letters = []
    for letter, quantity in LETTER_POOL.items():
        for i in range(quantity):
            all_letters.append(letter)

    letter_bank = []
    # Adding 10 random letters to user's letter_bank
    for i in range(10):
        random_int = random.randint(0, len(all_letters)-1)
        letter_bank.append(all_letters[random_int])
        all_letters.pop(random_int)

    return letter_bank

draw_letters()

# Wave 2
def uses_available_letters(word, letter_bank):

    word = word.upper()
    # check if each character is in the word and occurs fewer or equal times to character in letter bank
    for character in word:
        if not word.count(character) <= letter_bank.count(character):
            return False
    return True

# Wave 3
def score_word(word):
    # initialize score dictionary
    score_chart = {
    ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
    ('D', 'G'): 2,
    ('B', 'C', 'M', 'P'): 3,
    ('F', 'H', 'V', 'W', 'Y'): 4,
    ('K'): 5,
    ('J', 'X'): 8,
    ('Q', 'Z'): 10
    }

    score = 0
    word = word.upper()
    # check if each tuple contains a character from the word and if so add the value to the score
    for char in word:
        for letter_tuple in score_chart:
            if char in letter_tuple:
                score += score_chart[letter_tuple]
                break

    # increase score for long words
    if len(word) >= 7:
        score += 8
        
    return score

    
# Wave 4
def get_highest_word_score(word_list):
    # initialize 2 variables: highest score and highest scoring word (0 and "")
    highest_score = 0
    highest_scoring_word = ""
    # loop through the word_list and score_word() every loop on the word
    for word in word_list:
        if score_word(word) > highest_score:
            highest_score = score_word(word)
            highest_scoring_word = word
        elif score_word(word) == highest_score:
            if len(word) == len(highest_scoring_word):
                continue
            elif len(highest_scoring_word) == 10:
                continue
            elif len(word) == 10:
                highest_scoring_word = word
                highest_score = score_word(word)
            elif len(word) < len(highest_scoring_word):
                highest_scoring_word = word
                highest_score = score_word(word)
    
    return highest_scoring_word, highest_score


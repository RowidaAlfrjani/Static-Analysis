import re

def sentence_info (a_sentence):
    a_sentence = re.sub(" +", " ", str(a_sentence))
    a_sentence = a_sentence.strip().lower()
    '''
    if str(a_sentence) == "":
        continue
    '''
    if "%" in a_sentence:
        contains_symbols_percentage = "True"
    else:
        contains_symbols_percentage ="False"

    sentence_length = len(str(a_sentence))
    sentence_words = len(str(a_sentence).split(" "))
    sentence_check= any(chr.isdigit() for chr in str(a_sentence))
    if sentence_check == True:
        contains_number = "True"
    else:
        contains_number = "False"

    tokens = str(a_sentence).split(" ")
    symbols = ""
    for token in tokens:
        ll = len(str(token))
        if str(token).isdigit() == True or str(token).isalpha() == True or str(token).isalnum() == True:
            #contains_symbols.append("False")
            continue
        else:
            #contains_symbols.append("True")
            if symbols == "":
                symbols = str(token)
            else:
                symbols = symbols + "|" + str(token)

    if symbols == "":
        symbols_check = False
    else:
        symbols_check = True
    return sentence_length, sentence_words, contains_number, contains_symbols_percentage, symbols_check
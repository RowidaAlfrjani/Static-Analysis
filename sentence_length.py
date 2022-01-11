import pandas as pd
import sys
from pathlib import Path
import csv
import re
import collections
import pandas as pd
import matplotlib.pyplot as plt
import xlsxwriter

WORD_CHAR = re.compile(r"[A-Za-z]+")


def sentence_l(root_folder, output_folder):
    for f1 in Path(root_folder).rglob("*_scored_label_list.csv"):
        test_file = pd.read_csv(f1, sep=",", header=0, encoding="utf8")
        '''
        outfile = open(
            output_folder + "/" +f1.name, "w", newline="", encoding="utf-8"
        )
        csvwriter = csv.writer(outfile, quotechar='"', quoting=csv.QUOTE_ALL)
        header = [
            "text",
            "sentence_length_char",
            "sentence_length_words",
            "contains_number",
            "contains_symbols",
            "symbols",
        ]
        csvwriter.writerow(header)
        '''
        sentence_length_char = []
        sentence_length_words = []
        contains_number = []
        #no_number = []
        contains_symbols= []
        contains_symbols_percentage= []
        token_length = []
        symbols_list = []
        #no_symbols = []

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(output_folder+ "/" +f1.name+'statistical_analysis.xlsx')
        worksheet1 = workbook.add_worksheet('original_data')
        worksheet2 = workbook.add_worksheet('All_data')
        worksheet3 = workbook.add_worksheet("All_tokens")
        # the header for sheet 1
        worksheet1.write(0, 0, "text")

        # the header for sheet 2
        row = 0
        col = 0
        worksheet2.write(row, col, "text")
        worksheet2.write(row, col + 1, "sentence_length_char")
        worksheet2.write(row, col + 2, "sentence_length_words")
        worksheet2.write(row, col + 3, "contains_number")
        worksheet2.write(row, col + 4, "contains_symbols")
        worksheet2.write(row, col + 5, "symbols")
        row += 1

        worksheet3.write(0, 0, "token")
        worksheet3.write(0, 1, "length")
        i = 1
        for index, raw in test_file.iterrows():
            sentence = raw[0]
            worksheet1.write(index + 1, 0, sentence)

            sentence = re.sub(" +", " ", str(sentence))
            sentence = sentence.strip().lower()
            #if "|" in str(sentence):
                #sentence_list = sentence.split("|")
            #else:
            sentence_list = [sentence]
            for a_sentence in sentence_list:
                a_sentence = re.sub(" +", " ", str(a_sentence))
                a_sentence = a_sentence.strip()
                if str(a_sentence) == "":
                    continue
                if "%" in a_sentence:
                    contains_symbols_percentage.append("True")
                else:
                    contains_symbols_percentage.append("False")

                sentence_length = len(str(a_sentence))
                sentence_words = len(str(a_sentence).split(" "))
                sentence_check= any(chr.isdigit() for chr in str(a_sentence))
                if sentence_check == True:
                    contains_number.append("True")
                else:
                    contains_number.append("False")

                tokens = str(a_sentence).split(" ")
                symbols = ""
                for token in tokens:
                    ll = len(str(token))
                    token_length.append(ll)
                    #if not WORD_CHAR.search(token):
                        #print(token.text)

                    worksheet3.write(i, 0, str(token))
                    worksheet3.write(i, 1, ll)
                    i = i + 1
                    if str(token).isdigit() == True or str(token).isalpha() == True or str(token).isalnum() == True:
                        #contains_symbols.append("False")
                        continue
                    else:
                        #contains_symbols.append("True")
                        if symbols == "":
                            symbols = str(token)
                        else:
                            symbols = symbols + "|" + str(token)
                        if str(token) not in symbols_list:
                            symbols_list.append(str(token))

                if symbols == "":
                    symbols_check = False
                    contains_symbols.append("False")

                else:
                    symbols_check = True
                    contains_symbols.append("True")

                #data = [a_sentence, sentence_length, sentence_words, sentence_check,symbols_check, symbols]
                worksheet2.write(row, col, a_sentence)
                worksheet2.write(row, col + 1, sentence_length)
                worksheet2.write(row, col + 2, sentence_words)
                worksheet2.write(row, col + 3, sentence_check)
                worksheet2.write(row, col + 4, symbols_check)
                worksheet2.write(row, col + 5, symbols)
                row += 1

                sentence_length_char.append(sentence_length)
                sentence_length_words.append(sentence_words)
                #csvwriter.writerow(data)
        # sheet 2= sentence_lenght_char
        xcel_r(workbook, sentence_length_char, "sentence_length_char", "sentence_length", "count")
        xcel_r(workbook, sentence_length_words, "sentence_length_words", "S_words", "count")
        xcel_r(workbook, contains_number, "number_count", "condition", "count")
        xcel_r(workbook, contains_symbols, "symbol_count", "condition", "count")
        xcel_r(workbook, contains_symbols_percentage, "symbol_percentage_count", "condition", "count")
        xcel_r(workbook, token_length, "token_length", "token_length", "count")
        #print(symbols_list)
        '''
        sentence_length_char = sorted(sentence_length_char)
        counter_length_char = collections.Counter(sentence_length_char)
        keys = counter_length_char.keys()
        values = counter_length_char.values()

        # Create a workbook and add a worksheet.
        #workbook = xlsxwriter.Workbook('Expenses01.xlsx')
        worksheet = workbook.add_worksheet('sentence_length_char')
        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0

        # Iterate over the data and write it out row by row.
        worksheet.write(row, col, "length_char")
        worksheet.write(row, col + 1, "count")
        row += 1
        for a, b in zip(keys,values):
            worksheet.write(row, col, a)
            worksheet.write(row, col + 1, b)
            row += 1
        '''

        workbook.close()





def xcel_r(workbook, l1, sheet_name, head1_name, head2_name):

    l1 = sorted(l1)
    counter_l1 = collections.Counter(l1)
    keys = counter_l1.keys()
    values = counter_l1.values()

    # Create a workbook and add a worksheet.
    # workbook = xlsxwriter.Workbook('Expenses01.xlsx')
    worksheet = workbook.add_worksheet(sheet_name)
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0

    # Iterate over the data and write it out row by row.
    worksheet.write(row, col, head1_name)
    worksheet.write(row, col + 1, head2_name)
    row += 1
    for a, b in zip(keys, values):
        worksheet.write(row, col, a)
        worksheet.write(row, col + 1, b)
        row += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root_folder = sys.argv[1]
    output_folder = sys.argv[2]

    sentence_l(root_folder, output_folder)


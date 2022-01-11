import pandas as pd
import sys
from pathlib import Path
import csv
import re
import collections
import pandas as pd
import xlsxwriter
from analysis import file_info
from analysis import sentence_info

def sentence_l(root_folder, output_folder):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(output_folder + "/" + 'qualitive_analysis.xlsx')
    worksheet1 = workbook.add_worksheet('All_data')
    #worksheet2 = workbook.add_worksheet("All_tokens")

    # the header for sheet 1
    row = 0
    headers = ["country_code", "website", "vam_id", "file_path" , "extraction_id", "page_number", "sentence_original", "sentence_clean", "sentence_number",
               "label", "label_confidence", "scored_entity_labels", "scored_entity_matches", "sentence_length_char", "sentence_length_words",
               "contains_number", "contains_symbols", "symbols"]
    for i in range(0, len(headers)):
        worksheet1.write(row, i, headers[i])

    row += 1

    #worksheet2.write(0, 0, "token")
    #worksheet2.write(0, 1, "length")

    for f1 in Path(root_folder).rglob("*_scored_label_list.csv"):

        test_file = pd.read_csv(f1, sep=",", header=0, encoding="utf8")
        country, website, vamid = file_info.file_info(root_folder, f1)

        for index, raw in test_file.iterrows():
            sentence = raw["sentence_original"]
            sentence_length, sentence_words, contains_number, contains_symbols_percentage, symbols_check = sentence_info.sentence_info(sentence)

            sentence_information =[]
            sentence_information.append(country)
            sentence_information.append(website)
            sentence_information.append(vamid)
            sentence_information.append(str(f1))
            sentence_information.append(raw["extraction_id"])
            sentence_information.append(raw["page_number"])
            sentence_information.append(raw["sentence_original"])
            sentence_information.append(raw["sentence_clean"])
            sentence_information.append(raw["sentence_number"])
            sentence_information.append(raw["label"])
            sentence_information.append(raw["label_confidence"])
            sentence_information.append(raw["scored_entity_labels"])
            sentence_information.append(raw["scored_entity_matches"])
            sentence_information.append(sentence_length)
            sentence_information.append(sentence_words)
            sentence_information.append(contains_number)
            sentence_information.append(contains_symbols_percentage)
            sentence_information.append(symbols_check)

            for i in range(0, len(headers)):
                try:
                    worksheet1.write(row, i, sentence_information[i])
                except:
                    pass

            row = row + 1



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
    #root_folder = sys.argv[1]
    root_folder = "G:\\My Drive\\10k-updated 20-12-2021"
    #output_folder = sys.argv[2]
    output_folder = "G:\\My Drive\\concative"

    sentence_l(root_folder, output_folder)


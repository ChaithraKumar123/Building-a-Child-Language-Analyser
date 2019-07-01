"""
Task 1: Handling with File Contents and Preprocessing
Author name :Chaithra Kumar 
Created Date :02-October -2018
Updated Date: 11-October -2018
Description of program :
To Read Transcripts of SLI and TD and pre-process to extract relevant content
The transcript are of two category one is SLI and the other is TD.
Each SLI and TD consists of *CHI: statments and the following statments are preprocessed
and the pre-processed files are stores in other files.
"""
import pandas as pd
import numpy as np
import re
import os

""" read_file is function that reads all the files in a given folder and stores back processed file to the new folder
        Parameters:
           path : String
                   Name of the folder from which files should be read
           new_folder : String 
                   Name of the new folder where files should be stored.
        Return:None
"""


def read_file(path, new_folder):
    # traverse only if it is a directory
    if os.path.isdir(path):
        # creating new_folder to store preprocessed files
        os.makedirs(new_folder, exist_ok=True)
        # traversing to all the files in the folder
        for filename in os.listdir(path):
            col = ['names', 'UnprocessedText']
            # reading the files in csv format and storing it in data frame with two columns names and Unprocessed text .
            # names include name of speaker and the text is stores in Unprocessed text
            df = pd.read_csv(os.path.join(path, filename),'rb', names=col, dtype='unicode', error_bad_lines=False,
                             delimiter="\t")
            # Calling function pre_process_file to process the text
            df = pre_process_file(df)
            # after processing the file store the data in the column Unprocessed text to a file.
            np.savetxt(new_folder + "/" + filename, df.p_text, fmt='%s')
        print("All scripts in " + path + " is Processed --New folder created " + new_folder)
    else:
        print(path + " given is not a directory or does not exists")


""" pre_process_file is function that pre-process the data frame .
        Parameters:
           df : data frame
                   data frame containing two columns names and Unprocessed text
        Return:Processed data frame
"""








def pre_process_file(df):
    # the rows containig names as null is filled with zero
    df.query("names == '' ").fillna
    df['names'].fillna(0, inplace=True)
    # if the row is *CHI: statments and followed row is 0 .Combine both the rows.
    for i in range(len(df) - 1):
        if df['names'].values[i] == "*CHI:" and df['names'].values[i + 1] == 0:
            df['UnprocessedText'][i] = df['UnprocessedText'][i] + " " + df['UnprocessedText'][i + 1]
    # filter *CHI: statments
    df = df.query("names == '*CHI:'")
    # creating copy of data frame
    df1 = df.copy()
    # create the new column to store processed_text
    # replace [* m:+ed] and [* m] with [*]
    df1['p_text'] = df1['UnprocessedText'].replace(regex='(\[\*\sm:\+ed\]| \[\*\sm\])', value='[*]')
    # Remove those words that have either ‘[’ as prefix or ‘]’ as suffix but retain these three
    # symbols: [//], [/], and [*]
    df1['p_text'] = df1['p_text'].replace(regex='\[(?!\/\]|\/\/\]|\*\]).*?\]', value='')
    # remove < or >
    df1['p_text'] = df1['p_text'].replace(regex='[<>]', value='')
    # remove ( brackets if not followed by .
    df1['p_text'] = df1['p_text'].replace(regex='\((?=[^.])', value='')
    # remove ( brackets if followed by a dot and don't end with ) example-(..a becomes ..a
    df1['p_text'] = df1['p_text'].replace(regex='\((?=\.[^\)])', value='')
    # remove ) if doesnt contain . before it.
    df1['p_text'] = df1['p_text'].replace(regex='(?<=[^.])\)', value='')
    # remove ) brackets if preceded by a dot and don't end with ) example- ..a) becomes ..a
    df1['p_text'] = df1['p_text'].replace(regex='(?<=[^\(]\.)\)', value='')
    # remove ()
    df1['p_text'] = df1['p_text'].replace(regex='()', value='')
    # Remove those words that have prefixes of ‘&’ and ‘+’
    df1['p_text'] = df1['p_text'].replace(regex='[&+][^\s+.!]+', value='')
    return df1

# main method to iterate both folders
def main():
        read_file("/Users/chaithrakumar/Documents/ENNI Dataset/SLI", "SLI_Cleaned")
        read_file("/Users/chaithrakumar/Documents/ENNI Dataset/TD", "TD_cleaned")


if __name__ == "__main__":
    main()

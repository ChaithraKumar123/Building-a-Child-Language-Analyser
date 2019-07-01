"""
Task 2: Construct a class to produce a number of statistics for each SLI or TD files
Author name :Chaithra Kumar
Created Date :02-October -2018
Updated Date: 11-October -2018
Description of program :
Construct a class that constructs a statistics such as:-
length of transcript,Unique words,Number of repetition,
Number of retracing,Number of Pauses and Number of Errors.
"""
import re
import os
# Creating a Analyser Class


class Analyser:

    """ Constructor __init__  to initial instance variable
            Instance Variables :
               self.length_trans : int
                      hold length of the script.
               self.size_vocab : int
                     hold count of unique words in script
               self.no_of_rep : int
                    hold count of Number of repetation of words indicated by [/]
               self.no_of_retracing : int
                    hold count of Number of retracing of words indicated by [//]
               self.no_of_error : int
                    hold count of grammatical errors  — indicated by  [*]
               self.no_of_pauses : int
                    hold count of pauses — indicated by  (.)

    """

    def __init__(self):
        self.length_trans = 0
        self.size_vocab = 0
        self.no_of_rep = 0
        self.no_of_retracing = 0
        self.no_of_error = 0
        self.no_of_pauses = 0

    """ 
       __str__: re-define __str__ method (the instance variables) in a readable format.
        Return:
            String of instance variables in a readable format
    """

    def __str__(self):
        return "Length of Transcript:" + str(self.length_trans) + "\n" \
               + "Size of Vocabulary:"+str(self.size_vocab) + "\n"  \
               + "Number of repetation:"+str(self.no_of_rep) + "\n" \
               + "Number of retracing:" + str(self.no_of_retracing) + "\n" \
               + "Number of Grammatical Errors:" + str(self.no_of_error) + "\n" \
               + "Number of Pauses:" + str(self.no_of_pauses) + "\n"
    """
        analyse_script method the performs analysis on cleaned script and assigns value to all statistics 
        of script(i.e instance variable of class)
        Parameter:
            cleaned_file: String
                contains path of the file
        Return : None
    
    """

    def analyse_script(self, cleaned_file):

        # check file path is valid!
        if os.path.isfile(cleaned_file):
            # set to store unique words
            unique_set = set()
            # read the file
            file = open(cleaned_file, "r")
            # traversing the file line by line
            for line in file:
                # if its end of the line and ends with . or ! or ?  increment line count of the script
                if (line.rstrip().endswith('.') or line.rstrip().endswith('!')
                                         or line.rstrip().endswith('?')):
                    self.length_trans = self.length_trans + 1
                # match only words and update the set
                match_pattern = re.findall(r'[A-Za-z]+', line)
                unique_set.update(set(match_pattern))
                # count number of [/] in a line and add it
                self.no_of_rep = self.no_of_rep + line.count('[/]')
                # count number of [//] in a line and add it
                self.no_of_retracing = self.no_of_retracing + line.count('[//]')
                # count number of [*] in a line
                self.no_of_error = self.no_of_error + line.count('[*]')
                # count number of (.) in a line
                self.no_of_pauses = self.no_of_pauses + line.count('(.)')
            # len of unique set is size of unique words in a script
            self.size_vocab = len(unique_set)
            print(unique_set)
        else:
            print(cleaned_file + " does not exists")
    # main method to construct objects of the class and call analyse_script function to get the Statistics of the script


def main():

    obj_sli = Analyser()
    obj_sli.analyse_script('TD_Cleaned/TD-5.txt')
    print(obj_sli)
    obj_td = Analyser()
    obj_td.analyse_script('TD_Cleaned/TD-1.txt')
    print(obj_td)


if __name__ == main():
    Analyser.main()


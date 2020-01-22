# Author:   Queuebee2
# Date:     22-01-2020
# Purpose:  Quickly fix a printing issue with XML output by narrowing column 'F'

import os


# column F looks like this
obnoxious = r"""<Column ss:AutoFitWidth="0" ss:Width="280" />"""

# fix it by decreasing F width by 200. Since we dont extract the string as is,
# replacing only desired parts in the whole XML is a quick fix.
good = r"""<Column ss:AutoFitWidth="0" ss:Width="80" />"""


# keyword that HAS to be in the filename
file_keyword = "IPV ("

# extention for new output file
custom_extention = " - edited automatically.xml"


# walk over files, fix XML and output as a new file.

def quicklyFixTheXMLs():
    """Open XML files, replace the wrong thing(s) with good thing(s)"""
    for _, _, files in os.walk("."):
        for filename in files:
            if file_keyword in filename:
                with open(filename, 'r') as f:
                    with open(filename.replace(".xml",custom_extention) , 'w') as out:
                        bad_for_printing = f.read()
                        good_for_printing = bad_for_printing.replace(obnoxious, good)
                        out.write(good_for_printing)
                        

                        print(f'did {filename}')
            


def findAutoEdited():
    """ Check if this script has already ran in the directory"""
    # _'s are root and dirs, which we dont use.
    for _, _, files in os.walk("."):
        for filename in files:
            if custom_extention in filename:
                return True

    return False


AlreadyUsedErrorMessage = f"""{50*"-"}\nWARNING\nIt seems the tool has already been used in this directory.\n{50*"-"}\n
Run it again? (Y/N/yes/YesPlease/no/nothnx/nah/nope)\ntype here and press return (↵ aka enter): """ 


if __name__ == '__main__':
    print('testing if this tool has already ran here...')
    
    if findAutoEdited():
        userChoice = input(AlreadyUsedErrorMessage)
    else:
        print('running tool!')
        userChoice = 'ouimerci'

    if userChoice.lower() in 'yyessyespleaseouimerci':
        quicklyFixTheXMLs()

    

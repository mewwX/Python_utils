import pandas as pd
import os


def convert_to_fixed_width2(input_file, output_file, column_widths):

    input_f = pd.read_csv("./datasets/fraudtestdata.csv", sep=",")
    
    myfile = "./datasets/fraudoutput.txt"
    
    # If file exists, delete it.
    if os.path.isfile(myfile):
        os.remove(myfile)
        
    # create file
    output_f = open(output_filepath, 'w')
    
    with open(output_filepath, 'w') as output_f :        
        index = "PAYER NSC ,PAYER ACCOUNT NO ,PAYER PHONE NO ,IBAN CODE ,SWIFT ID ,BENF NAME ,BANK NSC ,BANK ACCOUNT NO ,TRANSACTION AMOUNT ,PAYMT DONE TIME ,BENF ACTIVATE TIME ,COUNTRY CODE ,CURR CODE ,PAYER NAME"
        output_f.write(index + '\n')        
        for line in input_f.index:
            fixed_line = ''
            for column_name, width in column_widths.items():
                tmp = str(input_f[column_name][line])[:width]
                while len(tmp)<width :
                    tmp = tmp +" "
                fixed_line += tmp
            print(len(fixed_line),fixed_line)
            output_f.write(fixed_line + '\n')        
    output_f.close()

# "path/name.txt"
input_filepath = "./datasets/fraudtestdata.csv"
output_filepath = "./datasets/fraudoutput.txt"
    

# dict

#sum(column_widths.values()) = 276
column_widths = {
    "PAYER NSC": 6,
    "PAYER ACCOUNT NO": 11,
    "PAYER PHONE NO": 16,
    "IBAN CODE": 34,
    "SWIFT ID": 11,
    "BENF NAME": 35,
    "BANK NSC": 33,
    "BANK ACCOUNT NO": 35,
    "TRANSACTION AMOUNT": 12,
    "PAYMT DONE TIME": 26,
    "BENF ACTIVATE TIME": 26,
    "COUNTRY CODE": 12,
    "CURR CODE": 9,
    "PAYER NAME": 10
}    

try:

    convert_to_fixed_width2(input_filepath, output_filepath, column_widths)

except Exception as e:

    print("The file could not be processed")
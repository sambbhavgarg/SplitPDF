
from SplitPDF import SplitPDF

'''
data.xlsx needs to be in standard format -
  1. First Column: Full Name
  2. Second Column: First Name [excel formula to get first name from full name: =LEFT(A1, FIND(" ", A1) - 1)]
  3. Third Column: Email ID (optional)
  
The output will be erroneous if above standard is not met or corresponding changes arent made in SplitPDF.py
'''
   
config = {'program_name_dir': 'GSIP', #directory name where data, and output mailmerge PDF is located
            'data_dir': 'GSIP', #directory name where data, and output mailmerge PDF is located
            'excel_data_file_name': 'data.xlsx', # data file name; keep standard - data.xlsx for every program
            'all_certs_mail_merge_pdf': '', #Mailmerge output PDF, for example: AllCerts.pdf
            'out_dir_name_for_split_pdfs': '', #directory where you need all split PDFs
            'individual_file_suffix_1': '', # First Suffix to be added to each file, for example: <file name>" - suffix 1"
            'individual_file_suffix_2': '', # Second Suffix to be added to each file, for example: <file name>" - suffix 1"" - suffix 2"
            'sheet_num': 0, # sheet inside excel file that contains data
            'run': False, # boolean value to split pdf or just print results
            'create_sheet_with_attachments_column': False} # ignore

sPDF = SplitPDF(config)
sPDF.splitPDF()

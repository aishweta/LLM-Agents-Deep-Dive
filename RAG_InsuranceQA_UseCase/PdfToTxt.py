# importing required modules
from PyPDF2 import PdfReader
import re
import glob

#This User defined function will read the text and clean it.
def Text_cleaning(text):
    #Text Cleaning
    text=text.replace('\n',' ')
    text=text.replace('Ÿ',' ')
    text=text.replace('\x00',' ')
    text=text.replace('  ',' ')
    text=text.replace('•',' ')
    text=re.sub(' +', ' ', text)
    return text

#This User defined function will read the pdf file,clean the text from the file and save it in .txt file.
def text_extractor(input_folder_path,output_folder_path):
    # creating a pdf reader object
    #print(path)
    txt_path=input_folder_path+"\*.pdf"
    input_file_names=glob.glob(txt_path)
    for j in input_file_names:
        reader = PdfReader(j)
        data=[]
        for i in range(0 , len(reader.pages)):
            page = reader.pages[i]
        
            # extracting text from page
            text = page.extract_text()
            #Text Cleaning
            text=Text_cleaning(text)
            data.append(text)
        # Saving data into .txt file
        ##.txt File name
        s=str(re.escape('pdfs\\'))
        e=str(re.escape('.'))
        res=re.findall(s+"(.*)"+e,j)[0]
        Outp_path=output_folder_path+'\\'+res+".txt" 
        
        ## Writing in .txt file
        with open(txt_path, 'w',encoding="utf-8") as f:
            for line in data:
                f.write(line)
                f.write('\n')

text_extractor(r"\Data\pdfs",r"\Data\.txt")

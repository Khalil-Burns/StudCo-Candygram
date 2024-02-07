import pandas as pd
import re

candygrams = pd.read_csv('Studco Candygrams Form 2024 (Responses) - Form Responses 1.csv')


candygrams["Homeroom.filter"] = candygrams["Homeroom teacher of receiver (Block A)"].str.upper()

def filter(text):
    text = re.sub(r'\b(MR|MR\.|MS\.|MS|MRS\.|MRS)\b', '', text)
    words = text.split()
    
    if len(words) > 1:
        words = words[1:]
    
    text = ' '.join(words)
    text = re.sub(r'\s', '', text)
    
    return text


candygrams["Homeroom.filter"] = candygrams["Homeroom.filter"].apply(filter)

candygrams.sort_values(by="Homeroom.filter", inplace=True)
# del candygrams["Homeroom.filter"]
candygrams = candygrams.fillna('')

output = open("Studco_Candygrams_Messages_2024.txt","w")

for index, candygram in candygrams.iterrows():
    if (index < 10):
        output.write(f"Order ID: 000{index}\n")
    elif (index < 100):
        output.write(f"Order ID: 00{index}\n")
    elif (index < 1000):
        output.write(f"Order ID: 0{index}\n")
    else:
        output.write(f"Order ID: {index}\n")

    output.write(f"Homeroom: {candygram['Homeroom teacher of receiver (Block A)']}\n")
    output.write(f"Grade: {candygram['Grade of receiver']}\n")
    output.write(f"Hey {candygram['FULL Name of receiver (ex. John Doe)']},\n")

    if (str(candygram['Your special message (optional), max 100 characters']) == ""):
        output.write(" You've received  a candygram from a fellow lion!\n\n")
    else:
        output.write(f"  {candygram['Your special message (optional), max 100 characters']}\n\n")

    if (candygram['Anonymous sender? (Yes = sender name will not be displayed on candygram)'] == 'Yes'):
        output.write("  -  Anonymous\n")
    else:
        output.write(f"  -  {candygram['YOUR Full name (ex. John Doe)']}\n")

    output.write('-----------------------------------------------\n\n\n\n\n')


output.close()
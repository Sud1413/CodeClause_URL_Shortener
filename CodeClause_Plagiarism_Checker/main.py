from difflib import SequenceMatcher

with open('C:/Users/agnih/CodeClause/CodeClause_Plagiarism_Checker/India.txt') as file1, open('C:/Users/agnih/CodeClause/CodeClause_Plagiarism_Checker/Russia.txt') as file2:
    file1data = file1.read()
    file2data = file2.read()
    Sililarity = SequenceMatcher(None,file1data,file2data).ratio()
    print("The Plagiarism in percerntage is:- ", round(Sililarity*100))
import os
dir_path = 'assignment0' 
files_name = os.listdir(dir_path)
word_dict = {}
stop_words_file = open('stop_word.txt','r',encoding="utf-8")
stop_words = stop_words_file.read().split('\n')
stop_words_file.close
punctuations_file = open('punctuation.txt','r',encoding="utf-8")
puctuations = punctuations_file.read().split('\n')
punctuations_file.close
#print(puctuations)
for file_name in files_name:
    file_path = os.path.join(dir_path,file_name)
    file = open(file_path,'r',encoding='utf-8')
    content = file.read()
    
    # content = content.replace("\n","").replace(",","").replace(".","").replace("“","").replace("”","").replace("(","").replace(")","").replace("[","").replace("]","").replace("?","").replace("!","").replace("\"","").replace(";","")
    #print(content)
    for puctuation in puctuations:
        if puctuation=='’':
            content = content.replace(puctuation,"\'")
        elif puctuation=="\'":
            continue
        else:
            content = content.replace(puctuation,"")
    content = content.split(" ")
    for word in content:
        temp = word.split("\'")
        if len(temp)==2:
            word = temp[0]
        if word.lower() in stop_words:
            continue
        if word_dict.get(word)==None:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
            
sorted_word_list = sorted(word_dict.items(),key = lambda x:x[1], reverse=True)
import csv
csv_file = open("keyword, frequency.csv", "w",newline='')
mywriter = csv.writer(csv_file)
mywriter.writerow(["key", "frequency"])
for i in range(15):
    mywriter.writerow(sorted_word_list[i])

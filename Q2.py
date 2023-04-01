def countword():
    data = open('C:/Users/tamar/Desktop/הנדסה תעשייה וניהול/שנה ג/סמסטר ב/כרייה וניתוח נתונים מתקדם בפייתון/מטלה1/text.txt')
    word = data.readline()
    data = data.readlines()
    word_list = []
    num_of_word =0
    word = word.split()
    word = word[0]
    for j in data:
        word_list = j.split(" ")
        for k in word_list:
            if word == reword(k):
                num_of_word = num_of_word + 1 
    return num_of_word

def reword (word:str):
    new_word = ""
    for i in word:
        new_word = i + new_word         
    return new_word.lower()

n= countword()
print(n)








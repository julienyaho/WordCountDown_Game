import random

#Global variables
words =[]
letters=[]
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
l="abcdefghijklmnopqrstuvwxyz"
c=0

#generate letters
def inputLetters(i):
    for i in range(8):
        if i<3 :
            letter=input("please input  vowels, enter 0 :\n")
        elif i<7:
            letter=input("please input  consonants ,enter 1 :\n")
        else :
             letter=input("please input  letter ,enter 2 :\n")
             
        if letter=='0' :
            index=random.randint(0,len(vowels)-1)
            letters.append(vowels[index])
            print(vowels[index])
        elif letter=='1':
            index=random.randint(0,len(consonants)-1)
            letters.append(consonants[index])
            print(consonants[index])
        elif letter =='2':
            index=random.randint(0,len(l)-1)
            letters.append(l[index])
            print(l[index])
        else :
            print("please reenter letter")
            letters(i)
            break
    print(letters)


#inputLetters(0)

letters='uiuyhwdc'
         
#Function that checks words in dictionary and prints word with most letters in it.
def Wordcheck():
   #variables
   max_letters = 0
   max_word = ""
   num_letters = 0
   result =[]
   print(letters)
   f = open('wordsList.txt','r') #this open the dictionary and it read it 
   while True:
      word = f.readline() #this read every line in the dictionary
      if word == "": #if word is empty is goes to another line
         break;
      words.append(word) # else put word in the list
 
   f.close()

   
   for word in words: #check every word in list
      for let in letters: # this do a looping from vowels con
         if let in word: 
            num_letters = num_letters + 1   
      if (num_letters > max_letters)and (num_letters == (len(word)-1)):#this print the word & the len of theword
         print(word, len(word)-1,'\r') # this print out the word and the length of the word
         max_letters = num_letters 
         max_word = word #this len of the word 
         result.append(set(max_word))#this put the words in the list
      num_letters = 0   #num letters reset to 0
         
   print()
   print("Longest word is: ", max_word)
   print("Longest len is: ", len(max_word)-1)       
#Dictionary()
Wordcheck()
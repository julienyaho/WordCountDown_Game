import random

#Global variables
words =[]
letters=[]
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
l="abcdefghijklmnopqrstuvwxyz"
c=0

#generate letters


#inputLetters(0)
letters ='uaurpgst'
         
#Function that checks words in dictionary and prints word with most letters in it.
def Wordcheck():
#variables
    counter = 0
    longest_word = ""
    characters = 0
    result =[]
   
    f = open('wordsList.txt','r')
    while True:
        word = f.readline() #this read every line in the dictory
        if word == "": #if word is empty is goes to another line
            break;
        words.append(word) # else put word in the list
 
    f.close()

   
    for word in words: #check every word in list
        for letter in letters: # this do a looping from vowels con
            if letter in word: 
                characters += 1   #increment num of characters by 1
        if(characters > counter):#this print the word & the len of theword
            if(characters == (len(word)-1)):
                
                counter = characters 
                longest_word = word #this len of the word 
                result.append(set(longest_word))#this put the words in the list
        characters = 0   #num letters reset to 0
    #print(result)
    print("Longest word is: ", longest_word)
    print("Longest len is: ", len(longest_word)-1)       
#Dictionary()
Wordcheck()
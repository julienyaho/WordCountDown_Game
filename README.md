#**_WordCountDown_Game_**
**_Theory Of Algorithms_**
####**_Introduction_**
##**_Project Brief_**
* You are required to create two pieces: a Python script that solves the Countdown letters game, and a document explaining how your solver works. The Countdown letters game is as detailed on Wikipedia. Esentially, you are given a list of nine random letters which contains at least three vowels and four consonants. You must find the longest possible word in the Oxford English dictionary that is an anagram of some or all of the letters in the random list. If there is more than one word of longest length, then each is as acceptable a solution as the others.

###**_Instructions_**
* Find a list of words in the Oxford English dictionary. This won't be too easy - you might need to join a few different files          together. You might even try scraping the Oxford Dictionary's website. If you write any scripts to do that, include them in your      submission.
* Fork the GitHub gist template here. Note that you can use a GitHub gist the same way you would use any GitHub repository. Think       of it as a small, quick repository.

* Write a Python script that solves the Countdown letters game in the most efficient way you can.

* Write a README file (called _about.md in above gist) about your script.

* Add to your Python script a function to test your algorithm, which creates a random list of nine letters as they would be             generated in Countdown.

###**_Project Name_**: wordcountdown.py
###**_Language use_**: Python

####**_Global variables_**
| I first create a *Global Variables* as show below:- |

| Description | Code |
| :---| :---|
| `*I first create a Global Variables which are:-*` | 
| `*List of word that matches and reach requiremen*`      |`*words =[]`|
| `*This is random generated word*`                      |`*letters=[]`|
| `*Set of Vowels*`                                  |`*vowels="aeiou"`|
| `*Set of consonants*`          |`*consonants="bcdfghjklmnpqrstvwxyz"`|
| `*Set of all vowels & consonants*`| `*l="abcdefghijklmnopqrstuvwxyz"`|
                                                        

**def Wordcheck():**
* Function that checks words in dictionary and prints word with most letters in it 

  
**_Description_**                                      ||                                     **_Code_**

1. This open the dictionary in my project and then Read it                      ||   **f = open('wordsList.txt','r')**
2. This is a Loop                                                               ||   **_while True:_**
3. this read every line in the dictionary                                       ||   **_word = f.readline()_**
4. If word is empty is goes to the next line and read it                        ||   **_if word == "":_**
5. This Break line terminates the current loop                                  ||   **_break;_**
6. Else put word in the list                                                    ||   **_words.append(word)_**
7. This closes the file                                                         ||   **_f.close()_**
  
```python
    for word in words: #check every word in list.
        for letter in letters: # this do a looping from vowels & consonants.
            if letter in word: 
                characters += 1   #increment num of characters by 1.
        if(characters > counter):#this print the word & the len of theword.
            if(characters == (len(word)-1)):
                
                counter = characters 
                longest_word = word #this len of the word.
                result.append(set(longest_word))#this put the words in the list.
        characters = 0   #num letters reset to 0.
    #print(result)
    print("Longest word is: ", longest_word) #This print out the longest word. 
    print("Longest len is: ", len(longest_word)-1) #This print out the longest word number.      
#Dictionary()
Wordcheck()

```


### **_How to Runner this Program_**

  * When you download my project 
  * Open it on **_Nope Pad_** and right it on and **_Click Open containing floder_** in Cmd
  * When Cmd open type in **_python wordcountdown2.py_**
  * ![image](https://github.com/julienyaho/WordCountDown_Game/blob/master/Running_Program.PNG)
  * It will bring up the Longest Word and the Longest Number of the Word
  * ![image](https://github.com/julienyaho/WordCountDown_Game/blob/master/Fully_Running.PNG)
  
  
###**_References_**

1. https://forums.taleworlds.com/index.php?topic=257150.msg6167190
2. http://stackoverflow.com/questions/29292133/how-to-count-down-in-for-loop-in-python
3. https://www.youtube.com/watch?v=YV6qm6erphk
4. http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt


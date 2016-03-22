# WordCountDown_Game
* Theory Of Algorithms

##Project Brief
* You are required to create two pieces: a Python script that solves the Countdown letters game, and a document explaining how your solver works. The Countdown letters game is as detailed on Wikipedia. Esentially, you are given a list of nine random letters which contains at least three vowels and four consonants. You must find the longest possible word in the Oxford English dictionary that is an anagram of some or all of the letters in the random list. If there is more than one word of longest length, then each is as acceptable a solution as the others.

###Instructions
* Find a list of words in the Oxford English dictionary. This won't be too easy - you might need to join a few different files          together. You might even try scraping the Oxford Dictionary's website. If you write any scripts to do that, include them in your      submission.
* Fork the GitHub gist template here. Note that you can use a GitHub gist the same way you would use any GitHub repository. Think       of it as a small, quick repository.

* Write a Python script that solves the Countdown letters game in the most efficient way you can.

* Write a README file (called _about.md in above gist) about your script.

* Add to your Python script a function to test your algorithm, which creates a random list of nine letters as they would be             generated in Countdown.

####Introduction
#####Global variables
| I first create a *Global Variables* as show below:- |

| Description | Code |
| :---| :---|
| `*I first create a Global Variables whis are:-*` | 
| `*List of word that matches and reach requiremen*`      |`*words =[]`|
| `*This is random generated word*`                      |`*letters=[]`|
| `*Set of Vowels*`                                  |`*vowels="aeiou"`|
| `*Set of consonants*`          |`*consonants="bcdfghjklmnpqrstvwxyz"`|
| `*Set of all vowels & consonants*`| `*l="abcdefghijklmnopqrstuvwxyz"`|
                                                        

* def Wordcheck():
* Function that checks words in dictionary and prints word with most letters in it 

######Variables
  | Code |
  | :--- |
  |`*counter = 0`|
  |`*longest_word = ""`|
  |`*characters = 0`|
  |`*result =[]`|
  
  
  
  
  
  
## How to Runner this Program

  * When you download my project 
  * Open it on *Nope Pad* and right it on and *Click Open containing floder* in Cmd
  * When Cmd open type in *python wordcountdown2.py*
  * It will bring up the Longest Word and the Longest Number of the Word
  


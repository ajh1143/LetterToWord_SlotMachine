# NLTK Slot Machine

## Enter Letters, Get Lucky

### Process

Runs a simulation similar to a slot machine. 

A user is asked to enter 3 english language letters, with a minimum of at least 1 vowel. 

An NLTK Corpus Dictionary is loaded as a source of valid English language words. This list of valid words is compared to a 
generated list of permutations of the three letters chosen by the user, creating a list of possible valid words.

The user then "pulls a lever" using the space bar, and the three letters are randomly generated in a random order. If there is a
match between the Slot Machine results and the NLTK Corpus Dictionary, the user wins. 

The user may continue to play by using the space bar, or can end the simulation with any other key. 

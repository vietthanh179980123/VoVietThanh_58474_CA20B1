"""
Author: Vo Viet Thanh
Date: 8/10/2021
Program: Generating Sentences
Solution:
    1.Request
    Write a program that generates sentences.
    2.Analysis
    Sentences in any language have a structure defined by a grammar. They also include
    a set of words from the vocabulary of the language. The vocabulary of a language
    like English consists of many thousands of words, and the grammar rules are quite
    complex. For the sake of simplicity our program will generate sentences from a simplified subset of English. The vocabulary will consist of sample words from several
    parts of speech, including nouns, verbs, articles, and prepositions. From these words,
    you can build noun phrases, prepositional phrases, and verb phrases. From these
    constituent phrases, you can build sentences. For example, the sentence “The girl hit
    the ball with the bat” contains three noun phrases, one verb phrase, and one prepositional phrase. Table 5-3 summarizes the grammar rules for our subset of English.
    The rule for Noun phrase says that it is an Article followed by (1) a Noun. Thus, a
    possible noun phrase is “the bat.” Note that some of the phrases in the left column of
    Table 5-3 also appear in the right column as constituents of other phrases. Although
    this grammar is much simpler than the complete set of rules for English grammar,
    you should still be able to generate sentences with quite a bit of structure.
    The program will prompt the user for the number of sentences to generate. The proposed user interface follows:
    Enter the number of sentences: 3
    THE BOY HIT THE BAT WITH A BOY
    THE BOY HIT THE BALL BY A BAT
    THE BOY SAW THE GIRL WITH THE GIRL
    Enter the number of sentences: 2
    A BALL HIT A GIRL WITH THE BAT
    A GIRL SAW THE BAT BY A BOY
    3.Design
    Of the many ways to solve the problem in this case study, perhaps the simplest is
    to assign the task of generating each phrase to a separate function. Each function
    builds and returns a string that represents its phrase. This string contains words
    drawn from the parts of speech and from other phrases. When a function needs an
    individual word, it is selected at random from the words in that part of speech. When
    a function needs another phrase, it calls another function to build that phrase. The
    results, all strings, are concatenated with spaces and returned.
    The function for Sentence is the easiest. It just calls the functions for Noun phrase
    and Verb phrase and concatenates the results, as in the following:
    def sentence():
        'Builds and returns a sentence.'
        return nounPhrase() + " " + verbPhrase() + "."
    The function for Noun phrase picks an article and a noun at random from the vocabulary,
    concatenates them, and returns the result. We assume that the variables articles and
    nouns refer to collections of these parts of speech and develop these later in the design.
    The function random.choice returns a random element from such a collection.
    def nounPhrase() :
        'Builds and returns a noun phrase.'
        return random.choice(articles) + " " + random.choice(nouns)
    The design of the remaining two phrase-structure functions is similar.
    The main function drives the program with a count-controlled loop:
    def main():
        'Allows the user to input the number of sentences to generate.'
        number = int(input("Enter the number of sentences: "))
        for count in range(number):
            print(sentence())
    The variables articles and nouns used in the program’s functions refer to the collections of actual words belonging to these two parts of speech. Two other collections,
    named verbs and prepositions, also will be used. The data structure used to represent a collection of words should allow the program to pick one word at random.
    Because the data structure does not change during the course of the program, you
    can use a tuple of strings. Four tuples serve as a common pool of data for the functions in the program and are initialized before the functions are defined.
    4.Implementation (Coding)
    When functions use a common pool of data, you should define or initialize the data
    before the functions are defined. Thus, the variables for the data are initialized just
    below the import statement.
    5.Testing
    Poetry it’s not, but testing is still important. The functions developed in this case
    study can be tested in a bottom-up manner. To do so, you must initialize the data
    first. Then you can run the lowest-level function, nounPhrase, immediately to check
    its results, and you can work up to sentences from there.
    On the other hand, testing can also follow the design, which took a top-down path.
    You might start by writing headers for all of the functions and simple return statements that return the functions’ names. Then you can complete the code for the sentence function first, test it, and proceed downward from there. The wise programmer
    can also mix bottom-up and top-down testing as needed.
    ....
"""
import random
# Vocabulary: words in 4 different parts of speech
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
def sentence():
    """Builds and returns a sentence."""
    return nounphrase() + " " + verbphrase()
def nounphrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)
def verbphrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounphrase() + " " + \
    prepositionalphrase()
def prepositionalphrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounphrase()
def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
# The entry point for program execution
    if __name__ == "__main__":
        main()

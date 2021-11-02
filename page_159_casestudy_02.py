"""
Author: Vo Viet Thanh
Date: 8/10/2021
Program: Nondirective Psychotherapy
Solution:
    1.Request
    Write a program that emulates a nondirective psychotherapist.
    2.Analysis
    Analysis
    Figure 5-4 shows the program’s interface as it changes throughout a sequence of
    exchanges with the user.
    When the user enters a statement, the program responds in one of two ways:
    1. With a randomly chosen hedge, such as “Please tell me more.”
    2. By changing some key words in the user’s input string and appending this string
    to a randomly chosen qualifier. Thus, to “My teacher always plays favorites,” the
    program might reply, “Why do you say that your teacher always plays favorites?”
    Figure 5-4 A session with the doctor program
    'Good morning, I hope you are well today.
    What can I do for you?
    >> My mother and I don't get along
    Why do you say that your mother and you don't get along
    >> she always favors my sister
    You seem to think that she always favors your sister
    >> my dad and I get along fine
    Can you explain why your dad and you get along fine
    >> he helps me with my homework
    Please tell me more
    >> quit
    Have a nice day!'
    3.Design
    The program consists of a set of collaborating functions that share a common data
    pool.
    Two of the data sets are the hedges and the qualifiers. Because these collections do
    not change and their elements must be selected at random, you can use tuples to
    represent them. Their names, of course, are hedges and qualifiers.
    The other set of data consists of mappings between first-person pronouns and
    second-person pronouns. For example, when the program sees “I” in a patient’s
    input, it should respond with a sentence containing “you.” The best type of data
    structure to hold these correlations is a dictionary. This dictionary is named
    replacements.
    The main function displays a greeting, displays a prompt, and waits for user input.
    The following is pseudocode for the main loop:
    output a greeting to the patient
    while True
        prompt for and input a string from the patient
        if the string equals "Quit"
            output a sign-off message to the patient
            break
        call another function to obtain a reply to this string
        output the reply to the patient
    Our therapist might not be an expert, but there is no charge for its services. What’s
    more, our therapist seems willing to go on forever. However, if the patient must quit
    to do something else, she can do so by typing “quit” to end the program.
    The reply function expects the patient’s string as an argument and returns another
    string as the reply. This function implements the two strategies for making replies
    suggested in the analysis phase. A quarter of the time a hedge is warranted.
    Otherwise, the function constructs its reply by changing the persons in the patient’s
    input and appending the result to a randomly selected qualifier. The reply function
    calls yet another function, changePerson, to perform the complex task of changing
    persons
    def reply(sentence):
        'Builds and returns a reply to the sentence.'
        probability = random.randint(1, 4)
        if probability == 1:
            return random.choice(hedges)
        else:
            return random.choice(qualifiers) + changePerson(sentence)
    The changePerson function extracts a list of words from the patient’s string. It then
    builds a new list wherein any pronoun key in the replacements dictionary is replaced
    by its pronoun/value. This list is then converted back to a string and returned.
    161
    def changePerson(sentence):
        'Replaces first person pronouns with second person
        pronouns.'
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(replacements.get(word, word))
        return " ".join(replyWords)
    Note that the attempt to get a replacement from the replacements dictionary
    either succeeds and returns an actual replacement pronoun, or the attempt fails and
    returns the original word. The string method join glues together the words from the
    replyWords list with a space character as a separator.
    4.Implementation (Coding)
    The structure of this program resembles that of the sentence generator developed in
    the first case study of this chapter. The three data structures are initialized near the
    beginning of the program, and they never change. The three functions collaborate in
    a straightforward manner
    5.Testing
    As in the sentence-generator program, the functions in this program can be tested in
    a bottom-up or a top-down manner. As you will see, the program’s replies break down
    when the user addresses the therapist in the second person, when the user inputs
    contractions (for example, I’m and I’ll), when the user addresses the doctor directly
    with sentences like “You are not listening to me,” and in many other ways. As you’ll
    see in the Projects at the end of this chapter, with a little work you can make the
    replies more realistic.

"""
import random
hedges = ("Please tell me more.",
        "Many of my patients tell me the same thing.",
        "Please continue.")
qualifiers = ("Why do you say that ",
            "You seem to think that ",
            "Can you explain why ")
replacements = {"I":"you", "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours"}
def reply(sentence):
    """Builds and returns a reply to the sentence."""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changeperson(sentence)
def changeperson(sentence):
    """Replaces first person pronouns with second person
    pronouns."""
    words = sentence.split()
    replywords = []
    for word in words:
        replywords.append(replacements.get(word, word))
        return " ".join(replywords)
def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))
# The entry point for program execution
if __name__ == "__main:":
    main()

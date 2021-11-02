"""
Author: Võ Viết Thanh
Date: 24/09/2021
Program: Text Analysis
Solution:
    1. Request
    Write a program that computes the Flesch Index and grade level for text stored in a
    text file.
    2. Analysis
    The input to this program is the name of a text file. The outputs are the number of
    sentences, words, and syllables in the file, as well as the file’s Flesch Index and Grade
    Level Equivalent.
    During analysis, we consult experts in the problem domain to learn any information that might be relevant in solving the problem. For our problem, this information
    includes the definitions of sentence, word, and syllable.
    Note that the definitions of word and sentence are approximations. Some words, such
    as doubles and kettles, end in -es but will be counted as having one syllable, and an
    ellipsis ( … ) will be counted as three syllables.
    Flesch’s formula to calculate the index F is the following:
    F words sentences syllables words − × − × 206.835 1.015 ( / ) 84.6 ( / ) 5
    The Flesch-Kincaid Grade Level Formula is used to compute the Equivalent Grade
    Level G:G words sentences syllables words ( ) ( ) × × − 0.39 / 11.8 / 15.59 5 1
    3.Design
    This program will perform the following tasks:
    1. Receive the filename from the user, open the file for input, and input the text.
    2. Count the sentences in the text.
    3. Count the words in the text.
    4. Count the syllables in the text.
    5. Compute the Flesch Index.
    6. Compute the Grade Level Equivalent.
    7. Print these two values with the appropriate labels, as well as the counts from
    tasks 2–4.
    The first and last tasks require no design. Let’s assume that the text is input as a single string from the file and is then processed in tasks 2–4. These three tasks can be
    designed as code segments that use the input string and produce an integer value.
    Task 5, computing the Flesch Index, uses the three integer results of tasks 2–4 to
    compute the Flesch Index. Lastly, task 6 is a code segment that uses the same integers and computes the Grade Level Equivalent. The five tasks are listed in Table 4-8,
    where text is a variable that refers to the string read from the file.
    All the real work is done in the tasks that count the items:
    • Add the number of characters in text that end the sentences. These characters
    were specified in analysis, and the string method count is used to count them in
    the algorithm.
    • Split text into a list of words and determine the text length.
    • Count the syllables in each word in text.
    The last task is the most complex. For each word in the text, we must count the
    syllables in that word. From analysis, we know that each distinct vowel counts as a
    syllable, unless it is in the endings -ed, -es, or -e (but not -le). For now, we ignore the
    possibility of consecutive vowels.
    4.Implementation (Coding)
    The main tasks are marked off in the program code with a blank line and
    a comment.
    5.Testing
    Although the main tasks all collaborate in the text analysis program, they can be
    tested more or less independently, before the entire program is tested. After all, there
    is no point in running the complete program if you are unsure that even one of the
    tasks does not work correctly.
    This kind of procedure is called bottom-up testing. Each task is coded and tested
    before it is integrated into the overall program. After you have written code for one
    or two tasks, you can test them in a short script. This script is called a driver. For
    example, here is a driver that tests the code for computing the Flesch Index and the
    Grade Level Equivalent without using a text file:

    Program: fleschdriver.py
    Author: Ken
    Test driver for Flesch Index and Grade level.

    sentences = int(input("Sentences: "))
    words = int(input("Words: "))
    syllables = int(input("Syllables: "))
    index = 206.835 – 1.015 * (words / sentences) – \
     84.6 * (syllables / words)
    print("Flesch Index:", index)
    level = round(0.39 * (words / sentences) + 11.8 * \
     (syllables / words) – 15.59)
    print("Grade Level: ", level)
    This driver allows the programmer not only to verify the two tasks, but also to obtain
    some data to use when testing the complete program later on. For example, the
    programmer can supply a text file that contains the number of sentences, words, and
    syllables already tested in the driver, and then compare the two test results.
    In bottom-up testing, the lower-level tasks must be developed and tested before those
    tasks that depend on the lower-level tasks.
    When you have tested all of the parts, you can integrate them into the complete
    program. The test data at that point should be short files that produce the expected
    results. Then, you should use longer files. For example, you might see if plaintext versions of Dr. Seuss’s Green Eggs and Ham and Shakespeare’s Hamlet produce grade
    levels of 5th grade and 12th grade, respectively. Or you could test the program with
    its own source program file—but we predict that its readability will seem quite low,
    because it lacks most of the standard end-of-sentence marks!
    ....
"""
# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()
# Count the sentences
sentences = text.count('.') + text.count('?') + \
 text.count(':') + text.count(';') + \
 text.count('!')
# Count the words
words = len(text.split())
# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
        if word.endswith('le'):
            syllables += 1
# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
84.6 * (syllables / words)
level = round(0.39 * (words / sentences) + 11.8 * \
(syllables / words) - 15.59)
# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")

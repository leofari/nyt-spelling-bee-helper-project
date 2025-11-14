'''
Leo Farina
5/2/24
Comp 112.01
Final Project
'''

import os
from bs4 import BeautifulSoup
import requests
from datetime import date

# Get the Spelling Bee puzzle page
page = requests.get('https://www.nytimes.com/puzzles/spelling-bee')
soup = BeautifulSoup(page.text, 'html.parser')

# Find all <script> tags on the page
script_tags = soup.find_all('script')

# Locate the script tag that contains the gameData object
for item in script_tags:
    item_str = str(item)
    if "window.gameData" in item_str:
        scrapeMe = item_str
        break

# At this point, scrapeMe is a long string containing the game data,
# including the outer letters and the center letter.


def outerLetterInfo(scrapeMe):
    '''str -> str
    Searches through the long string scraped from the NYT website
    and returns the outer letters as a string.'''
    acc = ''
    for x in range(len(scrapeMe)):
        if scrapeMe[x:x+16] == '"outerLetters":[':
            outerLetters = scrapeMe[x+16:x+39]
            break
    for ch in outerLetters:
        if ch.isalpha():
            acc += ch
    return acc


def findCenterLetter(scrapeMe):
    '''str -> str
    Searches through the long string scraped from the NYT website
    and returns the center letter as a string.'''
    for x in range(len(scrapeMe)):
        if scrapeMe[x:x+16] == '"centerLetter":"':
            centerLetter = scrapeMe[x+16]
            return centerLetter


def findBadLetters(outerLetters):
    '''sig: str -> str
    Takes the string of valid letters (outerLetters) and uses the
    global centerLetter. Returns a string of all letters that are NOT valid.'''
    acc = ''
    for alpha in 'abcdefghijklmnopqrstuvwxyz':
        if alpha not in outerLetters and alpha not in centerLetter:
            acc = acc + alpha
    return acc


# Get the puzzle letters
outerLetters = outerLetterInfo(scrapeMe)
centerLetter = findCenterLetter(scrapeMe)
badLetters = findBadLetters(outerLetters)


# This helper removes '\n' from the end of a line
def remove_n(item):
    '''sig: str -> str
    Removes '\n' from the end of the line (if present)
    and returns the cleaned string.'''
    if '\n' in item:
        return item[:len(item) - 1]
    return item


def findCorrectWords(path):
    '''sig: str -> list
    Takes a file path as input,
    returns a list of words that fit the criteria for the daily spelling bee.'''
    OED = open(path, 'r')
    newlist = []
    while True:
        currentWord = remove_n(OED.readline())
        validWord = True

        # Stop when we reach the end of the file
        if currentWord == '':
            OED.close()
            return newlist

        # Check that every character is allowed
        for char in currentWord:
            if validWord:
                if char in badLetters:
                    validWord = False

        # Must contain the center letter and be at least 4 letters long
        if validWord and (centerLetter in currentWord) and (len(currentWord) >= 4):
            newlist += [currentWord]




# Helper function that sorts a list from low to high
def alphabatizeList(unsortedList):
    '''sig: list -> list
    Takes a list and sorts its elements from lowest to highest.
    Returns the sorted list.'''
    unsorted = True
    while unsorted:
        unsorted = False
        for x in range(1, len(unsortedList)):
            if unsortedList[x - 1] > unsortedList[x]:
                unsortedList[x - 1], unsortedList[x] = unsortedList[x], unsortedList[x - 1]
                unsorted = True
    return unsortedList


# Function that creates a dictionary mapping each word length to a list of words
def sort_by_len(unsortedList):
    '''sig: list -> dict
    Takes a list of words and creates a dictionary where each key is a word length
    mapped to the list of words of that length.'''
    myDict = {}
    for element in unsortedList:
        if len(element) not in myDict:
            myDict[len(element)] = [element]
        else:
            myDict[len(element)] += [element]
    # Sort each list of words alphabetically
    for key in myDict:
        alphabatizeList(myDict[key])
    return myDict


def createPangramKey(myDict):
    '''sig: dict -> dict
    Takes the dictionary created in sort_by_len and adds a "Pangrams" key
    containing any pangrams (words that use all puzzle letters).'''
    pangrams = []
    for key in myDict:
        # Pangrams must be at least 7 letters long
        if key >= 7:
            for element in myDict[key]:
                isPangram = True
                for letter in outerLetters + centerLetter:
                    if letter not in element:
                        isPangram = False
                if isPangram:
                    pangrams += [element]
    if pangrams != []:
        myDict["Pangrams"] = pangrams
    return myDict




def save_results(path, results):
    '''sig: str * dict -> None
    Takes a directory path and a results dict, and writes a file containing
    the results to that location.'''
    keys = list(results.keys())

    # Remove the "Pangrams" key before sorting (since it is a string)
    for x in range(len(keys)):
        if isinstance(keys[x], str):
            keys.pop(x)
            break  # only one string key is expected

    orderedKeys = alphabatizeList(keys)  # sorts the list from smallest to largest
    if "Pangrams" in results:
        orderedKeys.append("Pangrams")  # add pangram key at the end

    # Make sure the directory exists
    os.makedirs(path, exist_ok=True)

    today = date.today()
    todaysFile = os.path.join(path, f"{today}.txt")

    with open(todaysFile, 'w') as f:
        for x in orderedKeys:
            f.write(str(x) + ':\n')
            f.write(str(results[x]) + '\n')


import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Find all valid NYT Spelling Bee words from a word list."
    )
    parser.add_argument(
        "--wordlist", "-w",
        default="words_alpha.txt",
        help="Path to the word list file (default: words_alpha.txt in the current directory)."
    )
    parser.add_argument(
        "--output-dir", "-o",
        default="results",
        help="Directory where the results file will be saved (default: ./results)."
    )

    args = parser.parse_args()

    # Compute valid words
    newlist = findCorrectWords(args.wordlist)
    myDict = sort_by_len(newlist)
    results = createPangramKey(myDict)

    # Save to disk
    save_results(args.output_dir, results)


if __name__ == "__main__":
    main()








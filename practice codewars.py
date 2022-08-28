# Beginner Series #3 Sum of Numbers
#
#
# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including
# them and return it. If the two numbers are equal return a or b.
#
# Note: a and b are not ordered!

def get_sum(a,b):
    if a == b:
        return a
    if a > b:
        a, b = b, a
    list = [i for i in range(int(a), int(b) + 1)]
    list.sort()
    counter = 0
    for i in list:
        counter += i
    return counter


# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.
#
# Examples(Input1, Input2 --> Output):
#
# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"


def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"


# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string
# should be retained.
#
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    return ' '.join([word[::-1] for word in text.split(" ")])


# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
# No floats or non-positive integers will be passed.
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
# [10, 343445353, 3453445, 3453545353453] should return 3453455.

def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]


# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative
# numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.
#
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    poz = 0
    neg = 0
    result = []
    if arr == []:
        return []
    for i in arr:
        if i == 0:
            continue
        elif i > 0:
            poz += 1
        else:
            neg += i
    result.append(poz)
    result.append(neg)
    return result


# Write a function which calculates the average of the numbers in a given list.
#
# Note: Empty arrays should return 0.

def find_average(numbers):
    result = 0
    if numbers == []:
        return 0
    for i in numbers:
        result += i
    return result/len(numbers)

# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded
# with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets
# he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another
# specific given number of dragons, will he survive?
#
# Return True if yes, False otherwise :)

def hero(bullets, dragons):
    return True if bullets/2 >= dragons else False



# Complete the solution so that it reverses the string passed into it.
#
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string):
    string = list(string)
    string.reverse()
    return ''.join(string)

def solution(str):
    return str[::-1]


# Note: This kata is inspired by Convert a Number to a String!. Try that one too.
#
# Description
# We need a function that can transform a string into a number. What ways of achieving this do you know?
#
# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.
#
# Examples
# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7

def string_to_number(s):
    return int(s)


# Write function bmi that calculates body mass index (bmi = weight / height2).
#
# if bmi <= 18.5 return "Underweight"
#
# if bmi <= 25.0 return "Normal"
#
# if bmi <= 30.0 return "Overweight"
#
# if bmi > 30 return "Obese"

def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return 'Underweight'
    elif 18.5 <= bmi <= 25.0:
        return 'Normal'
    elif 25.0 <= bmi <= 30.0:
        return 'Overweight'
    else:
        return 'Obese'


# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
#
# Return your answer as a number.

def sum_mix(arr):
    total = 0
    for i in arr:
        if isinstance(i, int):
            total += i
        else:
            i = int(i)
            total += i
    return total


def sum_mix(arr):
    return sum(map(int, arr))



# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any
# elements with the same value next to each other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(iter):
    iter = list(iter)
    result = []
    for i in range(len(iter)):
        if i == 0 or iter[i] != iter[i - 1]:
            result.append(iter[i])
        else:
            continue
    return result


def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res


# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive.
# The string can contain any char.
#
# Examples input/output:
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    x = 0
    o = 0
    for i in s:
        if i == 'X' or i == 'x':
            x += 1
        elif i == 'O' or i == 'o':
            o += 1
        else:
            continue
    if x == o:
        return True
    else:
        return False


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


# Clock shows h hours, m minutes and s seconds after midnight.
#
# Your task is to write a function which returns the time since midnight in milliseconds.
#
# Example:
# h = 0
# m = 1
# s = 1
#
# result = 61000
# Input constraints:
#
# 0 <= h <= 23
# 0 <= m <= 59
# 0 <= s <= 59


def past(h, m, s):
    result = (h * 60 * 60 + m * 60 + s) * 1000
    return result


# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.
#
# This is the first kata in series:
#
# Find the unique number (this kata)
# Find the unique string
# Find The Unique




def find_uniq(arr):
    for i in range(len(arr)):
        if arr[i] == arr[i+1]:
            continue
        else:
            if i == 0 and arr[i] != arr[i + 2]:
                return arr[i]
            return arr[i + 1]
# Time: 1401 ms
# Completed in 5.25 ms


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
# Time: 879 ms
# Completed in 5.06ms



# Opposites Attract
# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each.
# If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
#
# Write a function that will take the number of petals of each flower and return true if they are in love and false if
# they aren't.

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    elif flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    else:
        return False

def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2


# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
#
# Examples
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
# Notes
# The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

def make_negative( number ):
    if number > 0:
        return number * -1
    elif number == 0:
        return 0
    else:
        return number


def make_negative(number):
    return -abs(number)


# Friend or Foe?
#
# Make a program that filters a list of strings and returns a list with only your friends name in it.
#
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure
# he's not...
#
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
#
# i.e.
#
# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.

def friend(x):
    friends = []
    for i in x:
        if len(i) == 4:
            friends.append(i)
        else:
            continue
    return friends


def friend(x):
    return [f for f in x if len(f) == 4]


# Will you make it?
#
# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is ' \
#         'running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles ' \
#         'per gallon. There are 2 gallons left.
#
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
#
# Function should return true if it is possible and false if not.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if mpg * fuel_left >= distance_to_pump else False


def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left



# Who likes it?
#
# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item. It must return the display
# text as shown in the examples:
#
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

def likes(names):
    if names == []:
        return 'no one likes this'
    else:
        if len(names) == 1:
            return '{} likes this'.format(names[0])
        elif len(names) == 2:
            return '{} and {} like this'.format(names[0], names[1])
        elif len(names) == 3:
            return '{}, {} and {} like this'.format(names[0], names[1], names[2])
        else:
            return '{}, {} and {} others like this'.format(names[0], names[1], len(names) - 2)



# Persistent Bugger.
#
# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.
#
# For example (Input --> Output):
#
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

def persistence(n):
    n_str = str(n)
    n_list = list(n_str)
    if len(n_list) == 1:
        return 0
    count = 0
    while len(n_list) != 1:
        b = 1
        for i in n_list:
            b *= int(i)
        count += 1
        n_str = str(b)
        n_list = list(n_str)
    return count


import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i



# Reversed sequence
#
# Build a function that returns an array of integers from n to 1 where n>0.
#
# Example : n=5 --> [5,4,3,2,1]

def reverse_seq(n):
    n = list(reversed(range(1, n + 1)))
    return n

def reverseseq(n):
    return list(range(n, 0, -1))



# 8 kyu
# Are You Playing Banjo?
#
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
#
# The function takes a name as its only argument, and returns one of the following strings:
#
# name + " plays banjo"
# name + " does not play banjo"
# Names given are always valid strings.

def are_you_playing_banjo(name):
    name = list(name)
    if name[0] == 'R' or name[0] == 'r':
        return '{} plays banjo'.format(''.join(name))
    else:
        return '{} does not play banjo'.format(''.join(name))


def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"



# 7 kyu
# Complementary DNA
#
# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the
#     development and functioning of living organisms.
#
# If you want to know more: http://en.wikipedia.org/wiki/DNA
#
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of
# the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or
# there is no DNA at all (again, except for Haskell).
#
# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)
#
# Example: (input --> output)
#
# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

def DNA_strand(dna):
    list = []
    for i in dna:
        if i == 'T':
            list.append('A')
        elif i == 'A':
            list.append('T')
        elif i == 'C':
            list.append('G')
        else:
            list.append('C')
    dna = ''.join(list)
    return dna

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])



# 8 kyu
# Remove String Spaces
#
# Simple, remove the spaces from the string, then return the resultant string.

def no_space(x):
    return x.replace(' ', '')



# 6 kyu
# Equal Sides Of An Array
#
# You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of
# the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would
# make this happen, return -1.
#
# For example:
#
# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index
# ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.
#
# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index
# ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.
#
# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.
#
# Note: Please remember that in most programming/scripting languages the index of an array starts at 0.
#
# Input:
# An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.
#
# Output:
# The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index
# that fits these rules, then you will return -1.
#
# Note:
# If you are given an array with multiple answers, return the lowest correct index.


def find_even_index(arr):
    for i in range(0,len(arr)):
        s1 = sum(arr[j] for j in range(0,i))
        s2 = sum(arr[j] for j in range(i+1,len(arr)))
        if s1 == s2:
            return i
    return -1

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1



# 8 kyu
# Find Maximum and Minimum Values of a List
#
# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively.
#
# Examples (Input -> Output)
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# Notes
# You may consider that there will not be any empty arrays/vectors.

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)



# 6 kyu
# Duplicate Encoder
#
# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that
# character appears only once in the original string, or ")" if that character appears more than once in the original
# string. Ignore capitalization when determining if a character is a duplicate.
#
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("
# Notes
# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX",
# the "XXX" is the expected result, not the input!

from collections import Counter
def duplicate_encode(word):
    str = []
    word = word.lower()
    word = list(word)
    count = Counter(word)
    for i in word:
        if count[i] == 1:
            str.append('(')
        else:
            str.append(')')
    str = ''.join(str)
    return str

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])



# 6 kyu
# Take a Ten Minutes Walk
#
# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to
# an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a
# Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings
# representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter
#     (direction) and you know it takes you one minute to traverse one city block, so create a function that will return
#     true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and
#     will, of course, return you to your starting point. Return false otherwise.
#
# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w'
# only). It will never give you an empty array (that's not a walk, that's standing still!).

def is_valid_walk(walk):
    finish_x, finish_y = 0, 0
    count_time = 0
    for i in walk:
        if i =='n':
            finish_y += 1
            count_time += 1
        elif i == 's':
            finish_y -= 1
            count_time += 1
        elif i == 'e':
            finish_x += 1
            count_time += 1
        else:
            finish_x -= 1
            count_time += 1
    if finish_x == 0 and finish_y == 0 and count_time == 10:
        return True
    else:
        return False


def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')



# 8 kyu
# Beginner Series №4 Cockroach
#
# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in
# cm per second, rounded down to the integer (= floored).
#
# For example:
# 1.08 --> 30
#
# Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.


def cockroach_speed(s):
    return int(s *100000/3600)



# 8 kyu
# If you can't sleep, just count sheep!!
#
# If you can't sleep, just count sheep!!
#
# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will
# always be valid, i.e. no negative integers.

def count_sheep(n):
    str = ''
    list = range(1, n + 1)
    for i in list:
        str += '{} sheep...'.format(i)
    return str

def count_sheep(n):
    return "".join("{} sheep...".format(i) for i in range(1, n+1))



# 7 kyu
# The highest profit wins!
#
# Story
# Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give
# him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the
# lowest possible price and sell it at the highest.
#
# Task
# Write a function that returns both the minimum and maximum number of the given list/array.
#
# Examples (Input --> Output)
# [1,2,3,4,5] --> [1,5]
# [2334454,5] --> [5,2334454]
# [1]         --> [1,1]
# Remarks
# All arrays or lists will always have at least one element, so you don't need to check the length. Also, your function
# will always get an array or a list, you don't have to check for null, undefined or similar.

def min_max(lst):
    n = []
    n.append(min(lst))
    n.append(max(lst))
    return n

def min_max(lst):
  return [min(lst), max(lst)]



# 8 kyu
# L1: Set Alarm
#
# Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever you are
# employed and the second parameter, vacation is true whenever you are on vacation.
#
# The function should return true if you are employed and not on vacation (because these are the circumstances under
# which you need to set an alarm). It should return false otherwise. Examples:
#
# setAlarm(true, true) -> false
# setAlarm(false, true) -> false
# setAlarm(false, false) -> false
# setAlarm(true, false) -> true

def set_alarm(employed, vacation):
    if employed == vacation or employed == False:
        return False
    else:
        return True



# 8 kyu
# Remove exclamation marks
#
# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    return s.replace('!', '')



# 8 kyu
# Keep Hydrated!
#
# Nathan loves cycling.
#
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
#
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest
# value.
#
# For example:
#
# time = 3 ----> litres = 1
#
# time = 6.7---> litres = 3
#
# time = 11.8--> litres = 5

def litres(time):
    return int(time * 0.5)



# 7 kyu
# String ends with?

# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument
# (also a string).
#
# Examples:
#
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false


def solution(string, ending):
    return string.endswith(ending)

def solution(string, ending):
    return ending in string[-len(ending):]



# 7 kyu
# Get the Middle Character
#
# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is
# odd, return the middle character. If the word's length is even, return the middle 2 characters.
#
# #Examples:
#
# Kata.getMiddle("test") should return "es"
#
# Kata.getMiddle("testing") should return "t"
#
# Kata.getMiddle("middle") should return "dd"
#
# Kata.getMiddle("A") should return "A"
# #Input
#
# A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due
# to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need
# to worry about your solution timing out.
#
# #Output
#
# The middle character(s) of the word represented as a string.

def get_middle(s):
    if len(s) % 2 == 0:
        return s[int(len(s)/2) - 1 : int(len(s)/2) + 1]
    else:
        return s[int(len(s)/2)]


# 8 kyu
# Transportation on vacation
#
# After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and
# your girlfriend and try to leave all the mess behind you.
#
# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you
# some good offers.
#
# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total.
# Alternatively, if you rent the car for 3 or more days, you get $20 off your total.
#
# Write a code that gives out the total amount for different days(d).

def rental_car_cost(d):
    if d < 3:
        return d * 40
    elif 3 <= d < 7:
        return d * 40 - 20
    else:
        return d * 40 - 50



# 8 kyu
# Double Char
#
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
#
# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

# Good Luck!

def double_char(s):
    result = []
    for i in s:
        result.append(i * 2)
    return ''.join(result)

def double_char(s):
    return ''.join(c * 2 for c in s)



# 6 kyu
# Build Tower
#
# Build Tower
# Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*"
# character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
# And a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]
# Go challenge Build Tower Advanced once you have finished this
# ( https://www.codewars.com/kata/57675f3dedc6f728ee000256 ):)


def tower_builder(n_floors):
    res = []
    i = 1
    width = n_floors + (n_floors - 1)
    for i in range(1, n_floors + 1):
        res.append("{0:^{1}.{2}}".format("*"*(i+(i-1)), width, width))
    return res

def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]



# 8 kyu
# Convert a string to an array
#
# Write a function to split a string and convert it into an array of words.
#
# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]
#
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

def string_to_array(s):
    list = []
    word = ''
    if s == '':
        return ['']
    for i in s:
        if i != ' ':
            word += i
        else:
            list.append(word)
            word = ''
    list.append(word)
    return list

def string_to_array(string):
    return string.split(" ")



# 6 kyu
# Mexican Wave
#
# Introduction
# The wave (known as the Mexican wave in the English-speaking world outside North America) is an example of metachronal
# rhythm achieved in a packed stadium when successive groups of spectators briefly stand, yell, and raise their arms.
# Immediately upon stretching to full height, the spectator returns to the usual seated position.
#
# The result is a wave of standing spectators that travels through the crowd, even though individual spectators never
# move away from their seats. In many large arenas the crowd is seated in a contiguous circuit all the way around the
# sport field, and so the wave is able to travel continuously around the arena; in discontiguous seating arrangements,
# the wave can instead reflect back and forth through the crowd. When the gap in seating is narrow, the wave can
# sometimes pass through it. Usually only one wave crest will be present at any given time in an arena, although
# simultaneous, counter-rotating waves have been produced. (Source Wikipedia)
# Task
# In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a
# string and you must return that string in an array where an uppercase letter is a person standing up.
# Rules
#  1.  The input string will always be lower case but maybe empty.
#
#  2.  If the character in the string is whitespace then pass over it as if it was an empty seat
# Example
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

# Good luck and enjoy!

# Kata Series
# If you enjoyed this, then please try one of my other Katas. Any feedback, translations and grading of beta Katas are
# greatly appreciated. Thank you.
#
# Maze Runner
#
# Scooby Doo Puzzle
#
# Driving License
#
# Connect 4
#
# Vending Machine
#
# Snakes and Ladders
#
# Mastermind
#
# Guess Who?
#
# Am I safe to drive?
#
# Mexican Wave
#
# Pigs in a Pen
#
# Hungry Hippos
#
# Plenty of Fish in the Pond
#
# Fruit Machine
#
# Car Park Escape


def wave(people):
    if len(people) == 0:
        return []
    else:
        result = []
        people = people.lower()
        for e, i in enumerate(people):
            if i == ' ':
                continue
            else:
                result.append(people[:e] + people[e].upper() + people[e+1:])
        return result


def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]



# 8 kyu
# Function 3 - multiplying two numbers
#
# Implement a function called multiply, which takes two numbers and returns their product:
#
# multiply(2, 3) = 6
# multiply(0, 188) = 0
# multiply(85, 144) = 12240

def multiply(x, y):
    return x * y



# 6 kyu
# Array.diff
#
# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the
# result.
#
# It should remove all values from list a, which are present in list b keeping their order.
#
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    c = []
    for i in a:
        if i not in b:
            c.append(i)
        else:
            continue
    return c

def array_diff(a, b):
    return [x for x in a if x not in b]



# 8 kyu
# Convert a Number to a String!
#
# We need a function that can transform a number (integer) into a string.
#
# What ways of achieving this do you know?
#
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

def number_to_string(num):
    return str(num)



# 7 kyu
# You're a square!
#
# A square of squares
# You like building blocks. You especially like building blocks that are squares. And what you even like more, is to
# arrange them into a square of square building blocks!
#
# However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those
# blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just
# have to check if your number of building blocks is a perfect square.
#
# Task
# Given an integral number, determine if it's a square number:
#
# In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words,
# it is the product of some integer with itself.
#
# The tests will always use some integral number, so don't worry about that in dynamic typed languages.
#
# Examples
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false

def is_square(n):
    sqrt = pow(n, 0.5)
    return True if n == sqrt * sqrt else False

import math

def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;


import math

def is_square(n):
    if n < 0:
        return False
    sqrt = math.sqrt(n)
    return sqrt.is_integer()



# 6 kyu
# Your order, please
#
# Your task is to sort a given string. Each word in the string will contain a single number. This number is the
# position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string. The words in the input String will only contain valid
# consecutive numbers.
#
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""


def order(sentence):
    count_words = len(sentence.split())
    list_sentence = list(range(0, count_words))
    order_str = ''.join(map(str, list(range(1, count_words + 1))))
    a = sentence.split()
    for i, val in enumerate(a):
        for x in val:
            if x in order_str:
                list_sentence[int(x) - 1] = val
            else:
                continue
    list_sentence = ' '.join(list_sentence)
    return list_sentence


def order(words):
    return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
# The first number in strings in this list a = ['2is', '1This', '4Test', '3a'] is a very powerful feature for
# comparison these strings! No matter that '2is shorter than '1This' and '1This' starts with big letter and '2is start
# with small letter. sorted() function will compare these strings using number 2 and number 1 only becuase they are
# both at the beginning of the strings (which are in the list)
#
# but the problem here is that we can't do it when the numbers are not at the beginning.By the way, the incoming data
# in this kata is something like this 'ca2da ab1ra b3ra'. See ? Wee need to do something with these numbers! We need
# to transofrm this 'ca2da ab1ra b3ra' in this ['2cada', '1abra', '3bra'].
# Now we can use sorted(['2cada', '1abra', '3bra']) and the output will be  ['1abra','2cada', '3bra']
#
# just try to do that: a = ['2is', '1This', '4Test', '3a']
# print(sorted(a))
# Output: ['1This', '2is', '3a', '4Test']
#
# and now let's change the position of numbers in strings! a = ['i2s', 'This1', '4Test', 'a3']
# print(sorted(a)) Output: ['4Test', 'This1', 'a3', 'i2s']
#
# Ok, now the code:
#
# for example, the incoming data is 'ca2da Ab1ra b3ra then
#
# -----> words.split() -----> ['ca2da', 'Ab1ra', 'b3ra']
#
# ----->  key=lambda w:sorted(w)  -----> ['2cada', '1Abra', '3bra'] (Numbers take priority over letters in str type)
#
# ----->  sorted(['2cada', '1Abra', '3bra'])  -----> ['1Abra','2cada', '3bra'] Warning ! After comparison the items
# in the list regain their previous form but now they are sorted
# so the final result after sorted(['2cada', '1Abra', '3bra']) will be ['Ab1ra', 'ca2da', 'b3ra']
# Just what we need, right ?
#
# and finally -----> ' '.join(['Ab1ra', 'ca2da', 'b3ra']) -----> 'Ab1ra ca2da b3ra'



# 7 kyu
# Find the next perfect square!
#
# You might know some pretty large perfect squares. But what about the NEXT one?
#
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
#
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is
# non-negative.
#
# Examples:(Input --> Output)
#
# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square


import math

def find_next_square(sq):
    result = ((math.sqrt(sq) + 1) ** 2)
    return result if result % 1 == 0 else -1



# 6 kyu
# Sort the odd
#
# Task
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even
# numbers at their original positions.
#
# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(arr):
    dict = {}
    result = []
    for i, e in enumerate(arr):
        if e % 2 == 0:
            dict[i] = e
        else:
            result.append(e)
    result = sorted(result)
    for i in dict:
        result.insert(i, dict[i])
    return result

# ???
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]



# 6 kyu
# Count characters in your string
#
# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the
# result should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be empty object literal, {}.

def count(string):
    dict = {}
    for i in string:
        dict[i] = string.count(i)
    return dict

from collections import Counter

def count(string):
    return Counter(string)



# 5 kyu
# Directions Reduction
#
# Once upon a time, on a way through the old wild mountainous west,…
# … a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST".
# Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
#
# Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild
# west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die
# of thirst!
#
# How I crossed a mountainous desert the smart way.
# The directions given to the man are, for example, the following (depending on the language):
#
# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
# or
# { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
# or
# [North, South, South, East, West, North, West]
# You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place!
# So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:
#
# ["WEST"]
# or
# { "WEST" }
# or
# [West]
# Other examples:
# In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.
#
# The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final
# result is [] (nil in Clojure).
#
# In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they
# become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].
#
# Task
# Write a function dirReduc which will take an array of strings and returns an array of strings with the needless
# directions removed (W<->E or S<->N side by side).
#
# The Haskell version takes a list of directions with data Direction = North | East | West | South.
# The Clojure version returns nil when the path is reduced to nothing.
# The Rust version takes a slice of enum Direction {North, East, West, South}.
# See more examples in "Sample Tests:"
# Notes
# Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible.
# "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't
# become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
# if you want to translate, please ask before translating.

def dirReduc(arr):
    res = ' '.join(arr)
    res2 = res.replace('NORTH SOUTH', '').replace('SOUTH NORTH', '').replace('WEST EAST', '').replace('EAST WEST', '')
    res3 = res2.split()
    return dirReduc(res3) if len(res3) < len(arr) else res3


opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan



# 8 kyu
# Sentence Smash
#
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful,
# there shouldn't be a space at the beginning or the end of the sentence!
#
# Example
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

def smash(words):
    return ' '.join(words)



# 8 kyu
# DNA to RNA Conversion
#
# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four
# nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
#
# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical
# structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').
#
# Create a function which translates a given DNA string into RNA.
#
# For example:
#
# "GCAT"  =>  "GCAU"

# The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid,
# i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.

pairs = {'A':'A','T':'U','C':'C','G':'G'}
def dna_to_rna(dna):
    return ''.join(pairs[x] for x in dna)

def DNAtoRNA(dna):
    return dna.replace('T', 'U')



# 8 kyu
# Beginner Series #1 School Paperwork
#
# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork
# has 'm' pages.
#
# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
#
# Example:
# n= 5, m=5: 25
# n=-5, m=5:  0
# Waiting for translations and Feedback! Thanks!

def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0



# 8 kyu
# Removing Elements
#
# Take an array and remove every second element from the array. Always keep the first element and start removing with
# the next element.
#
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
#
# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):
    return my_list[::2]

def remove_every_other(my_list):
    return [v for c,v in enumerate(my_list) if not c%2]


# 7 kyu
# Two to One

# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible,
# containing distinct letters - each taken only once - coming from s1 or s2.
#
# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(s1, s2):
    return "".join(sorted([c for c in set(s1 + s2)]))



# 6 kyu
# Simple Encryption #1 - Alternating Split
#
# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed
# characters of S with all the even-indexed characters of S, this process should be repeated N times.
#
# Examples:
#
# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"
#
# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption function which reverses the process.
#
# If the string S is an empty value or the integer N is not positive, return the first argument without changes.
#
# This kata is part of the Simple Encryption Series:
#
# Simple Encryption #1 - Alternating Split
# Simple Encryption #2 - Index-Difference
# Simple Encryption #3 - Turn The Bits Around
# Simple Encryption #4 - Qwerty
# Have fun coding it and please don't forget to vote and rank this kata! :-)

def encrypt_once(text):
    e_str = ""
    o_str = ""

    for i in range(0, len(text)):
        if i % 2 != 0:
            e_str += text[i]
        else:
            o_str += text[i]

    return e_str + o_str


def encrypt(text, n):

    s = [text]
    if n <0:
        return text
    for i in range(1, n + 1):
        s.append(encrypt_once(s[i - 1]))

    return s[n]


def decrypt_once(text):
    decry_one = ""
    decry_two = ""

    mid = int(len(text) / 2)  ##find mid index

    decry_one += text[0:mid]  ## breaks string into two strings
    decry_two += text[mid:]

    s = ""

    for i in range(0, mid):
        s += decry_two[i] + decry_one[i]  ## combine alternating even and odd indices

    if len(text) % 2 != 0:
        s += decry_two[mid]  ## if length is odd , add the last index of decry_two

    return s


def decrypt(text, n):
    s = [text]
    if n < 0:
        return text
    for i in range(1, n + 1):
        s.append(decrypt_once(s[i - 1]))

    return s[n]

# ___________________________________
def decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text



# 8 kyu
# Switch it Up!

# When provided with a number between 0-9, return it in words.
#
# Input :: 1
#
# Output :: "One".
#
# If your language supports it, try using a switch statement.

nums = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
def switch_it_up(num):
    return nums[num]

def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]
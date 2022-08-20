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


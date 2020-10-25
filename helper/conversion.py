import re

amount = r'thousand|million|billion'
number = r'[0-9]+(,[0-9]{3})*\.*[0-9]*'

word_re = rf'\${number}(-|\sto\s)?({number})?\s({amount})'
value_re = rf'\${number}'

'''
TODO

Given either a string or a list of strings as input, return
a number (int or float) which is equal to the monetary value

money_conversion("$12.2 million") --> 12200000 ## Word Syntax
money_conversion("$790,000") --> 790000		   ## Value Syntax

use test_money_conversion.py to test your solution
'''
def word_to_value(word):
    value_dict = {"thousand": 10**3, "million":10**6, "billion":10**9}
    return value_dict[word]

def parse_value_syntax(string):
    value_str = re.search(number, string).group()
    value = float(value_str.replace(",", ""))
    return value

def parse_word_syntax(string):
    value = parse_value_syntax(string)
    word = re.search(amount, string, flags=re.I).group()
    word_value = word_to_value(word)
    return value * word_value

def money_conversion(money):

    if isinstance(money, list):
        money = money[0]

    word_syntax = re.search(word_re, money)
    value_syntax = re.search(value_re, money)

    if word_syntax:
        return parse_word_syntax(word_syntax.group())

    elif value_syntax:
        return parse_value_syntax(value_syntax.group())



#print(re.search(number, "70,345,125.123").group())


## --- TESTING ---
print( money_conversion("$12.2 million") == 12200000 )
#
print( money_conversion("$790,000") == 790000 )
#
print( money_conversion("$3 million") == 3000000 )

print( money_conversion("$99 million") == 99000000 )

print(money_conversion("$3.5 million") == 3500000)

print(money_conversion("$1.234 million") == 1234000)

print(money_conversion("$1.25 billion") == 1250000000)

print(money_conversion("$900.9 thousand") == 900900)

#print( money_conversion("$3.5 to 4 million") == 3500000)

print(money_conversion("$950000") == 950000)

print(money_conversion("$127,850,000") == 127850000)

print(money_conversion("$10,000,000.50") == 10000000.5)

# print(money_conversion("70 crore") is None)

# print(money_conversion("$3.5-4 million") == 3500000 )

# print(money_conversion("estimated $5,000,000 (USD)") == 5000000)
#
# print(money_conversion("60 million Norwegian Kroner "
# 					   "(around $8.7 million in 1989)") == 8700000 )
#
# print(money_conversion(['$410.6 million (gross)',
# 	'$378.5 million (net)']) == 410600000)



## --- My Trail ---
"""
def money_conversion(money):
    if isinstance(money, list):
        return float(money[0].split()[0][1:]) * (10 ** 6)
    else:
        money = money.split()
        try:
            #print(money[0][1:], ":", money[-1])
            if len(money) == 1:
                return float("".join(money[0][1:].split(",")))
            else:
                if money[-1] == "thousand":
                    return round(float(money[0][1:]) * (10 ** 3))
                elif money[-1] == "million":
                    return round(float(money[0][1:]) * (10 ** 6))
                elif money[-1] == "billion":
                    return round(float(money[0][1:]) * (10 ** 9))
                elif money[-1] not in ["thousand", "million", "billion", "crore"] :
                    if money[0] == "estimated":
                        return float("".join(money[1][1:].split(",")))
                    else:
                        return round(float(money[5][1:]) * (10 ** 6))
                elif money[-1] == "crore":
                    return None

        except Exception as ex:
            print(ex)
            return float(money[0][1:].split("-")[0]) * (10 ** 6)

"""

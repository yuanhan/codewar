# Convert string to camel case
# 5kyu
# https://www.codewars.com/kata/convert-string-to-camel-case/python

'''
Description:

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

Examples:

# returns "theStealthWarrior"
to_camel_case("the-stealth-warrior")

# returns "TheStealthWarrior"
to_camel_case("The_Stealth_Warrior")
'''


def to_camel_case(text):
    if text == '':
        return ''
    else:
        camel_case = text[0]
        for i in range(1, len(text)):
            if text[i] == '-' or text[i] == '_':
                pass
            elif text[i - 1] == '-' or text[i - 1] == '_':
                camel_case += text[i].upper()
            else:
                camel_case += text[i]
    return camel_case


def to_camel_case(text):
    return text[0] + ''.join([w[0].upper() + w[1:]
                              for w in text.replace("_", "-").split("-")])[1:] if text else ''


def to_camel_case(text):
    return text[0] + ''.join([w[0].upper() + w[1:]
                              for w in text.replace("_", "-").split("-")])[1:] if text else ''

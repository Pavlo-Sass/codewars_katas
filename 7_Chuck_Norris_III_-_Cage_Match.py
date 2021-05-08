# It's Friday night, and Chuck is bored. He's already run 1,000 miles, stopping only to eat a family sized bag of
# Heatwave Doritos and a large fistful of M&Ms. He just can't stop thinking about kicking something!
#
# There is only one thing for it, Chuck heads down to his local MMA gym and immediately challenges every fighter
# there to get in the cage and try and take him down... AT THE SAME TIME!
#
# You are provided an array of strings that represent the cage and Chuck's opponents. Your task, in traditional Chuck
# style, is to take their heads off!! Throw punches, kicks, headbutts (or more likely - regex or iteration...) but
# whatever you do, remove their heads. Return the same array of strings, but with the heads ('O') removed and
# replaced with a space (' ').
#
# If the provided array is empty, or is an empty string, return 'Gym is empty'. If you are given an array of numbers,
# return 'This isn't the gym!!'.
import re

def head_smash(arr):

    if isinstance(arr, int):
        return 'This isn\'t the gym!!'
    if len(arr) < 1:
        return 'Gym is empty'
    for i in range(len(arr)):
        arr[i] = re.sub(r'O', ' ', arr[i])
    return arr


a = head_smash(
        [
            '***  _O_   **   _O_   **   _O_   **   _O_  ***',
            '*** /(.)J  **  /(.)J  **  C(.)J  **  C(.)J ***',
            '*** _| |_  **  _| |_  **  _| |_  **  _( )_ **'])

print(a)
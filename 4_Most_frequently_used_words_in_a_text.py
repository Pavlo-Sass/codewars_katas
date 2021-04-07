# Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the
# top-3 most occurring words, in descending order of the number of occurrences.
#
# Assumptions:
# A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII. (No need to handle
# fancy punctuation.)
# Matches should be case-insensitive, and the words in the result should be lowercased.
# Ties may be broken arbitrarily.
# If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an
# empty array if a text contains no words.
# Examples:
# top_3_words("In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income.")
# # => ["a", "of", "on"]
#
# top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# # => ["e", "ddd", "aa"]
#
# top_3_words("  //wont won't won't")
# # => ["won't", "wont"]

import re


def top_3_words(text):
    dictionary = {}
    # checking if not letter char in word
    text = re.sub(r'[^a-zA-Z0-9\']', ' ', text)
    for word in text.lower().split():
        if not word.isalpha():
            # checking if remained letter in word
            if word == re.sub(r'[^\']', '', word):
                continue
        # add keyword to dictionary
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    # sorting dictionary by values
    dict_items = list(dictionary.items())
    dict_items.sort(key=lambda i: i[1], reverse=True)
    # preparing the answer
    answer = []
    # calculating len of answer
    if len(dict_items) < 3:
        limit = len(dict_items)
    else:
        limit = 3
    # forming answer
    for i in range(limit):
        answer.append(dict_items[i][0])
    return answer


text = """won't In_a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""
text2 = "  //wont won't won't"
text3 = "  '''  "
text4 = "'wW.evIYu:;.:LMaM'NQ.!:-:WE'm' _?:WE'm'-LMaM'NQ:/,evIYu-evIYu ?vEp'nJYh?;," \
        "Vvun-!-jfjolPPaoA-/:!evIYu/:vdJBzxLY,:! evIYu/ -,:evIYu!/ ;LMaM'NQ.!  Vvun;;?;?evIYu ;FqseQ./ Vvun; . " \
        "vEp'nJYh,-.?.LMaM'NQ;!: .vdJBzxLY/ vdJBzxLY vEp'nJYh/,.kljriwZhR:_/FqseQ,--," \
        "xYRG.-!vEp'nJYh/??:vdJBzxLY:.!_;xYRG:;Vvun -_ Vvun ;,vdJBzxLY;-evIYu;evIYu__?/xYRG--!FqseQ," \
        ":Vvun:.vdJBzxLY-Vvun-?:;:Vvun/FqseQ!,!Vvun.;-,.vEp'nJYh,vdJBzxLY;!;!vEp'nJYh;__?jfjolPPaoA!," \
        "._.kljriwZhR?vdJBzxLY.,:;!FqseQ- WE'm'?;pKAxCBp_FqseQ-;-vdJBzxLY --evIYu ?,;!xYRG_Vvun?jfjolPPaoA-evIYu," \
        "?:-:WE'm' -/:xYRG -LMaM'NQ:.kljriwZhR,:;;.jfjolPPaoA-?-.kljriwZhR _.??LMaM'NQ?,jfjolPPaoA?," \
        "evIYu//kljriwZhR?xYRG-Vvun,/.?LMaM'NQ;;_/.'wW-/._vdJBzxLY_vEp'nJYh;Vvun;._evIYu/_FqseQ?;! :vdJBzxLY. " \
        "evIYu:!;_jfjolPPaoA!-:; vEp'nJYh_?-,xYRG_?.-!LMaM'NQ!-vdJBzxLY_jfjolPPaoA?!/.LMaM'NQ T'QZOkQiYa/ LMaM'NQ!:," \
        ";LMaM'NQ-//xYRG -. 'wW!--- vdJBzxLY,!-,/evIYu_?WE'm' :kljriwZhR:?;?vEp'nJYh/?_'wW " \
        "??vdJBzxLY_?;;.WE'm'!-/xYRG :,,/pKAxCBp_;vEp'nJYh!/;.vEp'nJYh!_vEp'nJYh_;-/LMaM'NQ:.," \
        "FqseQ/!;'wW/..LMaM'NQ!xYRG __?evIYu.?;?evIYu_vdJBzxLY/;Vvun-;!!:jfjolPPaoA,.!vEp'nJYh_;-evIYu;!," \
        "Vvun  FqseQ:kljriwZhR_ Vvun.vEp'nJYh!;?!vdJBzxLY??-:-vEp'nJYh ;xYRG,.FzZbhW:./:;Vvun/!!;.FqseQ_--,!FqseQ;:;," \
        ":vdJBzxLY vdJBzxLY?;kljriwZhR:!/.,FqseQ;jfjolPPaoA.,vEp'nJYh_- WE'm':-?jfjolPPaoA_LMaM'NQ_:_ " \
        "vEp'nJYh!:::jfjolPPaoA/.,FqseQ_?/evIYu_/,-FqseQ,/. ;jfjolPPaoA,-!," \
        ";WE'm' -xYRG-xYRG__:Vvun:/Vvun!?-:vEp'nJYh!.-.,'wW :-_vEp'nJYh.; .-vdJBzxLY ?_.kljriwZhR/ " \
        "Vvun/-;vdJBzxLY;--:/jfjolPPaoA;-.? xYRG!. ?LMaM'NQ--evIYu?:,/xYRG ,-, evIYu; LMaM'NQ?vEp'nJYh, !," \
        ";FqseQ::;jfjolPPaoA:!vEp'nJYh;:!jfjolPPaoA,::/evIYu-_;!jfjolPPaoA!. evIYu;. vdJBzxLY?,!Vvun--_:-xYRG:_," \
        "_Vvun,_WE'm'_-_WE'm';/ 'wW?,__.FqseQ?vdJBzxLY/Vvun.::,evIYu,FqseQ,,?vdJBzxLY_,:?xYRG;--:xYRG: "

# ['eviyu', 'vdjbzxly', 'vvun']

print(top_3_words(text3))

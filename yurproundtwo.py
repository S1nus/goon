import string
import random
from random import randint
#alpha version of the Goon tweet converter
#accepts a string and returns it as if it were said by OmgChrissIssAHoee
def chriss(s):
    s = string.capwords(s)
    words = s.split();
    sr = list(map(staticReplace,words))
    sr = list(map(endRules,sr))
    sr = list(map(iRules,sr))
    sr = specialCases(sr)
    sr = double(sr)
    print(sr)
    sr = addspaces(sr)
    sr = nonwordedits(sr, partialwords)
    sr = finalize(sr, prefix, suffix)
    return sr
#dictionary of static
partialwords = {
   'th' : 'dh', 'Is' : 'Ihss',  'tt' : 'xt',}


#list of tweet prefixes to be added to the beginning of tweet
prefix = ["'  ", "- ", "-  ", "' "]
#list of tweet suffixes to be added to the end of the tweet
suffix = ["  '_'", '  <3', ' (:', " :'/", '  <|3']

#consults static replacement dictionary and returns word accordingly 
def staticReplace(s):
    return {
        s : s,
        'Fuck': 'Fuxkk',
        'Is': 'Ihss',
        'Fucking': 'Fuhxkking',
        'Yup' : 'YURPP',
        'Back' : 'Baxckk',
        'Man' : 'Men',
        'Guys': 'Men',
        'Dudes' : 'Men',
        'Me' : 'Mhe',
        'Wtf' : probableSwitch('WTF','WTFF',0.5),
        
    }[s]
#takes all words that begin with I and uncapitalizes I and capitalizes the next
#character within that string, still gotta do the I Am -> iAm 
def iRules(s):
    if s[0] == 'I' and len(s) > 1:
        return 'i' + s[1].capitalize() + s[2:]
    else: return s
    
#if string s ends with a g probabilistically replace with q or qq
#might overload probableSwitch so it can take like up to 4 elements somehow
def endRules(s):
    if s[-1] == 'g':
       return s[:-1] + probableSwitch('q','qq',0.4)
    if s[-1] == 'k' and s[-2] == 'c':
        return s[:-2] + probableSwitch('xk','xxck',0.5)
    if s[-1] == '!':
        return s[:-1] + probableSwitch(' ! ','! \'',0.66)
    else: return s


#picks an object using a specified probability as a double between 0 and 1
def probableSwitch(item, candidate, probability):
    rand = random.random()
    if rand < probability:
        return candidate
    else: return item

#looks through the list of words and combines and decapitalizes I + next word/What's Up 
def specialCases(s):
    counter = 0 
    while counter < len(s):
        if s[counter] == 'I':
            s[counter] = 'i' + s[counter + 1]
            s.remove(s[counter+1])
            counter = counter + 1
        else:
            if s[counter] == "What's" and s[counter + 1]  == 'Up':
                s[counter] = 'WhatsUpp'
                s.remove(s[counter + 1])
                counter = counter + 1
            counter = counter + 1 
    return s

#each word has a 5% chance to have two characters added to end and 5% to have 3
def double(s):
    counter = 0
    while counter < len(s):
        if randint(1,20) == 4:
            s[counter] = s[counter] + s[counter][-1] + s[counter][-1]
            counter = counter + 1
        else:
            if randint(1,20) == 5:
                s[counter] = s[counter] + s[counter][-1]
                counter = counter + 1
            else:
                counter = counter + 1
    return s

#converts list to String and adds spaces
def addspaces(s):
    newstring = ''
    for x in s:
        newstring = newstring + ' ' + x
    return newstring[1:]

#searches through string and replaces partial word changes
def nonwordedits(s, dict):
    for x in partialwords:
        s = s.replace(x, dict[x])
    return s

#adds prefix and suffix to string
def finalize(s, pre, suf):
    return pre[randint(0, len(pre)-1)] + s + suf[randint(0, len(suf)-1)]




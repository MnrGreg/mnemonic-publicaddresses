#!/usr/bin/env python3
"""
# Exploring possibilities to derive mnemonic phrases from public addresses
# Bitcoin bip-0039 wordlist * 10 colors * 900 adjectives = wordlist of 17mil = 7x color/adjective/noun combinations 
#
# dictionaries:
#   https://github.com/bitcoin/bips/raw/master/bip-0039/english.txt
#   https://gist.github.com/Xeoncross/5381806b18de1f395187
#   https://github.com/dolph/dictionary 
#   https://github.com/taikuukaits/SimpleWordlists/raw/master/Wordlist-Nouns-Common-Audited-Len-3-6.txt
#   https://github.com/taikuukaits/SimpleWordlists/blob/master/Wordlist-Adjectives-All.txt
#
# references:
# https://github.com/Cygnusfear/bijective-mnemonics/blob/master/index.md
# https://www.royalfork.org/2017/12/10/eth-graphical-address/
# https://iancoleman.io/bip39/
#
# 40bit public address combinations = 16^40
# 16^2 = 2048 = 15 words
# 16^3 = 4096 = 14 words
# 16^4 = 65536 = 10 words
# 16^5 = 1048576 = 9 words
# 16^6 = 16777216 = 7 words
# 16^7 = 268435456 = 6 words
"""

publicaddress = "0xbE5C59873f34580c0a28dAbD8396482d72F5F330"
base_size = 16777216
hex_symbols = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" ]

#colors = [ "blue","red","yellow","orange","green","purple","pink","black","white" ]
colors = [ "\033[1;34;40m", "\033[1;31;40m", "\033[1;93;40m", "\033[1;33;40m", "\033[1;92;40m", "\033[1;35;40m", "\033[1;95;40m", "\033[1;90;40m", "\033[1;97;40m" ]

wordlist = []
with open('english.txt') as f:
    wordlist = f.read().splitlines()

adjectives = []
with open('Positive-Adjective-List.txt') as f:
    adjectives = f.read().splitlines()

words = []
for word in wordlist:
    for adjective in adjectives:
        for color in colors:
            words.append(color+adjective+"."+word+"\033[0;0m")

word_idx = {}
count = 0
for word in words:
    word_idx[word] = count
    count += 1

def hex_str_to_int(hex_str):
    result = 0
    hex_str = hex_str[2:len(hex_str)]
    hex_str = hex_str[::-1]
    idx = 0
    for i in hex_str:
        value = ((16 ** idx) * int(i, 16))
        #print(str(value))
        result += value
        idx = idx + 1
    return result

def get_different_base_indices(x, base):
    digits = []
    while (x > 0):
        digits.append(x % base)
        x = x // base
    return list(reversed(digits))

def publicaddress_to_mnemonic(publicaddress):
    if publicaddress[0:2] != "0x":
        print ('invalid public address')
        exit
    else:
        number = hex_str_to_int(publicaddress)
        #print("hex to int number:", number)
        indices = get_different_base_indices(number, base_size)
        result = []
        #print("indices:", indices)
        for index in indices:
            result.append(words[index])
        return result

def mnemonic_to_publicaddress(mnemonic_str):
    words_ = mnemonic_str.split()
    words_ = list(reversed(words_))
    number = 0
    count = 0
    for word in words_:
        number += (base_size ** count) * word_idx[word]
        count += 1
    hex_indices = get_different_base_indices(number, 16);
    result = "0x"
    for idx in hex_indices:
        result = result + hex_symbols[idx]
    return result

if __name__ == '__main__':
    print("\nword list size:", str(len(words)))
    print("public address:", publicaddress)
    mnemonic = publicaddress_to_mnemonic(publicaddress)
    print("\nmnemonic phrase from public address:\n","\n".join(map(str, mnemonic)))
    print("\npublic address from mnemonic phrase:", mnemonic_to_publicaddress(" ".join(map(str, mnemonic))))
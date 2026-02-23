import re
num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
             11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
             15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
             19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
             50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
             90: 'Ninety', 0: 'Zero'}




def cleaning_fun(text):
    text = text.replace("\n", " ")
    new_text = ""
                

#are these needed ,
    symbols = "@#$^&*()[]{}<>~+=|/"
    punctuations = ".,;:!?\"'"
    clean=""
    for t in text:
        if t.isalpha() or t==" ":
            clean+=t
        elif t in symbols:
            continue
        elif t.isalnum():
            clean+=t
    #here is we encounter a punctuaion we replace it with a space 
        elif t in punctuations :
            clean += " "
        else :
            continue
    clean= " ".join(clean.split())
    for c in clean:
        #if condition to check if the chrcter is not lowercase 
        if 'A' <= c <= 'Z':    
            #change the text from uppercase to lowercase     
            new_text += chr(ord(c) + 32)  
        else:
            new_text += c
    return new_text


def remove_percent(text):
# Pattern:the pattenr is strictly nothing or space, then number, then "%" and ,then strictly nothing or space

    pattern =r'(?<!%)\b\d+%(?=\s|$)'

    valids = re.findall(pattern, text)
    print(valids)
    clean_words = []
#split the text into words to iterate based on words 
    for word in text.split():
        if '%' in word:
        #we keep the word if is matched and adds it to the clean version
            if re.match(pattern,word):
                clean_words.append(word)
        #if it doesnt match then replave the symbol with nothing and then append 
            else:
                word=word.replace('%','')
                clean_words.append(word)
            
    #incase the word does have % symbols we add it anyways 
        else:
            clean_words.append(word)
    mergedText=' '.join(clean_words)
    
    return mergedText


def n2w(n):
    try:
        return num2words[n]
    except KeyError:
        try:
            return num2words[n - n % 10] + " " + num2words[n % 10].lower()
        except KeyError:
            print('Number out of range')
#function to change number into letters
def fun( text):
    i=0
    final_resul=""
    while i < len(text):
        #in there is a number found 
        if text[i].isdigit():
            number=""
        #if its found we add to the number
            while i < len(text) and text[i].isdigit() :
        
            
                number+=text[i]
            
                i+=1
            #call the fun n2w (number to word)  and then add it to the finl resultt
            if number:
                value = n2w(int(number))
                
        
                final_resul += value
        #if its not a number just add it as it is to the final result
        else:
            final_resul+=text[i]
            i+=1
    final_resul=final_resul.lower()
    return final_resul
def decontracted(phrase):
    # specific contracted
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can't", "can not", phrase)

    # general contrac
    phrase = re.sub(r"n't", " not", phrase)
    phrase = re.sub(r"'re", " are", phrase)
    phrase = re.sub(r"'s", " is", phrase)
    phrase = re.sub(r"'d", " would", phrase)
    phrase = re.sub(r"'ll", " will", phrase)
    phrase = re.sub(r"'t", " not", phrase)
    phrase = re.sub(r"'ve", " have", phrase)
    phrase = re.sub(r"'m", " am", phrase)
    return phrase
def normalise_text(text):
    text=cleaning_fun(text)
    text=remove_percent(text)
    text=fun(text)
    text=decontracted(text)
    return text
    
text1="Today she Cooked 40% bou%rek. Later, she addedd two chamiyya, no pizza, and one tea   " 
text2="Five pizza were ready, but 3 bourak burned!"
text3="We only had 8 chamiyya, no pizza, and one tea"
text4="is 6 too much? i ate nine bourak lol"

print(normalise_text(text1))
print(normalise_text(text2))
print(normalise_text(text3))
print(normalise_text(text4))
     

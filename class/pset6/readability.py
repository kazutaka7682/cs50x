import cs50

def count_letters(text):
    counter1 = 0
    for i in range(len(text)):
        if text[i] >= "a" and text[i] <= "z":
            counter1 += 1
        elif text[i] >= "A" and text[i] <= "Z":
            counter1 += 1
    return counter1

def count_words(text):
    counter2 = 1
    for i in range(len(text)):
        if text[i] == " ":
            counter2 += 1
    return counter2

def count_sentences(text):
    counter3 = 0
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == "!":
            counter3 += 1
    return counter3
        
text = cs50.get_string("Text: ")

#print(count_letters(text))
#print(count_words(text))
#print(count_sentences(text))
L = (count_letters(text) * 100.0) / count_words(text)
#print(L)
S = (count_sentences(text) * 100.0) / count_words(text)
#print(S)
index = 0.0588 * L - 0.296 * S - 15.8
#print(index)
grade = round(index)
#print(grade)

if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")

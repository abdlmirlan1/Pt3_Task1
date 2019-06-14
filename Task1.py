def count(sent):
    sent = sent.split()
    upper = 0
    lower = 0
    total = 0
    for word in sent:
        for letter in word:
            total += 1
            if letter.isupper():
                upper += 1
            elif letter.islower():
                lower += 1
    print("Lower:", int(lower*100/total), "Upper:", int(upper*100/total))

count("Hello My NaMe is makers")


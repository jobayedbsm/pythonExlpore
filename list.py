# Reversing a Sentence (Words Order)
sentence="I love you"
#  first splic the each world
sentence=sentence.split(" ")
sentence.reverse()

sentence=" ".join(sentence)
print(sentence)

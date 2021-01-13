def uncommon(sentence1: str, sentence2: str) -> list[str]:
    set1 = set(sentence1.split(' '))
    set2 = set(sentence2.split(' '))
    uncommon_words = []

    for word in set1:
        if word not in set2:
            uncommon_words.append(word)

    for word in set2:
      if word not in set1:
          uncommon_words.append(word)  

    return uncommon_words

    

assert uncommon(sentence1 = "the quick", sentence2 = "brown fox") == ["the", "quick", "brown", "fox"]
assert uncommon(sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire") == ["beat", "to", "lost"]
assert uncommon(sentence1 = "copper coffee pot", sentence2 = "hot coffee pot") == ["copper", "hot"]
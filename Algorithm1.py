import spacy
nlp = spacy.load('en')
Sentences = ["The students are upstairs.", "The students are diligent.", "The students are scholars."]
Dictionary={}
sentence_Counter = 0
test = 1
for sentence in Sentences:
  sentence_Counter = sentence_Counter+1 
  doc = nlp(sentence)
  checking = 0
  for token in doc:
    print(token.text, token.pos_, token.dep_)
    try:
      if token.dep_ not in Dictionary[token.pos_]:
        Dictionary[token.pos_].append(token.dep_)
      check = Dictionary.get(token.pos_)
      check[0] = check[0] + 1
    except KeyError as error:   
        checking = checking + 1
        Dictionary[token.pos_]=[test]
        Dictionary[token.pos_].append(token.dep_)
        check = Dictionary.get(token.pos_)

print("There were",sentence_Counter, "sentences.")
print("Here is the breakdown: ")
print(Dictionary)


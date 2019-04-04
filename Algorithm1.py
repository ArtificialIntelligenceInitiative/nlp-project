import spacy
import wikipedia
G =wikipedia.summary("Facebook")
Sentences = []
reshaping = []
increment = 0
for word in G.split("."):
   Sentences.append(word)
 #print(Sentences)
print(Sentences)
nlp = spacy.load('en')

doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
Dictionary={}
sentence_Counter = 0
Sentences=["the cat caught a mouse"]
test = 1
for sentence in Sentences:
  sentence_Counter = sentence_Counter+1 
  doc = nlp(sentence)
  checking = 0
  for token in doc:
   # print(token.text, token.pos_, token.dep_)
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


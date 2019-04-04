import spacy
nlp = spacy.load('en')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
Dictionary={}
T_F = True
for token in doc:
  print(token.text, token.pos_, token.dep_)
  try:
    if token.dep_ not in Dictionary[token.pos_]:
      Dictionary[token.pos_].append(token.dep_)
  except KeyError as error:
      Dictionary[token.pos_]=[token.dep_]
    
print(Dictionary)

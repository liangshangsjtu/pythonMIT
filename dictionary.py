
# FIND THE WORDS THE OCCUR MOST IN A SONG LYRICS
def lyrics_to_frequencies(lyrics):
  myDict={}
  for word in lyrics:
    if word in myDict:
      myDict[word]+=1
    else:
      myDict[word]=1
  return myDict
#SO myDict IS THE freqs DICTIONARY
def most_common_words(freqs):
  values = freqs.values()
  best=max(values)
  word=[]
  for k in freqs:
    if freqs[k]==best:
      words.append(k)
  return (words, best)

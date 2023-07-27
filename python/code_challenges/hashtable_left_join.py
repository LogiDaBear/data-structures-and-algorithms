from data_structures.hashtable import Hashtable

def left_join(synonyms, antonyms):

  results = []
  for word in synonyms.keys():
    syn = synonyms.get(word)
    ant = antonyms.get(word)
    if syn is not None and ant is not None:
      row = [word, syn, ant]
      results.append(row)

  return results
  """
  Performs a left join on two hashmaps.

  Args:
    synonyms: A hashmap that has word strings as keys, and a synonym of the key as values.
    antonyms: A hashmap that has word strings as keys, and an antonym of the key as values.

  Returns:
    A new data structure that contains the results of the left join.
  """
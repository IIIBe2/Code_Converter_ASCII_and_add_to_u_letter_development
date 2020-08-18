import eel 
import random

eel.init('web', allowed_extensions=['.js', '.html'])

def QuantityMod(Quantity, choices_simv):
  Temp = ""
  for x in range(Quantity):
    Temp += "&#" + str(choices_simv[int(random.random() * len(choices_simv))]) + ";"
    print(Quantity)
    print(Temp)
  return Temp


@eel.expose
def get_recode(recoding_text, strf, Quantity):
  choices_simv = list(range(768, 880))
  res = ""
  kl = 0
  Teemp = []
  Text = str(recoding_text)
  Teemp = list(map(int, strf.split()))
  try:
    for q in Teemp:
      choices_simv.remove(q)
  except Exception: jk = 3
   
  for i in Text:
    if i != ' ':
      res+= i + QuantityMod(int(Quantity), choices_simv)
    else:
      if i == ' ':
        res+= i

  return res



eel.start("main.html", size= (700, 1013))
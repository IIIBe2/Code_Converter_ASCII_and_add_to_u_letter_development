import eel 
import random

eel.init('web', allowed_extensions=['.js', '.html'])


@eel.expose
def get_recode(recoding_text, strf):
  choices_simv = list(range(768, 879))
  res = ""
  kl = 0
  Teemp = []
  Text = str(recoding_text)
  Teemp = list(map(int, strf.split()))
  try:
    for q in Teemp:
      print(choices_simv)
      print(Teemp)
      choices_simv.remove(q)
  except Exception: jk = 3
   
  for i in Text:
    if i != ' ':
      res+= i + "&#" + str(choices_simv[int(random.random() * len(choices_simv))]) + ";"
      
  return res


eel.start("main.html", size= (700, 937))
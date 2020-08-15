import eel 
import random

@eel.expose
def get_recode(recoding_text):
  res = ""
  Text = str(recoding_text)
 

  for i in Text:
    if i != ' ':
      res+= i + "&#" + str(random.randint(768, 879)) + ";"
      

  return res

eel.init("web")
eel.start("main.html", size= (700, 700))
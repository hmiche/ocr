import Functions
import time
import tesseract
  


text= tesseract.ocrtext('RC.jpg')
depart=time.time()



Functions.extractnom(text)
Functions.Capital(text)
Functions.date(text)
Functions.form(text)
Functions.extractActivité(text)
Functions.siege(text)


print()
print()
print("temps dexecution est :"+str(time.time()-depart))

  
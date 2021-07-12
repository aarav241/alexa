import datetime
import winsound

def alarm(Timing):
      altime = str(datetime.datetime.now().strptime(Timing,'%I:%M %p'))
      
      altime = altime[11:-3]
      print(altime)
      Horeal = altime[:2]
      Horeal= int(Horeal)
      Minreal =altime[3:5]
      Minreal = int(Minreal)
      print(f"alarm is set for {Timing}")
      
      while True:
          if Horeal==datetime.datetime.now().hour:
              if Minreal==datetime.datetime.now().minute:
                  print("alarm is running")
                  
                  winsound.PlaySound('abc',winsound.SND_LOOP)
                  
              elif Minreal<datetime.datetime.now().minute:
                  break
              
              
if __name__ == "__main__":
    alarm("1:42 PM")
    
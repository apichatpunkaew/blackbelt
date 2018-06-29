import json

def SetLab():
    Sessions_Attended = {"sessions" : "1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499"}
    StrSessions_Attended = Sessions_Attended["sessions"]
    ##print(StrSessions_Attended)   
    TempSesion = StrSessions_Attended.split(",")
    return TempSesion

def Readfile():
    file = open("Attended.json", "r") 
    data = json.load(file)
    StrInputSession = data["sessions"]
    TempInputSession = StrInputSession.split(",")
    ##print(TempInputSession)
    return TempInputSession
    
if __name__ == '__main__':
   AllSession = SetLab()
   AttendSession = Readfile()
   numberSession = len(set(AllSession) & set(AttendSession))
   print ("I have attended " +str(numberSession)+ " sessions!!")
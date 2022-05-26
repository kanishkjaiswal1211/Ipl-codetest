class Performance:
    def __init__(self,Name,Points,PastResults):
        self.Name=Name
        self.Points=Points
        self.PastResults=PastResults
    def loss(self):
        LossCount = 0
        WinCount=0
        SuccessiveLostCount = 1
        for i in range(len(self.PastResults)):
            if self.PastResults[i] == 0:
                LossCount+=1
              
            else :
                LossCount=0
                WinCount+=1
                
            if LossCount>=2:
                SuccessiveLostCount+=1
        
        if SuccessiveLostCount > 1:
            print("Team Name: ",self.Name)
            print("Total Points:" , self.Points)
            print("total sucessive lost count : " , SuccessiveLostCount)   
               




Gt_last=[1,1,0,0,1]
Gt=Performance("GT",20,Gt_last)
Gt.loss()

Lsg_last=[1,0,0,1,1]
Lsg=Performance("LSG",18,Lsg_last)
Lsg.loss()

Rr_last=[1,0,1,0,0]
Rr=Performance("RR",16,Rr_last)
Rr.loss()

Rcb_last=[0,1,1,0,0]
Rcb=Performance("Rcb",14,Rcb_last)
Rcb.loss()

Dc_last=[1,1,0,1,0]
Dc=Performance("DC",14,Dc_last)
Dc.loss()

Kkr_last=[0,1,1,0,1]
Kkr=Performance("KKR",12,Kkr_last)
Kkr.loss()

Mi_last=[0,1,0,1,1]
Mi=Performance("MI",6,Mi_last)
Mi.loss()

Pbks_last=[0,1,0,1,0]
Pbks=Performance("PBKS",12,Pbks_last)
Pbks.loss()

Csk_last=[0,0,1,0,1]
Csk=Performance("CSK",8,Csk_last)
Csk.loss()

Srh_last=[1,0,0,0,0]
Srh=Performance("SRH",12,Srh_last)
Srh.loss()
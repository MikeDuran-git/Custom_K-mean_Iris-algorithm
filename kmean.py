"""
@author: MIKE DURAN
"""
import math
import numpy as np
import pandas as pd
import matplotlib as plt
import random as rand
#hyperparametre : K=3 on se simplifie la tache 
K=3
root = "./"
iris_dataframe = pd.read_csv(root+"iris.csv")

class Point:
    def __init__(self,sl,sw,pl,pw):
        self.SL=sl
        self.SW=sw
        self.PL=pl
        self.PW=pw
    def distance(self,P):
        return math.sqrt(((P.SL -self.SL)**2)+((P.SW -self.SW)**2) +((P.PL-self.PL)**2) +((P.PW -self.PW)**2))            
    def add(self,P):
        self.SL+=P.SL
        self.SW+=P.SW
        self.PL+=P.PL
        self.PW+=P.PW


#ETAPE 1 : selection random des centres k centres
def initialisation_des_clusters(df):
    samples= df.sample(K)
    s1_1=samples['sepal_length'].iloc[0]
    s1_2=samples['sepal_width'].iloc[0]
    s1_3=samples['petal_length'].iloc[0]
    s1_4=samples['petal_width'].iloc[0]
    C1=[Point(s1_1,s1_2,s1_3,s1_4)]
    s1_1=samples['sepal_length'].iloc[1]
    s1_2=samples['sepal_width'].iloc[1]
    s1_3=samples['petal_length'].iloc[1]
    s1_4=samples['petal_width'].iloc[1]
    C2=[Point(s1_1,s1_2,s1_3,s1_4)]
    s1_1=samples['sepal_length'].iloc[2]
    s1_2=samples['sepal_width'].iloc[2]
    s1_3=samples['petal_length'].iloc[2]
    s1_4=samples['petal_width'].iloc[2]
    C3=[Point(s1_1,s1_2,s1_3,s1_4)]  
    return [(C1,samples.index[0]), (C2,samples.index[1]), (C3,samples.index[2])]

def MinDistance(distance1,distance2,distance3):
    return min(distance1,min(distance2,distance3))

def insignation_instance_aux_partitions(First_centers,df):
    C1=First_centers[0][0]
    P1=C1[0]
    index1=First_centers[0][1]
    Group1 = []
    Group1.append(P1)
    C2=First_centers[1][0]
    P2=C2[0]
    index2=First_centers[1][1]
    Group2 = []
    Group2.append(P2)
    C3=First_centers[2][0]
    P3=C3[0]
    index3=First_centers[2][1]
    Group3=[]
    Group3.append(P3)
    for index in range(0,len(df)-1):
        if index!=index1 and index!=index2 and index!=index3:
            P=Point(df.iloc[index][0] ,df.iloc[index][1] ,df.iloc[index][2] ,df.iloc[index][3] )
            #initialisation de la distance des trois points par rapport aux C.
            distance1=P1.distance(P)
            distance2=P2.distance(P)
            distance3=P3.distance(P)
            #Determination de la plus courte distance
            if distance1==MinDistance(distance1,distance2,distance3):           
                Group1.append(P)
            elif distance2==MinDistance(distance1,distance2,distance3):  
                Group2.append(P)
            elif distance3==MinDistance(distance1,distance2,distance3):  
                Group3.append(P)
    return [Group1,Group2,Group3]

def phase_2(Centers,df):
    P1=Centers[0]
    P2=Centers[1]
    P3=Centers[2]
    Group1 = []
    Group2 = []
    Group3 = []
    for index in range(0,len(df)-1):
        P=Point(df.iloc[index][0] ,df.iloc[index][1] ,df.iloc[index][2] ,df.iloc[index][3] )
        #initialisation de la distance des trois points par rapport aux C.
        distance1=P1.distance(P)
        distance2=P2.distance(P)
        distance3=P3.distance(P)
            #Determination de la plus courte distance
        if distance1==MinDistance(distance1,distance2,distance3):           
            Group1.append(P)
        elif distance2==MinDistance(distance1,distance2,distance3):  
            Group2.append(P)
        elif distance3==MinDistance(distance1,distance2,distance3):  
            Group3.append(P)
    return [Group1,Group2,Group3]

def mise_a_jour_des_centres_de_partitions(Groups):
    
    newGroup= []
    for group in Groups:
        Moyenne = Point(0,0,0,0) 
        for p in group:
            Moyenne.add(p)
        nbrval=len(group)
        Moyenne=Point(Moyenne.SL/nbrval,Moyenne.SW/nbrval,Moyenne.PL/nbrval,Moyenne.PW/nbrval)
        newGroup.append(Moyenne)
    return newGroup

def begin():
    First_centers= initialisation_des_clusters(iris_dataframe)
    Groups=insignation_instance_aux_partitions(First_centers,iris_dataframe)
    print("Group1 = "+ str(len(Groups[0])) )
    print("Group2 = "+ str(len(Groups[1])) )
    print("Group3 = "+ str(len(Groups[2])) )
    i=0
    while i <500:
        i+=1
        print(i)
        New_centers=mise_a_jour_des_centres_de_partitions(Groups)
        Groups=phase_2(New_centers,iris_dataframe)
    print("Group1 = "+ str(len(Groups[0])) )
    print("Group2 = "+ str(len(Groups[1])) )
    print("Group3 = "+ str(len(Groups[2])) )
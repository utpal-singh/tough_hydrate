#! /usr/bin/python    

from os import system

tstep=1.0
tchop = 10
timetab=[]
temptab=[]
presstab=[]
for l in open('100_timestep.txt','r'):
    if not l.strip():
        continue
    words = l.split()
    timetab.append(float(words[0]))
    temptab.append(float(words[1]))
    presstab.append(float(words[2]))
    


for t in range(0,len(timetab)):
    output_incon = "INCON_%d" %(t)
    output_tchange = "tchange_%d" %(t)
    pressure = presstab[t]

    top=0
    incon = []
    for l in open('SAVE','r'):
        if not l.strip():
            continue
        words = l.split()
        if top == 1:
            new = ' %9.13E %s %s %s\n' %(pressure,words[1],words[2],words[3])
            incon.append(new)
            top=0
        else:
            #print words[0]
            if words[0] == "A0000":
                top=1
            if words[0] == "size_of_last_tstep":
                tstep = float(words[2])
            incon.append(l)        
   

    #output new INCON file
    fout1 = open(output_incon,'w')
    for i in range(0,len(incon)):   
        fout1.write("%s"%(incon[i]))
    fout1.write("\n")
    fout1.close()



    n = '%03d' %t
    
    print ("copy "+output_incon+" INCON")
    system("cp "+output_incon+" INCON")
    print ("copy "+output_tchange+" tchange")
    system("cp "+output_tchange+" tchange")
    print ("TH.win64<tchange_P>tchange_P.out")
    system("./TH.lin64.exe<tchange_P>tchange_P.out")
    # print ("grep CONVERGENCE tchange_P.out")
    # system("grep CONVERGENCE tchange_P.out")
    print ("copy tchange_P.out tchange_P_"+n+".out")
    system("cp tchange_P.out tchange_P_"+n+".out")
    print ("copy SAVE SAVE_P_"+n)
    system("cp SAVE SAVE_P_"+n)
    

##    output_connx = 'Plot_Data_Conx_%d' %(t)
##    system("copy Plot_Data_Conx "+output_connx)
##
##    output_elem = 'Plot_Data_Elem_%d' %(t)
##    system("copy Plot_Data_Elem "+output_elem)
##    #print "cat connections
##
##    output_connx = 'Conx_Time_Series_%d' %(t)
##    system("copy Conx_Time_Series "+output_connx)
##
##system("cat Plot_Data_Elem_0 Plot_Data_Elem_1 > Elem_Data")
##system("cat Plot_Data_Conx_0 Plot_Data_Conx_1 > Conx_Data")
##system("cat Conx_Time_Series_0 Conx_Time_Series_1 > Time_Series")
##
##for p in range(0,len(presstab)):
##    nt = "%d" %t
##    system("cat Plot_Data_Elem_"+nt+" >> Elem_Data")
##    system("cat Plot_Data_Conx_"+nt+" >> Conx_Data")
##    system("cat Conx_Time_Series_"+nt+" >> Time_Series")
##
##
####for  t in range(0,len(timetab)):
    output_incon_T = "INCON_%d" %(t)
    output_tchange_T = "tchange_%d" %(t)

    temperature = temptab[t] 
    starttime = timetab[t]*365*24*60*60
    
    if len(timetab) > t+1:
        endtime = timetab[t+1]*365*24*60*60
    else:
        endtime = 10*365*24*60*60

    top=0
    incon = []
    for l in open('SAVE','r'):
        if not l.strip():
            continue
        words = l.split()
        if top == 1:
            new = ' %s %s %s %9.13E\n' %(words[0],words[1],words[2],temperature)
            incon.append(new)
            top=0
        else:
            #print words[0]
            if words[0] == "A0000":
                top=1
            if words[0] == "size_of_last_tstep":
                tstep = float(words[2])
            incon.append(l)        


 #output new INCON file
    fout1 = open(output_incon_T,'w')
    for i in range(0,len(incon)):   
        fout1.write("%s"%(incon[i]))
    fout1.write("\n")
    fout1.close()



    #change end time of simulation
    top=0
    tchange = []
    for l in open('tchange_T','r', encoding='utf-8'):
        if not l.strip():
            tchange.append(("\n"))
            continue     
        if top == 2:
            words = l.split()
            new = ' %9.3E %9.3E %9.3E %9.3E          %9.3E %9.3E\n' %(starttime,endtime,tstep,float(words[3]),float(words[4]),tchop)
            tchange.append(new)
            top=0
        else:
            #print words[0]
            if top == 1:
                top = 2        
            if l[0:5] == "PARAM":
                top=1       
            tchange.append(l)        
    
  
    #output new tchange file
    fout2 = open(output_tchange_T,'w')
    for i in range(0,len(tchange)):   
        fout2.write("%s"%(tchange[i]))
    fout2.close()

    n = '%03d' %t

    print ("copy "+output_incon_T+" INCON")
    system("cp "+output_incon_T+" INCON")
    print ("copy "+output_tchange_T+" tchange")
    system("cp "+output_tchange_T+" tchange")
    print ("TH.win64<tchange_T>tchange_T.out")
    system("./TH.lin64.exe<tchange_T>tchange_T.out")
    # print ("grep CONVERGENCE tchange_T.out")
    # system("grep CONVERGENCE tchange_T.out")
    print ("copy tchange_T.out tchange_T_"+n+".out")
    system("cp tchange_T.out tchange_T_"+n+".out")
    print ("copy SAVE SAVE_T"+n)
    system("cp SAVE SAVE_T"+n)

    output_connx = 'Plot_Data_Conx_%d' %(t)
    system("cp Plot_Data_Conx "+output_connx)

    output_elem = 'Plot_Data_Elem_%d' %(t)
    system("cp Plot_Data_Elem "+output_elem)
    #print "cat connections

    output_connx = 'Conx_Time_Series_%d' %(t)
    system("cp Conx_Time_Series "+output_connx)

# system("cat Plot_Data_Elem_0 Plot_Data_Elem_1 > Elem_Data")
# system("cat Plot_Data_Conx_0 Plot_Data_Conx_1 > Conx_Data")
# system("cat Conx_Time_Series_0 Conx_Time_Series_1 > Time_Series")

# for t in range(0,len(timetab)):
#     nt = "%d" %t
#     system("cat Plot_Data_Elem_"+nt+" >> Elem_Data")
#     system("cat Plot_Data_Conx_"+nt+" >> Conx_Data")
#     system("cat Conx_Time_Series_"+nt+" >> Time_Series")

















##
##
##system("rm Conx_Time_Series")
##a=0
##fout3 = open("Conx_Time_Series",'w')
##for l in open('Time_Series','r'):
##    if l.strip()[0].isalpha() and a==1:
##            continue
##    else:
##        a=1
##        fout3.write("%s"%(l))
##fout3.close()
##
####run t_hydrate
##
##print ("mv Elem_Data Plot_Data_Elem")
##system("mv Elem_Data Plot_Data_Elem")
##
##print ("mv Conx_Data Plot_Data_Conx")
##system("mv Conx_Data Plot_Data_Conx")
##
##print ("remove intermediate files")
##system("rm Conx_Time_Series_*")
##system("rm Plot_Data_Conx_*")
##system("rm Plot_Data_Elem_*")
##system("rm tchange_*")
##system("rm INCON_*")
##system("rm SAVE_*")





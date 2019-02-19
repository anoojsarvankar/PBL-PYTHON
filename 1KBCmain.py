import random
import time
resultset=[]
splitlines=[]
num_lines=0
def OpenDB(level):
    global resultset
    global num_lines
    if(level==1):
        file=open('QuestionDB1.txt','r')
        f=file.read()
        temp=f.split('\n')
        num_lines=len(temp)
        file.close()
        for i in temp:
            resultset.append(i.split('='))
    elif(level==2):
        file = open('QuestionDB2.txt', 'r')
        f = file.read()
        temp = f.split('\n')
        num_lines = len(temp)
        file.close()
        for i in temp:
            resultset.append(i.split('='))
    elif(level==3):
        file = open('QuestionDB3.txt', 'r')
        f = file.read()
        temp = f.split('\n')
        num_lines = len(temp)
        file.close()
        for i in temp:
            resultset.append(i.split('='))

repeatcheck = [-1]
def Checkrepeat(temp):
    global repeatcheck
    for i in repeatcheck:
        if(i==temp):
            return(0)
    else:
        repeatcheck=repeatcheck+[temp]
        return(1)
qstnnodb=0
repeated=0
def QstnChooser():
    global repeated
    global qstnnodb
    global num_lines
    temp1=random.randint(0,num_lines-1)
    if(Checkrepeat(temp1)==1):
        repeated = 0
        qstnnodb=temp1
        print(resultset[temp1][0],'\n','1.',resultset[temp1][1],'2.',resultset[temp1][2],'3.',resultset[temp1][3],'4.',resultset[temp1][4])
    else:
        repeated=1
qstnno=1
while(qstnno<=10):
    if(qstnno<4):
        OpenDB(1)
        print(qstnno,'-question:\t playing for:',qstnno,'Lakh/-\n')
        QstnChooser()
        if(repeated==1):
            while(repeated!=0):
                QstnChooser()
        answerinp=input('Enter your choice!\n')
        if(answerinp==resultset[qstnnodb][5]):
            time.sleep(1)
            print('Ye Sahi jawaab!')
            qstnno+=1
            if(qstnno==4):
                print('\n\n\n\n')
                print("Pehela padaav paar!\n ",qstnno-1,'Lakh Rs\n\n')
                time.sleep(5)
                print('LETS PROCEED')
        else:
            time.sleep(3)
            print("APSOOS !\n YE GALAT JAWAB HAI!!\n\n")
            print('Sahi jawab hai\n',resultset[qstnnodb][5])
            exit()
    if(qstnno==4):
        repeatcheck.clear()
        repeatcheck+=[-1]
    if (qstnno > 3 and qstnno < 7):
        resultset.clear()
        OpenDB(2)
        print(qstnno, '-question:\t playing for:', qstnno, 'Lakh/-\n')
        QstnChooser()
        if (repeated == 1):
            while (repeated != 0):
                QstnChooser()
        answerinp = input('Enter your choice!\n')
        if (answerinp == resultset[qstnnodb][5]):
            print('Congratulations!')
            qstnno += 1
            if(qstnno==7):
                print('\n\n\n\n')
                print("Doosra padaav paar!\n ", qstnno - 1, 'Lakh Rs\n\n')
                time.sleep(5)
                print('LETS PROCEED')
        else:
            print("GALAT JAWAB !!")
            print('Sahi jawab hai\n', resultset[qstnnodb][5])
            exit()
    if (qstnno == 7):
        repeatcheck.clear()
        repeatcheck += [-1]
    if (qstnno > 6 and qstnno <= 10):
        resultset.clear()
        OpenDB(3)
        print(qstnno, '-question:\t playing for:', qstnno, 'Lakh/-\n')
        QstnChooser()
        if (repeated == 1):
            while (repeated != 0):
                QstnChooser()
        answerinp = input('Enter your choice!\n')
        if (answerinp == resultset[qstnnodb][5]):
            print('Congratulations!')
            qstnno += 1
        else:
            print("GALAT JAWAB !!")
            print('Sahi jawab hai\n', resultset[qstnnodb][5])
            exit()
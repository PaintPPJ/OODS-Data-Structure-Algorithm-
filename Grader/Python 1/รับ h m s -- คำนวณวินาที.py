'''
Chapter : 1 - item : 1 - รับ h m s --> คำนวณวินาที

รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์
เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน ชั่วโมง นาที และ วินาที


แล้วแสดงผลเป็น วินาที
แสดงผลตามตัวอย่าง



'''

print("*** Converting hh.mm.ss to seconds ***");
inputall = input("Enter hh mm ss : ")
numH,numM,numS = inputall.split() # ต่อ input 
numH=int(numH);
numM=int(numM);
numS=int(numS);

changetomi = numH * 60;
changetoSec = (changetomi+numM) * 60;
total = changetoSec + numS;


if(numH<0):
    print("hh("+str(numH)+") is invalid!")
    exit()
    
if(numM>=60 or numM<0):
    print("mm("+str(numM)+") is invalid!")    
    exit()

if(numS<0 ):
    print("mm("+str(numS)+") is invalid!")    
    exit()   


if(int(numH)<=9):
    numH="0"+str(numH);
if(int(numM)<=9):
    numM="0"+str(numM);
if(int(numS)<=9):
    numS="0"+str(numS);

print(str(numH)+":"+str(numM)+":"+str(numS)+" = "+str(f'{total:,}')+" seconds");

'''
*** Converting hh.mm.ss to seconds ***
Enter hh mm ss : 11 22 33
11:22:33 = 40,953 seconds

*** Converting hh.mm.ss to seconds ***
Enter hh mm ss : 2 37 59
02:37:59 = 9,479 seconds

*** Converting hh.mm.ss to seconds ***
Enter hh mm ss : 9 28 37
09:28:37 = 34,117 seconds

*** Converting hh.mm.ss to seconds ***
Enter hh mm ss : 0 1 2
00:01:02 = 62 seconds

*** Converting hh.mm.ss to seconds ***
Enter hh mm ss : 2 3 4
02:03:04 = 7,384 seconds

*** Converting hh.mm.ss to seconds ***
Enter hh mm ss : 12 88 45
mm(88) is invalid!

*** Converting hh.mm.ss to seconds ***
Enter hh mm ss : 12 60 32
mm(60) is invalid!

*** Converting hh.mm.ss to seconds ***
Enter hh mm ss : 25 -5 3
mm(-5) is invalid!

*** Converting hh.mm.ss to seconds ***
Enter hh mm ss : 3 -5 -9
mm(-5) is invalid!

*** Converting hh.mm.ss to seconds ***
Enter hh mm ss : 3 7 0
03:07:00 = 11,220 seconds

*** Converting hh.mm.ss to seconds ***
Enter hh mm ss : 0 0 7
00:00:07 = 7 seconds

'''
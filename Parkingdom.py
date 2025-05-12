#주차관리 플랫폼 "Parkingdom"
#등록된 주차시설치: A주차장/천안위치, B주차장/서울위치, C주차장/강릉위치
#A주차장 지하1f 50대 2f 50대, 야외 50대
#B주차장 지하1f 50대 2f 100대
#C주차장 야외 50대
#차량번호 id등록, password:4자리
#detail:가까운 주차장찾기, 가격변경가능, datetime

data, paydata, entri= {"11q1234":"1234"}, {}, {}
area=['A','B','C','D','E']
Aprice, Bprice, Cprice = 500, 800, 300
Adata={"1f":50,"2f":50,"out":50}
A1f, A2f, Aout = [], [], []
Bdata={"1f":100,"2f":100}
B1f, B2f = [], []
Cdata={"out":50}
Cout=[]


from random import randint,choice
from datetime import datetime
from urllib.request import urlopen
import json

#프론트메뉴 
def Front():
    print("-"*72,"\n")
    front=int(input("1.로그인하기 2.회원가입하기 3.관리하기 4.종료하기:(예시:1)"))
    print()
    print("-"*72)
    return front
#가입
def Signup():
    print("-"*72,"\n")    
    print("*Parkingdom회원가입*\n")
    ID=input("차량 번호를 입력해주세요:(예시:86모0384)")

    if ID in data:
        print("이미 가입된 회원입니다.")
    else:
        PW=input("비밀번호를 4자리 입력해주세요:")
        if len(PW) == 4:
            data[ID]=PW
            print("-"*72,"\n")
            print(" "*7,"Parkingdom회원이 되신 것을 진심으로 축하합니다:)")
            print()
            print("-"*72)
        else:
            print("4자리의 비밀번호를 설정해주세요")
    
#로그인
def Login():
    while True:
        ID=input("차량 번호(ID)를 입력해주세요:")
        if ID in data:
            PW=input("비밀번호를 입력해주세요:")
            if PW==data[ID]:
                print("-"*72,"\n")
                print("안녕하세요",ID,"차주님")
                print("***가장 가까운 주차장을 찾는 중이에요***")
                print()
                print("-"*72)
                return ID, PW
                Parking(ID,PW)
                Paying(ID,PW)
            else:
                print("비밀번호가 틀렸습니다")
                continue
        else:
            print("없는 ID입니다 회원가입해주세요")
            Signup()
    
#주차하기
def Parking(ID,PW):
    with urlopen("http://ipinfo.io/json") as response:
        ldata=json.load(response)
        #A주차장/천안위치
        if ldata['city']=="Cheonan":
            print("-"*72,"\n")
            print("현재 가장 가까운 주차장은 A주차장입니다")
            print("가격은 10분당",Aprice,"원입니다")
            print("주차가능공간 | 1.지하1층:",Adata["1f"],"대 | 2.지하2층:",Adata["2f"],"대 | 3.야외:",Adata["out"],"대")
            print()
            print("-"*72)
            floor=int(input("원하는 주차공간번호를 입력해주세요:(예시:1)"))
            if floor == 1 and Adata["1f"] != 0 :
                while True:
                    num=randint(1,10)
                    zone=choice(area)
                    Pspot = f"{zone}{num}"
                    if Pspot in A1f:
                        continue
                    else:
                        A1f.append(Pspot)
                        Adata["1f"] -= 1
                        entry=str(datetime.now())[5:19]
                        entri[(ID,PW)]=entry
                        paydata[ID]="A"
                        break
                print("지하 1층의",Pspot,"위치에 배정되었습니다")
                print("입차시간:",entry)
            elif floor == 2 and Adata["2f"] != 0 :
                while True:
                    num=randint(1,10)
                    zone=choice(area)
                    Pspot = f"{zone}{num}"
                    if Pspot in A2f:
                        continue
                    else:
                        A2f.append(Pspot)
                        Adata["2f"] -= 1
                        entry=str(datetime.now())[5:19]
                        entri[(ID,PW)]=entry
                        paydata[ID]="A"
                        break
                print("지하 2층의",Pspot,"위치에 배정되었습니다")
                print("입차시간:",entry)
            elif floor == 3 and Adata["out"] != 0 :
                while True:
                    num=randint(1,10)
                    zone=choice(area)
                    Pspot = f"{zone}{num}"
                    if Pspot in Aout:
                        continue
                    else:
                        Aout.append(Pspot)
                        Adata["out"] -= 1
                        entry=str(datetime.now())[5:19]
                        entri[(ID,PW)]=entry
                        paydata[ID]="A"
                        break
                print("야외 공간의",Pspot,"위치에 배정되었습니다")
                print("입차시간:",entry)
            else:
                print("주차장이 만석입니다")
        #B주차장/서울위치    
        elif ldata['city']=="Seoul":
            print("-"*72,"\n")
            print("현재 가장 가까운 주차장은 B주차장입니다")
            print("가격은 10분당",Bprice,"원입니다")
            print("주차가능공간 | 1.지하1층:",Bdata["1f"],"대 | 2.지하2층:",Bdata["2f"],"대")
            print()
            print("-"*72)
            floor=int(input("원하는 주차공간번호를 입력해주세요:(예시:1)"))
            if floor == 1 and Bdata["1f"] != 0 :
                while True:
                    num=randint(1,10)
                    zone=choice(area)
                    Pspot = f"{zone}{num}"
                    if Pspot in B1f:
                        continue
                    else:
                        B1f.append(Pspot)
                        Bdata["1f"] -= 1
                        entry=str(datetime.now())[5:19]
                        entri[(ID,PW)]=entry
                        paydata[ID]="B"
                        break
                print("지하 1층의",Pspot,"위치에 배정되었습니다")
                print("입차시간:",entry)
            elif floor == 2 and Bdata["2f"] != 0 :
                while True:
                    num=randint(1,20)
                    zone=choice(area)
                    Pspot = f"{zone}{num}"
                    if Pspot in B2f:
                        continue
                    else:
                        B2f.append(Pspot)
                        Bdata["2f"] -= 1
                        entry=str(datetime.now())[5:19]
                        entri[(ID,PW)]=entry
                        paydata[ID]="B"
                        break
                print("지하 2층의",Pspot,"위치에 배정되었습니다")
                print("입차시간:",entry)
            else:
                print("주차장이 만석입니다")
        #C주차장/강릉위치 
        elif ldata['city']=="Gangneung":
            print("-"*72,"\n")
            print("현재 가장 가까운 주차장은 C주차장입니다")
            print("가격은 10분당",Cprice,"원입니다")
            print("주차가능공간 |",Cdata["out"],"대")
            print()
            print("-"*72)
            if Cdata["out"] != 0 :
                while True:
                    num=randint(1,10)
                    zone=choice(area)
                    Pspot = f"{zone}{num}"
                    if Pspot in Cout:
                        continue
                    else:
                        Cout.append(Pspot)
                        Cdata["out"] -= 1
                        entry=str(datetime.now())[5:19]
                        entri[(ID,PW)]=entry
                        paydata[ID]="C"
                        break
                print(Pspot,"위치에 배정되었습니다")
                print("입차시간:",entry)
            else:
                print("주차장이 만석입니다")
        else:
            print("-"*72)
            print()
            print("현재 위치는:", ldata['city'], "입니다.")
            print("죄송합니다. 현재 해당 도시에 등록된 주차장이 없습니다.\n")
            print("-"*72)
            Down()
            
                
#출차하기
def Paying(ID,PW):
    while True:
        print("-"*72,"\n")
        print(ID,"차량 출차를 원하면 비밀번호를 입력해주세요")
        out_PW=input("비밀번호:")
        print()
        print("-"*72)
        if out_PW==PW:
            ent=entri[(ID,PW)]
            out=str(datetime.now())[5:19]
            day=abs(int(out[3:5])-int(ent[3:5]))
            hour=abs(int(out[6:8])-int(ent[6:8]))
            minu=abs(int(out[9:11])-int(ent[9:11]))
            if paydata[ID]== "A":
                price= Aprice
            if paydata[ID]== "B":
                price= Bprice
            if paydata[ID]== "C":
                price= Cprice
            total=(day/(24*60)+(hour/60)+minu)//10*price
            while True:
                print("-"*72,"\n")
                print("현재 시간:",out,"총 주차시간:",day,"일",hour,"시간",minu,"분")
                print("결제금액:",total,"원")
                print()
                print("-"*72)
                print("1.멤버쉽결제 {10%할인가} 2.일반결제")
                pay=int(input("결제방식을 선택해주세요:"))
                if pay ==1:
                    secure=input("비밀번호를 입력하세요:")
                    if secure == PW:
                        dis=total-(total*0.1)
                        print(dis,"원 결제완료되었습니다 안녕히가십시오:)")
                        return
                        
                    else:
                        print("잘못된 번호입니다")
                        continue
                            
                            
                elif pay ==2:
                    secure=input("비밀번호를 입력하세요:")
                    if secure == PW:
                        print(total,"원 결제완료되었습니다")
                        return
                        
                    else:
                        print("잘못된 번호입니다")
                        continue
                else:
                    print("잘못된 입력입니다")
                    continue
        else:
            print("비밀번호가 틀렸습니다")
            continue
            
#관리
def Setting():
    global Aprice, Bprice, Cprice
    set_menu=int(input("1.A주차장세팅 2.B주차장세팅 3.C주차장세팅| 세팅할 주차장을 선택하시오:"))
    if set_menu==1:
        SPW=int(input("관리자 비밀번호를 입력해주세요:"))
        if SPW== 1111:
            newp =int(input("변경할 10분당 단가를 입력해주세요(단위:원)"))
            Aprice=newp          
            print("가격변경완료")       
    elif set_menu==2:
        SPW=int(input("관리자 비밀번호를 입력해주세요:"))
        if SPW== 2222:
            newp =int(input("변경할 10분당 단가를 입력해주세요(단위:원)"))
            Bprice=newp          
            print("가격변경완료")
    elif set_menu==3:
        SPW=int(input("관리자 비밀번호를 입력해주세요:"))
        if SPW== 3333:
            newp =int(input("변경할 10분당 단가를 입력해주세요(단위:원)"))
            Cprice=newp          
            print("가격변경완료")
    else:
        print("잘못된 입력입니다.")

def Down():
    print("Parkingdom을 이용해주셔서 감사합니다:)")
    return
    
#Main
while True:
    front=Front()
    if front ==1:
        ID, PW = Login()
        Parking(ID,PW)
        Paying(ID,PW)
    elif front ==2:
        Signup()
    elif front ==3:
        Setting()
    elif front ==4:
        Down()
        break
    else:
        print("잘못된 입력입니다")
        continue
        
        
    
            

    




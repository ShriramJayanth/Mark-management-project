import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Longbottom@32",
    database="pok")
h="hostel"
m="M"
f="F"
d="dayscholar"
cur=mydb.cursor()
print("1.show all data\n2.add data\n3.modify data\n4.total pass%\n5.total fail%\n6.clear data\n7.hostel mark stats\n8.day scholar mark stats\n9.boys mark stats\n10.girls mark stats\n11.python mark stats\n12.aptitude mark stats\n13.maths mark stats\n14.english mark stats\n15.physics mark stats\n16.chemistry mark stats\n17.delete specific data\n18.show specific data\n19.close")
while(True):
    a=input("Enter your choice:")
    if(a=="1"):
        cur.execute("select * from main")
        data=cur.fetchall()
        print("registernum    ","name    ","python    ","aptitude    ","maths    ","english    ","physics    ","chemistry    ","status    ","gender    ")
        for i in data:
           print(*i,sep=("         "))
    elif(a=="2"):
        rno=input("registeredno:")
        name=input("name:")
        py=int(input("python marks:"))
        ap=int(input("aptitude marks:"))
        mat=int(input("maths marks:"))
        eng=int(input("english marks:"))
        phy=int(input("physics marks:"))
        che=int(input("chemistry marks:"))
        st=input("status:")
        gen=input("Gender:")
        cur.execute("insert into main(registernum,name,python,aptitude,maths,english,physics,chemistry,status,gender)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rno,name,py,ap,mat,eng,phy,che,st,gen))
        mydb.commit()
    elif(a=="4"):
        cur.execute("select count(*) from main")
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and aptitude>=50 and maths>=50 and english>=50 and physics>=50 and chemistry>=50")
        per=cur.fetchall()
        try:
           print(round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("NONE")
            
    elif(a=="5"):
        cur.execute("select count(*) from main")
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and aptitude>=50 and maths>=50 and english>=50 and physics>=50 and chemistry>=50")
        per=cur.fetchall()
        try:
           print(round(100-per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("NONE")   
    elif(a=="6"):
        cur.execute("delete from main")
        mydb.commit()
    elif(a=="3"):
        rno=input("enter the registered number:")
        while(True):
           print("which data are you willing to change\n1.name\n2.python marks\n3.aptitude marks\n4.maths marks\n5.english marks\n6.physics marks\n7.chemistry marks\n8.status\n9.gender\n10.close")
           b=int(input("enter your choice:"))
           if(b==1):
                 ch=input("enter the new data:")
                 cur.execute("update main set name=%s where registernum=%s",(ch,rno))
           elif(b==2):
                 ch=int(input("enter the new data:"))
                 cur.execute("update main set python=%s where registernum=%s",(ch,rno))
           elif(b==3):
                 ch=int(input("enter the new data:"))
                 cur.execute("update main set aptitude=%s where registernum=%s",(ch,rno))
           elif(b==4):
                 ch=int(input("enter the new data:"))
                 cur.execute("update main set maths=%s where registernum=%s",(ch,rno))
           elif(b==5):
                 ch=int(input("enter the new data:"))
                 cur.execute("update main set english=%s where registernum=%s",(ch,rno))
           elif(b==6):
                 ch=int(input("enter the new data:"))
                 cur.execute("update main set physics=%s where registernum=%s",(ch,rno))
           elif(b==7):
                 ch=int(input("enter the new data:"))
                 cur.execute("update main set chemistry=%s where registernum=%s",(ch,rno))
           elif(b==8):
                 ch=(input("enter the new data:"))
                 cur.execute("update main set status=%s where registernum=%s",(ch,rno))
           elif(b==9):
                 ch=(input("enter the new data:"))
                 cur.execute("update main set gender=%s where registernum=%s",(ch,rno))
           elif(b==10):
                 break
           else:
               print("wrong value entered.")
           mydb.commit()
    elif(a=="19"):
         break
    elif(a=="7"):
        cur.execute("select count(*) from main where status=%s",(h,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and aptitude>=50 and maths>=50 and english>=50 and physics>=50 and chemistry>=50 and status=%s",(h,))
        per=cur.fetchall()
        try:
           print("hostel pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and aptitude>=50 and maths>=50 and english>=50 and physics>=50 and chemistry>=50 and status=%s and gender=%s",(h,m))
        per=cur.fetchall()
        try:
           print("hostel boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel boys pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and aptitude>=50 and maths>=50 and english>=50 and physics>=50 and chemistry>=50 and status=%s and gender=%s",(h,f))
        per=cur.fetchall()
        try:
           print("hostel girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel girls pass percentage:NONE")   
        
    elif(a=="8"):
        cur.execute("select count(*) from main where status=%s",(d,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and aptitude>=50 and maths>=50 and english>=50 and physics>=50 and chemistry>=50 and status=%s",(d,))
        per=cur.fetchall()
        try:
           print("day scholar pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("day scholar fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("day scholar pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and aptitude>=50 and maths>=50 and english>=50 and physics>=50 and chemistry>=50 and status=%s and gender=%s",(d,m))
        per=cur.fetchall()
        try:
           print("dayscholar boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar boys pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and aptitude>=50 and maths>=50 and english>=50 and physics>=50 and chemistry>=50 and status=%s and gender=%s",(d,f))
        per=cur.fetchall()
        try:
           print("dayscholar girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar girls pass percentage:NONE")   
    elif(a=="9"):
        cur.execute("select count(*) from main where gender=%s",(m,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and aptitude>=50 and maths>=50 and english>=50 and physics>=50 and chemistry>=50 and gender=%s",(m,))
        per=cur.fetchall()
        try:
           print("boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("boys pass percentage:NONE")   
    elif(a=="10"):
        cur.execute("select count(*) from main where gender=%s",(f,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and aptitude>=50 and maths>=50 and english>=50 and physics>=50 and chemistry>=50 and gender=%s",(f,))
        per=cur.fetchall()
        try:
           print("girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("girls pass percentage:NONE")   
    elif(a=="11"):
        cur.execute("select count(*) from main")
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50")
        per=cur.fetchall()
        try:
           print("total pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("total fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("total pass percentage:NONE")
        cur.execute("select count(*) from main where gender=%s",(m,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and gender=%s",(m,))
        per=cur.fetchall()
        try:
           print("boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("boys pass percentage:NONE")   
        cur.execute("select count(*) from main where gender=%s",(f,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and gender=%s",(f,))
        per=cur.fetchall()
        try:
           print("girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("girls pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s",(d,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and status=%s",(d,))
        per=cur.fetchall()
        try:
           print("day scholar pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("day scholar fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("day scholar pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50  and status=%s and gender=%s",(d,m))
        per=cur.fetchall()
        try:
           print("dayscholar boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar boys pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and status=%s and gender=%s",(d,f))
        per=cur.fetchall()
        try:
           print("dayscholar girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar girls pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s",(h,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and status=%s",(h,))
        per=cur.fetchall()
        try:
           print("hostel pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and status=%s and gender=%s",(h,m))
        per=cur.fetchall()
        try:
           print("hostel boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel boys pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50 and status=%s and gender=%s",(h,f))
        per=cur.fetchall()
        try:
           print("hostel girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel girls pass percentage:NONE")   
    elif(a=="12"):
        cur.execute("select count(*) from main")
        tot=cur.fetchall()
        cur.execute("select count(*) from main where python>=50")
        per=cur.fetchall()
        try:
           print("total pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("total fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("total pass percentage:NONE")   
        cur.execute("select count(*) from main where gender=%s",(m,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where aptitude>=50 and gender=%s",(m,))
        per=cur.fetchall()
        try:
           print("boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("boys pass percentage:NONE")   
        cur.execute("select count(*) from main where gender=%s",(f,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where aptitude>=50 and gender=%s",(f,))
        per=cur.fetchall()
        try:
           print("girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("girls pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s",(d,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where aptitude>=50 and status=%s",(d,))
        per=cur.fetchall()
        try:
           print("day scholar pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("day scholar fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("day scholar pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where aptitude>=50  and status=%s and gender=%s",(d,m))
        per=cur.fetchall()
        try:
           print("dayscholar boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar boys pass percentage:NONE")
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where aptitude>=50 and status=%s and gender=%s",(d,f))
        per=cur.fetchall()
        try:
           print("dayscholar girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar girls pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s",(h,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where aptitude>=50 and status=%s",(h,))
        per=cur.fetchall()
        try:
           print("hostel pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where aptitude>=50 and status=%s and gender=%s",(h,m))
        per=cur.fetchall()
        try:
           print("hostel boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel boys pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where aptitude>=50 and status=%s and gender=%s",(h,f))
        per=cur.fetchall()
        try:
           print("hostel girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel girls pass percentage:NONE")   
    elif(a=="13"):
        cur.execute("select count(*) from main")
        tot=cur.fetchall()
        cur.execute("select count(*) from main where maths>=50")
        per=cur.fetchall()
        try:
           print("total pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("total fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("total pass percentage:NONE")   
        cur.execute("select count(*) from main where gender=%s",(m,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where maths>=50 and gender=%s",(m,))
        per=cur.fetchall()
        try:
           print("boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("boys pass percentage:NONE")   
        cur.execute("select count(*) from main where gender=%s",(f,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where maths>=50 and gender=%s",(f,))
        per=cur.fetchall()
        try:
           print("girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("girls pass percentage:NONE")
        cur.execute("select count(*) from main where status=%s",(d,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where maths>=50 and status=%s",(d,))
        per=cur.fetchall()
        try:
           print("day scholar pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("day scholar fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("day scholar pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where maths>=50  and status=%s and gender=%s",(d,m))
        per=cur.fetchall()
        try:
           print("dayscholar boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar boys pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where maths>=50 and status=%s and gender=%s",(d,f))
        per=cur.fetchall()
        try:
           print("dayscholar girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar girls pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s",(h,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where maths>=50 and status=%s",(h,))
        per=cur.fetchall()
        try:
           print("hostel pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where maths>=50 and status=%s and gender=%s",(h,m))
        per=cur.fetchall()
        try:
           print("hostel boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel boys pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where maths>=50 and status=%s and gender=%s",(h,f))
        per=cur.fetchall()
        try:
           print("hostel girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel girls pass percentage:NONE")   
    elif(a=="14"):
        cur.execute("select count(*) from main")
        tot=cur.fetchall()
        cur.execute("select count(*) from main where english>=50")
        per=cur.fetchall()
        try:
           print("total pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("total fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("total pass percentage:NONE")   
        cur.execute("select count(*) from main where gender=%s",(m,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where english>=50 and gender=%s",(m,))
        per=cur.fetchall()
        try:
           print("boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("boys pass percentage:NONE")   
        cur.execute("select count(*) from main where gender=%s",(f,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where english>=50 and gender=%s",(f,))
        per=cur.fetchall()
        try:
           print("girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("girls pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s",(d,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where english>=50 and status=%s",(d,))
        per=cur.fetchall()
        try:
           print("day scholar pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("day scholar fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("day scholar pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where english>=50  and status=%s and gender=%s",(d,m))
        per=cur.fetchall()
        try:
           print("dayscholar boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar boys pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where english>=50 and status=%s and gender=%s",(d,f))
        per=cur.fetchall()
        try:
           print("dayscholar girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar girls pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s",(h,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where english>=50 and status=%s",(h,))
        per=cur.fetchall()
        try:
           print("hostel pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where english>=50 and status=%s and gender=%s",(h,m))
        per=cur.fetchall()
        try:
           print("hostel boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel boys pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where english>=50 and status=%s and gender=%s",(h,f))
        per=cur.fetchall()
        try:
           print("hostel girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel girls pass percentage:NONE")   
    elif(a=="15"):
        cur.execute("select count(*) from main")
        tot=cur.fetchall()
        cur.execute("select count(*) from main where physics>=50")
        per=cur.fetchall()
        try:
           print("total pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("total fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("total pass percentage:NONE")   
        cur.execute("select count(*) from main where gender=%s",(m,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where physics>=50 and gender=%s",(m,))
        per=cur.fetchall()
        try:
           print("boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("boys pass percentage:NONE")   
        cur.execute("select count(*) from main where gender=%s",(f,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where physics>=50 and gender=%s",(f,))
        per=cur.fetchall()
        try:
           print("girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("girls pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s",(d,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where physics>=50 and status=%s",(d,))
        per=cur.fetchall()
        try:
           print("day scholar pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("day scholar fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("day scholar pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where physics>=50  and status=%s and gender=%s",(d,m))
        per=cur.fetchall()
        try:
           print("dayscholar boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar boys pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where physics>=50 and status=%s and gender=%s",(d,f))
        per=cur.fetchall()
        try:
           print("dayscholar girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar girls pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s",(h,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where physics>=50 and status=%s",(h,))
        per=cur.fetchall()
        try:
           print("hostel pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where physics>=50 and status=%s and gender=%s",(h,m))
        per=cur.fetchall()
        try:
           print("hostel boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel boys pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where physics>=50 and status=%s and gender=%s",(h,f))
        per=cur.fetchall()
        try:
           print("hostel girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel girls pass percentage:NONE")   
    elif(a=="16"):
        cur.execute("select count(*) from main")
        tot=cur.fetchall()
        cur.execute("select count(*) from main where chemistry>=50")
        per=cur.fetchall()
        try:
           print("total pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("total fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("total pass percentage:NONE")   
        cur.execute("select count(*) from main where gender=%s",(m,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where chemistry>=50 and gender=%s",(m,))
        per=cur.fetchall()
        try:
           print("boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("boys pass percentage:NONE")   
        cur.execute("select count(*) from main where gender=%s",(f,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where chemistry>=50 and gender=%s",(f,))
        per=cur.fetchall()
        try:
           print("girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("girls pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s",(d,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where chemistry>=50 and status=%s",(d,))
        per=cur.fetchall()
        try:
           print("day scholar pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("day scholar fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("day scholar pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where chemistry>=50  and status=%s and gender=%s",(d,m))
        per=cur.fetchall()
        try:
           print("dayscholar boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar boys pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s and gender=%s",(d,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where chemistry>=50 and status=%s and gender=%s",(d,f))
        per=cur.fetchall()
        try:
           print("dayscholar girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("dayscholar girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("dayscholar girls pass percentage:NONE")   
        cur.execute("select count(*) from main where status=%s",(h,))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where chemistry>=50 and status=%s",(h,))
        per=cur.fetchall()
        try:
          print("hostel pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
          print("hostel fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel pass percentage:NONE")  
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,m))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where chemistry>=50 and status=%s and gender=%s",(h,m))
        per=cur.fetchall()
        try:
          print("hostel boys pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
          print("hostel boys fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel boys pass percentage:NONE")  
        cur.execute("select count(*) from main where status=%s and gender=%s",(h,f))
        tot=cur.fetchall()
        cur.execute("select count(*) from main where chemistry>=50 and status=%s and gender=%s",(h,f))
        per=cur.fetchall()
        try:
           print("hostel girls pass percentage:",round(per[0][0]/tot[0][0]*100,2),"%")
           print("hostel girls fail percentage:",100-round(per[0][0]/tot[0][0]*100,2),"%")
        except ArithmeticError as e:
            print("hostel girls pass percentage:NONE")   
    elif(a=="17"):
        rno=input("enter registered number:")
        cur.execute("delete from main where registernum=%s",(rno,))
        mydb.commit()
    elif(a=="18"):
        rno=input("Enter registered number:")
        cur.execute("select * from main where registernum=%s",(rno,))
        data=cur.fetchall()
        print("registernum    ","name    ","python    ","aptitude    ","maths    ","english    ","physics    ","chemistry    ","status    ","gender    ")
        for i in data:
           print(*i,sep=("         "))
        
    else:
        print("wrong value entered.")
        
        
        
        
         
        
        
        
 
        
        
        
        
                    
        
 

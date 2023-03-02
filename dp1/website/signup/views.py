from django.shortcuts import render
import mysql.connector as sql
un=''
gen=''
phno=''
em=''
pwd=''


# Create your views here.
def signaction(request):
    global un,phno,gen,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="28mg",database='website1')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="User Name":
                un=value
            if key=="password":
                pwd=value
            if key=="email":
                em=value
            if key=="gender":
                gen=value
            if key=="phno":
                phno=value
            
        
        c="insert into users Values('{}','{}','{}','{}','{}')".format(un,pwd,em,gen,phno)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')
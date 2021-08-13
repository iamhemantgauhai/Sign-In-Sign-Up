import json
out_dict={}
dict1={}
list1=[]
print('\n**********|->>> welcome in my websites <<<-|************\n')
print('\t\t>>>> 1.SIGNUP <<<< \n  \t\t>>>> 2.SIGNIN <<<< ')
user_ask = input("Would you want to Signin/signup => ")
def signup():
    print("************|welcme to signup Page|*************\n")
    username = input("Enter your username => " )
    phone_no = input("Enter your phone_number => " )
    email = input("Enter your email => ")
    password = input("Enter your password => " )
    l, u, p, d = 0, 0, 0, 0
    for i in password:
        if (i.islower()):
            l+=1      
        if (i.isupper()):
            u+=1     
        if (i.isdigit()):
            d+=1           
        if(i=='@' or i=='$' or i=='_' or i=="#" ):
            p+=1           
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
        print("\nYour Password is Valid")
        password2=input("Enter your confirm password => ")
        if password==password2:
            print("\n****|--> You Signed Up Succsefully <--|****")
        else:
            print("\n****|--> both password are wrong <--|****")
    else:
        print("invalid")
    out_dict["user_name"]=username
    out_dict["user_phone_no."]=phone_no
    out_dict["user_email"]=email
    out_dict["user_password"]=password
    list1.append(out_dict)
    dict1["userinfo"]=list1
    try:
        with open("userdetails.json","r+")as f:
            j=f.read()
            fs=json.loads(j)
            for i in fs:
                if i == "userinfo":
                    s=fs[i]
                    s.append(out_dict.copy())
                    dict1["userinfo"]=s
                    json.dumps(dict1,f,indent=4)
                    f.close()
    except:
        with open("userdetails.json","w") as fil:
            fil.write(json.dumps(dict1,indent=4))
def login():
    print("************|welcme to login Page|*************\n")
    i=0
    k=0
    while 1: 
        username = input("Enter your email for login => ")
        password = input("Enter your password for login => ")
        with open("userdetails.json",'r') as fd:
            users_data = json.load(fd)
        for dics in users_data['userinfo']:
            if dics['user_email']==username and dics['user_password']==password:
                print()
                print("|succesfully logged IN|\n")
                k = 1 
                break
        if k == 1:
            break    
        elif i == 3:
            print("\n****|--> User Not found <--|****\n")
            break
        else:
            print("\n****|--> <---You write the wrong password Please try again. <--|****\n")
        i+=1
    print("****|--> Thanks for visit in my website <--|****")
def main(user):
    if user=="1" or user=="signup":
        signup()
        b=input("\nDo you want login(1) or Exit(2) => ")
        if b == "1":
            login()
        else:
            print("****|--> Thanks for visit in my website <--|****")
    elif  user=="2" or user=='login':
        login()
    else:
        print("****|--> unvalid operation <--|****")
main(user_ask)
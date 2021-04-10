

profile={
    'username':None,
    'email':None,
    'password':None,
    'name':None,
    'age':None,
}
def verify(lst):
    for i in lst:
        if len(i)==0:
            return False
    return True 
def show_profile():
    print('Username: {}\nPassword: {}\nEmail: {}\nName: {}\n Age: {}'.format(profile['username'],profile['password'],profile['email'],profile['name'],profile['age'],))     

def login():
    username=input('Enter your username: ')
    password=input('Enter Your password: ')

    if len(username) and len(password):
       if username==profile['username'] and password==profile['password']:
           print('yepee,,,!!!!Congratulations')
           show_profile()
       else:
           print('Incorrecrect username or password',end='\n\n')
           login()

    else:
        print('try again')
        login()

def registration():
    username=input('Enter username: ')
    password=input('Enter password: ')
    con_password=input('Confirme Password: ')
    email=input('Enter email: ')
    name=input('Enter Name: ')
    age=input('Enter Your age: ')
    lst=[username,password,con_password,email,name,age]
    if verify(lst):
        profile['username']=username
        profile['password']=password
        profile['email']=email
        profile['name']=name
        profile['age']=age
        print('registration complete ,please sign in ')
        login()

    else:
        print('Wrong input')
        registration()    


is_user=input('Are you a user(y/n):')

if is_user=='y':
    login()
elif is_user=='n':
    registration()   
else:
    print('Wrong input')    

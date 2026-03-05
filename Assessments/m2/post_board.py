import datetime
users=[]
posts=[]
def login():
    print("_____LOGIN______")
    try:
        username=input("enter user name: ")
        if username=="":
            print("user name can not be empty")
        users.append(username)
        print("Login Succesfully")
        return username
    except Exception as e:
        print(e)

def createpost(current_user):
    print("______craete post______")
    try:
        title=input("enter title: ")
        if title=="":
            print("title can not be empty")
        description=input("enter description: ")
        if description=="":
            print("title can not be empty")
        date=datetime.datetime.now()
        post={
            "author":current_user,"title":title,"description":description,"date":date
        }
        posts.append(post)
        print("post created successfully")
    except Exception as e:
        print(e)

def main():
    current_user=login()
    while True:
        print("\n1.create post")
        print("2. view all posts")
        print("3. search users")
        print("4. exit")
        choice=int(input("entre choice(1,2,3,4):"))
        if choice==1:
            createpost(current_user)
        elif choice==2:
            viewallpost()
        elif choice==3:
            searchpost()
        elif choice==4:
            print("exit program")
            break
        else:
            print("invalid choice")

def viewallpost():
    print("______all post_____")
    if len(posts)==0:
        print("no post available")
        return
    for post in posts:
        print("author:",post["author"])
        print("title:",post["title"])
        print("description:",post["description"])
        print("date:",post["date"],"\n")

def searchpost():
    search=input("search user name: ")
    found=False
    for post in posts:
        if post["author"]==search:
            print("author:",post["author"])
            print("title:",post["title"])
            print("description:",post["description"])
            print("date:",post["date"],"\n")
            found=True

    if found==False:
        print("not available in this user")
main()



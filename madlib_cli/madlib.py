import re
"""
These functions are aimed to get the text from a file and do the madlib game with it
to test this code please only try 
merge("madlib_cli/assets/template1.txt") as its embedded with the other functions 

note: please comment the introduction print to pass the test!

"""


# print('Welcome To the game of Madlibs Where Your words will turn ,agically into a paragraph. \n how to play: \n 1- you will be asked to enter a words with a specific types \n 2- enjoy')

def read_template(path):

    # try:
    #     file = open(path)
    # except FileNotFoundError:
    #     content = "Error : Sorry file not found"
    # else:
    #     content = file.read()
    #     file.close()
    # finally:
    #     return content

    file=open(path)
    return file.read()





def parse_template(text):
    x=re.findall(r'{(.*?)}',text)
    x= tuple(x)
    stripped=re.sub(r'{(.*?)}',"{}",text)
    return stripped ,x

    

def merge(text,x):
    return text.format(*x)









    


## solving the code trials!

# print('Welcome To the game of Madlibs Where Your words will turn ,agically into a paragraph. \n how to play: \n 1- you will be asked to enter a words with a specific types \n 2- enjoy')

# def read_Text(path):
#     with open(path) as link:
#         content=link.read()
#     return content

# text=read_Text("madlib_cli/assets/template1.txt")

# x=re.findall("{.*?}",text)
# print(x)
# i=0
# answers=[]
# while i < len(x):
#     answer=input("enter  "+x[i]+"  ")
#     answers+=[answer]
#     content=text.replace( x[i] , answer)
#     i+=1
# # print(answers)

# with open("madlib_cli/assets/templateTEST.txt",'w+') as f:
#     f.write(content)
#     i=0
#     while i < len(x):
#         print(x[i], answers[i])
        
        
#         i+=1
        
#     print(content)
    
        
    
    

# print(text.format(Adjective=input('enter Adjective '),Noun=input('enter Noun ')))
# answers=[]
# x=''





# print(read_template("madlib_cli/assets/template1.txt"))  ## works fine
# print(parse_template("madlib_cli/assets/template1.txt"))  ##works fine
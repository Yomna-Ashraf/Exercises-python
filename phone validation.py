def valid(str1):
    
    if "-" in str1 and len(str1)==12:
        str1=str1.split("-")
    elif " " in str1 and len(str1)==12 :
        str1 = str1.split(" ")
    elif " " not in str1 and "-" not in str1 and len(str1)==10:

        return "true"
    elif ")" in str1 and "(" in str1 and "-" in str1 and len(str1)==13:
        str1=str1.split("-")
    elif ")" in str1 and "(" in str1 and "-" in str1 and " " in str1 :
        str1=str1.split(" ")
    elif len(str1)==14 and  "-" not in str1 and " " in str1 and str1.count(" ")==3 and"(" not in str1 and ")" not in str1:
        str1=str1.split(" ")
        print(str1)


        
            
   
    if len(str1)==3 and len(str1[0])==3 and len(str1[1])==3 and len(str1[2])==4:
        return "true" 
        
    elif len(str1) == 2 and len(str1[0])== 8 and len(str1[1])==4:
        return "true"
        
    elif len(str1)==2 and len(str1[0])==5 and len(str1[1])==8 and str1[1].count("-")==1:
        return "true"
        
    elif len(str1[0])==1 and len(str1)==4:
        print("iiii")
        return "true"
    


print(valid("(555)5)5-5555"))
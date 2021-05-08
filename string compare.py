def compare(str1 ,str2) : 
    sstring1 = set(str1)  
    sstring2 = set(str2) 
    matching = sstring1 & sstring2  
    print("No. of matching characters are : " + str(len(matching)) ) 
if __name__ == "__main__" : 
    str1 = 'aabcijek78lk12k' 
    str2 = 'abifhdhgi11@6k'   
    compare( str1 , str2 )

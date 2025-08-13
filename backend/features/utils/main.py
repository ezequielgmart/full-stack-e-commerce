def validate_email(email:str) -> bool:
    # 

    if "@" in email :
        data = email.split("@")

        if len(data) ==2:
            for i in data:
                    
                if i == "":
                    return False
                
            return True
        else:
            return False
            

"""
Not allowed 
test@domain (missing the TLD like .com)
test@domian. (trailing dot)
_@test.com (some characters are not allowed)

"""
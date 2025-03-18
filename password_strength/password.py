import string
import random
import streamlit as st
import re

#step1

st.set_page_config(page_title="Password Strength Checker",page_icon="🔒")
st.title("Password strength checker")
st.markdown("""
## welcome to the ultimate password strength checker!👋
use this simple tool to check the strength of your password and get suggestion on how to make it more strong.
            we will give you helpful tips to create a **Stong Password** 🔒""")
def generate_password(length):
    characters = string.digits + string.ascii_letters + "!@#$%^&*"
    print(characters)
    return "".join(random.choice(characters) for i in range(length))

# step 2  
def check_password_strength(password):
    score =0
    common_password = ["123456789","abc12345","pakistan"]
    if password in common_password:
        return "❌ This password is too common. choose a more unique one.","weak" 
    
    feedback =[]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("💎 Password should be at least 8 characters long.")   

    if  re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score +=1
    else:
        feedback.append("💎Include both uppercase and lowercase letters.")  

    if re.search(r"\d",password):
        score += 1
    else:
        feedback.append("💎 Add atleast one number(0-9).")

    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
        feedback.append("💎Include at least one special character (!@#$%^&*).")
    if score ==4:
        return "✅ Strong Password!","strong"
    elif score ==3:
        return "🛠 Moderate Password -Consider adding more security features.","Moderate"
    else:
        return "\n".join(feedback) ,"Weak"          

check_pssword = st.text_input("Enter your password",type="password")
if st.button("Check Strength"):
    if check_pssword:
       result,Strength = check_password_strength(check_pssword)
       if Strength == "strong":
           st.success(result)
           st.balloons()
       elif Strength == "Moderate":
           st.warning(result)    
       else:
           st.error("Weak password -Improve it using these tips:")
           for tip in result.split("\n"):
               st.write(tip)

    else:
        st.warning("please enter a password")    



# step 2 complete

#step 1

password_length = st.number_input("Enter the length of password",min_value=8, max_value=20, value = 10)
if st.button("Generate Password"):
    password = generate_password(password_length)
    st.success(f"{password}")
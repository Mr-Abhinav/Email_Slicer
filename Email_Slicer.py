#!/usr/bin/env python
# coding: utf-8

# In[2]:


def email_slicer(email):
    username, domain = email.split('@')
    return username, domain

def main():
    email = input("Enter an email address: ").strip()
    
    if '@' in email:
        username, domain = email_slicer(email)
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    else:
        print("Invalid email address format.")

if __name__ == "__main__":
    main()


# In[ ]:





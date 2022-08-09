# def replace_domain(email,newEmail,oldEmail='kaaj.com'):
#     for character in range(len(email)):
#         if email[character]=='@':
#             mail = email[0:character+1]
#             domain = email[character+1:]
#     if domain==newEmail:
#         print('Unchanged:',email)
#     else:
#         print('Changed:',mail+newEmail)
# mailAdd = input()
# newDom = input()
# replace_domain(mailAdd,newDom)
def mail(mail_address, new_domain, *old_domain):
    new_mail = ""
    for i in range(len(mail_address)):
        new_mail += mail_address[i]
        if mail_address[i] == "@":
            break
    new_mail += new_domain
    
    if new_mail == mail_address:
        print(f"Unchanged: {new_mail}")
    else:
        print(f"Changed: {new_mail}")

mail_address = input()
new_domain = input()
old_domain = input()
mail(mail_address, new_domain, old_domain)
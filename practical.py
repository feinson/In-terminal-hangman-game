

def fibonacci(n):
    initial_list =[0,1]
    if n == 1:
        return [0]
    elif n ==2:
        return initial_list
    else:
        prev=fibonacci(n-1)
        prev_length=len(prev)
        sum_from=prev_length-2
        prev.append(sum(prev[sum_from:]))
        return prev


print(fibonacci(100))








# def get_name():
#     while True:
#         good = True
#         name_in = input('Please enter your name\n')
#         to_check=[]
#         to_check[:0]="!@£$%^&*()"
#         for character in to_check:
#             if character in name_in:
#                 good = False

#         if good == True:
#             break
#         else:
#             print("Names cannot include any of the following characters: !@£$%^&*()")
#     return name_in

# def get_age():
#     while True:
#         age_in = input('Please enter your age\n')
#         try:
#             int_age = int(age_in)
#         except:
#             print("Age must be an integer value")
#         if int_age>12:
#             break
#         else:
#             print("Age must be at least 13")

#     return int_age

# def get_email():
#     while True:
#         email_in = input('Please enter your email\n')
#         if "@" in email_in:
#             break
#         else:
#             print("e-mail must contain an @-symbol")

#     return email_in

# def get_details():
#     return [get_name(), get_age(), get_email()]

# print(get_details())









# clothing = {"type": "dress", "price": "£30", "colour": "red"}

# def apparel_describer(dicky_wicky, attributes_to_print="all"):
#     if attributes_to_print == "all":
#         attributes_to_print=list(dicky_wicky.keys())
#         final=[]
#     for item in dicky_wicky:
#         if item in attributes_to_print:
#             print(f"{item} : {dicky_wicky[item]}")
#     print(len(attributes_to_print))
#     return "thats it"



# print(apparel_describer(clothing))
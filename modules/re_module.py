import re

def check_email(email):
  email_reg = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  #user_email = "admin_2@gmail.com" # admin.com
  result = re.match(email_reg, email)
  if result:
    print("Email is valid!")
  else:
    print("Email is invalid!")

#  admin 2 . - _ +  => ^[a-zA-Z0-9_.+-]+
#  @gmail /@companyname2 @[a-zA-Z0-9-]+
#  .com / .co.jp   \.[a-zA-Z0-9-.]+$

user1_email = "user1@example.com.mm"
check_email(user1_email)
user2_email = "user2@.com.en"
check_email(user2_email)
user3_email = "user3@example.com.jp"
check_email(user3_email)

# website url 
# phone no

test_str = "The rain in Spain"
findall_result = re.findall('[a-n]', test_str)
print(findall_result)
from models import storage
from models.base_model import BaseModel

# task 5
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = input("What is your name: ")
my_model.relationship = input("What is your relation to candidate: ")
my_model.my_number = int(input("What is your telephone number: "))
my_model.my_age = int(input("How old are you: "))
my_model.account_number = int(input("What is your bank account number: "))
my_model.save()
print(my_model)

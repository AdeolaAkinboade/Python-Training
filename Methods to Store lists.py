#need to store the data into something instead of having
#an infinite loop

user_prompt = 'Enter too dooo:'

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo)
    print(todos)

#NOTES
#todos.append() the .append() part is a method
#they are like functions
#they are attached to other objects
#append is associated with todos which is a list now
#you cant append something to a string you can append to a list
#different methods are compatible with different data types  eg todos.capitalize() to capitalize a string








#cannot store our list data like this because it overwrites pervious data when it loops
#user_prompt = 'Enter too dooo:'
#while True:
#   todo = input(user_prompt)
#    todos = [todo]
 #   print(todos)
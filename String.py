message = "Hello World"

print(message)
print("UpperCase: " , message.upper())
print("LowerCase: " , message.lower())
print("Length of message: " , len(message))
print("First character: " , message[0])
print("Fifth character: " , message[5])

name = input("What is your name: ")
print("Hello, " , name)

contains_world = "World" in message
print(contains_world, "to have word 'World' in message")

print("Updated message: " , message.replace("Hello", "Hi"))
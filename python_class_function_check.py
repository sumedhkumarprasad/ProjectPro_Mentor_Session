# Simple function
def square(x):
    return x * x

# Example class
class MyClass:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print("Hello, " + self.name + "!")
    
# Main section
if __name__ == "__main__":
    # Call the function
    result = square(5)
    print("Square:", result)
    
    # Create an instance of the class
    obj = MyClass("John")
    obj.greet()


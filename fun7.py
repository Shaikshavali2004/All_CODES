# def outer():
#     print("Hii")

#     def inner():
#         print("Hello") 

# outer()

# def outer():
#     print("Hii")

#     def inner():
#         print("Hello") 
    
#     inner()

# outer()

def outer():
    print("Hii")

    def inner():
        print("Hello") 
    
    return inner

inner=outer()
inner()
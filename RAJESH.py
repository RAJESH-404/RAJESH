import platform
b = platform.architecture()[0]
if b == '64bit':
    import tools off 
else:
    print("32bit Not Supported!")

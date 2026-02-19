text = "Yoooooo\nthis text has been\ngood one"
with open('lamb.test','w') as file:   #write to a file
    # with open('lamb.test', 'a') as file:  append a file
    file.write(text)
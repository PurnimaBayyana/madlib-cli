def file_initial_read():
    f= open('/Users/bayyanap/Documents/python/inputs.txt','r')
    contents =f.read()
    line = contents.split('{') 
    length = len(line)
    input_list =[]
    for i in range(length):
        istr = line[i] #.split('}')
        if "}" in istr:
            istr = line[i].split('}')
            input_list.append(istr[0])
            contents = contents.replace(istr[0],'')
    print(input_list)     
    print(contents)  
    data_list = []
    for inpdata in input_list:
        inputval = input(f"Enter an {inpdata}")
        data_list.append(inputval)
    contents = contents.format(*data_list)
    print(contents)   
        #if  istr.endswith('{'):
            #print(istr)
    f.close()
           
file_initial_read()  
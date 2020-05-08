
def file_initial_read(inputfile):
    f= open(inputfile,'r')
    #'/Users/bayyanap/Documents/python/inputfile.txt'
    contents =f.read()
    return contents
 
def split_content(contents):
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
    return input_list,contents
     
      
def merge(input_list,contents):
    #data_list =[]
    #for inpdata in input_list:
    #     inputval = input(f"Enter an {inpdata}")
    #     data_list.append(inputval)
    contents = contents.format(*input_list)
    return contents   
    



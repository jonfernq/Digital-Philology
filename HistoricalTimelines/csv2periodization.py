# csv2periodization.py - 

# create a tree-like periodization from a CSV file

import csv 
   
def make_new_record(line):
    # turns string node id: '2.1.4') 
    # into separate list elements: [2,1,4] 
    node = line[0].split('.')
    w = [0] * 4 
    last_id = 0
    if len(node) > 0: 
        w[0] = int(node[0])
        last_id = w[0]          
    if len(node) > 1: 
        w[1] = int(node[1])  
        last_id = w[1]                 
    if len(node) > 2: 
        w[2] = int(node[2]) 
        last_id = w[2] 
    if len(node) > 3: 
        w[3] = int(node[3]) 
        last_id = w[3]           
    line[1] = str(last_id).zfill(2) + ' ' + line[1]          
    z = w + line      
    return z 
    
def Sort(sub_li):
    # sort nodes by first field 
	sub_li.sort(key = lambda x: x[0])
	return sub_li
    
def chop_off_last(node):
     # get parent by chopping off last element in node id
     # example: 3.2.1 --> 3.2      
     ids = node.split('.') 
     ids.pop() # remove last element in list  
     if len(ids) > 0:     
         return '.'.join(ids) 
     else:
         return 'root' 



def main():

    csvfile = 'rajadhirat_toc_2.csv'
    
    # redb from csv file 
    with open(csvfile, mode ='r', encoding='utf-8')as file: 
      csvFile = list(csv.reader(file, delimiter='\t'))  

    new_tree = [] 
    csvFile.pop(0)  #  pop off first column header record 
    for line in csvFile:
        new_record = make_new_record(line) # turns string node id into separate list elements
        new_tree.append(new_record)        # append node record to nodes of tree list 
        #print(new_record) 
    # print(str(new_tree))     

    sorted_tree = Sort(new_tree)  # sort node records into levels, level 1 nodes, then level 2, etc 
    level1 = list(filter(lambda x: x[0] != 0 and x[1] == 0 and x[2] == 0 and x[3] == 0, sorted_tree))  
    level2 = list(filter(lambda x: x[0] != 0 and x[1] != 0 and x[2] == 0 and x[3] == 0, sorted_tree))  
    level3 = list(filter(lambda x: x[0] != 0 and x[1] != 0 and x[2] != 0 and x[3] == 0, sorted_tree)) 
    level4 = list(filter(lambda x: x[0] != 0 and x[1] != 0 and x[2] != 0 and x[3] != 0, sorted_tree))       
    print('\nlevel1:',level1) 
    print('\nlevel2:',level2)  
    print('\nlevel3:',level3)    
    print('\nlevel3:',level4)

    print("BEGIN TO BUILD TREE")     
    from treelib import Node, Tree
    tree = Tree()
    tree.create_node("Rajadhiraj Epic", "root")  # topmost 'root' node
    
    import sys 
    original = sys.stdout
    sys.stdout = open('rajadhirat_periodization.txt', 'w', encoding='utf-8') 
    
    # create_node(n[5]= child node description, n[4]=child node id, parent node id)  
    for n in level1:
        tree.create_node(n[5], n[4], parent="root")

    for n in level2:
        tree.create_node(n[5], n[4], parent=chop_off_last(n[4]))       
    
    for n in level3:
        tree.create_node(n[5], n[4], parent=chop_off_last(n[4]))       
    
    for n in level4:
        tree.create_node(n[5], n[4], parent=chop_off_last(n[4]))   
        
    tree.show()  
    
if __name__=="__main__":
    main()




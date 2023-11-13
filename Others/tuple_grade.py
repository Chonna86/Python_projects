def split_list(grade):
    list_grade1 = []
    list_grade2 = [] 
    final_tuple = (list_grade1,list_grade2)
    if len(grade) !=0:
        middle_value = sum(grade)//len(grade)
    for g in grade :
        if g <=  middle_value :
            list_grade1.append(g)
            
        elif g > middle_value :
            list_grade2.append(g)
    return final_tuple
print(split_list([34, 78, 87 ,97, 101,165]))
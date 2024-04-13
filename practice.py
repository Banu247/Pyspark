def sort_based_on_val(dictionary):
    values =list(dictionary.items())
    for i in range(0,len(values)):
        for j in range(i+1,len(values)):
            if (values[i][1])>(values[j][1]):

                values[i],values[j]=values[j],values[i]
            
        

    return dict(values)


print(sort_based_on_val({'a': 10, 'b': 3, 'c': 5}))

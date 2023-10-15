articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

finall_list = []
def find_articles(key, letter_case=False):
    
    
    for i in articles_dict :
        
        for k,v in i.items():
            
            if str(key) in i.items() :
                finall_list.append(i)
            
    return finall_list
print(find_articles("2021", letter_case=False))
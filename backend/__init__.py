def process_user_query(query_string):
    result=[]
    new_list= query_string.split()
    for i in new_list:
        result.append('Hi! ' + i)

    return result

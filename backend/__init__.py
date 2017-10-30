def process_user_query(query_string):
    result=[]
    word_list= query_string.split()
    for word in word_list:
        if word[0].isupper()==True:
            result.append('Hola! ' + word +' como estas?')
    return result

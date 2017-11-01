
import pandas as pd

def process_user_query(query_string):
    x1= pd.ExcelFile('Sample - Superstore Sales (Excel).xls')
    work=(x1.parse('Orders')).set_index('Row ID')
    iterlist=[]
    consumer=0
    corporate=0
    home_office=0
    small_business=0
    summation=0
    if query_string=='Losses':
        for profits in work['Profit']:
            if profits<=0:
                iterlist.append(profits)
            summation=sum(iterlist)
        return summation
    elif query_string=='Sales Max':
        for sales_number in work['Sales']:
            iterlist.append(sales_number)
        maximum_sales=max(iterlist)
        return maximum_sales

    elif query_string=='Businesses served':
        for business in work['Customer Segment']:
            if business == 'Consumer':
                consumer=consumer+1
            elif business =='Corporate':
                corporate= corporate+1
            elif business=='Home Office':
                home_office=home_office+1
            elif business == 'Small Business':
                small_business=small_business+1
        return {'Consumer':consumer, 'Corporate':corporate,'Home Office':home_office,'Small Business':small_business}
    elif query_string=='Revenue':
        for profit in work['Profit']:
            summation+=profit
        return summation
    else:
        return 'Search not found'


#print(process_user_query('Losser'))
#print(process_user_query('Revenue'))

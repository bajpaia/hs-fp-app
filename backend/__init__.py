
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
    sales=[]
    prices=[]
    products=[]
    revenue_con=0
    rev_corp=0
    rev_sma=0
    rev_hmo=0
    profit=[]
    region=[]
    priceavg=0
    for regions in work['Region']:
        region.append(regions)
    if query_string=='Losses':
        for profits in work['Profit']:
            if profits<=0:
                iterlist.append(profits)
            summation=sum(iterlist)
        return 'Losses in all regions '+str(summation)

    elif query_string=='Sales':
        for sales_number in work['Sales']:
            iterlist.append(sales_number)
        maximum=max(iterlist)
        for i, sales_number in enumerate (work['Sales']):
            if sales_number== maximum:
                region_of_sales= work['Region'][i+1]
                product= work['Product Name'][i+1]
                product_cat= work['Product Category'][i+1]

        return str(max(iterlist)), 'The region '+region_of_sales,'The product '+product,'in the ctaegory of '+product_cat

    elif query_string=='Businesses served':
        for i,business in enumerate(work['Customer Segment']):
            if business == 'Consumer':
                consumer=consumer+1
                revenue_con+= work['Profit'][i+1]
            elif business =='Corporate':
                corporate= corporate+1
                rev_corp+=work['Profit'][i+1]
            elif business=='Home Office':
                home_office=home_office+1
                rev_hmo+=work['Profit'][i+1]
            elif business == 'Small Business':
                small_business=small_business+1
                rev_sma+=work['Profit'][i+1]
        consumer= 'The number '+ str(consumer)

        revenue_con='The Revenue '+str(int(revenue_con))

        return {'Consumer':[consumer,revenue_con], 'Corporate':[corporate,int(rev_corp)],'Home Office':[home_office,int(rev_hmo)],'Small Business':[small_business,int(rev_sma)]}

    elif query_string=='Revenue':
        for profit in work['Profit']:
            summation+=profit
        return 'The Revenue for all products in all regions is '+ str(summation)

    elif query_string in region:
        for i,region in enumerate(work['Region']):
            if region==query_string:
                sales.append(work['Sales'][i+1])#i+1 to go to the next row as rowid is excel row no +1
                profit.append(work['Profit'][i+1])
                if work['Profit'][i+1]<=0:
                    iterlist.append(work['Profit'][i+1])

        max_sales= max(sales)
        min_sales=min(sales)
        profits=sum(profit)
        losses=sum(iterlist)
        for i,region in enumerate(work['Region']):
            if region==query_string:
                if max_sales==work['Sales'][i+1]:
                    pop_prod= work['Product Name'][i+1]
                    prro_add= work['Province'][i+1]

                elif min_sales==work['Sales'][i+1]:
                    unpop_prod=work['Product Name'][i+1]

        return 'The best selling product for the region is '+pop_prod+ ' with '+ str(int(min_sales))+ ' sales,\n generating '+str(profits) +' in revenue, in the province of '+prro_add+'.\n The lowest selling product is the '+unpop_prod+ ' with ' + str(int(min_sales))+' sales, with a loss of \n'+str(int(losses))
    else:
        return 'Error 404: The thing you are looking for does not exist or has not been coded in yet'

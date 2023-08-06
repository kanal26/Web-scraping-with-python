# importing requried libararies
import requests
from lxml import html
from pymongo import MongoClient

def insert_data_many(main_list):
    
    myclient = MongoClient("mongodb://localhost:27017/")
    db = myclient["Test_data"]
    collection = db["zaubacorpcom_url"]
    
    collection.create_index("Data_url", unique=True)
    try:
        # Insert the document using insert_many
        collection.insert_many(main_list,ordered=False)
    except:
        print("url is alredy available")
    
    print("<< == Successfully Inserted data == >>")
    myclient.close()


def get_data(totāl̥_page,main_list):
    for i in range(1,totāl̥_page):
        product_url = "https://www.zaubacorp.com/company-list/p-{}-company.html".format(str(i))
        
        cookies = {
            'drupal.samesite': '1',
            '_ga': 'GA1.2.1456870799.1691131005',
            '_gid': 'GA1.2.306500852.1691131005',
            '__stripe_mid': '8fa9ae8d-b779-4bb3-8724-21d1a4b58648c78552',
            '__stripe_sid': 'fdaa714d-bbbe-4bdc-a81e-17f23791e473ab6145',
            '__gads': 'ID=104255b865e28525-221b82f75480008d:T=1691131005:RT=1691147095:S=ALNI_MYx6FcuCPqNJob55XJs9AXiyz_x0Q',
            '__gpi': 'UID=00000c26e196b7b9:T=1691131005:RT=1691147095:S=ALNI_Mbxz5y-SGzqF3eDmkXi7_cI2PaX1g',
            '_gali': 'block-system-main',
            '_gat': '1',
            '_ga_VVR3BV80B8': 'GS1.2.1691146429.2.1.1691147200.60.0.0',
        }
        
        headers = {
            'authority': 'www.zaubacorp.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,gu;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'drupal.samesite=1; _ga=GA1.2.1456870799.1691131005; _gid=GA1.2.306500852.1691131005; __stripe_mid=8fa9ae8d-b779-4bb3-8724-21d1a4b58648c78552; __stripe_sid=fdaa714d-bbbe-4bdc-a81e-17f23791e473ab6145; __gads=ID=104255b865e28525-221b82f75480008d:T=1691131005:RT=1691147095:S=ALNI_MYx6FcuCPqNJob55XJs9AXiyz_x0Q; __gpi=UID=00000c26e196b7b9:T=1691131005:RT=1691147095:S=ALNI_Mbxz5y-SGzqF3eDmkXi7_cI2PaX1g; _gali=block-system-main; _gat=1; _ga_VVR3BV80B8=GS1.2.1691146429.2.1.1691147200.60.0.0',
            'referer': 'https://www.zaubacorp.com/company-list/p-1-company.html',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        }
        
        response = requests.get(product_url,headers= headers,cookies =cookies)
        tree = html.fromstring(response.content) 
        
        data = tree.xpath("//table[@class='table table-striped col-md-12 col-sm-12 col-xs-12']/tr")
        main_list = []

        for j in range(1,(len(data)+1)):

            listOfGlobals = {'Data_url':'','page_product_url':'','Status':''}

            Data = tree.xpath("//table[@class='table table-striped col-md-12 col-sm-12 col-xs-12']/tr[{}]/td//text()".format(j))

            Data_url = tree.xpath("//table[@class='table table-striped col-md-12 col-sm-12 col-xs-12']/tr[{}]/td/a/@href".format(j))[0]
            listOfGlobals['Data_url'] = Data_url    
            listOfGlobals['page_product_url'] = product_url
            listOfGlobals['Status'] = '0'
            main_list.append(listOfGlobals)
           
        insert_data_many(main_list)
       
if __name__ == "__main__":
    totāl̥_page = int(13334)
    main_list =[]
    get_data(totāl̥_page,main_list)
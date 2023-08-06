# importing requried libararies
import requests
from lxml import html
from pymongo import MongoClient
import sys
from multiprocessing import Pool

def update_data(product_url):
    myclient = MongoClient("mongodb://localhost:27017/")
    db = myclient["Test_data"]

    url_collection = db["zaubacorpcom_url"]
    query = {"Data_url": str(product_url)}
    
    update = {"$set": {"Status": "1"}}
    # Update a single document that matches the query
    result = url_collection.update_one(query, update)
    
    # Print the result
    print("Modified document count:", result.modified_count)
    print("<< == Successfully updated data == >>")
    
    myclient.close()

def insert_data(listOfGlobals):
    
    myclient = MongoClient("mongodb://localhost:27017/")
    
    db = myclient["Test_data"]
    collection = db["zaubacorpcom_data"]
    
    result = collection.insert_one(listOfGlobals)
    print("<< == Successfully Inserted data == >>")
    myclient.close()
    

def get_product_data(urlList):
    product_url = urlList['Data_url']

    print("product_url == >>",product_url)
    
    listOfGlobals = {'product_url':'','CIN':'','Company_Name':'','Company_Status':'','RoC':'','Registration_Number':'','Company_Category':'','Company_Sub_Category':'','Class_of_Company':'','Date_of_Incorporation':'','Age_of_Company':'','Activity':'','Number_of_Members':''}
   
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
    print(response)
    
    tree = html.fromstring(response.content) 
           
    Data = tree.xpath("//div[@class='col-lg-12 col-md-12 col-sm-12 col-xs-12']/h4[contains(text(),'Company Details')]//following-sibling::table/tbody/tr/td/p//text()")
    
    listOfGlobals['product_url'] = product_url                                                    
    try:
        CIN = product_url.split('/')[-1]
    except:
        CIN = ''
    listOfGlobals['CIN'] = CIN
    
    try:
        Company_Name = Data[1]
    except:
        Company_Name = ''
    listOfGlobals['Company_Name'] = Company_Name
    
    try:
        Company_Status = Data[3]
    except:
        Company_Status = ''
    listOfGlobals['Company_Status'] = Company_Status

    try:
        RoC = Data[5]
    except:
        RoC = ''
    listOfGlobals['RoC'] = RoC

    
    try:
        Registration_Number = Data[7]
    except:
        Registration_Number = ''
    listOfGlobals['Registration_Number'] = Registration_Number

    
    try:
        Company_Category = Data[9]
    except:
        Company_Category = ''
    listOfGlobals['Company_Category'] = Company_Category

    
    try:
        Company_Sub_Category = Data[11]
    except:
        Company_Sub_Category = ''
    listOfGlobals['Company_Sub_Category'] = Company_Sub_Category

    try:
        Class_of_Company = Data[13]
    except:
        Class_of_Company = ''
    listOfGlobals['Class_of_Company'] = Class_of_Company

    
    try:
        Date_of_Incorporation = Data[15]
    except:
        Date_of_Incorporation = ''
    listOfGlobals['Date_of_Incorporation'] = Date_of_Incorporation

    
    try:
        Age_of_Company = Data[17]
    except:
        Age_of_Company = ''
    listOfGlobals['Age_of_Company'] = Age_of_Company

    
    try:
        Activity = Data[19] + Data[20] + Data[21]
        
    except:
        Activity = ''
    listOfGlobals['Activity'] = Activity

    
    try:
        Number_of_Members = Data[23]
    except:
        Number_of_Members = ''
    listOfGlobals['Number_of_Members'] = Number_of_Members

   
    insert_data(listOfGlobals)
    update_data(product_url)
       
def main(from_c,to_c):

    myclient = MongoClient("mongodb://localhost:27017/")
    db = myclient["Test_data"]

    url_collection = db["zaubacorpcom_url"]
    myquery = { "Status":"0" }

    mydoc = url_collection.find(myquery, {"Data_url": 1})
    results = list(mydoc)

    #multi instance code
    document_count = len(results)
    print(document_count)

    top_index = (to_c-1)*int((document_count/from_c))
    end_index = top_index + int((document_count/from_c))
    print((document_count, top_index, end_index))

    urlList = [row for row in results[top_index:end_index]]
    for x in urlList:
        p = Pool(int(sys.argv[3]))
        p.map(get_product_data, urlList)
    
    myclient.close()

if __name__ == "__main__":
  main(int(sys.argv[1]), int(sys.argv[2]))
        
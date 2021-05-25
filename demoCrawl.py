print("Version 0.0.1")
print("==============================")
#Input and Select
bankName = input("Nhap ten ngan hang ban muon kiem tra ty gia (Chu thuong ghi lien khong dau, VD: bidv, vietcombank,..): ")
print("Ban da chon ngan hang " + bankName + ". Luu output sau thanh file [ten file cua ban].html va mo no bang web browser hoac excel.")

#Crawl
import requests
#https://portal.vietcombank.com.vn/Personal/TG/Pages/ty-gia.aspx?devicechannel=default
response = requests.get("https://tygia.vn/ty-gia/" + bankName)
#print(response)
#print(response.content)

#Separate
from bs4 import BeautifulSoup
dataTree = BeautifulSoup(response.content, "html.parser")
#print(dataTree)
dataFil = dataTree.findAll('table', class_='table table-bordered table-hover')
print(dataFil)



#--------BS Objects--------------------
#Tag
#Name
#Attributes
#Multi-values Properties
#NavigableString
#-------Control path inside DTree------
#.content and .children
#.string, .strings and .stripped strings
#.parent and .parents
#.next_sibling and .previous_sibling
#.next_sinlings and .previous_siblings
#.next_element and .previous_element
#.next_elements and .previous_elements
#DTree-searching
# Filter
###String
###Regular Expression
###List
###True
###Function
# findAll()
###Name Argument
###Keyword Argument 
###searching by CSS class
###String Argument
###Limit Argument
###Recursive Argument
#find()
#find_<....>()
#CSS Selector
#Edit and encapsulation
#Output Handle and Endcoding
#Debug and tests
#-----------------------------------
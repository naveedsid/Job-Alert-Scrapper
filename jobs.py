from bs4 import BeautifulSoup
import requests
url = "https://jobsalert.pk/pakistan-national-shipping-corporation-jobs-online-form/63573"
response = requests.get(url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
posted_date = []
post_title = []
newspaper = []
last_date = []

#Post Company Logo
sin_pos_logo = soup.select('.container-fluid .freelance-image img')[0]
print("Post Company Logo: "+sin_pos_logo.get('data-lazy-src'))

#Post Main Title
sin_pos_main_title = soup.select('.header-details h1')[0]
print("Post Main Title: "+sin_pos_main_title.string)

# Post Location
sin_pos_main_location = soup.select('.header-details p')[1]
print("Job Offer Company: "+sin_pos_main_location.get_text())

# Post Vacancies
sin_pos_main_vacancies = soup.select('.header-details ul li')[0]
print("Post Vacancies Count: "+sin_pos_main_vacancies.get_text())


# Right Side Details
# Post Availability
sin_pos_main_availibility = soup.select('.right-side-detail ul li')[0]
print("Availability: "+sin_pos_main_availibility.get_text())

# Post Expererience
sin_pos_main_experience = soup.select('.right-side-detail ul li')[1]
print("Post Experience: "+sin_pos_main_experience.get_text())

# Post Region
sin_pos_main_region = soup.select('.right-side-detail ul li')[2]
print("Post Region: "+sin_pos_main_region.get_text())

# Post Education
sin_pos_main_education = soup.select('.right-side-detail ul li')[3]
print("Post Education: "+sin_pos_main_education.get_text())





# Post Title
sin_pos_title = soup.select('.stickyrow .stickycol9 h2')[0]
print("Post Title: "+sin_pos_title.string)

# Category
sin_pos_cat = soup.select('.stickyrow .post-meta div:nth-child(2) span a')[0]
print("Categories: "+sin_pos_cat.string)


# Offered Salary
sin_pos_salary = soup.select('.stickyrow .ms-4 .key-field')[0]
print("Post Estimated Salary: "+sin_pos_salary.string)

sin_pos_age = soup.select('.stickyrow .ms-4 .key-field')[1]
print("Post Required Age: "+sin_pos_age.string)

#sin_pos_gender = soup.select('.stickyrow .ms-4 .key-field')[2]
#print(sin_pos_gender.string)

sin_pos_designation = soup.select('.stickyrow .ms-4 .key-field')[4]
print("Post Designation: "+sin_pos_designation.get_text())

#Last Date
#sin_pos_last_date = soup.select('.lastdate span')[1]
#print("Post Late Date: "+sin_pos_last_date.string)

# Table of Content Start Here
#for sin_pos_para in soup.select('.pcontent p')[1:]:
#    print(sin_pos_para.get_text())


if "Table of Conte" in str(soup.select('.pcontent')):
    print(soup.select('.pcontent ul')[1].get_text())
else:
    print(soup.select('.pcontent ul')[0].get_text())


#Iterate on all elements and identify them first
# v_postions = soup.select('.pcontent *')
# for index, vaccant_position in enumerate(v_postions):
#     if "Vacant" in str(vaccant_position):   
#         print(soup.select('.pcontent p')[index+1])
        #print(vaccant_position)
        #print(index)


#How to Apply
sin_pos_how_to_apply = soup.select('.pcontent ol')[0]
print(sin_pos_how_to_apply.get_text())

for sin_para in soup.select('.pcontent h5 ~ p'):
    #print(sin_para)
    if "Last Date" in str(sin_para):
        only_last_date = sin_para.get_text()
        print(only_last_date)
    elif "To Apply Online" in str(sin_para):
        only_apply_link = sin_para.select('a')[0].get('href')
        print("Link For Online Apply: "+only_apply_link)
    elif "Address" in str(sin_para):
        only_address = sin_para.get_text()
        print(only_address)
    elif "Advertisement Image" in str(sin_para):
        only_link_ad_img = sin_para.select('a')[0].get('href')
        print("Advertisement Image Link: "+only_link_ad_img)
    elif "Application Form Will" in str(sin_para):
        print("Application Form will be available soon")
    elif "Application Form" in str(sin_para):
        only_app_form_link = sin_para.select('a')[0].get('href')
        print("Application Form Link: "+only_app_form_link)
    else:
        print(sin_para)

inner_response = requests.get(only_link_ad_img)
innerhtmlcontent = inner_response.content
innersoup = BeautifulSoup(innerhtmlcontent, 'html.parser')


inner_ad_img = innersoup.select('.pcontent img')
print(inner_ad_img[0].get('data-lazy-src'))



#All P tag right after h5
# print(len(soup.select('.pcontent h5 ~ p')))

#Extract Only Text direct from element
# only_last_date = sin_para.find(string=True, recursive=False)


# sin_pos_lower_paras = soup.select('.pcontent p')[-4:]
# print(sin_pos_lower_paras)
# print(len(sin_pos_lower_paras))


#Lower Last Date
# sin_pos_lower_last_date = soup.select('div.pcontent > p:nth-child(13) > strong')[0]
# if "Last Date To Apply" in str(sin_pos_lower_last_date):
#     print(sin_pos_lower_last_date.find(string=True, recursive=False))
# else:
#     print("Lower Last Date is not found...!")



# Short Method for Extracting Table Data
# for sin_tr in soup.select('table.table-hover-jobs tr'):
#     for sin_td in sin_tr:
#         print(sin_td, end='')
    



# Main Loop of Automate Whole Process
# for sin_tr in soup.select('table.table-hover-jobs tr'):
#     if sin_tr.find('th'):
#         continue
#     # Extracting posting date
#     job_date = sin_tr.select('td:nth-child(1)')
#     print(job_date[0].string)
    
#     # Extracting post title
#     job_title = sin_tr.select('td:nth-child(2) a')
#     print(job_title[0].string)
#     print(job_title[0].get('href'))
#     # Call here function which extract a single post complete content

#     # Extracting post newspaper
#     job_newspaper = sin_tr.select('td:nth-child(3) span')
#     print(job_newspaper[0].string)

#     # Extracting post last date
#     job_last_date = sin_tr.select('td:nth-child(4) i')
#     print(job_last_date[0].string)
#     print('\n')
    
    



    
    

#bulk_jobs_posts = soup.select('table.table-hover-jobs tr')
#print(bulk_jobs_posts)



#job_tbl = soup.find_all('table', class_='job-ads-list')
#add_headers = soup.select('.table-hover-jobs')
#print(add_headers)

#for single_header in add_headers:
#    print(single_header)

#print(link.get('src'))

#print(soup.find(id='sample-id'))

# for link in soup.find_all('a'):
#         print(link.get('href'))



#print(soup.prettify())


#soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
#print(soup.prettify())
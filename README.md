# Intelligent Medical Information Website

#### Introduction
This project is an intelligent medical information website. The medical website provides a convenient and fast way for people to obtain knowledge about health, diseases, medical diagnosis, and drug information. People can search for health-related information on the website anytime and anywhere, helping them better understand their health status and options. The medical website can provide rich health education resources, conveying correct medical knowledge and preventive methods to the public, helping to reduce the occurrence and spread of diseases, and improving people's health awareness. The medical website can offer online consultation and inquiry services, allowing patients to communicate with doctors remotely and obtain preliminary diagnoses and suggestions, thus reducing the time and cost of medical treatment. The medical website can integrate medical resources, including information on hospitals, clinics, and pharmacies, helping patients better choose and locate suitable medical institutions and services. This project is aimed at the general public, providing them with a variety of medical-related assistance.
#### Instructions

1、First, clone the repository: git clone https://gitee.com/cgnnnn/medical.git

2、Import the dependency libraries according to requirement.txt

3、Create a schema in MySQL, assuming its name is medical, and set the character set to UTF-8

4、Change the MySQL and Neo4j information in local_settings.py

5、Run the Neo4j files in neo4j_data to complete the Neo4j data import
Neo4j data Baidu Cloud link:

链接：https://pan.baidu.com/s/1czk-d4CU2n-gCmGcbQa9UQ?pwd=70q4 

提取码：70q4 

--来自百度网盘超级会员V6的分享

6、Execute the following code in the terminal to complete the model migration:

python manage.py makemigrations

python manage.py migrate

7、Execute insert_data.py in utils/data_importer (change the database information in conn to your own) to import data into the MySQL database and complete data initialization

8、Run the following command in the terminal to create a Django super administrator:

python manage.py createsuperuser

9、Run the Django project and visit 127.0.0.1:8000/ckeditor/upload/, log in as an administrator (CKEditor requires administrator privileges to upload images to the Django server backend)

10、Browse your website

#### Demonstration
https://www.bilibili.com/video/BV12F411m7eA/?spm_id_from=333.999.0.0

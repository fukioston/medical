# 智慧医疗信息网站

#### 介绍
本项目是智慧医疗信息网站。 医疗网站为人们提供了方便快捷的途径，可以获取关于健康、疾病、医疗诊疗、药物信息等方面的知识。人们可以随时随地在网站上寻找健康相关信息，帮助他们更好地了解自己的健康状况和选项。医疗网站可以提供丰富的健康教育资源，向公众传递正确的医疗知识和预防方法，有助于减少疾病的发生和传播，提高人们的健康意识。 医疗网站可以为用户提供在线咨询和问诊服务，使患者能够远程与医生交流，获取初步诊断和建议，从而减少就医的时间和成本。医疗网站可以整合医疗资源，包括医院、诊所、药店等信息，帮助患者更好地选择和定位合适的医疗机构和服务。
本项目面向社会群众，为社会群众提供众多医疗方面的相关帮助。
#### 使用说明

1、首先克隆库：git clone https://gitee.com/cgnnnn/medical.git  

2、根据requirement.txt导入依赖库

3、在MySQL中创建schema，假设其名字为medical，字符集设为utf-8

4、在local_settings.py内更改MySQL信息和neo4j信息。

5、运行neo4j_data中的neo4j文件完成neo4j数据导入
neo4j_data百度网盘链接：

链接：https://pan.baidu.com/s/1czk-d4CU2n-gCmGcbQa9UQ?pwd=70q4 

提取码：70q4 

--来自百度网盘超级会员V6的分享

6、在终端执行如下代码完成model迁移

python manage.py makemigrations

python manage.py migrate

7、执行utils/data_importer下的insert_data.py（把conn内的数据库信息改成自己的）使数据导入MySQL数据库,完成数据初始化

8、文件在终端输入：python manage.py createsuperuser 以创建django超级管理员

9、运行django项目，访问127.0.0.1:8000/ckeditor/upload/，登录管理员（CKEditor上传图片到Django服务器后台需要管理员权限）

10、浏览你的网站吧

#### 使用效果
https://www.bilibili.com/video/BV12F411m7eA/?spm_id_from=333.999.0.0

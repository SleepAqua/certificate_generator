# 证书生成器
# Certificate Generator

## 描述
## Description
**这是一个可以自动生成许多许多证书文件，然后把他们分别发送给正确的人的程序~**
**This is a program which can automatically generate many certificate files (based on "template.docx") in doc and pdf, then send them all to the corresponding persons due to the configurations given in "receivers.xlsx" by email (mail configuration given in "mail_info.json")**

## 要求
## Prerequisities
* Python3
* Carefulness

## 使用方法
## Usage
将配置文件修改好后，直接双击"clickme.bat"就好了 （Linux用户请双击"clickme.sh"哦）
After the configurations are set, double click "clickme.bat" (for Windows users) or "clickme.sh" (for Linux users). 
Yes, just simple like this!

## 配置
## Configuration
* "template.docx": 保证字体不是临时修改的，要直接修改字体样式!
* "template.docx": make sure the fonts in your template are not *temporary*, which means you should always set the fonts themselves rather than selecting the words and modify them temporarily.
* "receivers.xlsx": 前三列必须是 编号、姓名、邮箱地址！
* "receivers.xlsx": make sure the first three columns in your receivers table are respectively ID, NAME, and EMAIL ADDRESS. ID and NAME will be put on the generated certificate and the EMAIL ADDRESS will receive the corresponding certificate.
* "mail_info.json": 可能不明白的应该只有hosts了吧，如果不明白，请查看[如何查看各种邮箱的服务SMTP/POP3地址及端口号](https://jingyan.baidu.com/article/647f0115b78f8d7f2148a8e8.html)
* "mail_info.json": if you do not know what "host" mean, please check [如何查看各种邮箱的服务SMTP/POP3地址及端口号](https://jingyan.baidu.com/article/647f0115b78f8d7f2148a8e8.html)
* 最后一步!!! 告诉程序应该在第几行修改编号和姓名，直接修改clickme文件即可
* The last step!!! tell the program where to modify the ID and the NAME: which row are they in? Modify this on "clickme.bat/sh", the default value for ID and NAME are respectively 12 and 1 (well, since we always put certificate id on the top).

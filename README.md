# Certificate Generator

## Description
**This is a program which can automatically generate many certificate files (based on "template.docx") in doc and pdf, then send them all to the corresponding persons due to the configurations given in "receivers.xlsx" by email (mail configuration given in "mail_info.json")**

## Prerequisities
* Python3
* Carefulness

## Usage
After the configurations are set, double click "clickme.bat" (for Windows users) or "clickme.sh" (for Linux users). 
Yes, just simple like this!

## Configuration
* "template.docx": make sure the fonts in your template are not *temporary*, which means you should always set the fonts themselves rather than selecting the words and modify them temporarily.
* "receivers.xlsx": make sure the first three columns in your receivers table are respectively ID, NAME, and EMAIL ADDRESS. ID and NAME will be put on the generated certificate and the EMAIL ADDRESS will receive the corresponding certificate.
* "mail_info.json": if you do not know what "host" mean, please check [如何查看各种邮箱的服务SMTP/POP3地址及端口号](https://jingyan.baidu.com/article/647f0115b78f8d7f2148a8e8.html)
* The last step!!! tell the program where to modify the ID and the NAME: which row are they in? Modify this on "clickme.bat/sh", the default value for ID and NAME are respectively 7 and 1 (well, since we always put certificate id on the top).
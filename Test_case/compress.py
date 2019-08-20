#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2019/1/25
#!/usr/bin/env python
#coding:utf-8

import zipfile,os


#把整个文件夹内的文件打包成zip文件（包括压缩路径下的字文件夹的文件）
def compress(get_files_path, set_files_path):
    f = zipfile.ZipFile(set_files_path , 'w', zipfile.ZIP_DEFLATED )
    for dirpath, dirnames, filenames in os.walk( get_files_path ):
        fpath = dirpath.replace(get_files_path,'') #注意2
        fpath = fpath and fpath + os.sep or ''     #注意2
        for filename in filenames:
            f.write(os.path.join(dirpath,filename), fpath+filename)
    f.close()
    print ("compress operate success")

if __name__=='__main__':
    get_files_path = "D:\Page_Object\Test_reports\\report\html" #需要压缩的文件夹
    set_files_path = "D:\Page_Object\Test_reports\\report\html456.zip" #存放的压缩文件地址(注意:不能与上述压缩文件夹一样)
    compress(get_files_path, set_files_path)
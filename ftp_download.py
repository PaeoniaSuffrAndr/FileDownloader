#encoding=utf-8
__author__ = 'wentao'

import urllib
from log import LOG
import os

log = LOG(1024*1024*2)
log.info('任务开始！')
log.info('pid:%s' % os.getpid())
# print(u'任务开始！')
try:
    file = open('./ftp.list')  # 打开ftp列表文件
    while True:
        url = file.readline()  # 读取一行
        if not url:  # 如果读取失败
            break  # 结束循环
        url = url.replace('\n', '')  # 处理行末换行符
        log.info('正在分析地址[%s]' % url)
        # print(u'正在分析地址[%s]' % url)
        try:
            part_path = os.path.join(os.getcwd(),'data\\internettv')  # 主目录
            #index = url.find('/', 6)  # 获取目录开始位置
            #fileUrl = url[index:]  # 获取完整路径
            fileUrl = url
            url = 'ftp://IPTV:8mmY15Gp@10.1.201.172' + url
            if fileUrl.find('/', 0) != 0:
                fileUrl = '/' + fileUrl
            dir_file = os.path.split(fileUrl)  # 切分目录和文件名
            dirname = part_path + dir_file[0]  # 拼接目录名
            filename = dir_file[1]  # 取到文件名
            savepath = '%s/%s' % (dirname, filename)
            if not os.path.exists(dirname):  # 判断目录是否存在
                log.info('目录[%s]不存在，正在创建目录！' % dirname)
                # print(u'目录[%s]不存在，正在创建目录！' % dirname)
                os.makedirs(dirname)  # 创建目录
            if os.path.exists(savepath):
                log.info('文件[%s]已存在，自动跳过！' % savepath)
                # print(u'文件[%s]已存在，自动跳过！' % savepath)
            else:
                log.info('正在下载[%s]' % url)
                # print(u'正在下载[%s]' % url)
                log.info('将保存至[%s]' % savepath)
                # print(u'将保存至[%s]' % savepath)
                try:
                    urllib.urlretrieve(url, savepath)  # 下载文件到对应目录
                    log.info('下载完毕！')
                    # print(u'下载完毕！')
                except Exception,e:
                    log.info('下载文件[%s]错误：%s' % (url, e))
                    # print('下载文件[%s]错误：%s' % (url, e))
        except Exception,e:
            log.info('分析地址[%s]错误：%s' % (url, e))
            # print('分析地址[%s]错误：%s' % (url, e))
    file.close()
except Exception,e:
    log.info('文件打开失败：%s' % e)
    # print('文件打开失败：%s' % e)
log.info('任务结束！')
# print(u'任务结束！')
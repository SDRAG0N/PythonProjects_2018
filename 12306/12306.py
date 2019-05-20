# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Arvin'
import requests
from settings import *
import cons
import user
import codes
import time
import urllib
import re

req = requests.Session()

dict_station = {}
for i in cons.station.split('@'):
    tmp_list = i.split('|')
    #print(tmp_list)
    if len(tmp_list) > 2:
        dict_station[tmp_list[1]] = tmp_list[2]
#print(dict_station)

from_station = dict_station[FROM_STATION]
to_station = dict_station[TO_STATION]
#print(from_station,to_station)

def queryTicket():#query_ticket
    response = req.get('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(TRAIN_DATE, from_station, to_station))
    result = response.json()
    print(result)
    return result['data']['result']

def login():
    print('正在加载验证码图片..')
    response = req.get('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.4626756029297192')
    codeImg = response.content
    fn = open('code.png', 'wb')
    fn.write(codeImg)
    fn.close()
    print('正在识别验证码...')
    data = {
        'answer':codes.get_code(),#坐标型验证码
        'login_site':'E',
        'rand':'sjrand'
            }
    response = req.post('https://kyfw.12306.cn/passport/captcha/captcha-check', data=data, headers=cons.headers)
    result = response.json()
    if result['result_code'] != '4':
        time.sleep(3)
        login()
        return
    data = {
        'username':user.user,
        'password':user.pwd,
        'appid':'otn'
    }
    response = req.post('https://kyfw.12306.cn/passport/web/login', data=data, headers=cons.headers)
    response.encoding = 'utf-8'
    print(response.text)
    result = response.json()
    print(result)
    if result['result_code'] != 0:
        login()
        return
    response = req.post('https://kyfw.12306.cn/otn/login/userLogin', data={'_json_att':''}, headers=cons.headers)
    print(response.url)
    #print(response.text)
    response = req.post('https://kyfw.12306.cn/passport/web/auth/uamtk', data={'appid':'otn'}, headers=cons.headers)
    tk = response.json()['newapptk']
    response = req.post('https://kyfw.12306.cn/otn/uamauthclient', data={'tk':tk}, headers=cons.headers)
    print(response.text)
    print('登录成功')

def order(secretStr):
    response = req.get('https://kyfw.12306.cn/otn/index/initMy12306', headers=cons.headers)
    print(response.url)
    #return
    #下单第一个请求
    response = req.post('https://kyfw.12306.cn/otn/login/checkUser', data={'_json_att':''}, headers=cons.headers)
    response.encoding = 'utf-8'
    print(response.text)
    result = response.json()['data']['flag']
    if not result:
        print('下单第一步请求失败!..')
        return
    print('下单第一步请求成功!..')
    secretStr = urllib.parse.unquote(secretStr)
    print(secretStr)
    data = {
        'secretStr':secretStr,
        'train_date':TRAIN_DATE,
        'back_train_date':BACK_TRAIN_DATE,
        'tour_flag':'dc',
        'purpose_codes':'ADULT',
        'query_from_station_name':FROM_STATION,
        'query_to_station_name':TO_STATION,
        'undefined':''
    }
    # 下单第二个请求
    response = req.post('https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest', data=data, headers=cons.headers)
    print(response.text)
    response.encoding = 'utf-8'
    result = response.json()['status']
    if not result:
        print('下单第二步请求失败!')
        return
    print('下单第二步请求成功!')
    # 下单第三个请求
    response = req.post('https://kyfw.12306.cn/otn/confirmPassenger/initDc', data={'_json_att':''}, headers=cons.headers)
    result = response.text
    reg = r"globalRepeatSubmitToken = '(.*?)'"
    REPEAT_SUBMIT_TOKEN = re.findall(reg, result)[0]
    reg = r"'key_check_isChange':'(.*?)'"
    key_check_isChange = re.findall(reg, result)[0]
    data = {
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN
    }
    response = req.post('https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs', data=data, headers=cons.headers)
    response.encoding = 'utf-8'
    print(response.text)
    result = response.json()
    if not result['status']:
        print('下单第三步请求失败...')
        return
    print('下单第三步请求成功...')
    #第四次请求
    data = {
        'cancel_flag':'2',
        'bed_level_order_num':'000000000000000000000000000000',
        'passengerTicketStr': '4,0,1,贺俊,1,432522199611122452,18390248820,N',
        'oldPassengerStr': '贺俊,1,432522199611122452,1_',
        # 'passengerTicketStr':'4,0,1,朱思圣,1,431321199806300097,18390248820,N',
        # 'oldPassengerStr': '朱思圣,1,510321199004116190,1_',
        #     'passengerTicketStr': '4,0,1,李天强,1,510321199004116190,18173119351,N',
        #'oldPassengerStr':'李天强,1,510321199004116190,1_',
        'tour_flag':'dc',
        'randCode':'',
        'whatsSelect':'1',
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN
    }


    response = req.post('https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo', data=data, headers=cons.headers)
    response.encoding = 'utf-8'
    print(response.text)
    #第五个请求
    data = {
        'train_date':'Fri Jan 12 2018 00:00:00 GMT+0800 (中国标准时间)',
        'train_no':train_no,
        'stationTrainCode':stationTrainCode,
        'seatType':'4',
        'fromStationTelecode':fromStationTelecode,
        'toStationTelecode':toStationTelecode,
        'leftTicket':leftTicket,
        'purpose_codes':'00',
        'train_location':train_location,
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN,
    }
    response = req.post('https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount', data=data, headers=cons.headers)
    response.encoding = 'utf-8'
    print(response.text)
    #第6步
    data = {
        'passengerTicketStr': '4,0,1,贺俊,1,432522199611122452,18390248820,N',
        'oldPassengerStr': '贺俊,1,432522199611122452,1_',
        # 'passengerTicketStr': '4,0,1,朱思圣,1,431321199806300097,18390248820,N',
        # 'oldPassengerStr': '朱思圣,1,510321199004116190,1_',
        # 'passengerTicketStr': '4,0,1,李天强,1,510321199004116190,18173119351,N',
        # 'oldPassengerStr': '李天强,1,510321199004116190,1_',
        'randCode':'',
        'purpose_codes':'00',
        'key_check_isChange':key_check_isChange,
        'leftTicketStr':leftTicket,
        'train_location':train_location,
        'choose_seats':'',
        'seatDetailType':'000',
        'whatsSelect':'1',
        'roomType':'00',
        'dwAll':'N',
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN
    }
    response = req.post('https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue', data=data, headers=cons.headers)
    response.encoding = 'utf-8'
    print(response.text)

n = 0
'''
23 = 软卧
28 = 硬卧
3 = 车次
'''

for i in queryTicket():
    tmp_list = i.split('|')
    # for ii in tmp_list:
    #     print(n)
    #     print(ii)
    #     n += 1
    set = tmp_list[SET]
    secretStr = tmp_list[0]
    train_no = tmp_list[2]
    stationTrainCode = tmp_list[3]
    fromStationTelecode = tmp_list[6]
    toStationTelecode = tmp_list[7]
    leftTicket = tmp_list[12]
    train_location = tmp_list[15]

    if set == '' or set == '无':
        print('无票',tmp_list[SET],tmp_list[3])
    else:
        print('有票',tmp_list[SET],tmp_list[3])
        #登录
        login()
        order(secretStr)
        break

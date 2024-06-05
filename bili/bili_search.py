#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv

def get_start():
    op = Options()
    op.add_experimental_option('excludeSwitches', ['enable-automation'])
    service = Service(r'D:\source\softwareTest\selecode\chromedriver.exe')
    web = webdriver.Chrome(service=service,options=op)
    url = f'https://search.bilibili.com/all?keyword={key_word}'
    web.get(url)
    web.maximize_window()

    time.sleep(3)
    for video_num in range(1,7):
        for poision in range(1,7):
            try:
                # /html/body/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div[2]/div/div/a/h3
                # /html/body/div[3]/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div[2]/div/div/a/h3
                title = web.find_element(By.XPATH,f'/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[{poision}]/div/div[{video_num}]/div/div[2]/div/div/a/h3').text
                username = web.find_element(By.XPATH,f'/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[{poision}]/div/div[{video_num}]/div/div[2]/div/div/p/a/span[1]').text
                view_num = web.find_element(By.XPATH,f'/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[{poision}]/div/div[{video_num}]/div/div[2]/a/div/div[2]/div/div/span[1]').text
                danmu = web.find_element(By.XPATH,f'/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[{poision}]/div/div[{video_num}]/div/div[2]/a/div/div[2]/div/div/span[2]').text
                duration = web.find_element(By.XPATH,f'/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[{poision}]/div/div[{video_num}]/div/div[2]/a/div/div[2]/div/span').text
                pub_time = web.find_element(By.XPATH,f'/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[{poision}]/div/div[{video_num}]/div/div[2]/div/div/p/a/span[2]').text.replace('· ','')
                print([title,pub_time,username,view_num,danmu,duration])
                with open(f'{key_word}.csv', mode='a', encoding='utf-8-sig', newline='') as f:  # 将格式化数据写入
                    csv_writer = csv.writer(f)
                    csv_writer.writerow([title,pub_time,username,view_num,danmu,duration])
                break
            except:
                pass


if __name__ == '__main__':
    key_word = '书籍'
    with open(f'{key_word}.csv', mode='w', encoding='utf-8-sig', newline='') as f:  # 将格式化数据写入
        csv_writer = csv.writer(f)
        csv_writer.writerow(['标题', '发布时间','用户名', '播放量', '弹幕数', '时长'])
    get_start()

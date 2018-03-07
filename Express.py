#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import ttk
import tkinter as tk
import urllib, requests, json

root = tk.Tk()
root.title("快递查询")
root.geometry('800x400')

ExpressNum_Label = tk.Label(master=root,text="快递单号",width=10, heigh=3)
ExpressNumEntry = tk.Entry()
company_Label = tk.Label(root, text="快递公司", width=10, heigh=3)
companyname = tk.StringVar()
CompanyEntry = ttk.Combobox(root, textvariable=companyname, width=6)
CompanyEntry['values'] = ("申通","中通","圆通", "顺丰","EMS","韵达","芝麻开门", "百世汇通", "如风达", "天天")
var1 = tk.StringVar()
InfoListbox = tk.Listbox(root, listvar=var1, width=110, heigh=16)

def check_inquiry():
    res = GetInquery().json()['data']
    ExpressInfo = GetExpressInfo(res)
    DisplayInfo(ExpressInfo)

def GetInquery():
    companycode = GetComName(CompanyEntry.get())
    data = {}
    data['type'] = companycode
    data['postid'] = ExpressNumEntry.get() #9754449512262
    query = requests.get("http://www.kuaidi100.com/query", params=data)
    return query

def GetComName(comCode):
    comdict = {'EMS':'ems','顺丰':'shunfeng', '申通':'shentong', '中通':'zhongtong','百世汇通':'huitongkuaidi','如风达':'rufengda',
               '天天':'tiantian','圆通':'yuantong','韵达':'yunda','芝麻开门':'zhimakaimen'}
    if comCode in comdict:
        return comdict[comCode]


def GetExpressInfo(res):
    InfoList = []
    for item in res:
        InfoList.insert(0, item['time']+item['context'])
    return InfoList

def DisplayInfo(ExpressInfo):
    InfoListbox.delete(0,'end')
    for item in ExpressInfo:
        InfoListbox.insert(0, item)


check = tk.Button(root, text="查询", width=10, command=check_inquiry)

ExpressNum_Label.grid(row=0, column=0)
ExpressNumEntry.grid(row=0, column=1)
company_Label.grid(row=0, column=2)
CompanyEntry.grid(row=0, column=3)
check.grid(row=0, column=4, padx=30)
InfoListbox.grid(row=1, columnspan=5, pady=15, padx=10)


root.mainloop()


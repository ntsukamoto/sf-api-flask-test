# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import json
from simple_salesforce import Salesforce

app = Flask(__name__)

USERNAME = ''
PASSWORD = ''
SECURITY_TOKEN = ''


def getArticleList():
    sf = Salesforce(username=USERNAME, password=PASSWORD,
                    security_token=SECURITY_TOKEN, sandbox=False)
    res = sf.query(
        'SELECT Name,Representative__c,Company_Code__c,Company_Name__c,Bankrupt_Date__c,Address__c,Establish_Date__c,Tel__c,Article__c FROM BankruptcyArticle__c WHERE Release__c=True ORDER BY Bankrupt_Date__c DESC')
    return res

def getNews(id):
    sf = Salesforce(username=USERNAME, password=PASSWORD,
                    security_token=SECURITY_TOKEN, sandbox=False)
    res = sf.query(
        'SELECT Name,Representative__c,Company_Code__c,Company_Name__c,Bankrupt_Date__c,Address__c,Establish_Date__c,Tel__c,Article__c FROM BankruptcyArticle__c WHERE Release__c=True and Name="B-00001"')
    return res

@app.route('/')
def newslist():
    al = getArticleList()
    return render_template('index.html', articlelist=al['records'])

@app.route('/article')
def displayNews():
    articleId = request.args.get('id')
    #ba = getNews(articleId)
    al =getArticleList()
    for com in al['records']:
        if com['Name'] == articleId:
            article=com
    return render_template('bankruptcy.html', article=article)

if __name__ == '__main__':
    app.run()

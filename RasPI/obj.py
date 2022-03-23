from urllib import response
import requests
import time


class User:
  def __init__(self, ID, password):
    self.ID = ID
    self.password = password
    self.token = None
    self.connet_server()

  def connet_server(self):
    resource = '/login'
    req = requests.post(self.url+resource, data=self.get_data)
    response = req.json()
    self.token = response['token']

  def get_token(self):
    return self.token

  def get_data(self):
    return {'id': self.ID, 'password': self.password}


class API:
  def __init__(self, domain, user):
    self.url = 'http://'+domain
    self.headers = {"Authorization": 'Bearer '+user.get_token}
    self.user = user

  def Record(self):
    resource = '/record'
    data = self.user.Get_data
    data['date'] = time.strftime('%Y-%m-%d')
    data['time'] = time.strftime(' %H:%M:%S')
    requests.post(self.url+resource, headers=self.headers,
                  data=data)

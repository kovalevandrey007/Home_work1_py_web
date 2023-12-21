import pytest
import requests
import yaml


with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def get_login():
    post = requests.post(url='https://test-stand.gb.ru/gateway/login', data={'username': 'andy08', 'password': '9f65c0c3f3'})
    if post.status_code == 200:
        return post.json()['token']

def get_post(token):
    path = 'https://test-stand.gb.ru/api/posts'
    get = requests.get(url=path, params = {'owner': 'notMe'}, headers={'X-Auth-token': token})
    if get.status_code == 200:
        return get.json()

def add_post(token):
    url = 'https://test-stand.gb.ru/api/posts'
    target = {'title': 'My python post', 'description': 'First post', 'content': 'content to andy08'}
    new_post = requests.post(url=url, data=target, headers={'X-Auth-token': token})
    if new_post.status_code == 200:
        return new_post.json()


if __name__ == '__main__':
    token = get_login()
    # post1 = get_post(token)
    print(get_post(token))
    print(add_post(token))
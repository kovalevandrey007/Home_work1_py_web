from check_post import get_post

id_check = 93422
def test_1(token):
    output = get_post(token)['data']
    res = []
    for item in output:
        res.append(item['id'])
    assert id_check in res

my_title ='My python post'
def test_2(token):
    out = get_post(token)['data']
    result = []
    for items in out:
        result.append(items['title'])
    assert my_title in result
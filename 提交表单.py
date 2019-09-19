import requests
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
val = {
    'hash': '5f5a0ecbb31ef7860c8d8aec79a23777',
    'name': 'mamama',
    'sex': '1',
    'phone': '13233177020',
    'email': '1030811746@qq.com',
    'campus': '1',
    'college': '软件学院',
    'major': '软件工程',
    'class': '1806',
    'studentid': '2018005760',
    'aim':'7',
    'aim2':'7',
    'reasion':'1111111111111111111111111111111111111111111111111111111111111111',
    'reasion2':'11111111111111111111111111111111111111111111111111111111111111111',
    'image': '(binary)'
}
r = requests.post('http://qzxy.tyut.edu.cn/api/usenroll',headers=headers,data=val)
print(r.status_code)
print(r.text)

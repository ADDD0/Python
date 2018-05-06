import urllib.request

req = urllib.request.Request('http://placekitten.com/g/500/600')
response = urllib.request.urlopen(req)

cat_img = response.read()

with open('cat_500_600.jpg', 'wb') as f:
    f.write(cat_img)

print(response.geturl())  # 返回当前url
print(response.info())  # 返回一个HTTPMessage对象,包含远程服务器返回的headers信息
print(response.getcode())  # 返回http状态,200表示正常

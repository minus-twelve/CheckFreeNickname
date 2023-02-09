import requests
print('zadaite nick')
nickname=input()
zanyato='<Response [200]>'
nezanyato='<Response [404]>'



massiv=['http://github.com/',
'http://hackerone.com/',
'http://www.deviantart.com/',
'http://vk.com/',
'http://www.youtube.com/user/',
'http://steamcommunity.com/id/',
'http://illustrators.ru/users/',
'http://www.behance.net/',
'http://www.twitch.tv/',
'http://habr.com/ru/users/'
]


dlinamassiva=len(massiv)
checkurl=['']*dlinamassiva
response=['']*dlinamassiva
checkresponse=['']*dlinamassiva

for (index, elem) in enumerate(massiv):
    massiv[index] = elem + nickname
    checkurl[index] = massiv[index]
    response[index] = requests.get(checkurl[index])
    checkresponse[index] = str(response[index])
    if checkresponse[index]==zanyato:
        print(checkurl[index],'ЗАНЯТО')
    else:
        if checkresponse[index]==nezanyato:
            print(checkurl[index],'СВОБОДНО')


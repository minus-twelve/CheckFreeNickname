import requests
print('zadaite nick')
nickname=input()
zanyato='<Response [200]>'
nezanyato='<Response [404]>'

massiv=['https://www.chess.com/member/',
'http://github.com/',
'https://www.patreon.com/',
'https://www.tiktok.com/@',
'http://vk.com/',
'https://www.youtube.com/user/',
'https://steamcommunity.com/id/',
'https://illustrators.ru/users/',
'https://www.deviantart.com/',
'https://www.behance.net/',
'https://www.twitch.tv/',
'https://hackerone.com/',
'https://habr.com/ru/users/']


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


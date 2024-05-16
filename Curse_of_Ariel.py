import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from playsound import playsound as ps
import pygame
from pygame import mixer

############################################################
########################### 변수 ###########################
############################################################

title = '''
  ,ad8888ba,                                                                     ad88            db                     88              88
 d8"'    `"8b                                                                   d8"             d88b                    ""              88
d8'                                                                             88             d8'`8b                                   88
88             88       88  8b,dPPYba,  ,adPPYba,   ,adPPYba,      ,adPPYba,  MM88MMM         d8'  `8b      8b,dPPYba,  88   ,adPPYba,  88
88             88       88  88P'   "Y8  I8[    ""  a8P_____88     a8"     "8a   88           d8YaaaaY8b     88P'   "Y8  88  a8P_____88  88
Y8,            88       88  88           `"Y8ba,   8PP"""""""     8b       d8   88          d8""""""""8b    88          88  8PP"""""""  88
 Y8a.    .a8P  "8a,   ,a88  88          aa    ]8I  "8b,   ,aa     "8a,   ,a8"   88         d8'        `8b   88          88  "8b,   ,aa  88
  `"Y8888Y"'    `"YbbdP'Y8  88          `"YbbdP"'   `"Ybbd8"'      `"YbbdP"'    88        d8'          `8b  88          88   `"Ybbd8"'  88
  '''
inven = []
items = ['사리엘 방 열쇠', '아리엘 방 열쇠', '라이터', '토끼 인형의 머리', '기도방 열쇠', '인형 상자 열쇠', '분침', '시침', '아리엘의 일기장1', '창고 열쇠', '책갈피', '시침 조각1', '시침 조각2', '본드', '바늘과 실', '토끼 인형의 몸통', '토끼 인형', '목각 인형의 하반신', '목각 인형의 상반신', '목각 인형', '작은 나이프', '병사의 태엽',
'종이 조각1', '종이 조각2', '종이 조각3', '종이 조각4', '소금 200g', '아리엘의 오르골', '더러운 천', '깨끗한 천']
rooms = ['아리엘 방', '사리엘 방', '기도방', '부부방', '식당', '부엌', '창고', '2층 화장실', '1층 화장실']
names = ['에글리즈', '데머너드', '아리엘', '사리엘']
unknown = '\033[31m\???\033[3m'
ariel = '\033[31m아리엘\033[3m'

question_dict = {}
quest_dict = {}

sariel = '너가날죽인거야'
demanad = '그래니가나를죽였어.'

############################################################
########################### 함수 ###########################
############################################################

def ts(sec):
  time.sleep(sec)


class item:
  def __init__(self, object):
    self.object = object

  def call_item(self):
    if self.object in items:
      return '\033[36m'+'\033[1m'+ self.object +'\033[0m'
    else: pass

class room:
  def __init__(self, place):
    self.place = place

  def call_room(self):
    if self.place in rooms:
      return '\033[33m'+'\033[1m'+ self.place +'\033[0m'
    else: pass

class name:
  def __init__(self, nickname):
    self.nickname = nickname

  def call_name(self):
    if self.nickname in names:
      return '\033[32m'+'\033[1m'+ self.nickname +'\033[0m'+'\033[3m'
    else: pass

mixer.init()

def bgm_play(title):
  mixer.music.load('BGM/' + title + '.wav')
  mixer.music.play(-1)

def bgm_stop():
  mixer.music.stop()

############################################################
########################### 게임 ###########################
############################################################

bgm_play('opening')
print('\033[31m'+'\033[1m' + title + '\n'); ts(3)
print('\033[0m' +'\033[1m' + '텍스트 게임 방법'); ts(2)
print('"Enter"를 눌러 텍스트를 넘기십시오.'); input()
print('"y" 또는 "n"을 눌러 질문에 답하십시오.'); input()
print('확인: y'); input(); print('취소: n\n'); input()
print('직접 입력해야 하는 경우에는 직접 입력하십시오.\n'); input()

while True:
  answer = input('"시작하기"를 입력하면 게임이 시작됩니다. '); print('')
  if answer == '시작하기':
    print('------------------------------------------------------------------------------------------------------------------------------------------', flush = True)
    print(''); ts(1); break
  else: print('게임을 시작하려면 "시작하기"를 입력해야 합니다.\n')

bgm_stop(); ts(2)

for i in range(3):
  ps('BGM/rain.wav')
print('\033[0m' + '빗소리가 들린다.\n'); input()
print('눈을 떠보니 익숙한 장소에 와 있었다.\n'); input()
print(f'{name("에글리즈").call_name()}: 여긴...\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 그리운 장소네...\033[0m\n'); input()
print('침대에서 일어나 주위를 둘러보았다.\n'); input(); ts(1)
print(f'{room("부부방").call_room()}인 것 같다.\n'); ts(1); input('?\n')

print('나무로 된 소파 위에 무언가가 있다.\n'); input(); ts(1)
print(f'{item("바늘과 실").call_item()}이 있다.', end="", flush=True); ts(1)
print(f' 실이 얼마 없어서 한 번만 사용할 수 있을 것 같다.\n'); input(); ts(1)
while True:
  question_0 = input('가져갈까?' ); print('')
  if question_0 in ['y', 'n']:
    if question_0 == 'y':
      ts(1); pass
    else:
      print(f'{name("에글리즈").call_name()}: 나중에 필요할지도 모르니 가져가자.\033[0m\n'); input()
    ps('SE/get_item.wav')
    print(f'{item("바늘과 실").call_item()}을 획득했다.\n'); input(); ts(1)
    inven.append('바늘과 실')
  else:
    continue
  break

print(f'{name("에글리즈").call_name()}: 불을 질러 태워버렸던 이 곳에 어째서 다시 돌아오게 된 걸까...\n\033[0m'); ts(1); input()

print('창 밖에 빗소리가 신경쓰인다.\n'); input()
question_1 = input('창 밖을 확인할까? '); print('')
if question_1 == 'y' or question_1 == '':
  ps('SE/open_window.wav')
  ps('BGM/wind.wav')
  ps('SE/close_window.wav')
  print(f'{name("에글리즈").call_name()}: 어두워서 아무것도 보이지 않아.\033[0m\n'); input()
else: pass
print(f'{name("에글리즈").call_name()}: 방 밖으로 나가보자.\033[0m\n'); input(); ts(2)
ps('SE/open_door.wav')

######################## 성민 코드 #########################

print('복도 한 가운데 반짝거리는 무언가가 있다.\n'); input()
while True:
    quest_0 = input('다가갈까? ')
    if quest_0 in ['y', 'n']:
        if quest_0 == 'y':
            ps("SE/footstep.wav")
            print(f'확인해보니 {item("사리엘 방 열쇠").call_item()}다.\n'); input()
            while True:
                quest_1 = input(f'{item("사리엘 방 열쇠").call_item()}를 주울까? '); print('')
                if quest_1 in ['y', 'n']:
                    if quest_1 == 'y':
                        ps("SE/get_item.wav")
                        print(f'{item("사리엘 방 열쇠").call_item()}을 획득했다.\n'); input()
                        inven.append('사리엘 방 열쇠')
                        break
                    else: continue
                else: continue
        else: continue
    else: continue
    break

ps("SE/footstep.wav")
print(f'{name("에글리즈").call_name()}: 아까 얻은 {item("사리엘 방 열쇠").call_item()}\033[3m를 이용하자.\033[0m\n'); input()
while True:
    quest_2 = input('열쇠를 이용해 방문을 열까? '); print('')
    if quest_2 in ['y', 'n']:
        if quest_2 == 'y':
            ps('SE/unlock.wav')
            print(f'{room("사리엘 방").call_room()} 문을 열었다.\n'); input()
            ps("SE/open_door.wav")
            inven.remove('사리엘 방 열쇠')
            ps("SE/koong.wav")
            print(f'{name("에글리즈").call_name()}: 무슨 소리지?\033[0m\n'); input()
            print(f'{name("에글리즈").call_name()}: 소리난 곳으로 가볼까?\033[0m\n'); input()
            print(f'{name("에글리즈").call_name()}: 궁금하긴하지만 목적은 {room("사리엘 방").call_room()}\033[3m이니까 {room("사리엘 방").call_room()} 먼저 들어가자.\033[0m\n'); input()
            break
        else: continue
    else: continue
    
ps("SE/footstep.wav")
print('침대 밑에 반짝거리는 것이 있다. \n'); input()
while True:
    print(f'침대 밑에 {item("기도방 열쇠").call_item()}가 놓여져있다. \n'); input()
    quest_3 = input('가져갈까? '); print('')
    if quest_3 in ['y', 'n']:
        if quest_3 == 'y':
            ps("SE/get_item.wav")
            print(f'{item("기도방 열쇠").call_item()}을 획득했다.\n'); input()
            inven.append('기도방 열쇠')
            print(f'{name("에글리즈").call_name()}: {room("기도방").call_room()}\033[3m...\033[0m\n'); input()
            print(f'{name("에글리즈").call_name()}: 자주 가서 기도했던 곳이지...\033[0m\n'); input()
            break
        else: continue
    else: continue



ps("SE/footstep.wav")
print(f'{name("에글리즈").call_name()}: 자꾸 그 소리가 신경이 쓰여...\033[0m', end="", flush=True); ts(1)
print(' 얼른 가봐야겠어.\033[0m\n'); input()
ps("SE/footstep.wav")
while True:
    print(f'2층 복도 책장에 {item("아리엘 방 열쇠").call_item()}가 놓여져있다.'); input()
    quest_4 = input('아리엘 방 열쇠를 주울까? '); print('')
    if quest_4 in ['y', 'n']:
        if quest_4 == 'y':
            ps("SE/get_item.wav")
            print(f'{item("아리엘 방 열쇠").call_item()}을 획득했다.\n'); input()
            inven.append('아리엘 방 열쇠')
            print(f'{name("에글리즈").call_name()}: 드디어 소리의 원인을 찾으러 갈 수 있어.\033[0m\n'); input()
            print(f'{name("에글리즈").call_name()}: 얼른 가보자.\033[0m\n'); input()
            break
        else: continue
    else: continue
    

ps("SE/footstep.wav")
while True:
    quest_5 = input('아리엘 방 열쇠를 이용해 방문을 열까? '); print('')
    if quest_5 in ['y', 'n']:
        if quest_5 == 'y':
            ps('SE/unlock.wav')
            print(f'{room("아리엘 방").call_room()}을 열었다.\n'); input()
            ps("SE/open_close.wav")
            inven.remove('아리엘 방 열쇠')
            print(f'{name("에글리즈").call_name()}: 소리의 원인이 사진첩이 떨어져서 난 소리였구나.\033[0m\n'); input()
            print(f'{name("에글리즈").call_name()}: 뭔가가 반짝이는 게 있는데 뭘까?\033[0m\n'); input()
            while True:
              quest_6 = input(f'{item("인형 상자 열쇠").call_item()}다. 주울까? '); print('')
              if quest_6 in ['y', 'n']:
                  if quest_6 == 'y':
                      ps("SE/get_item.wav")
                      print(f'{item("인형 상자 열쇠").call_item()}을 획득했다.\n'); input()
                      inven.append('인형 상자 열쇠')
                      break
                  else: continue
              else: continue
        else: continue
    else: continue
    break


print(f'{name("에글리즈").call_name()}: 인형 상자...?\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 그러고보니 아까 {item("아리엘 방 열쇠").call_item()}\033[3m를 주웠을 때 거기에 인형 상자가 있었어.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 얼른 가보자.\033[0m\n'); input()
ps("SE/footstep.wav")
while True:
    quest_7 = input(f'{item("인형 상자 열쇠").call_item()}를 이용해 열까? '); print('')
    if quest_7 == 'y':
        break
    elif quest_7 == 'n':
        print(f'{name("에글리즈").call_name()}: 열쇠가 있는데 안 열어볼 수 없지.\033[0m\n'); input()
        break
    else: continue

ps('SE/unlock.wav')
print('인형 상자를 열었다.\n')
inven.remove('인형 상자 열쇠')
print(f'{name("에글리즈").call_name()}: 토끼 인형의 머리...?\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 둘이 서로 싸우다가 뜯어졌나 보네.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 사이좋아 보였는데 이런 마찰도 있었구나.\033[0m\n'); input()

while True:
    quest_8 = input('토끼 인형의 머리를 가져갈까? ')
    if quest_8 == 'y':
        ps("SE/get_item.wav")
        print(f'{item("토끼 인형의 머리").call_item()}을 획득했다.\n'); input()
        inven.append('토끼 인형의 머리')
        break
    elif quest_8 == 'n':
        print(f'{name("에글리즈").call_name()}: 머리가 있으면 몸통도 있을 거야.\033[0m\n'); input()
        print(f'{name("에글리즈").call_name()}: 몸통까지 찾아보자.\033[0m\n'); input()
        break
    else: continue
    

print(f'{name("에글리즈").call_name()}: 뭐가 어떻게 된 건지는 모르겠지만,\033[0m', end="", flush=True); ts(1)
print(' 모이라님만 계신다면 무사히 돌아갈 수 있겠지...\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 이럴 때가 아니야.\033[0m', end="", flush=True); ts(1)
print(' 레이나님께 기도를 올려야 해.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 얼른 기도방으로 가보자.\033[0m\n'); input()
ps("SE/footstep.wav")
while True:
    quest_9 = input(f'{item("기도방 열쇠").call_item()}를 사용해 문을 열까? '); print('')
    if quest_9 in ['y', 'n']:
        if quest_9 == 'y':
            ps('SE/unlock.wav')
            print(f'{room("기도방").call_room()} 문을 열었다.\n'); input()
            ps("SE/open_door.wav")
            inven.remove('기도방 열쇠')
            print(f'{name("에글리즈").call_name()}: 어두워서 아무것도 보이지 않아.\033[0m\n'); input()
            print(f'{name("에글리즈").call_name()}: 밝혀줄 무언가가 필요해.\033[0m\n'); input()
            ps('SE/close_door.wav')
            break
        else: continue
    else: continue

print(f'{name("에글리즈").call_name()}: 건물 안에 있는데도 암흑처럼 깜깜했어.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 분명 무언가가 저 방으로 들어가지 못 하게 막고 있는 거겠지.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 다른 곳부터 확인해보자.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 1층 조사는 다 했던가?\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 혹시 모르니 확인하러 가보자.\033[0m\n'); input()

ps("SE/stair.wav")
ps('SE/footstep.wav')
ps('SE/chulkung.wav')
print(f'{room("부엌").call_room()} 문이 잠겨 있다.\n'); input()
ps('SE/footstep.wav')
ps('SE/open_close.wav')
print(f'{room("식당").call_room()} 문을 열었다.\n'); input()
print(f'식당 벽난로 위에 반짝이는 무언가가 있다.\n'); input()

print(f'{item("라이터").call_item()}가 있다.\n'); input()
while True:
    quest_10 = input('가져갈까? '); print('') 
    if quest_10 == 'y':
        break
    elif quest_10 == 'n':
        print(f'{name("에글리즈").call_name()}: 어두운 곳에서 사용하거나 무언가를 태울 때 도움이 될 거야.\033[0m\n'); input()
        break
    else:
        continue
ps("SE/get_item.wav")
print(f'{item("라이터").call_item()}를 획득했다.\n'); input()
inven.append('라이터')
print('1층에서 얻을 것은 더 이상 없는 것 같다.\n'); input()
print(f'{name("에글리즈").call_name()}: 2층으로 가서 더 확인해보자.\033[0m\n'); input()

ps('SE/stair.wav')
while True:
    print(f'2층 계단 앞 화분에 {item("창고 열쇠").call_item()}가 놓여져있다.\n'); input()
    quest_17 = input(f'{item("창고 열쇠").call_item()}를 가져갈까? '); print('')
    if quest_17 in ['y', 'n']:
        if quest_17 == 'y':
            ps("SE/get_item.wav")
            print(f'{item("창고 열쇠").call_item()}을 획득했다.\n'); input()
            inven.append('창고 열쇠')
            break
        else: continue
    else: continue

# 퍼즐
ps("SE/footstep.wav")
print(f'{room("사리엘 방").call_room()}책장에 책이 3개가 꽂아져있다.'); input()
print(f'사리엘의 일기장1'); input()
ps("SE/page2.wav")
print(f'오늘은 화창한 날이다.'); input()
print(f'오늘은 가족과 소풍가는날이다.'); input()
print(f'{name("에글리즈").call_name()}: 소풍 재밌었지....\033[0m\n'); input()
print(f'사리엘의 일기장2'); input()
ps("SE/page2.wav")
print(f'오늘은 기분이 좋은날이다..'); input()
print(f'오늘은 내 생일이기 때문이다.'); input()
print(f'하지만 아쉬운점이 하나있다.'); input()
print(f'엄마가 사주기로 약속한 인형을 안사주셨다...'); input()
print(f'{name("에글리즈").call_name()}: 그때 약속했었는데..못지켰지..\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 사주기로했었는데...미안해...\033[0m\n'); input()
ps("SE/page2.wav")
print(f'{item("아리엘의 일기장1").call_item()}'); input()
print(f'오늘은 동생과 함께 산책을 하러 나갔다.'); input()
print(f'산책을 하던도중 이쁜 꽃이 있어 꺽어서 동생이랑 엄마한테 줬다.'); input()
print(f'동생이랑 엄마가 좋아하는 모습을 보고 나도 행복했다.'); input()
print(f'{name("에글리즈").call_name()}: 다음 장부터는 글씨가 망가져서 무슨 말인지 모르겠어....\033[0m\n'); input()
ps("SE/page2.wav")
print(f'{item("아리엘의 일기장1").call_item()}의 일부가 찢어져 있다.'); input()
ps("SE/page2.wav")
ps("SE/page2.wav")
print(f'{name("에글리즈").call_name()}: 책갈피가 꽂혀 있네?\033[0m\n'); input()
ps("SE/get_item.wav")
print(f'{item("책갈피").call_item()}를 획득했다.'); input()
inven.append('책갈피')
print(f'{name("에글리즈").call_name()}: 생각해보니 {item("아리엘의 일기장1").call_item()}\033[3m이 왜 {room("사리엘 방").call_room()}\033[3m 책장에 꽂혀 있는거지...?\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: {room("아리엘 방").call_room()}\033[3m 책장에 꽂으러 가야겠어.\033[0m\n'); input()

while True:
    quest_11 = input(f'{item("아리엘의 일기장1").call_item()}을 가져갈까?'); input()
    if quest_11 in ['y', 'n']:
        if quest_11 == 'y':
            ps("SE/get_item.wav")
            print(f'{item("아리엘의 일기장1").call_item()}을 획득했다.'); input()
            inven.append('아리엘의 일기장1')
            break
        else: continue
    else: continue
    

while True:
    quest_12 = input(f'{item("아리엘의 일기장1").call_item()}을 책장에 꽂을까?'); input()
    if quest_12 in ['y', 'n']:
        if quest_12 == 'y':
            print(f'{item("아리엘의 일기장1").call_item()}을 꽂았다.'); input()
            inven.remove('아리엘의 일기장1')
            ps("SE/page1.wav")
            print(f'종이 한 장이 떨어져있다. '); input()
            while  True:
                quest_13 = input(f'종이 한 장을 읽을까? '); input()
                if quest_13 in ['y', 'n']:
                    if quest_13 == 'y':
                        print(f'당신이 바라보는 왼쪽이 답이야...'); input()
                        print(f'{name("에글리즈").call_name()}: 내 왼쪽....? 저 시계를 말하는 건가?\033[0m\n'); input()
                        print(f'{name("에글리즈").call_name()}: 왼쪽이 답이랬으니 시계에 가보자\033[0m\n'); input()
                        break
                    else: continue
                else: continue
        else: continue
    else: continue
    break
    

ps("SE/footstep.wav")
print('시계가 있다.')
print(f'{name("에글리즈").call_name()}: 시계에 {item("분침").call_item()}과 {item("시침").call_item()}\033[3m이 없네....\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: {item("분침").call_item()}과 {item("시침").call_item()}\033[3m을 찾으러 가자\033[0m\n'); input()


#아리엘 방
ps("SE/footstep.wav")
ps("SE/open_close.wav")
while True:
    print(f'종이 한 장이 바닥에 떨어져있다. '); input()
    print(f'종이 한 장을 읽자 '); input()
    if quest_13 in ['y', 'n']:
        if quest_13 == 'y':
            print(f'식물 심는 곳을 바라봐라 '); input()
            print(f'{name("에글리즈").call_name()}: 식물 심는곳....?\033[0m\n'); input()
            print(f'{name("에글리즈").call_name()}: 밖에 있을 리는 없고...집 안에 화분을 위주로 찾아봐야 겠어.\033[0m\n'); input()
            break
        else: continue
    else: continue

#사리엘 방
ps("SE/footstep.wav")
ps("SE/open_close.wav")
while True:
    print(f'책상 위에 무언가가 빛난다. '); input()
    print(f'{item("시침").call_item()}이 있다. 가져가자'); input()
    if quest_11 in ['y', 'n']:
        if quest_11 == 'y':
            print(f'시침을 주우려는 순간 시침이 반토막이 났다. '); input()
            ps("SE/get_item.wav")
            print(f'{item("시침 조각1").call_item()}을 획득했다.'); input()
            print(f'{item("시침 조각2").call_item()}을 획득했다.'); input()
            inven.append("시침 조각1")
            inven.append("시침 조각2")
            print(f'{name("에글리즈").call_name()}: 이런.....부러졌네...붙일 {item("본드").call_item()}\033[3m가 필요해.\033[0m\n'); input()
            break
        else: continue
    else: continue


# 복도 계단 앞
ps("SE/footstep.wav")
while True:
    print(f'화분에 반짝거리는 무언가가 있다. '); input()
    print(f'{item("분침").call_item()}놓여져 있다. '); input()
    if quest_12 in ['y', 'n']:
        if quest_12 == 'y':
            ps("SE/get_item.wav")
            print(f'{item("분침").call_item()}을 획득했다.'); input()
            inven.append('분침')
            break
        else: continue
    else: continue

#사리엘 방
ps("SE/footstep.wav")
ps("SE/open_close.wav")
while True:
    print(f'책상 서랍속에{item("본드").call_item()}를 발견했다.\n'); input()
    quest_13 = input('가져갈까? '); print('')
    if quest_13 in ['y', 'n']:
        if quest_13 == 'y':
            ps("SE/get_item.wav")
            print(f'{item("본드").call_item()}를 획득했다. '); input()
            inven.append("본드")
            print(f'{name("에글리즈").call_name()}: 이제 {item("시침").call_item()}\033[3m을 붙일 수 있겠어..\033[0m\n'); input()
            print(f'{name("에글리즈").call_name()}: 조합해보자.\033[0m\n'); input()
            while True:
                print(f'{item("본드").call_item()}를 이용해 붙이자. '); input()
                ps("SE/get_item.wav")
                print(f'{item("시침").call_item()}을 얻었다. '); input()
                inven.remove("시침 조각1")
                inven.remove("시침 조각2")
                inven.append("시침")
                break
        else: continue
    else: continue
    break


ps("SE/footstep.wav")
ps("SE/open_close.wav")
while True:
    quest_16 = input(f'{item("분침").call_item()}과 {item("시침").call_item()}을 이용해 시계를 만드시겠습니까? '); print('')
    if quest_16 in ['y', 'n']:
        if quest_16 == 'y':
            print(f'시계가 완성되었다.\n'); input()
            inven.remove("분침")
            inven.remove("시침")
            ps("SE/clock.wav")
            print('시계가 돌아가더니 10시 30분에서 멈췄다.\n'); input()
            print(f'{name("에글리즈").call_name()}: 이게 답이랬어...잘 생각해보자\033[0m\n'); input()
            break
        else: continue
    else: continue

print(f'{name("에글리즈").call_name()}: 더 이상 얻을 만한 정보가 없는 것 같아.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 복도로 나가자.\033[0m\n'); input()
ps('SE/open_close.wav')
ps('SE/footstep.wav')
print('?\n'); ts(1)
print('2층 복도 계단 앞에 그림에서 위화감이 느껴진다.\n'); input()
print(f'{name("에글리즈").call_name()}: 이상하게 테두리만 습기에 젖어 있어.\033[0m\n'); input()
while True:
  quest_18 = input(f'{item("라이터").call_item()}를 사용하여 그림을 태울까? '); print('')
  if quest_18 in ['y', 'n']:
      if quest_18 == 'y':
          print('그림의 뒤가 보인다.\n'); input()
          print('자세히 보니 멈춰 있는 작은 시계가 있다.\n'); input()
          break
      else: continue
  else: continue

print(f'{name("에글리즈").call_name()}: 혹시 이 시계의 시간을 10시 30분으로 맞추는 게 아닐까?\033[0m\n'); input()
print('작은 시계의 시간을 10시 30분으로 맞췄다.\n'); input()
ts(1.5)
print('아무 일도 일어나지 않\n'); ts(0.5)

ps('SE/koong.wav')
print('1층에서 무슨 소리가 들린 것 같다.\n'); input()

############################################################

print(f'{name("에글리즈").call_name()}: {room("창고").call_room()}\033[3m쪽에서 들린 것 같은데...\033[0m'); input()
ps('SE/footstep.wav')
ps('SE/chulkung.wav')
print('잠겨 있다.'); input()

ps('SE/unlock.wav')
print(f'{item("창고 열쇠").call_item()}를 사용하여 {room("창고").call_room()} 문을 열었다.'); input()
inven.remove('창고 열쇠')

while True:
  question_2 = input('문을 열까? '); print('')
  if question_2 == 'y':
    while True:
      question_3 = input('정말로? '); print('')
      if question_3 == 'y':
        pass
      else:
        print(f'{name("에글리즈").call_name()}: 소리의 원인을 찾아야 해.\033[0m\n'); input()
      break
  else: continue
  break

ps('SE/open_warehouse.wav')

print('술통 사이로 건초더미가 보인다.\n'); input()
while True:
  question_4 = input('건초 더미를 조사할까?'); print('')
  if question_4 == 'y':
    pass
  elif question_4 == 'n':
    print(f'{name("에글리즈").call_name()}: 소리의 원인을 찾아야 해.\033[0m\n'); input()
  else:
    continue
  break

for i in range(3):
  ps('SE/bususu.wav')
print(f'{item("토끼 인형의 몸통").call_item()}이 있다.\n'); input()
ps('SE/get_item.wav')
print(f'{item("토끼 인형의 몸통").call_item()}을 얻었다.\n'); input()
inven.append('토끼 인형의 몸통')


while True:
  question_5 = input(f'{item("토끼 인형의 머리").call_item()}와 {item("토끼 인형의 몸통").call_item()}을 \
    {item("바늘과 실").call_item()}로 붙일까?'); print('')
  if question_5 == 'y':
    pass
  elif question_5 == 'n':
    print(f'{name("에글리즈").call_name()}: 토끼 인형을 만들어 {room("아리엘 방").call_room()}\033[3m 책상 위에 올려놓자.\033[0m\n'); input()
  else:
    continue
  break

ps('SE/get_item.wav')
print(f'{item("토끼 인형").call_item()}을 얻었다.\n'); input()
inven.remove("토끼 인형의 머리")
inven.remove("토끼 인형의 몸통")
inven.append("토끼 인형")

for i in range(3):
  print("...", end="", flush=True); ts(1)
print("!"); input()
ps('SE/fierce.wav')
print(f'{item("토끼 인형").call_item()}이 살아 움직인다.'); input()
print(f'{item("토끼 인형").call_item()}이 손에서 떨어져 {room("부엌").call_room()}쪽으로 뛰어갔다.')

while True:
  question_6 = input('쫓아갈까? '); print('')
  if question_6 == 'y':
    ts(2)
    ps('SE/glass_far.wav')
    print(f'{name("에글리즈").call_name()}: !!!\033[0m\n'); input()
  elif question_6 == 'n':
    print(f'{name("에글리즈").call_name()}: 다가가기 무서우니 {room("1층 화장실").call_room()}\033[3m부터 확인하자.\033[0m\n'); input()
    ps('SE/glass_far.wav')
    print(f'{name("에글리즈").call_name()}: !!!\033[0m\n'); input()
    print(f'{name("에글리즈").call_name()}: {room("부엌").call_room()}\033[3m쪽에서 유리 깨지는 소리가 들렸다.\033[0m\n'); input()
    print(f'{name("에글리즈").call_name()}: 어쩔 수 없네...\033[0m\n'); input()
  else:
    continue
  break

print(f'잠겨 있던 {room("부엌").call_room()} 문이 열려 있다.\n'); input()
ps('SE/ymm.wav')
print(f'{room("부엌").call_room()} 안을 들여다보니 {item("토끼 인형").call_item()}이 건육보관함을 열어 건육을 먹고 있다.\n'); input()

for i in range(3):
  print("...", end="", flush=True); ts(1)
print("!"); input()

print(f'{item("토끼 인형").call_item()}과 눈이 마주쳤다.\n'); input()
ps('SE/fierce.wav')
ps('SE/close_door_fast.wav')
print(f'급히 {room("부엌").call_room()} 문을 닫았다.\n'); input()
print(f'{name("에글리즈").call_name()}: {item("토끼 인형").call_item()}\033[3m이 움직이다니 말도 안 돼...!\033[0m'); input()
print('......', end=""); input('문을 닫으니 조용해졌다.'); ts(3)
ps('SE/scream.wav')
print('!\n'); input()
print(f'{room("부엌").call_room()} 안에서 비명 소리가 났다.'); input()

while True:
  question_7 = input('문을 열까? '); print('')
  if question_7 == 'y':
    break
  elif question_7 == 'n':
    print(f'{name("에글리즈").call_name()}: ...\033[0m\n'); input()
    continue
  else: continue

ps('SE/open_door.wav')

print(f'{item("토끼 인형").call_item()}이 아궁이에서 불에 타고 있다.\n'); input(); ts(2)
print('자세히 보니 무언가가 있다.\n'); input()
ps('SE/get_item.wav')
print(f'{item("목각 인형의 하반신").call_item()}을 얻었다.\n'); input()
inven.append('목각 인형의 하반신')

print(f'{name("에글리즈").call_name()}: {room("부엌").call_room()}\033[3m에 무언가 가져갈 만한 것이 없을까...\033[0m'); input()

while True:
  if question_dict == {'선반 위':1, '식기 보관함':2, '조미료 보관함':3, '쓰레기통':4}:
    question_dict = {}
    break
  else:
    print('어느 곳을 확인해볼까?\n')
    question_8 = input('1. 선반 위\n2. 식기 보관함\n3. 조미료 보관함\n4. 쓰레기통\n')
    if question_8 in ['1','선반 위', '1. 선반 위']:
      if '선반 위' not in question_dict:
        ps('SE/crunch.wav')
        print('가져갈 만한 것은 없는 것 같다.'); input()
        question_dict['선반 위'] = 1
      else:
        print('이미 확인했던 곳이다.\n'); input()
    
    elif question_8 in ['2','식기 보관함', '2. 식기 보관함']:
      if '식기 보관함' not in question_dict:
        ts(2)
        print(f'{item("작은 나이프").call_item()}가 있다.\n'); input()
        ps('SE/get_item.wav')
        print(f'{item("작은 나이프").call_item()}을 얻었다.\n'); input()
        inven.append('작은 나이프')
        question_dict['식기 보관함'] = 2
      else:
        print('이미 확인했던 곳이다.\n'); input()

    elif question_8 in ['3','조미료 보관함', '3. 조미료 보관함']:
      if '조미료 보관함' not in question_dict:
        ts(2)
        print(f'{item("소금 200g").call_item()}이 있다.\n'); input()
        ps('SE/get_item.wav')
        print(f'{item("소금 200g").call_item()}을 얻었다.\n'); input()
        inven.append('소금 200g')
        while True:
          question_9 = input('맛을 볼까? '); print('')
          if question_9 == 'y':
            ts(2)
            print(f'{name("에글리즈").call_name()}: 먹으면 안 될 것 같다.\033[0m\n'); input()
            break
          elif question_9 == 'n':
            break
          else:
            continue
        question_dict['조미료 보관함'] = 3
      else:
        print('이미 확인했던 곳이다.\n'); input()

    elif question_8 in ['4','쓰레기통', '4. 쓰레기통']:
      if '쓰레기통' not in question_dict:
        ts(2)
        print(f'{item("종이 조각1").call_item()}이 있다.\n'); input()
        ps('SE/get_item.wav')
        print(f'{item("종이 조각1").call_item()}을 얻었다.\n'); input()
        inven.append('종이 조각1')
        question_dict['쓰레기통'] = 4
      else:
        print('이미 확인했던 곳이다.\n'); input()
        
    else: continue

print(f'{name("에글리즈").call_name()}: {room("부엌").call_room()}\033[3m은 다 살펴본 것 같아.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: {room("1층 화장실").call_room()}\033[3m을 살펴봐야 겠어.\033[0m\n'); input()

ps('SE/stair.wav')
for i in range(3):
  print("...", end="", flush=True); ts(1)
print("?"); input()
print('누군가가 내려오는 소리가 들린다.\n'); input()

bgm_play('tense')
print(f'{name("에글리즈").call_name()}: 건육 보관함으로 들어가 숨어야 겠어!\033[0m\n'); input()
ps('SE/open_door.wav')
ps('SE/footstep_another.wav')
ps('SE/footstep_another.wav')
print("...", end="", flush=True); ts(1.5)
print("...", end="", flush=True); ts(1.5)
print("...\n"); input()
ps('SE/close_door.wav'); ts(1)
bgm_stop()
print(f'{name("에글리즈").call_name()}: ...\033[0m\n'); input()

while True:
  question_10 = input('문을 열까? '); print('')
  if question_10 == 'y':
    while True:
      question_11 = input('정말로? '); print('')
      if question_11 == 'y':
        pass
      else:
        print(f'{name("에글리즈").call_name()}: 나가도 괜찮을 것 같다.\033[0m\n'); input()
      ps('SE/ggi_ik.wav')
      break
  else: continue
  break

print(f'{name("에글리즈").call_name()}: 방금 그건 누구였던 걸까...\033[0m\n'); input()
print('바닥에 무언가 떨어져 있다.'); input()
ps('SE/get_item.wav')
print(f'{item("종이 조각3").call_item()}를 얻었다.\n'); input()
inven.append('종이 조각3')
print(f'{name("에글리즈").call_name()}: 아까 얻었던 {item("종이 조각1").call_item()}\033[3m과 관련이 있을까?\033[0m\n'); input()
print(f'{item("종이 조각1").call_item()}에는 \033[3m\033[1m"내 오르골을 돌릴"\033[0m이라고 적혀 있다.\n'); input()
print(f'{item("종이 조각3").call_item()}에는 \033[3m\033[1m"오직 왕을 지키는"\033[0m이라고 적혀 있다.\n'); input()
print(f'{name("에글리즈").call_name()}: 오르골과 왕이라...\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 아직 단서가 부족한 것 같아.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 아직 안 가본 곳은 {room("1층 화장실").call_room()}\033[3m과 {room("2층 화장실").call_room()}\033[3m 뿐인 것 같은데.\033[0m\n'); input()

while True:
  if quest_dict == {'1층 화장실':1, '2층 화장실':2}:
    quest_dict = {}
    break
  else:
    print('어느 곳을 확인하러 가볼까?')
    question_12 = input('1. 1층 화장실\n2. 2층 화장실')
    if question_12 in ['1', '1층 화장실', '1. 1층 화장실']:
      if '1층 화장실' not in quest_dict:
        ps('SE/footstep.wav')
        ps('SE/open_close.wav')
        ps('SE/pongdang.wav')
        print('?'); input()
        print('순간 창문 밖에서 누군가가 쳐다 본 듯한 느낌이 들었다.\n'); input()
        print(f'{name("에글리즈").call_name()}: 기분탓이겠지...\033[0m\n'); input()
        ps('SE/pongdang.wav')
        print('천 보관함이 열려 있다.\n'); input()

        while True:
          question_13 = input('확인해볼까? '); print('')
          if question_13 == 'y':
            pass
          elif question_13 == 'n':
            print(f'{name("에글리즈").call_name()}: 컵 같은 게 있는 것 같은데?\033[0m\n'); input()
          else: continue
          print('투명한 액체가 가득 담긴 유리컵이 있다.\n'); input()
          print('500㎖라는 눈금까지 있는 것으로 보아 상당한 양인 것 같다.\n'); input()
          break

        while True:
          if question_dict == {'마셔본다':1, '두드려본다':2, '손을 넣어본다':3}:
            question_dict = {}
            break
          else:
            print('어떻게 할까?\n')
            question_14 = input('1. 마셔본다.\n2. 두드려본다.\n3. 손을 넣어본다.'); print('')
            if question_14 in ['1', '마셔본다.', '마셔본다', '1. 마셔본다.', '1. 마셔본다']:
              if '마셔본다' not in question_dict:
                print('천 보관함 바닥에 붙어 있어 뗄 수 없다.\n'); input()
                question_dict['마셔본다'] = 1
              else:
                print('마시려는 시도는 그만두자.\n'); input()

            elif question_14 in ['2', '두드려본다.', '두드려본다', '2. 두드려본다.', '2. 두드려본다']:
              if '두드려본다' not in question_dict:
                ps('SE/thing.wav')
                print('?\n'); input()
                print('무언가가 유리컵 안에서 움직였다.\n'); input()
                question_dict['두드려본다'] = 2
              else:
                print(f'{name("에글리즈").call_name()}: 안에 무언가 있는 것 같은데...\033[0m\n'); input()

            elif question_14 in ['3', '손을 넣어본다.', '손을 넣어본다', '3. 손을 넣어본다.', '3. 손을 넣어본다']:
              if '손을 넣어본다' not in question_dict:
                print('독극물일지도 모른다.\n'); input()
                print('손을 넣는 건 위험하다.\n'); input()
                question_dict['손을 넣어본다'] = 3
              else:
                print('손을 넣으려는 시도는 그만두자.\n'); input()

            else: continue

        quest_dict['1층 화장실'] = 1
        print(f'{name("에글리즈").call_name()}: 부력을 이용하면 안에 든 것을 꺼낼 수 있지 않을까?\033[0m\n'); input()
        print(f'{item("소금 200g").call_item()}을 사용했다.\n'); input()
        for i in range(3):
          print("...", end="", flush=True); ts(1)
        print('!\n'); input()
        print('작은 검은색 공이 컵 위로 올라왔다.\n'); input()
        print('검은색 공 가운데에 선이 그어져 있다.\n'); input()
        print('반으로 쪼갤 수 있을 것 같다.\n'); input()
        while True:
          question_15 = input('반으로 쪼갤까? '); print('')
          if question_15 == 'y':
            break
          elif question_15 == 'n':
            print(f'{name("에글리즈").call_name()}: 내용물이 궁금하니까 쪼개보자.\033[0m\n'); input()
          else:
            continue
        print(f'{item("병사의 태엽").call_item()}이 들어 있다.\n'); input()
        ps('SE/get_item.wav')
        print(f'{item("병사의 태엽").call_item()}를 얻었다.\n'); input()
        inven.append('병사의 태엽')
      else:
        print(f'{name("에글리즈").call_name()}: 이미 확인해본 곳이야.\033[0m\n'); input()

    elif question_12 in ['2', '2층 화장실', '2. 2층 화장실']:
      if '2층 화장실' not in quest_dict:
        ps('SE/footstep.wav')
        ps('SE/open_close.wav')
        ps('SE/pongdang.wav')
        print('이중문을 열었더니 더러운 천 하나가 있다.\n'); input()
        print(f'{item("더러운 천").call_item()}을 얻었다.\n'); input()
        inven.append('더러운 천')
        print(f'{name("에글리즈").call_name()}: 천을 물러 씻어내 보자.\033[0m\n'); input()
        ps('SE/water1.wav')
        ps('SE/water2.wav')
        ps('SE/water1.wav')
        print(f'{item("깨끗한 천").call_item()}을 얻었다.\n'); input()
        inven.remove('더러운 천')
        inven.append('깨끗한 천')
        quest_dict['2층 화장실'] = 2
      else:
        print(f'{name("에글리즈").call_name()}: 이미 확인해본 곳이야.\033[0m\n'); input()

    else: continue

print('어디선가 맛있는 냄새가 난다.\n'); input()
print(f'{name("에글리즈").call_name()}: {room("부엌").call_room()}\033[3m쪽에서 나는 냄새인 것 같은데.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 내려가서 확인해보자.\033[0m\n'); input()
ps('SE/footstep.wav')
ps('SE/open_close.wav')
ps('SE/boiling.wav')
print('포트에서 무언가 끓고 있다.\n'); input()
ps('SE/shred.wav')
print('...?', end="", flush=True); ts(1)
print('보이지 않는 누군가가 보이지 않는 무언가를 썰고 있다.\n'); input()
print('\033[3m아~, 덥다 더워~.\n'); input()
print('거기 아가씨. 무언가 닦을 것 좀 주지 않을래요?\033[0m\n'); input()

while True:
  question_16 = input(f'{item("깨끗한 천").call_item()}을 건네줄까? '); print('')
  if question_16 == 'y':
    break
  elif question_16 == 'n':
    print(f'{name("에글리즈").call_name()}: (어차피 쓸 데가 없을 것 같으니 주도록 하자.)\033[0m\n'); input()
    break
  else:
    continue

print(f'{item("깨끗한 천").call_item()}을 건네주었다.\n'); input()
inven.remove('깨끗한 천')
print('\033[3m아~, 정말 고마워요, 아가씨. ', end="", flush=True)
print('답례로 이걸 줄게요.\033[0m\n'); input()
ps('SE/get_item.wav')
print(f'{item("종이 조각2").call_item()}를 받았다.\n'); input()
inven.append('종이 조각2')
print(f'{item("종이 조각2").call_item()}에는 \033[1m\033[3m"수 있는 사람은"\033[0m이라고 적혀 있다.\n'); input()
print(f'{name("에글리즈").call_name()}: 하나만 더 모으면 이 말의 의미를 이해할 수 있을 것 같은데...\033[0m\n'); input()
print('\033[3m아~, 근데 아가씨. ', end="", flush=True)
print('\033[3m이 집에 살던 사람하고 많이 닮은 것 같은데.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: !!!\033[0m\n', end="", flush=True); ts(1)
print(' 저는 이 집에 처음 와봐요...\033[0m\n'); input()
print('\033[3m아~, 하긴 그 사람은 불에 타서 죽었댔지~.\n'); input()
print('아니, \033[31m\033[1m불을 지른 사람이랬나? ', end="", flush=True); ts(1)
ps('SE/hahahaha.wav')
print('하하하하하하하하하하하하하하하하하하하하하하하하하하하하하하하하하하하하하하\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: !!!!!\033[0m\n'); input()
ps('SE/close_door_fast.wav')
print(f'{name("에글리즈").call_name()}: 으... 소름끼치는 웃음소리였어.\033[0m\n'); input()

ps('SE/bell2.wav')
print('2층에서 누군가가 종을 울렸다.\n'); input()
ps('SE/footstep.wav')
ps('SE/bear.wav')
print('눈이 없는 곰인형이 2층 복도를 돌아다니고 있다.\n'); input()
print(f'{name("에글리즈").call_name()}: 히익...!!\033[0m\n'); input()
print('곰인형이 이 쪽의 소리를 들은 것 같다.\n'); input()
ps('SE/fierce.wav')

ts(0.5)
bgm_play('tense')
print(f'{name("에글리즈").call_name()}: (어떡하지...)\033[0m\n'); input()
print('!!!\n'); input()
print(f'{name("에글리즈").call_name()}: (저 곰인형은 눈이 없으니까 날 공격하기 어려울 거야.)\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: (아까 얻은 {item("작은 나이프").call_item()}\033[3m로 처치해버리자.)\033[0m\n'); input()
ps('SE/footstep_another.wav')
ps('SE/fierce.wav')
ps('SE/puk.wav')
ps('SE/scream.wav')
bgm_stop()
print('눈이 없는 곰인형은 인간 같은 비명을 지르며 쓰러졌다.\n'); input()

while True:
  question_17 = input('곰 인형의 배를 가를까? '); print('')
  if question_17 == 'y':
    break
  elif question_17 == 'n':
    print(f'{name("에글리즈").call_name()}: 이번에도 무언가가 나올지도 몰라.\033[0m\n'); input()
    break
  else:
    continue

print('곰 인형 몸 속에 무언가가 있다.\n'); input()
ps('SE/get_item.wav')
print(f'{item("목각 인형의 상반신").call_item()}을 얻었다.\n'); input()
inven.append('목각 인형의 상반신')

while True:
  question_18 = input('목각 인형의 상반신과 하반신을 조립할까? '); print('')
  if question_18 == 'y':
    break
  elif question_18 == 'n':
    print(f'{name("에글리즈").call_name()}: 조립해서 인형 상자에 가져다 놓자.\033[0m\n'); input()
    break
  else:
    continue
ps('SE/crunch.wav')
ps('SE/get_item.wav')
print(f'{item("목각 인형").call_item()}을 획득했다.\n'); input()
inven.remove('목각 인형의 상반신')
inven.remove('목각 인형의 하반신')
inven.append('목각 인형')
print(f'{item("목각 인형").call_item()}의 입에서 종이 한 장이 나왔다.\n'); input()
ps('SE/get_item.wav')
print(f'{item("종이 조각4").call_item()}를 얻었다.'); input()
inven.append('종이 조각4')

print(f'{name("에글리즈").call_name()}: 드디어. 4개의 조각을 모두 모았어!\033[0m\n'); input()
print(f'{item("종이 조각4").call_item()}에는 \033[1m\033[3m"병사님 뿐이야."\033[0m이라고 적혀 있다.\n')
print('\033[3m\033[1m내 오르골을 돌릴 수 있는 건 오직 왕을 지키는 병사님 뿐이야.\033[0m')
print(f'{name("에글리즈").call_name()}: 병사님 뿐이라는 건 혹시, 오르골을 {item("병사의 태엽").call_item()}\033[3m으로 돌려야 한다는 건가?\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 흠...\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 너무 많이 돌아다녔더니 피곤하네...\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 내 방으로 들어가서 잠시 쉬어야 겠어.\033[0m\n'); input()
ps('SE/footstep.wav')
ps('SE/open_close.wav')

print(f'{name("에글리즈").call_name()}: ...\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 으...\033[0m', end="", flush=True); ts(1)
print(' 왠지 머리가 어질어질한데...\033[0m\n'); input()
print('침대 위로 쓰러졌다.\n'); input()

bgm_play('unknown_memory'); ts(2)
print(f'{name("데머너드").call_name()}: 오늘은 우리 예쁜 딸 {name("사리엘").call_name()}의 생일이네~.\033[0m\n'); input()
print(f'{name("사리엘").call_name()}: 와아아아~~~.\033[0m\n'); input()
print(f'{name("데머너드").call_name()}: 아빠의 선물은 ~~~.\033[0m\n'); input()
print(f'{name("사리엘").call_name()}: 성무른~?(선물은~?)\033[0m\n'); input()
print(f'{name("데머너드").call_name()}: 따라 부르기 쉬운 아빠의 자작곡이랍니다~~~.\033[0m\n'); input()
print(f'{name("사리엘").call_name()}: 와아아아~~~.\033[0m\n'); input()
print(f'{name("데머너드").call_name()}: 너의 네 번째 ~ 생일을 ~ 맞이했으니 ~\033[0m', end=""); input()
print(f'{name("데머너드").call_name()}: 가족 모두 ~ 오늘은 ~ 재밌게 놀자 ~\033[0m', end=""); input()
print(f'{name("데머너드").call_name()}: 날씨도 좋고 ~ 따뜻해 ~ 집 뒤에 있는 ~\033[0m', end=""); input()
print(f'{name("데머너드").call_name()}: 죽원에서 ~ 신나게 ~ 뛰어놀자 ~\033[0m', end=""); input()
print(f'{name("데머너드").call_name()}: 인형은 꼭 ~ 다음에 ~ 선물할게요 ~\033[0m', end=""); input()
print(f'{name("데머너드").call_name()}: 거짓말이 ~ 아니야 ~ 우리 공주님 ~\033[0m', end=""); input()
print(f'{name("데머너드").call_name()}: 야외에서 ~ 노는 게 ~ 기대가 되네 ~\033[0m'); input()
print(f'{name("사리엘").call_name()}: 와아아아~~~.\033[0m\n'); input()
print(f'{name("데머너드").call_name()}: 우리 공주님. 아빠의 자작곡 어때요?\033[0m\n'); input()
print(f'{name("사리엘").call_name()}: 좋아요~~~.\033[0m\n'); input()
print(f'{name("데머너드").call_name()}: 좋아요?\033[0m', end=""); ts(1)
print(' 가사에 숨겨진 비밀이 있는데~.\033[0m\n'); input()
print(f'{name("데머너드").call_name()}: 그 비밀이 무엇인지 알겠니?\033[0m\n'); input()
print(f'{name("사리엘").call_name()}: 으음~~~.\033[0m\n'); input()
print(f'{name("사리엘").call_name()}: 힌트! 힌트!\033[0m\n'); input()
bgm_stop()

bgm_play('Disappearance')
print(f'{name("데머너드").call_name()}: 하하하.\033[0m', end=""); ts(1)
print(' 그럼, 앞글자만 읽어보겠니?\033[0m\n'); input()
print(f'{name("사리엘").call_name()}: 아끌짜?(앞글자?)\033[0m\n'); input()
print(f'{name("사리엘").call_name()}: 음...\033[0m', end="", flush=True); ts(0.8)

for i in range(len(sariel)):
  print(f'{sariel[i]}..\033[0m', end="", flush=True); ts(0.8)
print('??\033[0m\n'); input('')

for i in range(len(demanad)):
  print(f'\033[31m\033[1m{demanad[i]}', end="", flush=True); ts(0.5)
print('\033[31m\033[1m.\033[0m\n'); ts(1)

bgm_stop()

print(f'{name("에글리즈").call_name()}: !!!!!!!\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 방금 그건...\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 꿈...\033[0m', end="", flush=True); ts(0.8)
print(' 이겠지...?\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: ???\033[0m\n'); input()

print('닫혀 있던 옷장 문이 열려 있다.\n'); input()
print('옷장 속에 작은 상자 하나가 있다.\n'); input()
ps('SE/get_item.wav')
print(f'{item("아리엘의 오르골").call_item()}을 얻었다.\n'); input()
inven.append('아리엘의 오르골')
print(f'{name("에글리즈").call_name()}: 이건...\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 그이가 아리엘에게 주었던 마지막 선물...\033[0m\n'); input()

while True:
  question_19 = input(f'{item("아리엘의 오르골").call_item()}을 재생시킬까? '); print('')
  if question_19 == 'y':
    break
  elif question_19 == 'n':
    print(f'{name("에글리즈").call_name()}: 그이가 생각이 나...\033[0m\n'); input()
    print(f'{name("에글리즈").call_name()}: 한 번만 재생해보자.\033[0m\n'); input()
    break
  else:
    continue

ps('SE/wound.wav')
bgm_play('orgel'); ts(4)
bgm_stop()
print(f'{name("에글리즈").call_name()}: ??\033[0m\n'); input()
print('오르골이 재생을 멈췄다.\n'); input()
print(f'{name("에글리즈").call_name()}: 고장이 난 건가...?\033[0m\n'); input()
ps('SE/close_door_fast.wav')
print(f'{name("에글리즈").call_name()}: !!!\033[0m\n'); input()
print('갑자기 방 문이 닫히더니 아무것도 보이지 않을 정도로 어두워졌다.\n'); input()
bgm_play('tense')
print(f'{name("에글리즈").call_name()}: 뭐야...\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 어떻게 된 거야...!!\033[0m\n'); input()
ps('SE/sururuk.wav')
print(f'{name("에글리즈").call_name()}: !!!\033[0m', end="", flush=True); ts(1)
print(' 방금 그건 무슨 소리였지?\033[0m\n'); input()
ps('SE/sururuk.wav')
print(f'{name("에글리즈").call_name()}: 뭐야...!!\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 아무나 살려줘!!\033[0m\n'); input()
ps('SE/sururuk.wav')
ps('SE/chulkung.wav')
ps('SE/knock.wav')
print(f'{name("에글리즈").call_name()}: 누군가 방 문을 열어줘!!\033[0m\n'); input()
ps('SE/sururuk.wav')
ps('SE/chulkung.wav')
ps('SE/chulkung.wav')
ps('SE/knock.wav')
print(f'{name("에글리즈").call_name()}: 누군가 방 ㅁ\033[0m\n'); ts(0.5)
bgm_stop()
ps('SE/koong.wav')
ps('SE/mashed.wav')
ts(3)

print('눈을 뜨니 침대에 쓰러져 있었다.\n'); input()
print(f'{name("에글리즈").call_name()}: 방금 그건...\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 꿈...\033[0m', end="", flush=True); ts(0.8)
print(' 이겠지...?\033[0m\n'); input()
print('?\n'); ts(1)
print('오른손에 무언가 있다.\n'); input()
print(f'{item("아리엘의 오르골").call_item()}이다.\n'); input()
print(f'{name("에글리즈").call_name()}: 하...\033[0m', end="", flush=True); ts(0.6)
print('하하...\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 꿈이 아니었네.\033[0m\n'); input()

print('\033[3m\033[1m내 오르골을 돌릴 수 있는 건 오직 왕을 지키는 병사님 뿐이야.\033[0m')
print(f'{name("에글리즈").call_name()}: !!!\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: {item("병사의 태엽").call_item()}\033[3m을 이 오르골에 끼워서 돌리면 되는 건가?\033[0m\n'); input()
ps('SE/wound.wav')
bgm_play('orgel')
print(f'{item("병사의 태엽").call_item()}을 {item("아리엘의 오르골").call_item()}에 끼워 재생했다.\n'); input()
inven.remove('병사의 태엽')
inven.remove('아리엘의 오르골')
for i in range(3):
  print("...", end="", flush=True); ts(1)
print("!"); input()
print('오르골에서 무슨 소리가 들리는 것 같다.\n'); input()

ps('SE/roar.wav')
print(f'{name("에글리즈").call_name()}: !!!!!!!\033[0m\n'); input()
ps('SE/glass_near.wav')
print('오르골을 창문 밖으로 던졌다.\n'); input()

bgm_play('ariel')
ps('SE/roar.wav')
print(f'{unknown}: 에글리즈!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m\n'); input()
ps('SE/glass_near.wav')
print(f'{unknown}: 내 오르골을 돌려서 날 꺼내주다니.\033[0m\n'); input()
print(f'{unknown}: 멍청한 년.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: "내"라니...', end="", flush=True); ts(0.6)
print(' 설마...', end="", flush=True); ts(0.8)
print(f' {name("아리엘").call_name()}이니...?\033[0m\n'); input()

ps('SE/roar.wav')
print(f'{ariel}: 닥쳐!!!!\033[0m\n'); input()
print(f'{ariel}: 너 같은 년한테서 내 이름 듣고 싶지 않아.\033[0m\n'); input()
print(f'{ariel}: 날 죽인 뒤 집마저 태워버리고,', end="", flush=True); ts(1)
print('어떻게 15년 동안 아무렇지 않게 살았어?\033[0m\n'); input()

print(f'{name("에글리즈").call_name()}: 아니야...', end="", flush=True); ts(0.5)
print('엄만 널 죽인 게 아니야.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 모이라님께서 널 구원해주시리라 믿고,', end="", flush=True); ts(1)
print('널 그 분께 보내기 위해 의식을 행한거야...!\033[0m\n'); input()
print(f'{ariel}: 역시 엄마는 정신이 나갔어.\033[0m\n'); input()
print(f'{ariel}: 엄마가 기도를 드리던 날부터 엄마는 미쳤어.\033[0m\n'); input()
print(f'{ariel}: 내가 동생을 죽인 뒤로,', end="", flush=True); ts(1)
print(' 얼마나 힘든 시간을 보냈는지 알아?\033[0m\n'); input()

print(f'{name("에글리즈").call_name()}: 아니야...\033[0m\n'); input()
print(f'{ariel}: 매일 밤마다 사리엘의 목소리가 들려왔어.\033[0m\n'); input()
print(f'{ariel}: 왜 죽였어?', end="", flush=True); ts(0.8)
print('왜 죽였어?', end="", flush=True); ts(0.8)
print(' 언니,', end="", flush=True); ts(0.5)
print(' 날 왜 죽였어?\033[0m\n'); input()

print(f'{name("에글리즈").call_name()}: 아니야....\033[0m\n'); input()
print(f'{ariel}: 사리엘이 태어난 뒤로', end="", flush=True); ts(0.8)
print(' 아빠의 사랑은 모두 사리엘한테로 갔어.\033[0m\n'); input()
print(f'{ariel}: 그래도 내 동생이니까', end="", flush=True); ts(0.8)
print(' 미워하지는 않았어.\033[0m\n'); input()

print(f'{name("에글리즈").call_name()}: 아니야.....\033[0m\n'); input()
print(f'{ariel}: 하지만 아빠가 돌아가시고나서부터', end="", flush=True); ts(1)
print(' 사리엘의 생일 때문이라는 생각이 자꾸 들었어.\033[0m\n'); input()
print(f'{ariel}: 사리엘의 잘못이 아니라는 거 아는데.\033[0m\n'); input()
print(f'{ariel}: 엄마가 나한테 세뇌를 했기 때문이야.\033[0m\n'); input()
print(f'{ariel}: 그 날 엄마가 내게 그런 말만 안 했어도...!\033[0m\n'); input()

print(f'{name("에글리즈").call_name()}: 아니야......!!!!!!!!!!!\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 모이라님의 말씀이 틀렸을 리 없어...\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 그래...', end="", flush=True); ts(0.5)
print(' 넌 내 딸이 아니야.\033[0m\n'); input()
print(f'{ariel}: 미쳤어...\033[0m\n'); input()
print(f'{ariel}: 역시 엄마는 여기서 죽어야 해.\033[0m\n'); input()
print('\033[3m\033[1m가족사진에 있는 네 딸을 죽여.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 난 너같은 딸을 낳은 적이 없단다...\033[0m\n'); input()

ps('SE/open_fast.wav')
print(f'{ariel}: 안 돼!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m\n'); input()
ps('SE/footstep_fast.wav')
ps('SE/sting_drawing.wav')
print(f'{item("작은 나이프").call_item()}로 가족사진에 있는 {name("아리엘").call_name()}\033[0m을 찔렀다.\n'); input()
ps('SE/ariel_scream.wav')
print(f'{ariel}: 아아ㅏ아아ㅏㅏ아ㅏ아ㅏㅏ아아ㅏ아ㅏㅏㅏ아아아ㅏㅏ아ㅏ아ㅏ아ㅏㅏ악!!!!!!!!!!!!!!!!!!!!!!!!\033[0m\n'); input()
bgm_stop()
ts(3)

print(f'{name("에글리즈").call_name()}: 그래...\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 이제 다 끝났어.\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 거봐,', end="",flush=True); ts(0.5)
print(' 아리엘.', end="", flush=True); ts(0.8)
print(' 모이라님의 말씀을 따르면', end="", flush=True); ts(0.8)
print(' 모든 게 잘 된다니까?\033[0m\n'); input()

ps('SE/open_door.wav')
print(f'{room("기도방").call_room()} 문이 열렸다.\n'); input()
print(f'{name("에글리즈").call_name()}: 아...', end="", flush=True); ts(0.5)
print(' 아...', end="", flush=True); ts(0.5)
print(' 모이라님...', end="", flush=True); ts(0.8)
print(' 곧바로 감사의 기도를 올리겠습니다.\033[0m\n'); input()

ps('SE/footstep.wav')
ps('SE/dark2.wav')
bgm_play('pray_room')
print(f'{name("에글리즈").call_name()}: ...???\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}: 그럴수가...\033[0m\n'); input()
ps('SE/dark1.wav')
print(f'{name("에글리즈").call_name()}: 하..', end="", flush=True); ts(0.5)
print('하하..', end="", flush=True); ts(0.5)
print('하하하하..', end="", flush=True); ts(0.5)
print('하하하하하하하하하하하하하하하하하하하하하하하!!!!!!!!!!!!\033[0m\n'); input()
print(f'{name("에글리즈").call_name()}\033[0m는 {item("작은 나이프").call_item()}로 자신의 목을 그었다.\n'); input()
ts(2)

print('기도방 벽면에 적힌 글이 있다.\n'); input()
print('\033[31m\033[1meglise = devotee\n'); input()
print('에글리즈 = 신을 믿는 신자\n'); input()
print('demanad = dead man\033[0m\n'); input()
print('de-man-ad = dead man\n'); input
ts(2)
bgm_stop()

print('Curse of Ariel\n\n'); input()
bgm_play('ending')

print('\033[1m\033[3m')
print('마을에서 조금 떨어진 곳,', end="", flush=True); ts(1)
print(' 조용하고 한적한 시골에서', end="", flush=True); ts(1)
print(' 에글리즈와 데마나드 부부는'); ts(1)
print('딸인 아리엘과 함께', end="", flush=True); ts(1)
print(' 셋이서 행복한 삶을 보내고 있었다.\n\n'); ts(1.5)

print('[xx07년]\n'); ts(1)
print('아리엘이 3살이 되는 해 4월 6일에', end="", flush=True); ts(1.5)
print( '여동생 사리엘이 태어난다.\n\n'); ts(1)

print('[xx11년 4월 6일]\n'); ts(1)
print('사리엘이 4살이 되는 해 아침,', end="", flush=True); ts(1.5)
print(' 사리엘은 생일선물로', end="", flush=True); ts(1)
print(' 데마나드의 자작곡을 선물로 받았다.\n'); ts(1.2)
print('사리엘은 언제든지 들을 수 있고', end="", flush=True); ts(1)
print(' 쉽게 따라 부를 수 있다며 기뻐했다.\n\n'); ts(1.5)

print('[xx14년 4월 6일]\n'); ts(1)
print('사리엘이 7살이 되는 해 아침', end="", flush=True); ts(1)
print(' 사리엘이 생일선물로', end="", flush=True); ts(0.7)
print(' 인형을 가지고 싶었는데', end="", flush=True); ts(0.8)
print(' 옷을 받아 속상한 마음에', end="", flush=True); ts(0.8)
print(' 데마나드에게 짜증을 냈다.'); ts(1.5)
print('데마나드는', end="", flush=True); ts(0.5)
print(' 사리엘의 풀이죽은 모습을 보고', end="", flush=True); ts(1.2)
print(' 마을에서 파는 인형을', end="", flush=True); ts(1)
print(' 사가지고 오기로 결심했다.'); ts(1.2)
print('그러나,', end="", flush=True); ts(0.5)
print(' 그 날 밤이 되어도', end="", flush=True); ts(0.8)
print(' 데마나드는 돌아오지 못했다.\n\n'); ts(1.5)

print('[xx14년 4월 7일]\n'); ts(1)
print('다음날 아침 에글리즈는', end="", flush=True); ts(1)
print(' 데마나드가 간다고 했던', end="", flush=True); ts(1)
print(' 그 마을을 향해 걸어갔다.\n'); ts(1.5)
print('집에서 출발한지 얼마 되지 않았을 때쯤', end="", flush=True); ts(1.5)
print(' 에글리즈는 바닥에 쓰러져 있는', end="", flush=True); ts(1)
print(' 데마나드를 발견했다.'); ts(1)
print('데마나드는 내장과 눈이 없었고', end="", flush=True); ts(1)
print(' 한쪽 손엔 인형이 있었다.'); ts(1)
print('들짐승에게 당한 것이라고 생각했다.'); ts(1.2)
print('집에 들어온 에글리즈는', end="", flush=True); ts(1)
print('사리엘에게 인형을 주었다.'); ts(1)
print('에글리즈는 충격에 빠져', end="", flush=True); ts(1)
print(' 며칠을 방에서 나오지 않았다.\n\n'); ts(1.2)

print('[xx14년 4월 18일]\n'); ts(1)
print('며칠 동안이나 제대로 된 식사를 못한 자매는', end="", flush=True); ts(1.5)
print(' 사소한 것에 서로 싸우게 되었다.'); ts(1.2)
print('그 소리를 듣다', end="", flush=True); ts(0.7)
print(' 결국 참지 못한 에글리즈는', end="", flush=True); ts(1)
print(' 방에서 나왔다.'); ts(0.7)
print('그녀는 아이들에게 진실을 얘기해주었고,', end="", flush=True); ts(1.2)
print(' 자매는 슬픔에 잠겨 하루를 보냈다.\n\n'); ts(1.2)

print('[xx14년 4월 19일]\n'); ts(1)
print('다음날 에글리즈는', end="", flush=True); ts(0.7)
print(' 마을에서 믿는다는 신의 종교에 빠져', end="", flush=True); ts(1.2)
print(' 매일 같이 기도를 올렸다.'); ts(1)
print('그 신의 이름은', end="", flush=True); ts(0.7)
print(' \033[1m"모이라"\033[0m],', end="", flush=True); ts(0.7)
print(' 사람의 운명을 결정하는 신이다.'); ts(1)
print('에글리즈는 기도를 올릴수록', end="", flush=True); ts(1)
print(' 머릿속에 무언가가 선명해져가는 기분을 느꼈다.\n\n'); ts(1.5)

print('[xx16년 2월 13일]\n'); ts(1)
print('기도를 올린지 666일이 되던 날,', end="", flush=True); ts(1)
print(' 에글리즈는 확신했다.'); ts(1)
print('데마나드를 죽인 것은', end="", flush=True); ts(1)
print(' \033[1m사리엘이라고.\033[0m'); ts(1)
print('사리엘이 그 날', end="", flush=True); ts(0.7)
print(' 데마나드에게 화를 내지만 않았어도', end="", flush=True); ts(1.2)
print(' 데마나드가 인형을 사러 가는 일이 없었을 것이라고.\ㅜ'); ts(2)

print('그 날 밤,', end="", flush=True); ts(0.7)
print(' 사리엘이 잠든 시각.'); ts(1)
print('에글리즈는', end="", flush=True); ts(0.5)
print(' 마을에서의 기도와 모임을 통해 알게 된', end="", flush=True); ts(1.5)
print(' 그 날의 날짜인 13의 의미.'); ts(1)
print('사리엘이 태어난 날짜인 4와 6의 의미.'); ts(1.2)

print('\033[31m13:', end="", flush=True); ts(0.5)
print(' "재탄생을 위해 몸을 던져라."', end="", flush=True); ts(1)
print('라는 뜻의 숫자\033[0m\n'); ts(0.8)
print('\033[31m4:', end="", flush=True); ts(0.5)
print('죽음을 의미하는 숫자'); ts(0.8)
print('\033[31m4:', end="", flush=True); ts(0.5)
print('악마가 좋아하는 숫자'); ts(0.8)

print('이 모든 것들을 설명해주었다.'); ts(1)
print('사리엘을 죽이면', end="", flush=True); ts(0.5)
print(' 데머너드가 돌아올 것이라는 말에', end="", flush=True); ts(1)
print(' 사리엘을 미워하는 마음이 너무 커졌다.'); ts(1.2)
print('어머니가 신에게서', end="", flush=True); ts(0.5)
print(' 진실을 들은 것이라고 생각한 아리엘은', end="", flush=True); ts(1)
print(' 그 날 밤,', end="", flush=True); ts(0.5)
print(' 자고 있던 사리엘을 죽였다.\n\n'); ts(1)

print('[xx16년 2월 21일\n'); ts(1)
print('일주일이 지나도 데머너드가 돌아오지 않자', end="", flush=True); ts(1)
print(' 아리엘은 에글리즈를 원망하게 되었고,'); ts(1)
print(' 그녀를 죽이려 시도했지만', end="", flush=True); ts(0.7)
print(' 에글리즈에게 제압 당해 죽임을 당했다.\n\n'); ts(1.5)

print('다음날 아침,', end="", flush=True); ts(0.5)
print('에글리즈는 집을 불 태우고 그 자리를 떠났다.\n'); ts(1.5)

print('[xx31년 2월 21일\n'); ts(1)
print('에글리즈가 이 집을 떠난지 15년이 지났다.\n'); ts(1.5)
print('정신을 차려 보니', end="", flush=True); ts(0.7)
print(' 창 밖엔 비가 내리고 있었고,', end="", flush=True); ts(1)
print(' 에글리즈는 부부방 침대 위에 있었다.'); ts(2)

bgm_stop()

bgm_play('credit')
print('옵저버: 김호준'); ts(0.5)
print('드라이버: 원성민'); ts(0.5)
print('기획: 김호준'); ts(0.5)
print('디버깅: 원성민'); ts(0.5)
print('스토리: 김호준'); ts(0.5)
print('배경음악: 김호준'); ts(0.5)
print('효과음: 김호준'); ts(0.5)
print('부부방: 김호준'); ts(0.5)
print('아리엘 방: 원성민'); ts(0.5)
print('사리엘 방: 원성민'); ts(0.5)
print('식당: 원성민'); ts(0.5)
print('2층 복도 책장: 원성민'); ts(0.5)
print('부엌: 김호준'); ts(0.5)
print('창고: 김호준'); ts(0.5)
print('기도방: 김호준'); ts(1.5)

print('플레이 해주셔서 감사합니다.'); ts(3)

bgm_stop()
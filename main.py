import csv

score = {}
for star in range(6) :
	score[star] = {}
	for lv in range(1,10) :
		score[star][lv] = (star+5)*(100 + 10*(lv-1))

flame = {}
light = {}
snow = {}
darkness = {}
with open('singer.csv', encoding="utf8") as singerFile :
	reader = csv.DictReader(singerFile)
	for singer in reader :
		# print(singer)
		if int(singer['level']) > 0 :
			flame[singer['singer']] = score[int(singer['Flame'])][int(singer['level'])]
			light[singer['singer']] = score[int(singer['Light'])][int(singer['level'])]
			snow[singer['singer']] = score[int(singer['Snow'])][int(singer['level'])]
			darkness[singer['singer']] = score[int(singer['Darkness'])][int(singer['level'])]

def printFirst(string, mydict, max=6) :
	print(string)
	mean = 0
	count = 0
	for key in sorted(mydict.items(), key=lambda x: x[1], reverse=True):
		print(key)
		count += 1
		mean += key[1]
		if count >= max :
			break
	return mean/max

mean = {'Flame':printFirst("flame: ", flame), 'Light':printFirst("light: " ,light), 'Snow':printFirst("snow: ", snow), 'Darkness':printFirst("darkness: ", darkness)}

def getSecond(str) :
	minute,second = str.split('.')
	return int(minute)*60 + int(second)

songList = {}
with open('song.csv', encoding="utf8") as songFile :
	reader = csv.DictReader(songFile)
	for song in reader :
		# print(song)
		second = getSecond(song['time'])
		songBestScore = (int(song['note'])*1.74684)*mean[song['element']]  # 1.74684 is a const. that make single combo
		songList[song['song']] = songBestScore/second

# print(songList)
printFirst("Song: ", songList, 20)
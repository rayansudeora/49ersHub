import random

#if __name__ == '__main__':
#	main()

def main():
	fourgames = []
	onegameconf = []
	onegameout = []
	threegames = []
	twogamesconf = []
	twogamesout = []

	fourgames.append(NFCDivision2())
	fourgames.append(AFCDivision2())
	fourgames.append(NFCConference())
	fourgames.append(AFCConference())
	fourgames.append(OutofConference())

	onegameconf.append(NFCConference())
	onegameconf.append(AFCConference())

	onegameout.append(OutofConference())

	threegames.append(NFCDivision1())
	threegames.append(AFCDivision1())
	threegames.append(NFCConference())
	threegames.append(AFCConference())
	threegames.append(OutofConference())

	twogamesconf.append(NFCDivision1())
	twogamesconf.append(AFCDivision1())
	twogamesconf.append(NFCConference())
	twogamesconf.append(AFCConference())

	twogamesout.append(NFCDivision1())
	twogamesout.append(AFCDivision1())
	twogamesout.append(OutofConference())

	return fourgames,onegameconf,onegameout,threegames,twogamesconf,twogamesout

def NFCDivision2():
	Random = False
	while not Random:
		nfcwest = ["49ers", "Seahawks", "Cardinals", "Rams"]
		random.shuffle(nfcwest)
		nfcwest2 = ["49ers", "Seahawks", "Cardinals", "Rams"]
		random.shuffle(nfcwest2)
		game1 = (nfcwest[0]+" at "+nfcwest[1])
		game2 = (nfcwest[2]+" at "+nfcwest[3])
		game3 = (nfcwest2[0]+" at "+nfcwest2[1])
		game4 = (nfcwest2[2]+" at "+nfcwest2[3])
		game1order=''.join(sorted(game1))
		game3order=''.join(sorted(game3))
		game4order=''.join(sorted(game4))
		if game1order==game3order or game1order==game4order or nfcwest[0]==nfcwest2[0] or nfcwest[0]==nfcwest2[2] or nfcwest[1]==nfcwest2[1] or nfcwest[1]==nfcwest2[3] or nfcwest2[0]==nfcwest[0] or nfcwest2[0]==nfcwest[2] or nfcwest2[1]==nfcwest[1] or nfcwest2[1]==nfcwest[3]:
			Random = False
		else:
			Random = True
			


	Random2 = False
	while not Random2:
		nfcsouth = ["Falcons", "Panthers", "Saints", "Buccaneers"]
		random.shuffle(nfcsouth)
		nfcsouth2 = ["Falcons", "Panthers", "Saints", "Buccaneers"]
		random.shuffle(nfcsouth2)
		game5 = (nfcsouth[0]+" at "+nfcsouth[1])
		game6 = (nfcsouth[2]+" at "+nfcsouth[3])
		game7 = (nfcsouth2[0]+" at "+nfcsouth2[1])
		game8 = (nfcsouth2[2]+" at "+nfcsouth2[3])
		game5order=''.join(sorted(game5))
		game7order=''.join(sorted(game7))
		game8order=''.join(sorted(game8))
		if game5order==game7order or game5order==game8order or nfcsouth[0]==nfcsouth2[0] or nfcsouth[0]==nfcsouth2[2] or nfcsouth[1]==nfcsouth2[1] or nfcsouth[1]==nfcsouth2[3] or nfcsouth2[0]==nfcsouth[0] or nfcsouth2[0]==nfcsouth[2] or nfcsouth2[1]==nfcsouth[1] or nfcsouth2[1]==nfcsouth[3]:
			Random2 = False
		else:
			Random2 = True

	Random3 = False
	while not Random3:
		nfcnorth = ["Bears", "Lions", "Packers", "Vikings"]
		random.shuffle(nfcnorth)
		nfcnorth2 = ["Bears", "Lions", "Packers", "Vikings"]
		random.shuffle(nfcnorth2)
		game9 = (nfcnorth[0]+" at "+nfcnorth[1])
		game10 = (nfcnorth[2]+" at "+nfcnorth[3])
		game11 = (nfcnorth2[0]+" at "+nfcnorth2[1])
		game12 = (nfcnorth2[2]+" at "+nfcnorth2[3])
		game9order=''.join(sorted(game9))
		game11order=''.join(sorted(game11))
		game12order=''.join(sorted(game12))
		if game9order==game11order or game9order==game12order or nfcnorth[0]==nfcnorth2[0] or nfcnorth[0]==nfcnorth2[2] or nfcnorth[1]==nfcnorth2[1] or nfcnorth[1]==nfcnorth2[3] or nfcnorth2[0]==nfcnorth[0] or nfcnorth2[0]==nfcnorth[2] or nfcnorth2[1]==nfcnorth[1] or nfcnorth2[1]==nfcnorth[3]:
			Random3 = False
		else:
			Random3 = True

	Random4 = False
	while not Random4:
		nfceast = ["Cowboys", "Giants", "Eagles", "Redskins"]
		random.shuffle(nfceast)
		nfceast2 = ["Cowboys", "Giants", "Eagles", "Redskins"]
		random.shuffle(nfceast2)
		game13 = (nfceast[0]+" at "+nfceast[1])
		game14 = (nfceast[2]+" at "+nfceast[3])
		game15 = (nfceast2[0]+" at "+nfceast2[1])
		game16 = (nfceast2[2]+" at "+nfceast2[3])
		game13order=''.join(sorted(game13))
		game15order=''.join(sorted(game15))
		game16order=''.join(sorted(game16))
		if game13order==game15order or game13order==game16order or nfceast[0]==nfceast2[0] or nfceast[0]==nfceast2[2] or nfceast[1]==nfceast2[1] or nfceast[1]==nfceast2[3] or nfceast2[0]==nfceast[0] or nfceast2[0]==nfceast[2] or nfceast2[1]==nfceast[1] or nfceast2[1]==nfceast[3]:
			Random4 = False
		else:
			Random4 = True
			return game1,game2,game3,game4,game5,game6,game7,game8,game9,game10,game11,game12,game13,game14,game15,game16

						
def NFCDivision1():

	Random = False
	while not Random:
		nfcwest = ["49ers", "Seahawks", "Cardinals", "Rams"]
		random.shuffle(nfcwest)
		game1 = (nfcwest[0]+" at "+nfcwest[1])
		game2 = (nfcwest[2]+" at "+nfcwest[3])
		Random=True
			
	Random2 = False
	while not Random2:
		nfcsouth = ["Falcons", "Panthers", "Saints", "Buccaneers"]
		random.shuffle(nfcsouth)
		game5 = (nfcsouth[0]+" at "+nfcsouth[1])
		game6 = (nfcsouth[2]+" at "+nfcsouth[3])
		Random2=True

	Random3 = False
	while not Random3:
		nfcnorth = ["Bears", "Lions", "Packers", "Vikings"]
		random.shuffle(nfcnorth)
		game9 = (nfcnorth[0]+" at "+nfcnorth[1])
		game10 = (nfcnorth[2]+" at "+nfcnorth[3])
		Random3=True

	Random4 = False
	while not Random4:
		nfceast = ["Cowboys", "Giants", "Eagles", "Redskins"]
		random.shuffle(nfceast)
		game13 = (nfceast[0]+" at "+nfceast[1])
		game14 = (nfceast[2]+" at "+nfceast[3])        
		Random4 = True
	return game1,game2,game5,game6,game9,game10,game13,game14

def AFCDivision1():
	

	Random = False
	while not Random:
		nfcwest = ["Broncos", "Chiefs", "Raiders", "Chargers"]
		random.shuffle(nfcwest)
		game1 = (nfcwest[0]+" at "+nfcwest[1])
		game2 = (nfcwest[2]+" at "+nfcwest[3])
		Random=True
			
	Random2 = False
	while not Random2:
		nfcsouth = ["Texans", "Colts", "Jaguars", "Titans"]
		random.shuffle(nfcsouth)
		game5 = (nfcsouth[0]+" at "+nfcsouth[1])
		game6 = (nfcsouth[2]+" at "+nfcsouth[3])
		Random2=True

	Random3 = False
	while not Random3:
		nfcnorth = ["Ravens", "Bengals", "Browns", "Steelers"]
		random.shuffle(nfcnorth)
		game9 = (nfcnorth[0]+" at "+nfcnorth[1])
		game10 = (nfcnorth[2]+" at "+nfcnorth[3])
		Random3=True

	Random4 = False
	while not Random4:
		nfceast = ["Bills", "Patriots", "Dolphins", "Jets"]
		random.shuffle(nfceast)
		game13 = (nfceast[0]+" at "+nfceast[1])
		game14 = (nfceast[2]+" at "+nfceast[3])        
		Random4 = True
	return game1,game2,game5,game6,game9,game10,game13,game14

def AFCDivision2():
  
	Random = False
	while not Random:
		nfcwest = ["Broncos", "Chargers", "Raiders", "Chiefs"]
		random.shuffle(nfcwest)
		nfcwest2 = ["Broncos", "Chargers", "Raiders", "Chiefs"]
		random.shuffle(nfcwest2)
		game1 = (nfcwest[0]+" at "+nfcwest[1])
		game2 = (nfcwest[2]+" at "+nfcwest[3])
		game3 = (nfcwest2[0]+" at "+nfcwest2[1])
		game4 = (nfcwest2[2]+" at "+nfcwest2[3])
		game1order=''.join(sorted(game1))
		game3order=''.join(sorted(game3))
		game4order=''.join(sorted(game4))
		if game1order==game3order or game1order==game4order or nfcwest[0]==nfcwest2[0] or nfcwest[0]==nfcwest2[2] or nfcwest[1]==nfcwest2[1] or nfcwest[1]==nfcwest2[3] or nfcwest2[0]==nfcwest[0] or nfcwest2[0]==nfcwest[2] or nfcwest2[1]==nfcwest[1] or nfcwest2[1]==nfcwest[3]:
			Random = False
		else:
			Random = True



	Random2 = False
	while not Random2:
		nfcsouth = ["Texans", "Titans", "Jaguars", "Colts"]
		random.shuffle(nfcsouth)
		nfcsouth2 = ["Texans", "Titans", "Jaguars", "Colts"]
		random.shuffle(nfcsouth2)
		game5 = (nfcsouth[0]+" at "+nfcsouth[1])
		game6 = (nfcsouth[2]+" at "+nfcsouth[3])
		game7 = (nfcsouth2[0]+" at "+nfcsouth2[1])
		game8 = (nfcsouth2[2]+" at "+nfcsouth2[3])
		game5order=''.join(sorted(game5))
		game7order=''.join(sorted(game7))
		game8order=''.join(sorted(game8))
		if game5order==game7order or game5order==game8order or nfcsouth[0]==nfcsouth2[0] or nfcsouth[0]==nfcsouth2[2] or nfcsouth[1]==nfcsouth2[1] or nfcsouth[1]==nfcsouth2[3] or nfcsouth2[0]==nfcsouth[0] or nfcsouth2[0]==nfcsouth[2] or nfcsouth2[1]==nfcsouth[1] or nfcsouth2[1]==nfcsouth[3]:
			Random2 = False
		else:
			Random2 = True
 

	Random3 = False
	while not Random3:
		nfcnorth = ["Ravens", "Bengals", "Steelers", "Browns"]
		random.shuffle(nfcnorth)
		nfcnorth2 = ["Ravens", "Bengals", "Steelers", "Browns"]
		random.shuffle(nfcnorth2)
		game9 = (nfcnorth[0]+" at "+nfcnorth[1])
		game10 = (nfcnorth[2]+" at "+nfcnorth[3])
		game11 = (nfcnorth2[0]+" at "+nfcnorth2[1])
		game12 = (nfcnorth2[2]+" at "+nfcnorth2[3])
		game9order=''.join(sorted(game9))
		game11order=''.join(sorted(game11))
		game12order=''.join(sorted(game12))
		if game9order==game11order or game9order==game12order or nfcnorth[0]==nfcnorth2[0] or nfcnorth[0]==nfcnorth2[2] or nfcnorth[1]==nfcnorth2[1] or nfcnorth[1]==nfcnorth2[3] or nfcnorth2[0]==nfcnorth[0] or nfcnorth2[0]==nfcnorth[2] or nfcnorth2[1]==nfcnorth[1] or nfcnorth2[1]==nfcnorth[3]:
			Random3 = False
		else:
			Random3 = True


	Random4 = False
	while not Random4:
		nfceast = ["Bills", "Patriots", "Jets", "Dolphins"]
		random.shuffle(nfceast)
		nfceast2 = ["Bills", "Patriots", "Jets", "Dolphins"]
		random.shuffle(nfceast2)
		game13 = (nfceast[0]+" at "+nfceast[1])
		game14 = (nfceast[2]+" at "+nfceast[3])
		game15 = (nfceast2[0]+" at "+nfceast2[1])
		game16 = (nfceast2[2]+" at "+nfceast2[3])
		game13order=''.join(sorted(game13))
		game15order=''.join(sorted(game15))
		game16order=''.join(sorted(game16))
		if game13order==game15order or game13order==game16order or nfceast[0]==nfceast2[0] or nfceast[0]==nfceast2[2] or nfceast[1]==nfceast2[1] or nfceast[1]==nfceast2[3] or nfceast2[0]==nfceast[0] or nfceast2[0]==nfceast[2] or nfceast2[1]==nfceast[1] or nfceast2[1]==nfceast[3]:
			Random4 = False
		else:
			Random4 = True

	return game1,game2,game3,game4,game5,game6,game7,game8,game9,game10,game11,game12,game13,game14,game15,game16
			
def NFCConference():

	nfcwest = ["49ers", "Seahawks", "Cardinals", "Rams"]
	nfcsouth = ["Falcons", "Panthers", "Saints", "Buccaneers"]
	nfcnorth = ["Bears", "Lions", "Packers", "Vikings"]
	nfceast = ["Cowboys", "Giants", "Eagles", "Redskins"]
	nfcteams = ["Cowboys", "Giants", "Eagles", "Redskins", "Bears", "Lions", "Packers", 'Vikings', 'Falcons', 'Panthers', 'Saints', 'Buccaneers', "Cardinals", 'Rams', '49ers', 'Seahawks']

	Random = False
	while not Random:
		random.shuffle(nfcteams)
		game1 = (nfcteams[0]+" at "+nfcteams[1])
		game2 = (nfcteams[2]+" at "+nfcteams[3])
		game3 = (nfcteams[4]+" at "+nfcteams[5])
		game4 = (nfcteams[6]+" at "+nfcteams[7])
		game5 = (nfcteams[8]+" at "+nfcteams[9])
		game6 = (nfcteams[10]+" at "+nfcteams[11])
		game7 = (nfcteams[12]+" at "+nfcteams[13])
		game8 = (nfcteams[14]+" at "+nfcteams[15])
		if nfcteams[0] in nfcwest and nfcteams[1] in nfcwest or nfcteams[0] in nfceast and nfcteams[1] in nfceast or nfcteams[0] in nfcnorth and nfcteams[1] in nfcnorth or nfcteams[0] in nfcsouth and nfcteams[1] in nfcsouth or nfcteams[2] in nfcwest and nfcteams[3] in nfcwest or nfcteams[2] in nfceast and nfcteams[3] in nfceast or nfcteams[2] in nfcnorth and nfcteams[3] in nfcnorth or nfcteams[2] in nfcsouth and nfcteams[3] in nfcsouth or nfcteams[4] in nfcwest and nfcteams[5] in nfcwest or nfcteams[4] in nfceast and nfcteams[5] in nfceast or nfcteams[4] in nfcnorth and nfcteams[5] in nfcnorth or nfcteams[4] in nfcsouth and nfcteams[5] in nfcsouth or nfcteams[6] in nfcwest and nfcteams[7] in nfcwest or nfcteams[6] in nfceast and nfcteams[7] in nfceast or nfcteams[6] in nfcnorth and nfcteams[7] in nfcnorth or nfcteams[6] in nfcsouth and nfcteams[7] in nfcsouth or nfcteams[8] in nfcwest and nfcteams[9] in nfcwest or nfcteams[8] in nfceast and nfcteams[9] in nfceast or nfcteams[8] in nfcnorth and nfcteams[9] in nfcnorth or nfcteams[8] in nfcsouth and nfcteams[9] in nfcsouth or nfcteams[10] in nfcwest and nfcteams[11] in nfcwest or nfcteams[10] in nfceast and nfcteams[11] in nfceast or nfcteams[10] in nfcnorth and nfcteams[11] in nfcnorth or nfcteams[10] in nfcsouth and nfcteams[11] in nfcsouth or nfcteams[12] in nfcwest and nfcteams[13] in nfcwest or nfcteams[12] in nfceast and nfcteams[13] in nfceast or nfcteams[12] in nfcnorth and nfcteams[13] in nfcnorth or nfcteams[12] in nfcsouth and nfcteams[13] in nfcsouth or nfcteams[14] in nfcwest and nfcteams[15] in nfcwest or nfcteams[14] in nfceast and nfcteams[15] in nfceast or nfcteams[14] in nfcnorth and nfcteams[15] in nfcnorth or nfcteams[15] in nfcsouth and nfcteams[15] in nfcsouth:
			Random = False
		else:
			Random = True

	return game1,game2,game3,game4,game5,game6,game7,game8
			
def AFCConference():
	afcwest = ["Broncos", "Chiefs", "Raiders", "Chargers"]
	afcsouth = ["Texans", "Colts", "Jaguars", "Titans"]
	afcnorth = ["Ravens", "Bengals", "Browns", "Steelers"]
	afceast = ["Bills", "Dolphins", "Patriots", "Jets"]
	afcteams = ["Bills", "Dolphins", "Patriots", "Jets", "Ravens", "Bengals", "Browns", "Steelers", "Texans", "Colts", "Jaguars", "Titans", "Broncos", "Chiefs", "Raiders", "Chargers"]

	Random = False
	while not Random:
		random.shuffle(afcteams)
		game1 = (afcteams[0]+" at "+afcteams[1])
		game2 = (afcteams[2]+" at "+afcteams[3])
		game3 = (afcteams[4]+" at "+afcteams[5])
		game4 = (afcteams[6]+" at "+afcteams[7])
		game5 = (afcteams[8]+" at "+afcteams[9])
		game6 = (afcteams[10]+" at "+afcteams[11])
		game7 = (afcteams[12]+" at "+afcteams[13])
		game8 = (afcteams[14]+" at "+afcteams[15])
		if afcteams[0] in afcwest and afcteams[1] in afcwest or afcteams[0] in afceast and afcteams[1] in afceast or afcteams[0] in afcnorth and afcteams[1] in afcnorth or afcteams[0] in afcsouth and afcteams[1] in afcsouth or afcteams[2] in afcwest and afcteams[3] in afcwest or afcteams[2] in afceast and afcteams[3] in afceast or afcteams[2] in afcnorth and afcteams[3] in afcnorth or afcteams[2] in afcsouth and afcteams[3] in afcsouth or afcteams[4] in afcwest and afcteams[5] in afcwest or afcteams[4] in afceast and afcteams[5] in afceast or afcteams[4] in afcnorth and afcteams[5] in afcnorth or afcteams[4] in afcsouth and afcteams[5] in afcsouth or afcteams[6] in afcwest and afcteams[7] in afcwest or afcteams[6] in afceast and afcteams[7] in afceast or afcteams[6] in afcnorth and afcteams[7] in afcnorth or afcteams[6] in afcsouth and afcteams[7] in afcsouth or afcteams[8] in afcwest and afcteams[9] in afcwest or afcteams[8] in afceast and afcteams[9] in afceast or afcteams[8] in afcnorth and afcteams[9] in afcnorth or afcteams[8] in afcsouth and afcteams[9] in afcsouth or afcteams[10] in afcwest and afcteams[11] in afcwest or afcteams[10] in afceast and afcteams[11] in afceast or afcteams[10] in afcnorth and afcteams[11] in afcnorth or afcteams[10] in afcsouth and afcteams[11] in afcsouth or afcteams[12] in afcwest and afcteams[13] in afcwest or afcteams[12] in afceast and afcteams[13] in afceast or afcteams[12] in afcnorth and afcteams[13] in afcnorth or afcteams[12] in afcsouth and afcteams[13] in afcsouth or afcteams[14] in afcwest and afcteams[15] in afcwest or afcteams[14] in afceast and afcteams[15] in afceast or afcteams[14] in afcnorth and afcteams[15] in afcnorth or afcteams[15] in afcsouth and afcteams[15] in afcsouth:
			Random = False
		else:
			Random = True

	return game1,game2,game3,game4,game5,game6,game7,game8

			
def OutofConference():
	afcteams = ["Bills", "Dolphins", "Patriots", "Jets", "Ravens", "Bengals", "Browns", "Steelers", "Texans", "Colts", "Jaguars", "Titans", "Broncos", "Chiefs", "Raiders", "Chargers"]
	nfcteams = ["Cowboys", "Giants", "Eagles", "Redskins", "Bears", "Lions", "Packers", 'Vikings', 'Falcons', 'Panthers', 'Saints', 'Buccaneers', "Cardinals", 'Rams', '49ers', 'Seahawks']
	nflteams = ["Bills", "Dolphins", "Patriots", "Jets", "Ravens", "Bengals", "Browns", "Steelers", "Texans", "Colts", "Jaguars", "Titans", "Broncos", "Chiefs", "Raiders", "Chargers", "Cowboys", "Giants", "Eagles", "Redskins", "Bears", "Lions", "Packers", 'Vikings', 'Falcons', 'Panthers', 'Saints', 'Buccaneers', "Cardinals", 'Rams', '49ers', 'Seahawks']
	Random = False
	while not Random:
		random.shuffle(nflteams)
		game1 = (nflteams[0]+" at "+nflteams[1])
		game2 = (nflteams[2]+" at "+nflteams[3])
		game3 = (nflteams[4]+" at "+nflteams[5])
		game4 = (nflteams[6]+" at "+nflteams[7])
		game5 = (nflteams[8]+" at "+nflteams[9])
		game6 = (nflteams[10]+" at "+nflteams[11])
		game7 = (nflteams[12]+" at "+nflteams[13])
		game8 = (nflteams[14]+" at "+nflteams[15])
		game9 = (nflteams[16]+" at "+nflteams[17])
		game10 = (nflteams[18]+" at "+nflteams[19])
		game11 = (nflteams[20]+" at "+nflteams[21])
		game12 = (nflteams[22]+" at "+nflteams[23])
		game13 = (nflteams[24]+" at "+nflteams[25])
		game14 = (nflteams[26]+" at "+nflteams[27])
		game15 = (nflteams[28]+" at "+nflteams[29])
		game16 = (nflteams[30]+" at "+nflteams[31])
		if nflteams[0] in afcteams and nflteams[1] in afcteams or nflteams[0] in nfcteams and nflteams[1] in nfcteams or nflteams[2] in afcteams and nflteams[3] in afcteams or nflteams[2] in nfcteams and nflteams[3] in nfcteams or nflteams[4] in afcteams and nflteams[5] in afcteams or nflteams[4] in nfcteams and nflteams[5] in nfcteams or nflteams[6] in afcteams and nflteams[7] in afcteams or nflteams[6] in nfcteams and nflteams[7] in nfcteams or nflteams[8] in afcteams and nflteams[9] in afcteams or nflteams[8] in nfcteams and nflteams[9] in nfcteams or nflteams[10] in afcteams and nflteams[11] in afcteams or nflteams[10] in nfcteams and nflteams[11] in nfcteams or nflteams[12] in afcteams and nflteams[13] in afcteams or nflteams[12] in nfcteams and nflteams[13] in nfcteams or nflteams[14] in afcteams and nflteams[15] in afcteams or nflteams[14] in nfcteams and nflteams[15] in nfcteams or nflteams[16] in afcteams and nflteams[17] in afcteams or nflteams[16] in nfcteams and nflteams[17] in nfcteams or nflteams[18] in afcteams and nflteams[19] in afcteams or nflteams[18] in nfcteams and nflteams[19] in nfcteams or nflteams[20] in afcteams and nflteams[21] in afcteams or nflteams[20] in nfcteams and nflteams[21] in nfcteams or nflteams[22] in afcteams and nflteams[23] in afcteams or nflteams[22] in nfcteams and nflteams[23] in nfcteams or nflteams[24] in afcteams and nflteams[25] in afcteams or nflteams[25] in nfcteams and nflteams[25] in nfcteams or nflteams[26] in afcteams and nflteams[27] in afcteams or nflteams[26] in nfcteams and nflteams[27] in nfcteams or nflteams[28] in afcteams and nflteams[29] in afcteams or nflteams[28] in nfcteams and nflteams[29] in nfcteams or nflteams[30] in afcteams and nflteams[31] in afcteams or nflteams[30] in nfcteams and nflteams[31] in nfcteams:
			Random = False
		else:
			Random = True

	return game1,game2,game3,game4,game5,game6,game7,game8,game9,game10,game11,game12,game13,game14,game15,game16







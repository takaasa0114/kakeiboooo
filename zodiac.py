text="子 丑 寅 卯 辰 巳 午 未 申 酉 戌 亥"
zodiac=(text.split(" "))
uzodiac=str(input("あなたの干支は"))
zodiacnumber=int(zodiac.index(uzodiac))
print(zodiac[((zodiacnumber+4)%12):((zodiacnumber+5)%12)])
print(zodiac[((zodiacnumber+8)%12):((zodiacnumber+9)%12)])

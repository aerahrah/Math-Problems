
# a=int(input("input first value: "))
# b=int(input("input second value: "))
# c=int(input("input third value: "))
# d=int(input("input fourth value: "))
     

# if((a == b and c == d)or(a==c and b==d)or(c==b and a==d)):
#     print("Two Pair")  
# else:
#     print("not two pair")
        
      
season = int(input("Enter month in integer: "))
day = int(input("Enter day: "))
if(season == 1 or season == 2 or season == 3):
    season = "winter"
elif(season == 4 or season == 5 or season == 6):
    season = "spring"
elif(season == 7 or season == 8 or season == 9):
    season = "summer"
elif(season == 10 or season == 11 or season == 12):
    season = "fall"
if( day%3 == 0 and day>= 21):
    if(season == "winter"):
        season = "spring"
    elif(season == "spring"):
        season = "summer"
    elif(season == "summer"):
        season = "fall"
    elif(season == "fall"):
        season = "winter"
    print(season)
else:
    print(season)


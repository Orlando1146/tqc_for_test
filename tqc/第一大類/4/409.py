某次選舉有兩位候選人，分別是No.1: Nami、No.2: Chopper。請撰寫一程式，輸入五張選票，輸入值如為1即表示針對1號候選人投票；
輸入值如為2即表示針對2號候選人投票，如輸入其他值則視為廢票。每次投完後需印出目前每位候選人的得票數，最後印出最高票者為當選人；
如最終計算有相同的最高票數者或無法選出最高票者，顯示【=> No one won the election.】。
nami=cho=null=0
for vot in range(5):
    tick=eval(input())
    if tick ==1:
        nami+=1
    elif tick ==2:
        cho+=1
    else:
        null+=1
    print(f"Total votes of No.1: Nami =  {nami}\nTotal votes of No.2: Chopper =  {cho}\nTotal null votes = {null}")
if nami > cho :
    print("=>No1 Nami won the election.")
elif nami == cho:
    print("=> No one won the election.")
else:
    print("=> No2 Chopper won the election.")
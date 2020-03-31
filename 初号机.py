backpack={}
class airplaneError(Exception):
    pass
class behaviorError(Exception):
    pass
class code():
    def __init__(self,sth):
        self.__ind=0
        self.text=[i for i in sth.lower().split('\n') if i != '']
        self.meanList=[]
        for i in range(0,len(self.text)):
            self.meanList.append(self.text[i].split())
    def FenXi(self):
        willR=''
        if (self.meanList[0][0]=='come' and 'island' in self.meanList[0])and(self.meanList[-1][0]=='leave' and 'island' in self.meanList[-1]):
            willR+='#start\n'
            for i in self.meanList[1:]:
                if i[0]=='god' and i[1]=='create' and len(i)==3:
                    willR+='    '*self.__ind+"backpack['{}']=0".format(i[2])+'\n'
                elif i[0]=='use' and len(i)==4:
                    if i[2]=='mix':
                        willR+='    '*self.__ind+"backpack['{}']+=backpack['{}']".format(i[3],i[1])+'\n'
                    elif i[2]=='cut':
                        willR+='    '*self.__ind+"backpack['{}']-=backpack['{}']".format(i[3],i[1])+'\n'
                        willR+='    '*self.__ind+"if backpack['{}']<0:".format(i[3])+'\n'
                        willR+='    '*(self.__ind+1)+r'''raise behaviorError("You can't do that on the island\n")'''+'\n'
                    elif i[2]=='fry':
                        willR+='    '*self.__ind+"backpack['{}']*=backpack['{}']".format(i[3],i[1])+'\n'
                    elif i[2]=='rape':
                        willR+='    '*self.__ind+"backpack['{}']/=backpack['{}']".format(i[3],i[1])+'\n'
                    elif i[2]=='fold':
                        willR+='    '*self.__ind+"backpack['{}']**=backpack['{}']".format(i[3],i[1])+'\n'
                    elif i[2]=='hit':
                        willR+='    '*self.__ind+"backpack['{}']//=backpack['{}']".format(i[3],i[1])+'\n'
                    elif i[2]=='fray':
                        willR+='    '*self.__ind+"backpack['{}']%=backpack['{}']".format(i[3],i[1])+'\n'
                    elif i[2]=='feign':
                        willR+='    '*self.__ind+"backpack['{}']=backpack['{}']".format(i[3],i[1])+'\n'
                    elif i[2]=='swap':
                        willR+='    '*self.__ind+"backpack['{0}'],backpack['{1}']=backpack['{1}'],backpack['{0}']".format(i[3],i[1])+'\n'
                    elif i[2]=='fight':
                        willR+='    '*self.__ind+"backpack['{0}']=max(backpack['{1}'],backpack['{0}'])".format(i[3],i[1])+'\n'
                    elif i[2]=='bicker':
                        willR+='    '*self.__ind+"backpack['{0}']=min(backpack['{1}'],backpack['{0}'])".format(i[3],i[1])+'\n'
                elif i[0]=='get' and len(i)==3:
                    willR+='    '*self.__ind+"backpack['{}']+={}".format(i[2],i[1])+'\n'
                elif i[0]=='eat' and len(i)==3:
                    willR+='    '*self.__ind+"backpack['{}']-={}".format(i[2],i[1])+'\n'
                    willR+='    '*self.__ind+"if backpack['{}']<0:".format(i[2])+'\n'
                    willR+='    '*(self.__ind+1)+r'''raise behaviorError("You can't do that on the island\n")'''+'\n'
                elif i[0]=='need' and len(i)==2:
                    willR+='    '*self.__ind+"backpack['{}']=int(input())".format(i[1])+'\n'
                elif i[0]=='pick' and len(i)==2:
                    willR+='    '*self.__ind+"backpack['{}']=ord(input())".format(i[1])+'\n'
                elif i[0]=='share' and len(i)==3:
                    if i[1]=='monkey':
                        willR+='    '*self.__ind+"print(backpack['{}'])".format(i[2])+'\n'
                    elif i[1]=='human':
                        willR+='    '*self.__ind+"print(chr(backpack['{}']),end='')".format(i[2])+'\n'
                elif i[0]=='judge' and i[1]=='have' and i[-1]=='then' and len(i)==5:
                    willR+='    '*self.__ind+"if backpack['{1}']=={0}:".format(i[2],i[3])+'\n'
                    self.__ind+=1
                elif i[0]=='eat' and i[2]=='till' and i[-1]=='empty' and len(i)==4:
                    willR+='    '*self.__ind+"while backpack['{}']!=0:".format(i[1])+'\n'
                    self.__ind+=1
                    willR+='    '*self.__ind+"backpack['{}']-=1".format(i[1])+'\n'
                elif i[0]=='do' and i[1]=='till' and i[2]=='have' and len(i)==5:
                    willR+='    '*self.__ind+"while backpack['{}']!={}:".format(i[4],i[3])+'\n'
                    self.__ind+=1
                elif (i[0]=='end' or i[0]=='again')and len(i)==1:
                    self.__ind-=1
                elif i[0]=='leave' and 'island' in i:
                    willR+='#end'
##                else:
##                    willR+='    '*self.__ind+r'''raise behaviorError("You can't do that on the island\n")'''+'\n'
        else:
            willR=r'''raise airplaneError("You didn't land or leave the island properly\n")'''+'\n'
        return willR
###########################################################
with open('isl.island','r',encoding='utf-8') as f:
    try:
        exec(code(f.read()).FenXi())
    except BaseException as error:
        print('发生错误：{}'.format(error))
print('\nTEST:',backpack)
input()

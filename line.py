# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token='EkmfOIpoeCijfSyGd08a.+oB38GWyDcfEJ2pdUvGh2G.FJqxyRU2uP9hWnu4nciMGC2RC5Adp+n3oNCpB2dZTbM=')
cl.loginResult()

kc = LINETCR.LINE()
kc.login(token='EkfRXrHkBS6HRnw358o8.Tz8IGemBO2GJbmx0LFTDka.n/pbInR7vFeoykl+xZIrC/iNaIn8s+RtgIBz2cvpP24=')
kc.loginResult()

kk = LINETCR.LINE()
kk.login(token='Ek3wFPSsBYjopI8wSBs9.ymwVrvVFUkfRyEAsNMAW2q.Urle+NHKrrpqPaL9MYbQUinpoD5hAz0wg6UQgEllM+4=')
kk.loginResult()

ki = LINETCR.LINE()
ki.login(token='Ek14p3E9otKlJ5hPMe8b.tiosdnNgoYYYlzTul8ZR2W.pTahOUfBkf1ozPV/shKf9ljinVQtTtVhZu1Wie6Y/UQ=')
ki.loginResult()

ks = LINETCR.LINE()
ks.login(token='EkRXtyrehkVYuqaHwyR6.X0acdtz2tGaEZ4a/flc79G.rWbBrdBsYNECcVPqfFCuOBSTJaYz1WP0cjn+W3DbRp8=')
ks.loginResult()

kz = LINETCR.LINE()
kz.login(token='EkfP7iPioYBaeCCunmh5.w5xRziKx+M1DszXyHWp91q.qrYC1SgqgXhepm3mBCh6NdMxhVA5VRFY5kVInTluj1U=')
kz.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" Bot Key
[Id︎]
[Mid]
[Me︎]
[TL︎:「Text」]
[Mc 「mid」]
[K on/off]
[Join︎ on/off]
[Gcancel:︎「Number of people」]
[Group cancelalll︎]
[Leave︎ on/off]
[Add on/off]
[Share on/off]
[Message change:「text」]
[Message check]
[Confirm]
[Jam on/off]
[Change clock:「name」]
[Up]
[Cv join]

[*] Command in the groups [*]

[Curl]
[Ourl]
[url]
[url:「Group ID」]
[Invite：「mid」]
[Kick：「mid」]
[Ginfo]
[jointicket]
[Cancel]
[Gn 「group name」]
[Nk 「name」]

[*] Command Owner only [*]

[Bye]
[Kill ban]
[Kill 「@」]
[Ban 「@」] By Tag
[Unban 「@」] By Tag
[Ban︎] Share Contact
[Unban︎] Share Contact
[Banlist︎]
[Cek ban]
[Cv mid]
[Cv ︎invite:「mid」]
[Cv ︎rename:「name」]
[Cv ︎gift]
[Respo︎n]
[Bot cancel]
[Title:]
"""
KAC=[cl,ki,kk,kc,ks,kz]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
Emid = kz.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid]
admin=["uc9601a92d1616bcfbe9243127b6ad47f"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"Rem ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "proteksi":True,
    "proteksiinvite":True, 
    "atjointicket":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = ks.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        
                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = kz.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kz.updateGroup(X)
                        Ti = kz.reissueGroupTicket(op.param1)
                        ks.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kz.updateGroup(X)
                        Ti = kz.reissueGroupTicket(op.param1)
                        
                if op.param3 in Emid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kz.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
     
        if op.type == 19:
            if op.param3 in admin:
                cl.kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1,[op.param3])	 
        if op.type == 13:
            if op.param2 not in admin:
            	if wait["proteksi invite"] == True:
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    cl.kickoutFromGroup(op.param1,[op.param2])
                
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 11: 
            if op.param2 not in Bots:
                if op.param2 not in admin:
                	if wait["proteksi"] == True:
                         G = cl.getGroup(op.param1)
                         G.preventJoinByTicket = True
                         cl.updateGroup(G)
                         cl.kickoutFromGroup(op.param1,[op.param2])
        	
        if op.type == 19:
            if op.param2 not in admin:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        ks.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kz.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kz.updateGroup(X)
                    Ti = kz.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ks.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ks.updateGroup(G)
                    Ticket = ks.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kz.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kz.updateGroup(G)
                    Ticket = kz.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            if msg.text in ["panggil semua"]:

                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]

                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(6)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(7)
                    akh = akh + 1
                    cb2 += "@nrik \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        #ki.sendText(msg.to,"deleted")
                        #kk.sendText(msg.to,"deleted")
                        #kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        #ki.sendText(msg.to,"It is not in the black list")
                        #kk.sendText(msg.to,"It is not in the black list")
                        #kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        #ki.sendText(msg.to,"already")
                        #kk.sendText(msg.to,"already")
                        #kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        #ki.sendText(msg.to,"aded")
                        #kk.sendText(msg.to,"aded")
                        #kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        #ki.sendText(msg.to,"deleted")
                        #kk.sendText(msg.to,"deleted")
                        #kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        #ki.sendText(msg.to,"It is not in the black list")
                        #kk.sendText(msg.to,"It is not in the black list")
                        #kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["/Key","/help","/Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
                 if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                 else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Kurumi gn " in msg.text):
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Kurumi gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Katou gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Katou gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Hatsune gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Hatsune gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif ("Megumin gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Megumin gn ","")
                    kz.updateGroup(X)
                else:
                    kz.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
            	if msg.from_ in admin:
                    midd = msg.text.replace("Kick ","")
                    cl.kickoutFromGroup(msg.to,[midd])
            elif "Kurumi kick " in msg.text:
            	if msg.from_ in admin:
                    midd = msg.text.replace("Kurumi kick ","")
                    ki.kickoutFromGroup(msg.to,[midd])
            elif "Katou kick " in msg.text:
            	if msg.from_ in admin:
                    midd = msg.text.replace("Katou kick ","")
                    kk.kickoutFromGroup(msg.to,[midd])
            elif "Hatsune kick " in msg.text:
            	if msg.from_ in admin:
                    midd = msg.text.replace("Hatsune kick ","")
                    kc.kickoutFromGroup(msg.to,[midd])
            elif "Ram kick " in msg.text:
            	if msg.from_ in admin:
                    midd = msg.text.replace("Ram kick ","")
                    ks.kickoutFromGroup(msg.to,[midd])
            elif "Megumin kick " in msg.text:
            	if msg.from_ in admin:
                    midd = msg.text.replace("Megumin kick ","")
                    kz.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Kurumi invite " in msg.text:
                midd = msg.text.replace("Kurumi invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Katou invite " in msg.text:
                midd = msg.text.replace("Katou invite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Hatsune invite " in msg.text:
                midd = msg.text.replace("Hatsune invite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif "Ram invite " in msg.text:
                midd = msg.text.replace("Ram invite ","")
                ks.findAndAddContactsByMid(midd)
                ks.inviteIntoGroup(msg.to,[midd])
            elif "Megumin invite " in msg.text:
                midd = msg.text.replace("Megumin invite ","")
                kz.findAndAddContactsByMid(midd)
                kz.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["Cv1"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif msg.text in ["Cv2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","rem gift","Rem gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Kurumi gift","kurumi gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Katou gift","katou gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","hatsune gift","Hatsune gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","megumin gift","Megumin gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                kz.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                ks.sendMessage(msg)
                kz.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 ourl","Cv1 link on"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 ourl","Cv2 link on"]:
                if msg.from_ in admin:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done")
                    else:
                        kk.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 ourl","Cv3 link on"]:
                if msg.from_ in admin:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off"]:
                 if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                 else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 curl","Cv1 link off"]:
                if msg.from_ in admin:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 curl","Cv2 link off"]:
                if msg.from_ in admin:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 curl","Cv3 link off"]:
                if msg.from_ in admin:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif msg.text in["mid ku","Mid ku"]:
                cl.sendText(msg.to,msg.from_)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
                kz.sendText(msg.to,Emid)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Kurumi mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "Katou mid" == msg.text:
                kk.sendText(msg.to,Bmid)
            elif "Hatsune mid" == msg.text:
                kc.sendText(msg.to,Cmid)
            elif "Ram mid" == msg.text:
                ks.sendText(msg.to,Dmid)
            elif "Megumin mid" == msg.text:
            	kz.sendText(msg.to,Emid)
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe","hahaha"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Sedih","sedih"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv1 rename "]:
                string = msg.text.replace("Cv1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv2 rename "]:
                string = msg.text.replace("Cv2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
            	if msg.from_ in admin:
                    if wait["contact"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["contact"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
            	if msg.from_ in admin:
                    if wait["contact"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done ")
                    else:
                        wait["contact"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Proteksi invite on","proteksi invite on"]:
                if msg.from_ in admin:
                    if wait["proteksiinvite"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Proteksi invite mode ON")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["proteksiinvite"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Aktif")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Proteksi invite off","proteksi invite off"]:
                if msg.from_ in admin:
                    if wait["proteksiinvite"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Proteksi invite mode OFF")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["proteksiinvite"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Non-Aktif")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Proteksi on","proteksi on"]:
                if msg.from_ in admin:
                    if wait["proteksi"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Proteksi mode ON")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["proteksi"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Aktif")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Proteksi off","proteksi off"]:
                if msg.from_ in admin:
                    if wait["proteksi"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Proteksi mode OFF")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["proteksi"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Non-Aktif")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Set"]:
                if msg.from_ in admin:
                    md = ""
                    if wait["proteksiinvite"] == True: md+=" Proteksi invite : on\n"
                    else: md+=" Proteksi invite : off\n"
                    if wait["proteksi"] == True: md+=" Proteksi : on\n"
                    else: md+=" Proteksi : off\n"
                    if wait["contact"] == True: md+=" Contact : on\n"
                    else: md+=" Contact : off\n"
                    if wait["autoJoin"] == True: md+=" Auto join : on\n"
                    else: md +=" Auto join : off\n"
                    if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                    else: md+= " Group cancel : off\n"
                    if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
                    else: md+=" Auto leave : off\n"
                    if wait["timeline"] == True: md+=" Share : on\n"
                    else:md+=" Share : off\n"
                    if wait["autoAdd"] == True: md+=" Auto add : on\n"
                    else:md+=" Auto add : off\n"
                    if wait["commentOn"] == True: md+=" Comment : on\n"
                    else:md+=" Comment : off\n"
                    cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                gid = msg.text.replace("album removeâ†’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.from_ in admin:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
            	if msg.from_ in admin:
                    if wait["clock"] == True:
                        cl.sendText(msg.to,"already on")
                    else:
                        wait["clock"] = True
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"(%H:%M)")
                        profile = cl.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
            	if msg.from_ in admin:
                    if wait["clock"] == False:
                        cl.sendText(msg.to,"already off")
                    else:
                        wait["clock"] = False
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam Update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

            elif msg.text == "$set":
                    cl.sendText(msg.to, "Check sider")
                    #ki.sendText(msg.to, "Check sider")
                    #kk.sendText(msg.to, "Check sider")
                    #kc.sendText(msg.to, "Check sider")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "$read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------------------------------

#-----------------------------------------------

            elif msg.text in ["All join"]:
            	if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kz.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text in ["Kurumi join"]:
            	if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["Katou join"]:
            	if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Hatsune join"]:
            	if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Bye all"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        kz.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Kurumi"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Katou"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Hatsune"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Ram"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ks.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Megumin"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kz.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
                if msg.from_ in admin:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Fuck You")
                        kc.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc,ks]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Cleanse" in msg.text:
                if msg.from_ in admin:
                    print "ok"
                    _name = msg.text.replace("Cleanse","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ki.sendText(msg.to,"Hanya Pembersihan ô")
                    kk.sendText(msg.to,"Group dibersihkan.")
                    kc.sendText(msg.to,"Bye All")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    targets.remove("uc9601a92d1616bcfbe9243127b6ad47f","u5b95eb648917fe6d5d499c588703fdd5","uc740020d36764e001ecf803e14b0bbf6","u4c83920cd9c63b2cb22d9b542fccebdb","u60c5af455bdfb8a16b61e6929e66b0d9","ub59f2280431ba3682304c5f495fb5d28","ufce6f7f20c1874215e8f63c3b95807da")
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        kk.sendText(msg.to,"Not found.")
                        kc.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[ki,kk,kc,ks,kz]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Group cleanse")
                                kk.sendText(msg.to,"Group cleanse")
                                #kc.sendText(msg.to,"Group cleanse")
            elif "Nk " in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Nk ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                            try:
                                klist=[ki,kk,kc,ks,kz]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Succes")
                                kk.sendText(msg.to,"Fuck You")
            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Succes Cv")
                                except:
                                    ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = kz.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                        #kk.sendText(msg.to,"Not found Cv")
                        #kc.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                #cl.sendText(msg.to,"Succes Cv")
                                ki.sendText(msg.to,"Succes Ban")
                                #kk.sendText(msg.to,"Succes Cv")
                                #kc.sendText(msg.to,"Succes Cv")
                            except:
                                ki.sendText(msg.to,"Error")
                                #kk.sendText(msg.to,"Error")
                                #kc.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
                if msg.from_ in admin:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = kz.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        #ki.sendText(msg.to,"Not found Cv")
                        kk.sendText(msg.to,"Not found")
                        #kc.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                #cl.sendText(msg.to,"Succes Cv")
                                #ki.sendText(msg.to,"Succes Cv")
                                kk.sendText(msg.to,"Succes")
                                #kc.sendText(msg.to,"Succes Cv")
                            except:
                                #ki.sendText(msg.to,"Succes Cv")
                                kk.sendText(msg.to,"Succes")
                                #kc.sendText(msg.to,"Succes Cv")
#-----------------------------------------------
            elif msg.text in ["Test"]:
                ki.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
                kk.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
                kc.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
                ks.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
                kz.sendText(msg.to,"Ok Cv double thumbs up")
#-----------------------------------------------
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
				ks.sendText(msg.to,(bctxt)) 
				kz.sendText(msg.to,(bctxt)) 
#-----------------------------------------------

            elif msg.text in ["Rem"]:
                cl.sendText(msg.to,"Iya, ada apa? ")
                #kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                #kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Katou"]:
                kk.sendText(msg.to,"Iya, ada apa? ")
            elif msg.text in ["Kurumi"]:
                ki.sendText(msg.to,"Iya, ada apa? ")
            elif msg.text in ["Hatsune"]:
                kc.sendText(msg.to,"Iya, ada apa? ")
            elif msg.text in ["Ram"]:
                ks.sendText(msg.to,"Iya, ada apa? ")
            elif msg.text in ["Megumin"]:
            	kz.sendText(msg.to,"iya, ada apa? ")

#-----------------------------------------------------------------------
                
            elif msg.text in ["Pagi Rem"]:
                cl.sendText(msg.to,"Pagi juga kak ")
            elif msg.text in ["Pagi kurumi"]:
                ki.sendText(msg.to,"Pagi juga kak ")
            elif msg.text in ["Pagi Katou"]:
                kk.sendText(msg.to,"Pagi juga kak ")
            elif msg.text in ["Pagi Hatsune"]:
                kc.sendText(msg.to,"Pagi juga kak ")
            elif msg.text in ["Pagi Ram"]:
                ks.sendText(msg.to,"Pagi juga kak ")
            elif msg.text in ["Pagi Megumin"]:
            	kz.sendText(msg.to,"Pagi juga kak ")
            elif msg.text in ["Pagi semua"]:
                cl. sendText(msg.to,"Pagi juga kak ^_^")
                ki.sendText(msg.to,"Pagi juga kak ^_^")
                kk.sendText(msg.to,"Pagi juga kak ^_^")
                kc.sendText(msg.to,"Pagi juga kak ^_^")
                ks.sendText(msg.to,"Pagi juga kak ^_^")
                kz.sendText(msg.to,"Pagi juga kak ^_^")
                
#----------------------------------------------------------------------

            elif msg.text in ["Siang Rem"]:
                cl.sendText(msg.to,"Siang juga kak ")
            elif msg.text in ["Siang kurumi"]:
                ki.sendText(msg.to,"Siang juga kak ")
            elif msg.text in ["Siang Katou"]:
                kk.sendText(msg.to,"Siang juga kak ")
            elif msg.text in ["Siang Hatsune"]:
                kc.sendText(msg.to,"Siang juga kak ")
            elif msg.text in ["Siang Ram"]:
                ks.sendText(msg.to,"Siang juga kak ")
            elif msg.text in ["Siang Megumin"]:
            	kz.sendText(msg.to,"Siang juga kak ")
            elif msg.text in ["Siang semua"]:
                cl. sendText(msg.to,"Siang juga kak ^_^")
                ki.sendText(msg.to,"Siang juga kak ^_^")
                kk.sendText(msg.to,"Siang juga kak ^_^")
                kc.sendText(msg.to,"Siang juga kak ^_^")
                ks.sendText(msg.to,"Siang juga kak ^_^")
                kz.sendText(msg.to,"Siang juga kak ^_^")
                
#----------------------------------------------------------------------

            elif msg.text in ["Aku sayang rem"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to,"Rem juga sayang Kakak >_<")
            elif msg.text in ["Aku sayang katou"]:
                if msg.from_ in admin:
                    kk.sendText(msg.to,"Katou juga sayang Kakak >_<")

#----------------------------------------------------------------------

            elif msg.text in ["Malam Rem"]:
                cl.sendText(msg.to,"Malam juga kak ")
                cl.sendText(msg.to,"jangan tidur terlalu malam ya kak ^_^")
            elif msg.text in ["Malam kurumi"]:
                ki.sendText(msg.to,"Malam juga kak ")
                ki.sendText(msg.to,"Kalo punya PR jangan lupa di kerjakan ya kak (~_^)")
            elif msg.text in ["Malam Katou"]:
                kk.sendText(msg.to,"Malam juga kak ")
                kk.sendText(msg.to,"semoga malam ini kakak mimpiin aku ^_^")
            elif msg.text in ["Malam Hatsune"]:
                kc.sendText(msg.to,"Malam juga kak ")
                kc.sendText(msg.to,"Cepatlah istirahat supaya besok bangun dengan penuh semangat :)")
            elif msg.text in ["Malam Ram"]:
                ks.sendText(msg.to,"Malam juga kak ")
                ks.sendText(msg.to,"aku ingin ketemu kakak, semoga kita bertemu dimimpi :)")
            elif msg.text in ["Malam Megumin"]:
            	kz.sendText(msg.to,"Malam juga kak ")
                kz.sendText(msg.to,"Aku tidak sabar menunggu hari esok")
            elif msg.text in ["Malam semua"]:
                cl. sendText(msg.to,"Malam juga kak ^_^")
                ki.sendText(msg.to,"Malam juga kak ^_^")
                kk.sendText(msg.to,"Malam juga kak ^_^")
                kc.sendText(msg.to,"Malam juga kak ^_^")
                ks.sendText(msg.to,"Malam juga kak ^_^")
                kz.sendText(msg.to,"Malam juga kak ^_^")

#----------------------------------------------------------------------

            elif msg.text in ["Rem bilang hai"]:
                cl.sendText(msg.to,"Hai ^_^")
            elif msg.text in ["Katou bilang hai"]:
                kk.sendText(msg.to,"Hai ^_^")
            elif msg.text in ["Kurumi bilang hai"]:
                ki.sendText(msg.to,"Hai ^_^")
            elif msg.text in ["Hatsune bilang hai"]:
                kc.sendText(msg.to,"Hai ^_^")
            elif msg.text in ["Ram bilang hai"]:
                ks.sendText(msg.to,"Hai ^_^")
            elif msg.text in ["Megumin bilang hai"]:
            	kz.sendText(msg.to,"Hai ^_^")
            elif msg.text in ["HBD katou"]:
                kk.sendText(msg.to,"iya makasih >_<")
                kk.sendText(msg.to,"Katou sayang kakak >_<")
                
 #------------------------------------Absen------------------------
 
            elif msg.text in ["Absen"]:
                cl.sendText(msg.to,"Rem disini (~_^)")
                ki.sendText(msg.to,"Kurumi disini (~_^)")
                kk.sendText(msg.to,"Katou disini (~_^)")
                kc.sendText(msg.to,"Hatsune disini (~_^)")
                ks.sendText(msg.to,"Ram disini (~_^)")
                kz.sendText(msg.to,"Megumin disini (~_^)")
            elif msg.text in ["Bobo dlu bye","Bobo ah","Tidur ah"]:
            	cl. sendText(msg.to,"Have a nice dream Kak")
                ki.sendText(msg.to,"Have a nice dream Kak")
                kk.sendText(msg.to,"Have a nice dream Kak")
                kc.sendText(msg.to,"Have a nice dream Kak")
                ks.sendText(msg.to,"Have a nice dream Kak")
                kz.sendText(msg.to,"Have a nice dream Kak")
            elif msg.text in ["Katou"]:
                #ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Ada apa kak? ")
                #kc.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome","Wc"]:
                ki.sendText(msg.to,"Selamat datang di")
                kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping","P"]:
                #ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Knp sih kak? kangen? >_<")
                #kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif msg.text in ["Respon","respon"]:
                ki.sendText(msg.to,"Kurumi desu")
                kk.sendText(msg.to,"Katou desu")
                kc.sendText(msg.to,"Hatsune desu")
                ks.sendText(msg.to,"Ram desu")
                kz.sendText(msg.to,"Megumin desu")
#-----------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                #ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                #kk.sendText(msg.to, "%sseconds" % (elapsed_time))
                #kc.sendText(msg.to, "%sseconds" % (elapsed_time))


#-------------------------------[SEND UNICODE]--------------------------------#

            elif msg.text in ["BOM"]:
                if msg.from_ in admin:
                    kc.sendText(msg.to,"52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.61.6e.65.7a.52.69.64.77.61.6e.20.69.62.6")

#------------------------------------------------------------------------------------------------#

            elif msg.text in ["Ban"]:
            	if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"send contact")
                    #ki.sendText(msg.to,"send contact")
                    #kk.sendText(msg.to,"send contact")
                    #kc.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
            	if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"send contact")
                    #ki.sendText(msg.to,"send contact")
                    #kk.sendText(msg.to,"send contact")
                    #kc.sendText(msg.to,"send contact")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    #cl.sendText(msg.to,"Kosong")
                    #ki.sendText(msg.to,"nothing")
                    kk.sendText(msg.to,"Kosong")
                    #kc.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    #ki.sendText(msg.to,mc)
                    #kk.sendText(msg.to,mc)
                    #kc.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        #ki.sendText(msg.to,"There was no blacklist user")
                        #kk.sendText(msg.to,"There was no blacklist user")
                        #kc.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                        ks.kickoutFromGroup(msg.to,[jj])
                        kz.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    #ki.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    #kk.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    #kc.sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random:" in msg.text:
                if msg.from_ in admin:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumâ†’" in msg.text:
                try:
                    albumtags = msg.text.replace("albumâ†’","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1003)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Iksan\n\nhttp://line.me/ti/p/prgx13V6Wv")
            kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1003)
            kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Iksan\n\nhttp://line.me/ti/p/prgx13V6Wv")
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1003)
            kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1003)
            ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1003)
            ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Iksan\n\nhttp://line.me/ti/p/prgx13V6Wv")
            kz.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1003)
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

##############          ######  #####################  #####################  #####################  #####################  ################     #####################  #####################
###############         ######  #####################  #####################  #####################  #####################  #################    #####################  #####################
####### ########        ######  #######       #######  #####################  #####################  #######       #######  #######       ####   #####################  #####################
#######  ########       ######  #######       #######         #######                #######         #######       #######  #######       #####  #######       #######         #######       
#######   ########      ######  #######       #######         #######                #######         #######       #######  #######       #####  #######       #######         #######       
#######    ########     ######  #####################         #######                #######         #####################  ##################   #######       #######         #######       
#######     ########    ######  #####################         #######                #######         #####################  ##################   #######       #######         #######       
#######      ########   ######  #######       #######         #######                #######         #######       #######  #######       #####  #######       #######         #######       
#######       ########  ######  #######       #######         #######                #######         #######       #######  #######       #####  #######       #######         #######       
#######        ######## ######  #######       #######         #######                #######         #######       #######  #######       ####   #####################         #######       
#######         ##############  #######       #######         #######                #######         #######       #######  #################    #####################         #######       
#######          #############  #######       #######         #######                #######         #######       #######  ################     #####################         #######       

#version = 1.0

import sys, time
import telepot
from telepot.loop import MessageLoop
from pprint import pprint

gisella =open('gisella.tgs', 'rb')
comandi = 'QUESTO E\' IL BOT TELEGRAM UFFICIALE DEL NATTA\nI comandi sono:\n/help --> per visuallizare questo messaggio\n/orario --> per scaricare l\'orario di quest\'anno\n/classe --> per visualizzare l\'orario della classe riportata dopo il simbolo / (/3Ben - /2Clm )\n/professore --> per visualizzare l\'orario di lavoro del professore riportato dopo il simbolo (/cognome) /\n/assenza --> per segnalare l\'assenza di un professore. Per farlo basta scrivere affianco al comando il cognome del professore. Le assenze segnalate saranno visibili sul canale AssenzeNatta\n/nattachat --> per visualizzare il canale di discussione della scuola\n/assenzenatta --> per visualizzare il gruppo con le assenze del giorno\n/stickers --> per scaricare gli stikers del Natta\n/risposte --> per visualizzare la lista di risposte date dal bot in caso di digitazione di certe parole\n/modifica --> per scaricare il file del bot creato in python e apportare modifiche. Dopo inviare le modifiche al gruppo NattaHelp\n/aggiungi --> per dirci cosa vorreste aggiungere nel bot\n/segnala --> per segnalare un problema'

def rispondi(msg):
    chat_id = msg['chat']['id']
    comando = msg['text']
    print(msg)
    print(comando)
    pprint(msg)
    
    if comando == '/start':
        bot.sendMessage(chat_id, comandi)
        bot.sendMessage(chat_id, 'Gli orari dei professori saranno disponibili con l\'orario definitivo')

    elif comando == '/help':
        bot.sendMessage(chat_id, comandi)

    elif '/orario' in comando:
        orario = open('orario.pdf', 'rb')
        bot.sendDocument(chat_id, orario)
        orario.close()

    elif '/assenza' in comando:
        comando = comando.replace ("/assenza ", "")
        bot.sendMessage(-1001280042780, str(comando) + ' è assente')

    elif comando == '/nattachat':
        bot.sendMessage(chat_id, 'Per sparlare della scuola esiete un gruppo telegram: https://t.me/nattachat')

    elif comando == '/assenzenatta':
            bot.sendMessage(chat_id, 'Per entrare nel guppo dove sarà possibile vedere le assenze https://t.me/assenzenatta')

    elif comando == '/stickers':
        bot.sendMessage(chat_id, 'Crea stikers della scuola ed inviali qua: https://t.me/nattahelp')#creare stikers scuola

    elif comando == '/risposte':
        bot.sendMessage(chat_id, 'Prova a scrivere questo:\nGisella\nquaqua')

    elif comando == '/modifica':
        bot.sendMessage(chat_id, 'Scarica il file da: https://t.me/nattahelp')

    elif comando == '/aggiungi':
        bot.sendMessage(chat_id, 'Vuoi aggiungere contenuti al bot contattaci in questo gruppo telegram: https://t.me/nattahelp')

    elif comando == '/segnala':
        bot.sendMessage(chat_id, 'Hai rilevato un problema?\nSegnalalo a questo canale: https://t.me/nattahelp')

    elif 'Natta' in comando:
        natta = open('natta.png', 'rb')
        bot.sendPhoto(chat_id, natta)
        natta.close()

    elif 'qua qua' in comando:
        bot.sendMessage(chat_id, 'Qua qua lo dici a tua madre!')

    elif 'Qua qua' in comando:
        bot.sendMessage(chat_id, 'Qua qua lo dici a tua madre!')

    elif 'Gisella' in comando:
        bot.sendSticker(chat_id, gisella)
        gisella.close()

    elif comando == 'chat_id':
        bot.sendMessage(chat_id, chat_id)

########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################

    elif comando == '/1Agc':
        aAgc = open('1Agc.png', 'rb')
        bot.sendDocument(chat_id, aAgc)
        aAgc.close()
    elif comando == '/2Agc':
        bAgc = open('2Agc.png', 'rb')
        bot.sendDocument(chat_id, bAgc)
        bAgc.close()
    elif comando == '/3Agc':
        cAgc = open('3Agc.png', 'rb')
        bot.sendDocument(chat_id, cAgc)
        cAgc.close()
    elif comando == '/4Agc':
        dAgc = open('4Agc.png', 'rb')
        bot.sendDocument(chat_id, dAgc)
        dAgc.close()
    elif comando == '/5Agc':
        eAgc = open('5Agc.png', 'rb')
        bot.sendDocument(chat_id, eAgc)
        eAgc.close()
    elif comando == '/1Bgc':
        aBgc = open('1Bgc.png', 'rb')
        bot.sendDocument(chat_id, aBgc)
        aBgc.close()
    elif comando == '/2Bgc':
        bBgc = open('2Bgc.png', 'rb')
        bot.sendDocument(chat_id, bBgc)
        bBgc.close()
    elif comando == '/3Bgc':
        cBgc = open('3Bgc.png', 'rb')
        bot.sendDocument(chat_id, cBgc)
        cBgc.close()
    elif comando == '/4Bgc':
        dBgc = open('4Bgc.png', 'rb')
        bot.sendDocument(chat_id, dBgc)
        dBgc.close()
    elif comando == '/1Ait':
        aAit = open('1Ait.png', 'rb')
        bot.sendDocument(chat_id, aAit)
        aAit.close()
    elif comando == '/2Ait':
        bAit = open('2Ait.png', 'rb')
        bot.sendDocument(chat_id, bAit)
        bAit.close()
    elif comando == '/1Bit':
        aBit = open('1Bit.png', 'rb')
        bot.sendDocument(chat_id, aBit)
        aBit.close()
    elif comando == '/2Bit':
        bBit = open('2Bit.png', 'rb')
        bot.sendDocument(chat_id, bBit)
        bBit.close()
    elif comando == '/1Cit':
        aCit = open('1Cit.png', 'rb')
        bot.sendDocument(chat_id, aCit)
        aCit.close()
    elif comando == '/2Cit':
        bCit = open('2Cit.png', 'rb')
        bot.sendDocument(chat_id, bCit)
        bCit.close()
    elif comando == '/1Dit':
        aDit = open('1Dit.png', 'rb')
        bot.sendDocument(chat_id, aDit)
        aDit.close()
    elif comando == '/2Dit':
        bDit = open('2Dit.png', 'rb')
        bot.sendDocument(chat_id, bDit)
        bDit.close()
    #elif comando == '/1Eit':
    #    aEit = open('1Eit.xlsx', 'rb')
    #    bot.sendDocument(chat_id, aEit)
    elif comando == '/2Eit':
        bEit = open('2Eit.png', 'rb')
        bot.sendDocument(chat_id, bEit)
        bEit.close()
    #elif comando == '/1Fit':
    #    aFit = open('1Fit.xlsx', 'rb')
    #    bot.sendDocument(chat_id, aFit)
    elif comando == '/2Fit':
        bFit = open('2Fit.png', 'rb')
        bot.sendDocument(chat_id, bFit)
        bFit.close()
    elif comando == '/3Amm':
        cAmm = open('3Amm.png', 'rb')
        bot.sendDocument(chat_id, cAmm)
        cAmm.close()
    elif comando == '/4Amm':
        dAmm = open('4Amm.png', 'rb')
        bot.sendDocument(chat_id, )
        dAmm.close()
    elif comando == '/5Amm':
        eAmm = open('5Amm.png', 'rb')
        bot.sendDocument(chat_id, eAmm)
        eAmm.close()
    elif comando == '/3Dmm':
        cDmm = open('3Dmm.png', 'rb')
        bot.sendDocument(chat_id, cDmm)
        cDmm.close()
    elif comando == '/DAmm':
        dDmm = open('4Dmm.png', 'rb')
        bot.sendDocument(chat_id, dDmm)
        dDmm.close()
    elif comando == '/5Dmm':
        eDmm = open('5Dmm.png', 'rb')
        bot.sendDocument(chat_id, eDmm)
        eDmm.close()
    elif comando == '/3Emm':
        cEmm = open('3Emm.png', 'rb')
        bot.sendDocument(chat_id, cEmm)
        cEmm.close()
    elif comando == '/4Ben':
        dBen = open('4Ben.png', 'rb')
        bot.sendDocument(chat_id, dBen)
        dBen.close()
    elif comando == '/3Ben':
        cBen = open('3Ben.png', 'rb')
        bot.sendDocument(chat_id, cBen)
        cBen.close()
    elif comando == '/5Ben':
        eBen = open('5Ben.png', 'rb')
        bot.sendDocument(chat_id, eBen)
        eBen.close()
    elif comando == '/4Cmp':
        dCpl = open('4Cmp.png', 'rb')
        bot.sendDocument(chat_id, dCpl)
        dCpl.close()
    elif comando == '/3Cmp':
        cCpl = open('3Cmp.png', 'rb')
        bot.sendDocument(chat_id, cCpl)
        cCpl.close()
    elif comando == '/5Cmp':
        eCpl = open('5Cmp.png', 'rb')
        bot.sendDocument(chat_id, eCpl)
        eCpl.close()
    elif comando == '/1Asa':
        aAsa = open('1Asa.png', 'rb')
        bot.sendDocument(chat_id, aAsa)
        aAsa.close()
    elif comando == '/2Asa':
        bAsa = open('2Asa.png', 'rb')
        bot.sendDocument(chat_id, bAsa)
        bAsa.close()
    elif comando == '/3Asa':
        cAsa = open('3Asa.png', 'rb')
        bot.sendDocument(chat_id, cAsa)
        cAsa.close()
    elif comando == '/4Asa':
        dAsa = open('4Asa.xlsx', 'rb')
        bot.sendDocument(chat_id, dAsa)
        dAsa.close()
    elif comando == '/5Asa':
        eAsa = open('5Asa.png', 'rb')
        bot.sendDocument(chat_id, eAsa)
        eAsa.close()
    elif comando == '/5Blm':
        eBsa = open('5Blm.png', 'rb')
        bot.sendDocument(chat_id, eBsa)
        eBsa.close()
    elif comando == '/4Emm':
        bCsa = open('4Emm.png', 'rb')
        bot.sendDocument(chat_id, bCsa)
        bCsa.close()
    elif comando == '/3Csa':
        cCsa = open('3Csa.png', 'rb')
        bot.sendDocument(chat_id, cCsa)
        cCsa.close()
    elif comando == '/5Clm':
        eCsa = open('5Clm.png', 'rb')
        bot.sendDocument(chat_id, eCsa)
        eCsa.close()
    elif comando == '/4Asa':
        bDsa = open('4Asa.xlsx', 'rb')
        bot.sendDocument(chat_id, bDsa)
        bDsa.close()
    elif comando == '/3Dsa':
        cDsa = open('3Dsa.png', 'rb')
        bot.sendDocument(chat_id, cDsa)
        cDsa.close()
    elif comando == '/4Dsa':
        dDsa = open('4Dsa.png', 'rb')
        bot.sendDocument(chat_id, dDsa)
        dDsa.close()
    elif comando == '/1Blm':
        aBlm = open('1Blm.png', 'rb')
        bot.sendDocument(chat_id, aBlm)
        aBlm.close()
    elif comando == '/2Blm':
        bBlm = open('2Blm.png', 'rb')
        bot.sendDocument(chat_id, bBlm)
        bBlm.close()
    elif comando == '/3Blm':
        cBlm = open('3Blm.png', 'rb')
        bot.sendDocument(chat_id, cBlm)
        cBlm.close()
    elif comando == '/4Blm':
        dBlm = open('4Blm.png', 'rb')
        bot.sendDocument(chat_id, dBlm)
        dBlm.close()
    elif comando == '/2Clm':
        aClm = open('2Clm.png', 'rb')
        bot.sendDocument(chat_id, aClm)
        aClm.close()
    elif comando == '/4Csa':
        zClm = open('4Csa.png', 'rb')
        bot.sendDocument(chat_id, zClm)
        zClm.close()
    elif comando == '/1Csa':
        xClm = open('1Csa.png', 'rb')
        bot.sendDocument(chat_id, xClm)
        xClm.close()
    elif comando == '/5Dsa':
        yClm = open('5Dsa.png', 'rb')
        bot.sendDocument(chat_id, yClm)
        yClm.close()
    elif comando == '/5Bgc':
        wClm = open('5Bgc.png', 'rb')
        bot.sendDocument(chat_id, wClm)
        wClm.close()

########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################



bot = telepot.Bot('957296625:AAGDIcCgw9YQ9V3a5HzBan7cOAxis48q-os')
print(bot.getMe())
bot.message_loop(rispondi)

while 1:
    time.sleep(3)

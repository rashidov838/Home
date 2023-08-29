import requests
import hashlib
# response =requests.get('https://api.github.com')
# print(response)

# url="https://api.pwnedpasswords.com/range/"+"password123"
# res=requests.get(url)
# print(res)

# password_hash="CBFDAC6008F9CAB4083784CBD1874F76618D2A97"

# url="https://api.pwnedpasswords.com/range/"+password_hash[:5]
# res=requests.get(url) 
# print(res)
# print(res.encoding)



def request_api_data(query_param):
    url="https://api.pwnedpasswords.com/range/"+str(query_param)
    result=requests.get(url)
    if result.status_code!=200:
        raise RuntimeError(

            f'Errror: {result.status_code},check an API and try again '
        )
    return result



def get_psw_leaks_count(hashes,hash_to_check):
    hashes=(hash.split(":") for hash in hashes.splitlines())
    for hash,count in hashes:
        if hash==hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    shail_password=hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char,tail=shail_password[:5],shail_password[5:]
    response=request_api_data(first5_char)
    return get_psw_leaks_count(response.text,tail)


def main(passwords):
    for psw in passwords:
        count=pwned_api_check(psw)
        if count:
            print(f"{psw} was found {count} times ...... you should change your passsword")
        else:
            print(f'{psw} was not found.Good to go')
    return "Success"
main(['bekzodr1973','qwerty','zxccvb'])
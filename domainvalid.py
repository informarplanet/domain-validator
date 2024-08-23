# check domain valid from whois libery 
# pip install python-whois  step 1
# import whois

# def is_registre(domain_name):
#     try:
#         w = whois.whois(domain_name)
#     except Exception as e:
#         return "This is not a valid domain"
#     else:
#         domain=w.domain_name
#         # fetch nameserver
#         name_servers = w.name_servers

#         if not name_servers:
#             return "No name servers found"
        
#         # added all name server one by one using comma (,)
#         total_name_server = ", ".join(name_servers) 

#         return f'[++] Result for: {domain[0]}\n[++] Name servers are: {total_name_server} '

# if __name__ == "__main__":
#     print(is_registre("bing.com"))  # Should print the name servers as plain text

# import whois

# def whoisinformatio(domain_name):
#     try:
#         r=whois.whois(domain_name)
#     except Exception as e:
#         return "this domain not valid"
#     else:
#         #ftech domain name
#         domain=r.domain_name
#         # fetch nameserver
#         nameserver=list(set(r.name_servers))

#         if not nameserver:
#             return "No name servers found"
        
#         total_nameserver=",".join(nameserver)
#         return f'[++] Result For {domain[0]}\n[++]Name server is: {total_nameserver}'
        

# if __name__ == "__main__":
#     print(whoisinformatio("bing.com"))

import whois 

def is_registered ( domain_name ):
    try :
        w = whois . whois ( domain_name )
    except Exception:
       return  False
    else :
        return bool ( w .domain_name)
    
if __name__ == "__main__" :
     print ( is_registered ( "google.com" )) 

 
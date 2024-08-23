import whois
from domainvalid import is_registered

domain_name="techvern.com"
if is_registered(domain_name):
    whois_info= whois . whois ( domain_name )
    print (f'Domain register: {whois_info.domain_name}'  )
    print ( "WHOIS server:" , whois_info.whois_server)

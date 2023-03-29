import tldextract

def check_domain_match(company_domain_url, actual_domain_url):
    """
        returns True if domain matches for the given urls
    """
    if not company_domain_url or not actual_domain_url:
        return False
    import tldextract
    indeed_domain_extract = tldextract.extract(company_domain_url)
    actual_domain_extract = tldextract.extract(actual_domain_url)
    if indeed_domain_extract.registered_domain == actual_domain_extract.registered_domain:
        return True
    return False
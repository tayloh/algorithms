"""
Write a function that does the following:
Removes any duplicate query string parameters from the url
Removes any query string parameters specified within the 2nd argument (optional array)

An example:
www.saadbenn.com?a=1&b=2&a=2') // returns 'www.saadbenn.com?a=1&b=2'
"""
from collections import defaultdict
import urllib
import urllib.parse

# Here is a very non-pythonic grotesque solution
def strip_url_params1(url, params_to_strip=None):
    
    if not params_to_strip:
        params_to_strip = []
    if url:
        result = '' # final result to be returned
        tokens = url.split('?')
        domain = tokens[0]
        query_string = tokens[-1]
        result += domain
        # add the '?' to our result if it is in the url
        if len(tokens) > 1:
            result += '?'
        if not query_string:
            return url
        else:
            # logic for removing duplicate query strings
            # build up the list by splitting the query_string using digits
            key_value_string = []
            string = ''
            for char in query_string:
                if char.isdigit():
                    key_value_string.append(string + char)
                    string = ''
                else:
                    string += char
            dict = defaultdict(int)
            # logic for checking whether we should add the string to our result
            for i in key_value_string:
                _token = i.split('=')
                if _token[0]:
                    length = len(_token[0])
                    if length == 1:
                        if _token and (not(_token[0] in dict)):
                            if params_to_strip:
                                if _token[0] != params_to_strip[0]:
                                    dict[_token[0]] = _token[1]
                                    result = result + _token[0] + '=' + _token[1]
                            else:
                                if not _token[0] in dict:
                                    dict[_token[0]] = _token[1]
                                    result = result + _token[0] + '=' + _token[1]
                    else:
                        check = _token[0]
                        letter = check[1]
                        if _token and (not(letter in dict)):
                            if params_to_strip:
                                if letter != params_to_strip[0]:
                                    dict[letter] = _token[1]
                                    result = result + _token[0] + '=' + _token[1]
                            else:
                                if not letter in dict:
                                    dict[letter] = _token[1]
                                    result = result + _token[0] + '=' + _token[1]
    return result

# New refactored version of strip_url_params1 (a bit similar to strip_url_params2 since this also 
# uses list comprehension with a singular "main" for-loop to remove parameters)
def strip_url_params1_new(url, params_to_strip=[]):
    result = '' # final result to be returned
    if url and '?' in url:
        tokens = url.split('?')
        domain = tokens[0]
        queries = tokens[1].split('&')
        result += domain

        # remove duplicate parameters and those specified in params_to_strip
        query_str = ''
        for i in range(len(queries)):
            query = queries[i].split('=')
            if not(query[0] in params_to_strip) and not(query[0] in [q.split('=')[0] for q in queries[0:i]]):
                # if parameter should not be stripped, add it to query_str
                query_str += query[0] + '=' +  query[1] + '&'
        # assemble parameters with domain previously added
        result += '?' + query_str[0:(len(query_str)-1)]
    else: result = url

    return result

# A very friendly pythonic solution (easy to follow)
def strip_url_params2(url, param_to_strip=[]):
    if '?' not in url:
        return url

    queries = (url.split('?')[1]).split('&')
    queries_obj = [query[0] for query in queries]
    for i in range(len(queries_obj) - 1, 0, -1):
        if queries_obj[i] in param_to_strip or queries_obj[i] in queries_obj[0:i]:
            queries.pop(i)

    return url.split('?')[0] + '?' + '&'.join(queries)


# Here is my friend's solution using python's builtin libraries
def strip_url_params3(url, strip=None):
    if not strip: strip = []
    
    parse = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parse.query)
    
    query = {k: v[0] for k, v in query.items() if k not in strip}
    query = urllib.parse.urlencode(query)
    new = parse._replace(query=query)
    
    return new.geturl()

if __name__ == '__main__':
    print(strip_url_params1_new("www.saadbenn.com?a=1&b=2&a=2")) # should be "www.saadbenn.com?a=1&b=2"
    print(strip_url_params1("www.saadbenn.com?a=1&b=2", ['b'])) # should be "www.saadbenn.com?a=1"
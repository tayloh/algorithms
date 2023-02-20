"""
Write a function that does the following:
Removes any duplicate query string parameters from the url
Removes any query string parameters specified within the 2nd argument (optional array)

An example:
www.saadbenn.com?a=1&b=2&a=2') // returns 'www.saadbenn.com?a=1&b=2'
"""
from collections import defaultdict
import urllib
#import urllib.parse
import unittest

branchList = set()

# Here is a very non-pythonic grotesque solution
def strip_url_params1(url, params_to_strip=None):
    
    if not params_to_strip:
        branchList.add(11)
        params_to_strip = []
    else: branchList.add(12)
    if url:
        branchList.add(21)
        result = '' # final result to be returned
        tokens = url.split('?')
        domain = tokens[0]
        query_string = tokens[-1]
        result += domain
        # add the '?' to our result if it is in the url
        if len(tokens) > 1:
            branchList.add(31)
            result += '?'
        else: branchList.add(32)
        if not query_string:
            branchList.add(41)
            return url
        else:
            branchList.add(42)
            # logic for removing duplicate query strings
            # build up the list by splitting the query_string using digits
            key_value_string = []
            string = ''
            for char in query_string:
                if char.isdigit():
                    branchList.add(51)
                    key_value_string.append(string + char)
                    string = ''
                else:
                    branchList.add(52)
                    string += char
            dict = defaultdict(int)
            # logic for checking whether we should add the string to our result
            for i in key_value_string:
                _token = i.split('=')
                if _token[0]:
                    branchList.add(61)
                    length = len(_token[0])
                    if length == 1:
                        branchList.add(71)
                        if _token and (not(_token[0] in dict)):
                            branchList.add(81)
                            if params_to_strip:
                                branchList.add(91)
                                if _token[0] != params_to_strip[0]:
                                    branchList.add(101)
                                    dict[_token[0]] = _token[1]
                                    result = result + _token[0] + '=' + _token[1]
                                else: branchList.add(102)
                            else:
                                branchList.add(92)
                                if not _token[0] in dict:
                                    branchList.add(111)
                                    dict[_token[0]] = _token[1]
                                    result = result + _token[0] + '=' + _token[1]
                                else: branchList.add(112)
                        else: branchList.add(82)
                    else:
                        branchList.add(72)
                        check = _token[0]
                        letter = check[1]
                        if _token and (not(letter in dict)):
                            branchList.add(121)
                            if params_to_strip:
                                branchList.add(131)
                                if letter != params_to_strip[0]:
                                    branchList.add(141)
                                    dict[letter] = _token[1]
                                    result = result + _token[0] + '=' + _token[1]
                                else: branchList.add(142)
                            else:
                                branchList.add(132)
                                if not letter in dict:
                                    branchList.add(151)
                                    dict[letter] = _token[1]
                                    result = result + _token[0] + '=' + _token[1]
                                else: branchList.add(152)
                        else: branchList.add(122) 
                else: branchList.add(62)
    else: branchList.add(22)
    return result

# A very friendly pythonic solution (easy to follow)
def strip_url_params2(url, param_to_strip=[]): # pragma: no cover
    if '?' not in url:
        return url

    queries = (url.split('?')[1]).split('&')
    queries_obj = [query[0] for query in queries]
    for i in range(len(queries_obj) - 1, 0, -1):
        if queries_obj[i] in param_to_strip or queries_obj[i] in queries_obj[0:i]:
            queries.pop(i)

    return url.split('?')[0] + '?' + '&'.join(queries)


# Here is my friend's solution using python's builtin libraries
def strip_url_params3(url, strip=None):  # pragma: no cover
    if not strip: strip = []
    
    parse = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parse.query)
    
    query = {k: v[0] for k, v in query.items() if k not in strip}
    query = urllib.parse.urlencode(query)
    new = parse._replace(query=query)
    
    return new.geturl()

def branch_coverage():  # pragma: no cover
    allBranches = { 11, 12, 21, 22, 31, 32, 41, 42, 51, 52, 61, 62, 71, 72, 81, 82, 91, 92, 101, 102, 111, 112, 121, 122, 131, 132, 141, 142, 151, 152 }
    print("Branch coverage results")
    print("-----------------------")

    # Print which branches have been covered
    branchesTaken = "Branches taken:"
    for b in branchList:
        branchesTaken += " " + str(b)
    print(branchesTaken)

    # Print branches missed
    branchesMissed = "Branches missed:"
    for b in allBranches:
        if not(b in branchList):
            branchesMissed += " " + str(b)
    print(branchesMissed)

    # Print total branch coverage
    print("Branch coverage: " + str(len(branchList) / 30))

if __name__ == '__main__':
    #unittest.main(exit=False)
    
    # statements taken from tests/test_strings (only test cases for strip_url_params1)
    strip_url_params1("www.saadbenn.com?a=1&b=2&a=2")
    strip_url_params1("www.saadbenn.com?a=1&b=2", ['b'])
    strip_url_params1("bongi")
    strip_url_params1("www.saadbenn.com?=1")
    strip_url_params1("")

    branch_coverage()
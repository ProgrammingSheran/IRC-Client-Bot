import re

def parse_url(stream, stdout):
    '''
    Parses only the URL of the given domain file.
    Important! These functions only work for this specific file format!
    This function returns a list of the results.

    :param stream: File stream (_io.TextIOWrapper)
    :param stdout: Output as list
    :return: Result in form of a list
    '''

    for number, line in enumerate(stream):
        string = line.strip()
        wohttp = re.findall(r"[\w.-]+\.[\w]+", string)
        result = ""
        if wohttp:
            result = wohttp[0].strip()
            if result:
                stdout.append(result)

    return stdout

def parse_utype(stream, stdout):
    '''
    Parses the url and the threat type of the url.
    Important! This functions only works for a specific file format!
    This function returns a list of tuples with the results

    :param stream: File stream (_io.TextIOWrapper)
    :param stdout: Output as list
    :return: Result in form of a list
    '''

    for number, value in enumerate(stream):
        line = value.replace("\t", " ").strip()
        string = line.split(" ")
        if len(string) >= 2:
            if not string[0].startswith("#"):
                url = string[0]
                typ = string[1]
                stdout.append((url, typ))
            else:
                pass
        else:
            url = string[0]
            stdout.append(url)

    return stdout
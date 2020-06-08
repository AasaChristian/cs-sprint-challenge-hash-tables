# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    hash = {}
    for x in queries:
        hash[x] = x
    
    for f in files:
        words = f.split("/")
        if words[-1] in hash:
            result.append(f)


    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

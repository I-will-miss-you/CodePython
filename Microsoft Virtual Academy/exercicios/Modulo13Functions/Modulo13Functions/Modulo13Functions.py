def writeText(data, filename):
    file = open(filename, mode = 'w')
    file.write(data)
    return

writeText('Hello, world.', 'hello.txt')
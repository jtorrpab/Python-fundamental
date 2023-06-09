with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('\nnuevas cosas')
    file.write('\notras cosas')
    file.write('\ny mas  cosas')
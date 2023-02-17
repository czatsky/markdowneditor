# # write your code here

formatters = ['plain','bold','italic','inline-code',
              'link','header','new-line','ordered-list','unordered-list'
              ]
biipn = ['bold','italic','inline-code','plain','new-line']

def header(c):
        while True:
            level = int(input('Level: '))
            if level < 1 or level > 6:
                print('The level should be within the range of 1 to 6')
            else:
                break
        text = (input('Text: '))
        c = str(('#'*level+' '+text+'\n'))
        # c += ('')
        return c


def lists(c):
    while True:
        rows = int(input('Number of rows: '))
        if rows < 1:
            print('The number of rows should be greater than zero')
        else:
            break
    elements = []
    for i in range(rows):
        i += 1
        element = input(f'Row #{i}: ')
        if usfor == 'ordered-list':
            elements.append(f'{i}. ' + element)
        elif usfor == 'unordered-list':
            elements.append('* ' + element)
    c = str()
    for e in elements:
        c += (str(e) + '\n')
    return c

def bold_it_inl_plain_new(c):
    if usfor == 'bold':
        text = (input('Text: '))
        # print('**'+text+'**')
        c = str(('**'+text+'**'))
        return c

    if usfor == 'italic':
        text = (input('Text: '))
        # print('*'+text+'*')
        c = str('*'+text+'*')
        return c

    if usfor == 'inline-code':
        text = (input('Text: '))
        # print('`'+text+'`')
        c = str(('`'+text+'`'))
        return c

    if usfor == 'plain':
        text = (input('Text: '))
        # print(text)
        c = str(text)
        return c

    if usfor == 'new-line':
        # print('')
        c = str('\n')
        return c

def link(c):
    label = input('Label: ')
    url = input('URL: ')
    # print('['+label+']'+'('+url+')')
    c = str(('['+label+']'+'('+url+')'))
    return c

alldata = str()
if __name__ == "__main__":
    while True:
        usfor = input('Choose a formatter: ')
        if usfor == '!help':
            print('Available formatters: plain bold '
                  'italic header link inline-code new-line')
            print('Special commands: !help !done')
        elif usfor == '!done':
            f = open("output.md", "w")
            f.write(alldata)
            f.close()
            break
        elif usfor == 'header':
            alldata = (alldata+header(alldata))
            print(alldata)
        elif usfor in biipn:
            alldata = (alldata + bold_it_inl_plain_new(alldata))
            print(alldata)
        elif usfor == 'link':
            alldata = (alldata + link(alldata))
            print(alldata)
        elif usfor == 'unordered-list' or usfor == 'ordered-list':
            alldata = (alldata + lists(alldata))
            print(alldata)
        else:
            print('Unknown formatting type or command')

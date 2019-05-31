

with open('referat.txt','r', encoding='utf-8') as f:
    content = f.read()
    cnt_len = len(content)
    print(cnt_len)
    cnt_words = len(content.split())
    print(cnt_words)
    cnt_rpd = content.replace('.', '!')

with open('referat2.txt','w', encoding='utf-8') as new_file:
    new_file.write(cnt_rpd)


    # for line in f:
    #    # line = line.replace('.', '!')
        
    #     #new_text = line

    #     print(line)



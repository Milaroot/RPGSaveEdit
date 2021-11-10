import lzstring
from sys import argv

test = lzstring.LZString()

usage_msg = "Usage: "+ argv[0] +" (-e/-d) [file] [ouputfile]"

if len(argv) >= 2:
    mode = argv[1]

    if mode =='-d':

        with open(argv[2]) as f:                                 #decode part
            content = " ".join([l.rstrip() for l in f])
            f.close()

        with open(argv[3],'w', encoding='UTF-8') as wri:
            wri.write(test.decompressFromBase64(content))
            wri.close()

    elif mode =='-e':                                          #encode part

        with open(argv[2],'r', encoding='UTF-8') as f:
            content = " ".join([l.rstrip() for l in f])
            f.close()

        with open(argv[3],'w') as wri:
            wri.write(test.compressToBase64(content))
            wri.close()

    elif (mode =='-h') | (mode == '-help'):
        print("Examples:\n" +\
            " To decrypt a file 'file1.rpgsave to fileOP.txt.', do: " +\
            "'$ python "+ argv[0] +" -d file1.rpgsave  fileOP.txt'")

    else:
        print(usage_msg)
else:
       print(usage_msg)

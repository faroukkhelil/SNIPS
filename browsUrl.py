import webbrowser
import sys

opt=''
for i in range(2,len(sys.argv)) :
    if  i % 2 == 0 :
        opt=opt+sys.argv[i]+'='
    else :
        if i == len(sys.argv)-1 :
            opt=opt+sys.argv[i]
        else :
            opt=opt+sys.argv[i]+'&'

url=sys.argv[1]

webbrowser.open(url+'?'+opt, new=2)

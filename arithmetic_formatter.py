def arithmetic_arranger(oar,resp = False):

    sone = []
    stwo = []
    soper = []
    
    for i in oar:
        sone.append(i.split()[0])
        stwo.append(i.split()[2])
        soper.append(i.split()[1])

    #ERRORS

    if len(oar) > 5:
        return "Error: Too many problems."

    for i in soper:
        if str(i) != '+' and str(i) != '-':
            return 'Error: Operator must be '+' or '-'.'

    totalen = [max(len(n1),len(n2)) + 2 for n1, n2 in zip(sone, stwo)]

    #primeria linea
    fline = ''
    for i,v in enumerate(sone):
        if len(v)>4:
             return 'Error: Numbers cannot be more than four digits.'
        if v.isdigit():       
        	resto = totalen[i]-len(v)
        	strn = ""
        	while resto > 0:
        		strn +=" "
        		resto-=1
        	strn += v
        	fline+=strn
        	fline+="    "
        else:
            return 'Error: Numbers must only contain digits.'

    #segunda y cuarta linea
    sline = ''
    respline=''
    for i,v in enumerate(stwo):
        if len(v)>4:
             return 'Error: Numbers cannot be more than four digits.'
        if v.isdigit():  
        	resto = totalen[i]-len(v)-1
        	strn = soper[i]
        	while resto > 0:
        		strn +=" "
        		resto -=1
        	strn += v
        	sline+=strn
        	sline+="    "
        else:
            return 'Error: Numbers must only contain digits.'

        cl = ""
        rc = (totalen[i] - (len(str(int(v) + int(sone[i])))) )
        while rc > 0:
            cl += " " 
            rc -=1  
        if soper[i] == '+':
            cl += str(int(sone[i]) + int(v))
        else:
            cl += str(int(sone[i]) - int(v))
        respline+=cl
        respline+="    "
        
    #Tercera linea
    gline=''
    for i in totalen:
        resto = i
        strn = ""
        while resto > 0:
            strn +="-"
            resto -=1
        gline+=strn
        gline+="    "

    #imprimir
    if resp:
        return fline+'\n'+sline+'\n'+gline+'\n'+respline
    else:
        return fline+'\n'+sline+'\n'+gline

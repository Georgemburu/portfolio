def getTags (position,add=False):

    urlt = [
            {
                "url": "/",
                "name":"Home"
            },
            {
                "url": "/skill/Python",
                "name":"Frameworks"
            },
            {
                "url": "/skill/Python/Django",
                "name":"Projects"
            }
    ]
    if add:
        urlt.append(add)

    current = urlt[position]
    sendBack = [
            
        ]   
    count = 0
    while position >= count:
        sendBack.append(urlt[count])
        count+=1

    
    
    return sendBack
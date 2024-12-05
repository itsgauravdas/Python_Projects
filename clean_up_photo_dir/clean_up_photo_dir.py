import os 
for (dirname,dirs,files) in os.walk('.'):
    # print(f"Current directory: {dirname}")
    # print(f"Subdirectories: {dirs}")
    # print(f"Files: {files}")
    # print('-' * 40)
    for filename in files:
        if filename.endswith('.txt'):
            thefile = os.path.join(dirname, filename)
            size = os.path.getsize(thefile)
            if size == 2578 or size == 2565 : 
                print('T-Mobile', filename)
                continue
            
            fhand = open(thefile,'r')
            lines=list()
            for line in fhand:
                lines.append(line)
            fhand.close()
            
            if len(lines) == 3 and lines[2].startswith('sent from my iphone'):
                print('iphone', thefile)
                continue
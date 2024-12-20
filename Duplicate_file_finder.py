import hashlib 
import os 
import sys 
import keyboard


def image_finder(parent_folder):
    """
    Sample -
    {hash:[names]}
    """
    duplicate_img = {}
    for dirname,subdir,fileList in os.walk(parent_folder):
        print("Scaning %s...." %dirname)
        for filename in fileList:
            path = os.path.join(dirname,filename)
            file_hash = hash_file(path)
            if file_hash in duplicate_img:
                duplicate_img[file_hash].append(path)
            else:
                duplicate_img[file_hash] = [path]
    return duplicate_img

def delete_duplicates(duplicate_img):
    #Deleting those values whose keys are not unique 
    for key in duplicate_img:
        file_list = duplicate_img[key]
        while len(file_list) > 1:
            item=file_list.pop()
            os.remove(item)

#Join 2 dictionaries
def join_dict(dict1,dict2):
    for key in dict2.keys():
        if key in dict1:
          dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


# For finding Hash of various Files
# If 2 files have the same md5checksum,they most likely have the same content

def hash_file(path, blocksize=65536):
    img_file = open(path, 'rb')
    haser = hashlib.md5()
    buf = img_file.read(blocksize)
    while len(buf) > 0:
        haser.update(buf)
        buf = img_file.read(blocksize)
    img_file.close()
    return haser.hexdigest()

def print_results(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Found Duplicate Images - ')
        print('Details - ')
        print('<----------->')
        for result in results:
            for sudresult in result:
                print('\t%s' % sudresult)
            print('<------------------->')
    else:
        print('Unable to identify similar images')
        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        duplicate = {}
        folders = sys.argv[1:0]
        for i in folders:
            if os.path.exists(i):
                join_dict(duplicate,image_finder(i))
            else:
                print("%s is not a valid path . please verify" % i)
                sys.exit()
    print_results(duplicate)
     # Comment if not required
    print(
        "Do you want to delete the Duplicate Images (If Any)? Press [y] for Yes."
    )
    while True:
        if keyboard.read_key() =='y':
            print("Deleting Duplicate Files\n")
            delete_duplicates(duplicate)
            print("Thank You\n")
            break
        else:
            print("Nothing Deleted!!! Thank You\n")
            break
    else:
        print("Use Command Line Interface")
        print("Hint: python file_finder.py <path of folders>")
        print("Please Read comments for greater detailing")  
        
        

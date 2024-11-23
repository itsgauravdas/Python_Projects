import os 
import shutil 
import datetime 

def backup_files(source_dir, destination_dir):
    """
    Backup files from the source directory to the destination directory.
    :param source_dir: The directory containing the files to be backed up.
    :param destination_dir: The directory where the backup files will be stored.
    """
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_dir=os.path.join(destination_dir, f"backup_{timestamp}")
    
    try:
        shutil.copytree(source_dir,backup_dir)
    except OSError as e:
        print(f"Error creating backup : {e}")

if __name__ == "__main__":
    # Replace these paths with the appropriate source and destination directories
    source_dircctory = r'D:\Python\FASTAPI'
    destination_directory = r'D:\Python\mysql_py'
    
    backup_files(source_dircctory,destination_directory)
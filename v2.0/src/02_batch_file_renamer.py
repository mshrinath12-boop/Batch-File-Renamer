#Setup
import os
import logging
import time
from datetime import datetime
logging.basicConfig(
    filename= "Automation.log",
    level= logging.INFO,
    format= "%(asctime)s | %(levelname)s | %(message)s"
)
source_folder= "files"
start_time= time.time()
start_datetime= datetime.now()
success_count= 0
failed_count= 0
total_files= 0
count=1
for file in os.listdir(source_folder):
    print(file)
    name,extension= os.path.splitext(file)
    print(extension)
    source_path= os.path.join(source_folder,file)
    new_filename= f"Batch_{count:03}{extension}"
    destination_path= os.path.join(source_folder,new_filename)
    print(source_path)
    is_file= os.path.isfile(source_path)
    if is_file== False:
        continue
    if is_file==True:
        total_files+=1
    
    try:
       os.rename(source_path,destination_path)
       logging.info(f"File renamed successfully: {file}->{new_filename}")
       print(f"File renamed successfully: {file}->{new_filename}")
       count+=1
       success_count+=1
    except FileNotFoundError:
        logging.error(f"Failed to rename file: {file} not found ")
        print(f"Failed to rename file: {file} not found")
        failed_count+=1
    except PermissionError:
        logging.error(f"Acess denied to the requested file: {file}")
        print(f"Access denied to the requested  file: {file} ")
        failed_count+=1
end_time= time.time()
execution_time= end_time-start_time



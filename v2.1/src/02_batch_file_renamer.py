#Setup
import os
import logging
import time
from datetime import datetime
from datetime import date
logging.basicConfig(
    filename= "Automation.log",
    level= logging.INFO,
    format= "%(asctime)s | %(levelname)s | %(message)s"
)
run_date= date.today()
source_folder= "files"
start_time= time.time()
start_datetime= datetime.now()
success_count= 0
failed_count= 0
total_files= 0
count=1
for root,dirs,files in os.walk(source_folder):
    for filename in files:
        name,extension= os.path.splitext(filename)
        source_path= os.path.join(root,filename)
        new_filename= f"Batch_{count:03}{extension}"
        destination_path= os.path.join(root,new_filename)
        logging.info(f"Folder: {root}")
        logging.info(f"{filename}-> {new_filename}")
        print(f"Folder: {root}")
        print(f"{filename}->{new_filename}")
        try:
            os.rename(source_path,destination_path)
            logging.info(f"File renamed successfully: {filename}->{new_filename}")
            print(f"File renamed successfully: {filename}->{new_filename}")
            count+=1
            success_count+=1
        except FileNotFoundError:
            logging.error(f"Failed to rename file: {filename} not found ")
            print(f"Failed to rename file: {filename} not found")
            failed_count+=1
        except PermissionError:
            logging.error(f"Acess denied to the requested file: {filename}")
            print(f"Access denied to the requested  file: {filename} ")
            failed_count+=1
end_time= time.time()
end_datetime= datetime.now()
execution_time= end_time-start_time
with open ("Batch_renamer.txt","w") as report:
    report.write("================================\n")
    report.write("Batch_renamer v1.0\n")
    report.write("================================\n")
    report.write(f"Run date: {run_date}\n")
    report.write(f"Start Time: { start_datetime.strftime('%d %m %Y %H:%M:%S')}\n")
    report.write(f"End Time: { end_datetime.strftime('%d %m %Y, %H:%M:%S')}\n")
    report.write(f"Execution Time: {execution_time:.3f} seconds\n")
    report.write(f"Source Folder: {source_folder}\n")
    report.write(f"Total Files Processed: {total_files}\n")
    report.write(f"Renamed Files: {success_count}\n")
    report.write(f"Failed Files: {failed_count}\n")








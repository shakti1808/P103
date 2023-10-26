import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\gaura\Downloads"
to_dir  = "\Users\gaura\OneDrive\Desktop\Document_Files"

path =  {"Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt']}

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, { event.src_path} has been created!")
    
    def on_deleted(self, event):
       print(f"Oops! Someone deleted {event.src_path}!")
    
    def on_modified(self, event):
        print(f"Hey, { event.src_path} has bee changed!")
    
    def on_deleted(self, event):
       print(f"Hey! Someone moved {event.src_path}!")

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()
    

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,ext = os.path.splitext(file_name)
    if ext =='':
        continue
    if ext in [ '.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + file_name

        if os.path.exists(path2):
          print("Moving " + file_name + ".....")

          shutil.move(path1, path3)


        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt: 
    print("stopped!")
    observer.stop()
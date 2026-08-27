import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            print("File Created:", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            print("File Modified:", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            print("File Deleted:", event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            print("File Moved:")
            print("From:", event.src_path)
            print("To:", event.dest_path)


folder = "monitored"

observer = Observer()

handler = MyHandler()

observer.schedule(handler, folder, recursive=True)

observer.start()

print("Monitoring started...")
print("Folder:", folder)
print("Press CTRL+C to stop")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()
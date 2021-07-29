import dropbox
import os
class TransferData:
    def  __init__(self,access_token):
        self.access_token= access_token

     def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f= open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)

    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f= open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)
    
    for root,dirs,files in os.walk(file_from):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
            
        relative_path= os.path.relpath(local_path,file_from)
        dropbox_path= os.path.join(file_to, relative_path)
            
def main():
    access_token = 'sl.A1aNOCrddHO4XReBq8UX0MZDiksSrTS65J_nBg4twIncZ5VRGIOsETgxRBxf-jxSeCxlw7jYCdLezxMk5MYHVb2VdIigbPkFZ3yD4pmxICpmnpgU2EQFMnr288C8bq6H7d25zS0'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer:-")
    file_to = input("enter the full path to upload to dropbox")
    
    transferData.upload_file(file_from, file_to)
    print("file has been moved")

main()

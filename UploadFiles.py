import dropbox
import os
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for fileName in files:
                localPath = os.path.join(root,fileName)
                relativePath = os.path.relpath(localPath,file_from)
                dropboxPath = os.path.join(file_to,relativePath)
                with open(localPath,'rb')as f:
                    dbx.files_upload(f.read(),dropboxPath,mode = WriteMode('overwrite'))
        #with open(file_from,'rb') as f:
            #dbx.files_upload(f.read(),file_to)

def main():
        access_token = 'sl.Azn0TGrFGxLAn1pijdNLnwn3nrJTGHOF6bZtT2J9MtMYl9baut2YWXWIWYJXYrO592a91209I3vSyr_3sk4T1CEiiJbcxH67ZfFOMJ6quhgEc1e8kNjQTItnlFcfHl_pqffwUys'
        transferData = TransferData(access_token)

        file_from = str(input("Enter the folder path to transfer"))
        file_to = input("Enter the full path to upload to dropbox")

        transferData.upload_file(file_from,file_to)
        print("file has been moved")

main()
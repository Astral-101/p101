import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'ZJO_BMxscOcAAAAAAAAAAY0D07uXeW1RjWkeotHoODr0WLQctBRZfEUfGPNzi0pR'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test/test.txt'  

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been uplaoded succesfully")

if __name__ == '__main__':
    main()
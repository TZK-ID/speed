try:
    import os
    from speedtest import Speedtest
except ImportError:
    os.system('pip install speedtes-cli')

speedTest = Speedtest()
logo="""
╔═╗┌─┐┌─┐┌─┐┌┬┐  ┌┬┐┌─┐┌─┐┌┬┐ AU:TZK-ID
╚═╗├─┘├┤ ├┤  ││───│ ├┤ └─┐ │  FB:JAUNK
╚═╝┴  └─┘└─┘─┴┘   ┴ └─┘└─┘ ┴  YT:JAUNK NEWBIE
"""
class Speedtest:
    def __init__(self, download, upload):
        self.download=download
        self.upload=upload
    def test(self):
        print('Download =',self.download)
        print('upload =',self.upload)
if __name__=="__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    download=speedTest.download()
    upload=speedTest.upload()
    Speedtest(download, upload).test()


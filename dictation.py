#
# Copyright 2014 IMALIC3 All Rights Reserved.
# Writen by IMALIC3
#

import pycurl
import os.path
import sys

def main():
    if sys.argv[1] is not None:
        appId = '<APP-ID>'
        appKey = '<APP-KEY>'

        Id = 'C4461956B60B'
        url = 'https://dictation.nuancemobility.net:443/NMDPAsrCmdServlet/dictation?appId='+appId+'&appKey='+appKey+'&id='+Id

        curl = pycurl.Curl()
        curl.setopt(pycurl.SSL_VERIFYPEER, 0)
        curl.setopt(pycurl.SSL_VERIFYHOST, 0)
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.POST, 1)
        curl.setopt(pycurl.HTTPHEADER, ['Content-Type: audio/x-wav;codec=pcm;bit=16;rate=16000',
                                        'Accept-Language: tha-THA',
                                        'Transfer-Encoding: chunked',
                                        'Accept: text/plain',
                                        'Accept-Topic: Dictation'])

        filesize = os.path.getsize(sys.argv[1])
        curl.setopt(pycurl.POSTFIELDSIZE, filesize)
        fin = open(sys.argv[1], 'rb')
        curl.setopt(pycurl.READFUNCTION, fin.read)
        curl.perform()
    else:
        print('The client is invoked with the following arguments')
        print('param1 (string): wav_path')

if __name__ == "__main__":
    main()

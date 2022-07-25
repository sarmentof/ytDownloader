#-------------------------------------------------------------------------------
# Name:        ytDownloader
# Purpose:     Baixar vídeos do YouTube
#
# Author:      Fabianopzr
#
# Created:     23/07/2022
# Copyright:   (c) Fabianopzr 2022
# Licence:     MIT
#-------------------------------------------------------------------------------
from colorama import Fore, Style
from pytube import YouTube
from pytube.cli import on_progress
import os
from http.client import IncompleteRead

link = input("Digite o link: ")
sub_dir = "Downloads"
path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), sub_dir))
yt = YouTube(link,on_progress_callback=on_progress)

def main():
    try:
        def check_if_exists(file):
            if os.path.exists(path + '\\' + file):
                to_delete = input('Arquivo já existe. Remover? (s/N): ')
                if to_delete == 's':
                    os.remove(path + '\\' + file)
                    return True
                else:
                    return False
            else:
                return True

        def download():
            print(f'{Fore.MAGENTA}[>>]{Style.RESET_ALL} Baixando: {Fore.YELLOW}{yt.title}{Style.RESET_ALL}...')
            yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(path, max_retries=10)
            print('')
            print(f'{Fore.MAGENTA}[>>]{Style.RESET_ALL} {Fore.GREEN}Download terminado.{Style.RESET_ALL}')

        print(f'{Fore.GREEN}=============================================={Style.RESET_ALL}')
        print(f'{Fore.GREEN}=       ytDownloader v.0.1 by Fabianopzr     ={Style.RESET_ALL}')
        print(f'{Fore.GREEN}=============================================={Style.RESET_ALL}')
        file = yt.title + ".mp4"
        download() if check_if_exists(file) else print(f'{Fore.MAGENTA}[>>]{Style.RESET_ALL} {Fore.GREEN}Vídeo já baixado.{Style.RESET_ALL}')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()

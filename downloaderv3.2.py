from pytube import YouTube
import tkinter as tk
from tkinter import ttk, filedialog
from pydub import AudioSegment
import os

def download_video(format):
    video_url = url_entry.get()
    try:
        yt = YouTube(video_url)
        
        if format == "mp4":
            stream = yt.streams.get_highest_resolution()
            file_ext = "mp4"
        elif format == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
            file_ext = "mp3"
        
        # Abra a janela de seleção de diretório
        save_dir = filedialog.askdirectory()
        
        if save_dir:
            file_path = stream.download(output_path=save_dir)
            
            if format == "mp3":
                # Renomeie o arquivo para ter a extensão .mp3
                mp3_path = os.path.splitext(file_path)[0] + ".mp3"
                os.rename(file_path, mp3_path)
                status_label.config(text=f"Download concluído. Salvo em: {mp3_path}")
            else:
                status_label.config(text=f"Download concluído. Salvo em: {file_path}")
        else:
            status_label.config(text="Nenhum diretório selecionado. O download foi cancelado.")
    except Exception as e:
        status_label.config(text=f"Erro durante o download: {str(e)}")

# Crie a janela principal
root = tk.Tk()
root.title("Downloader de Vídeo e Áudio")

# Rótulo e campo de entrada para a URL do vídeo
url_label = ttk.Label(root, text="URL do Vídeo:")
url_label.grid(row=0, column=0, padx=10, pady=10)
url_entry = ttk.Entry(root, width=40)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Botões para iniciar o download em MP4 ou MP3
download_mp4_button = ttk.Button(root, text="Baixar Vídeo (MP4)", command=lambda: download_video("mp4"))
download_mp4_button.grid(row=1, column=0, padx=10, pady=10)

download_mp3_button = ttk.Button(root, text="Baixar Áudio (MP3)", command=lambda: download_video("mp3"))
download_mp3_button.grid(row=1, column=1, padx=10, pady=10)

# Rótulo para exibir o status do download
status_label = ttk.Label(root, text="")
status_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Iniciar a interface gráfica
root.mainloop()

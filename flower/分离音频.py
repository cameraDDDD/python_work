"""  
从视频文件中提取音频并保存为音频文件。  

:param video_file: 输入视频文件的路径 :param audio_file: 输出音频文件的路径 """  
try:  
# 加载视频文件 video = VideoFileClip(video_file)  
# 提取音频 audio = video.audio # 保存音频文件 audio.write_audiofile(audio_file)  

print(f"音频已成功从 '{video_file}' 中提取并保存为 '{audio_file}'。")  
except Exception as e:  
print(f"发生错误: {e}")  
finally:  
#关闭视频和音频对象 if 'audio' in locals():  
audio.close()  
if 'video' in locals():  
video.close()  

if __name__ == "__main__":  
# 设置视频文件和输出音频文件的路径 
video_file_path = "input_video.mp4"
#  替换为你的视频文件名 audio_file_path = "output_audio.mp3" # 替换为你想要保存的音频文件名 
#  提取音频 extract_audio(video_file_path, audio_file_path)
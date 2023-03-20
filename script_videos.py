import os

FRAMERATE = '60'
AMP_FACTOR = '4'


for filename in os.listdir("data/videos_a_traiter"):
    

    f = os.path.join("data/videos_a_traiter", filename)
    # checking if it is a file
    if os.path.isfile(f):
        try: 
            #create folder for png
            os.mkdir(os.path.join("data/vids", os.path.splitext(filename)[0]))
        except OSError as error: 
            print(error)

        #convert video into png

        os.system('ffmpeg -i ' + os.path.join("data/videos_a_traiter", filename) + ' -f image2 ' + os.path.join("data/vids", os.path.splitext(filename)[0]) + '/%06d.png')
        
        #create folder for amplified img

        try: 
            #create folder for png
            os.mkdir(os.path.join("data/output", os.path.splitext(filename)[0]))
        except OSError as error: 
            print(error)

        #compute amplified img

        os.system('python main.py --config_file=configs/o3f_hmhm2_bg_qnoise_mix4_nl_n_t_ds3.conf --phase=run --vid_dir=data/vids/'+ os.path.splitext(filename)[0] +' --out_dir=data/output/'+ os.path.splitext(filename)[0] + ' --amplification_factor=4')
        
        #recreate a video

        os.system('ffmpeg -y -f image2 -r ' + FRAMERATE + ' -i ' + os.path.join("data/output", os.path.splitext(filename)[0]) + '/%06d.png -c:v libx264 ' + os.path.join("data/amplified_videos", filename))

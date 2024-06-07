import cv2, os, glob
import numpy as np




def draw_text(img, text,
          font=cv2.FONT_HERSHEY_SIMPLEX,
          font_scale=1,
          font_thickness=2,
          text_color=(255, 255, 255),
          text_color_bg=(0, 0, 0),
          height=-1,
          width=-1,
          align='right'
          ):

    pad = 10
    img_copy = np.copy(img)
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_w, text_h = text_size

    if align is 'right':
        x = width - text_w-1
        y = height - text_h-1
        pos = (x, y)
        cv2.rectangle(img_copy, (x-2*pad, y-2*pad), (x + text_w + 2*pad, y + text_h + 2*pad), text_color_bg, -1)
        img = (np.round(img.astype(np.float32)*0.4 + img_copy.astype(np.float32)*0.6)).astype(np.uint8)
        cv2.putText(img, text, (x - pad, y + text_h + font_scale - 1 - pad), font, font_scale, text_color, font_thickness)
    elif align is 'center':
        x = (width - text_w-1) //2
        y = height - text_h-1
        pos = (x, y)
        cv2.rectangle(img_copy, (x-pad, y-2*pad), (x + text_w + 2*pad, y + text_h + 2*pad), text_color_bg, -1)
        img = (np.round(img.astype(np.float32)*0.4 + img_copy.astype(np.float32)*0.6)).astype(np.uint8)
        cv2.putText(img, text, (x, y + text_h + font_scale - 1 - pad), font, font_scale, text_color, font_thickness)
    elif align is 'left':
        x = 0
        y = height - text_h-1
        pos = (x, y)
        cv2.rectangle(img_copy, (x, y-2*pad), (x + text_w + 2*pad, y + text_h + 2*pad), text_color_bg, -1)
        img = (np.round(img.astype(np.float32)*0.4 + img_copy.astype(np.float32)*0.6)).astype(np.uint8)
        cv2.putText(img, text, (x + pad, y + text_h + font_scale - 1 - pad), font, font_scale, text_color, font_thickness)

    return text_size, img


# # SRx4 teaser
# H = 720
# W = 1280
# out_H = 480
# out_W = 854
# fps = 20.0
# task = 'SRx4'
# scenes = ['horsejump-high', 'car-roundabout', 'car-shadow', 'breakdance']
# other_methods = ['FMA-Net']

# for scene in scenes:
#     for other_method in other_methods:
#         ours_video_path = './DAVIS/SRx4/'+scene+'/DiffBIR_ours/video.mp4'
#         cap_ours = cv2.VideoCapture(ours_video_path)
#         other_video_path = './DAVIS/SRx4/'+scene+'/'+other_method+'/video.mp4'
#         cap_other = cv2.VideoCapture(other_video_path)
#         input_path = './DAVIS/SRx4/'+scene+'/lq/video.mp4'
#         cap_input = cv2.VideoCapture(input_path)

#         # Define the codec and create VideoWriter object
#         fourcc = cv2.VideoWriter_fourcc(*'XVID')
#         out = cv2.VideoWriter(task+'_'+scene+'_teaser.avi', fourcc, fps, (2*out_W,  out_H))
#         while cap_ours.isOpened() and cap_other.isOpened() and cap_input.isOpened():
#             ret_ours, frame_ours = cap_ours.read()
#             ret_other, frame_other = cap_other.read()
#             ret_input, frame_input = cap_input.read()
#             if not ret_ours or not ret_other or not ret_input:
#                 print("Can't receive frame (stream end?). Exiting ...")
#                 break
#             frame_input = cv2.resize(frame_input, (W, H), interpolation=cv2.INTER_AREA)
#             frame_ours = cv2.resize(frame_ours, (W, H), interpolation=cv2.INTER_AREA)
#             frame_other = cv2.resize(frame_other, (W, H), interpolation=cv2.INTER_AREA)
        
#             # edit here
#             _, frame_ours = draw_text(frame_ours, "Video Super-Resolution", height=H, width=W, align='right')
#             if other_method is 'hash':
#                 _, frame_other = draw_text(frame_other, "Hashing-nvd", height=H, width=W, align='left')
        
#             frame = cv2.hconcat([frame_input, frame_ours]) 
        
#             out.write(cv2.resize(frame, (2*out_W,  out_H), interpolation=cv2.INTER_AREA))
        
#         cap_ours.release()
#         cap_other.release()
#         out.release()
#         cv2.destroyAllWindows()

#     os.system('ffmpeg -y -i '+task+'_'+scene+'_teaser.avi -c:v libx264 -preset veryslow -crf 23 -pix_fmt yuv420p '+task+'_'+scene+'_teaser.mp4')



# # denoise teaser
# H = 720
# W = 1280
# out_H = 480
# out_W = 854
# fps = 20.0
# task = 'noise_75'
# scenes = ['003', '028', '002', '004']
# other_methods = ['VRT']

# for scene in scenes:
#     for other_method in other_methods:
#         ours_video_path = './REDS/noise_75/'+scene+'/DiffBIR_ours/video.mp4'
#         cap_ours = cv2.VideoCapture(ours_video_path)
#         other_video_path = './REDS/noise_75/'+scene+'/'+other_method+'/video.mp4'
#         cap_other = cv2.VideoCapture(other_video_path)
#         input_path = './REDS/noise_75/'+scene+'/lq/video.mp4'
#         cap_input = cv2.VideoCapture(input_path)

#         # Define the codec and create VideoWriter object
#         fourcc = cv2.VideoWriter_fourcc(*'XVID')
#         out = cv2.VideoWriter(task+'_'+scene+'_teaser.avi', fourcc, fps, (2*out_W,  out_H))
#         while cap_ours.isOpened() and cap_other.isOpened() and cap_input.isOpened():
#             ret_ours, frame_ours = cap_ours.read()
#             ret_other, frame_other = cap_other.read()
#             ret_input, frame_input = cap_input.read()
#             if not ret_ours or not ret_other or not ret_input:
#                 print("Can't receive frame (stream end?). Exiting ...")
#                 break
#             frame_input = cv2.resize(frame_input, (W, H), interpolation=cv2.INTER_AREA)
        
#             # edit here
#             _, frame_ours = draw_text(frame_ours, "Video Denoising", height=H, width=W, align='right')
#             if other_method is 'hash':
#                 _, frame_other = draw_text(frame_other, "Hashing-nvd", height=H, width=W, align='left')
        
#             frame = cv2.hconcat([frame_input, frame_ours]) 

        
#             out.write(cv2.resize(frame, (2*out_W,  out_H), interpolation=cv2.INTER_AREA))
        
#         cap_ours.release()
#         cap_other.release()
#         out.release()
#         cv2.destroyAllWindows()

#     os.system('ffmpeg -y -i '+task+'_'+scene+'_teaser.avi -c:v libx264 -preset veryslow -crf 23 -pix_fmt yuv420p '+task+'_'+scene+'_teaser.mp4')


# SRx8 compare
H = 720
W = 1280
out_H = 360
out_W = 640
fps = 20.0
tasks = ['SRx4', 'SRx8']
scenes = ['blackswan', 'goat', 'kite-surf', 'car-shadow', 'parkour', 'breakdance', 'drift-chicane', 'bmx-trees']
num_frames = [50, 90, 50, 40, 100, 84, 52, 80]
other_methods = ['lq', 'DiffBIR_perframe', 'FMA-Net', 'SDx4_perframe', 'vidtome']

for task in tasks:
    for scene, num_frame in zip(scenes, num_frames):
        for other_method in other_methods:

            # Define the codec and create VideoWriter object
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(task+'_'+scene+'_'+other_method+'_vs_ours.avi', fourcc, fps, (2*out_W,  out_H+10+num_frame))
            for seg in range(3): # 0: no temporal slice, 1: incremental slice, 2: fixed slice
                if other_method == 'SDx4_perframe':
                    ours_video_path = './DAVIS/'+task+'/'+scene+'/SDx4_ours/video.mp4'
                else:
                    ours_video_path = './DAVIS/'+task+'/'+scene+'/DiffBIR_ours/video.mp4'
                cap_ours = cv2.VideoCapture(ours_video_path)
                other_video_path = './DAVIS/'+task+'/'+scene+'/'+other_method+'/video.mp4'
                cap_other = cv2.VideoCapture(other_video_path)
                counter = 0
                slice_canvas = np.ones((10+num_frame, out_W*2, 3), dtype=np.uint8)*255
                while cap_ours.isOpened() and cap_other.isOpened():
                    ret_ours, frame_ours = cap_ours.read()
                    ret_other, frame_other = cap_other.read()
                    if not ret_ours or not ret_other:
                        print("Can't receive frame (stream end?). Exiting ...")
                        break
                    frame_ours = cv2.resize(frame_ours, (W, H), interpolation=cv2.INTER_AREA)
                    frame_other = cv2.resize(frame_other, (W, H), interpolation=cv2.INTER_AREA)
                
                    # edit here
                    if other_method == 'SDx4_perframe':
                        _, frame_ours = draw_text(frame_ours, "Ours (SD x4 upscaler)", height=H, width=W, align='right')
                    else:
                        _, frame_ours = draw_text(frame_ours, "Ours (DiffBIR)", height=H, width=W, align='right')
                    
                    if other_method == 'lq':
                        _, frame_other = draw_text(frame_other, "Input", height=H, width=W, align='left')
                    elif other_method == 'DiffBIR_perframe':
                        _, frame_other = draw_text(frame_other, "DiffBIR", height=H, width=W, align='left')
                    elif other_method == 'FMA-Net':
                        _, frame_other = draw_text(frame_other, "FMA-Net", height=H, width=W, align='left')
                    elif other_method == 'SDx4_perframe':
                        _, frame_other = draw_text(frame_other, "SD x4 upscaler", height=H, width=W, align='left')
                    elif other_method == 'vidtome':
                        _, frame_other = draw_text(frame_other, "VidToMe", height=H, width=W, align='left')
                
                    frame = cv2.hconcat([frame_other, frame_ours]) 

                    frame = cv2.resize(frame, (2*out_W,  out_H), interpolation=cv2.INTER_AREA)

                    if seg == 0:
                        frame = cv2.vconcat([frame, slice_canvas])
                    elif seg == 1:
                        slice = frame[frame.shape[0]//2, :, :]
                        slice_canvas[10+counter, :, :] = slice
                        frame[frame.shape[0]//2-2:frame.shape[0]//2+2:, :, :] = [0, 255, 255]
                        frame = cv2.vconcat([frame, slice_canvas])
                        full_slice_canvas = np.copy(slice_canvas)
                    elif seg == 2:
                        frame[frame.shape[0]//2-2:frame.shape[0]//2+2:, :, :] = [0, 255, 255]
                        frame = cv2.vconcat([frame, full_slice_canvas])
                    


                    # temporal slice
                    # if seg == 0:
                    

                    counter += 1
                
                    out.write(frame)
            
            cap_ours.release()
            cap_other.release()
            out.release()
            cv2.destroyAllWindows()

            os.system('ffmpeg -y -i '+task+'_'+scene+'_'+other_method+'_vs_ours.avi -c:v libx264 -preset veryslow -crf 23 -pix_fmt yuv420p '+task+'_'+scene+'_'+other_method+'_vs_ours.mp4')
            

# # denoising compare
# H = 720
# W = 1280
# out_H = 360
# out_W = 640
# fps = 20.0
# tasks = ['noise_75', 'noise_100', 'noise_random_50100']
# scenes = ['022', '026', '027', '024', '009', '006', '014', '000']
# other_methods = ['lq', 'DiffBIR_perframe_better', 'Shift-Net', 'vidtome', 'VRT']
# num_frame = 100

# for task in tasks:
#     for scene in scenes:
#         for other_method in other_methods:

#             # Define the codec and create VideoWriter object
#             fourcc = cv2.VideoWriter_fourcc(*'XVID')
#             out = cv2.VideoWriter(task+'_'+scene+'_'+other_method+'_vs_ours.avi', fourcc, fps, (2*out_W,  out_H+10+num_frame))
#             for seg in range(3): # 0: no temporal slice, 1: incremental slice, 2: fixed slice
#                 ours_video_path = './REDS/'+task+'/'+scene+'/DiffBIR_ours/video.mp4'
#                 cap_ours = cv2.VideoCapture(ours_video_path)
#                 other_video_path = './REDS/'+task+'/'+scene+'/'+other_method+'/video.mp4'
#                 cap_other = cv2.VideoCapture(other_video_path)
#                 counter = 0
#                 slice_canvas = np.ones((10+num_frame, out_W*2, 3), dtype=np.uint8)*255
#                 while cap_ours.isOpened() and cap_other.isOpened():
#                     ret_ours, frame_ours = cap_ours.read()
#                     ret_other, frame_other = cap_other.read()
#                     if not ret_ours or not ret_other:
#                         print("Can't receive frame (stream end?). Exiting ...")
#                         break
#                     frame_ours = cv2.resize(frame_ours, (W, H), interpolation=cv2.INTER_AREA)
#                     frame_other = cv2.resize(frame_other, (W, H), interpolation=cv2.INTER_AREA)
                
#                     # edit here
#                     _, frame_ours = draw_text(frame_ours, "Ours (DiffBIR)", height=H, width=W, align='right')
                    
#                     if other_method == 'lq':
#                         _, frame_other = draw_text(frame_other, "Input", height=H, width=W, align='left')
#                     elif other_method == 'DiffBIR_perframe_better':
#                         _, frame_other = draw_text(frame_other, "DiffBIR", height=H, width=W, align='left')
#                     elif other_method == 'Shift-Net':
#                         _, frame_other = draw_text(frame_other, "Shift-Net", height=H, width=W, align='left')
#                     elif other_method == 'VRT':
#                         _, frame_other = draw_text(frame_other, "VRT", height=H, width=W, align='left')
#                     elif other_method == 'vidtome':
#                         _, frame_other = draw_text(frame_other, "VidToMe", height=H, width=W, align='left')
                
#                     frame = cv2.hconcat([frame_other, frame_ours]) 

#                     frame = cv2.resize(frame, (2*out_W,  out_H), interpolation=cv2.INTER_AREA)

#                     if seg == 0:
#                         frame = cv2.vconcat([frame, slice_canvas])
#                     elif seg == 1:
#                         slice = frame[frame.shape[0]//2, :, :]
#                         slice_canvas[10+counter, :, :] = slice
#                         frame[frame.shape[0]//2-2:frame.shape[0]//2+2:, :, :] = [0, 255, 255]
#                         frame = cv2.vconcat([frame, slice_canvas])
#                         full_slice_canvas = np.copy(slice_canvas)
#                     elif seg == 2:
#                         frame[frame.shape[0]//2-2:frame.shape[0]//2+2:, :, :] = [0, 255, 255]
#                         frame = cv2.vconcat([frame, full_slice_canvas])


#                     counter += 1
                
#                     out.write(frame)
                
#             cap_ours.release()
#             cap_other.release()
#             out.release()
#             cv2.destroyAllWindows()

#             os.system('ffmpeg -y -i '+task+'_'+scene+'_'+other_method+'_vs_ours.avi -c:v libx264 -preset veryslow -crf 23 -pix_fmt yuv420p '+task+'_'+scene+'_'+other_method+'_vs_ours.mp4')



# get thumbnail images
# task = 'SRx4'
# scenes = ['blackswan', 'goat', 'kite-surf', 'car-shadow', 'parkour', 'breakdance', 'drift-chicane', 'bmx-trees']
# for scene in scenes:
#     ours_video_path = './DAVIS/'+task+'/'+scene+'/DiffBIR_ours/video.mp4'
#     os.system('ffmpeg -i '+ours_video_path+' -vf "select=eq(n\,0)" -q:v 3 ../thumbnails/'+scene+'_thumbnail.jpg')
# task = 'noise_75'
# scenes = ['022', '026', '027', '024', '009', '006', '014', '000']
# for scene in scenes:
#     ours_video_path = './REDS/'+task+'/'+scene+'/DiffBIR_ours/video.mp4'
#     os.system('ffmpeg -i '+ours_video_path+' -vf "select=eq(n\,0)" -q:v 3 ../thumbnails/'+scene+'_thumbnail.jpg')
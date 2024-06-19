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


# merigold teasers
H = 480
W = 854
out_H = 480
out_W = 854
fps = 20.0
task = 'SRx4'
scenes = ['dogs-jump', 'drone', 'goat', 'gold-fish', 'train']

for scene in scenes:
    ours_frames = sorted(glob.glob('ours/'+scene+'/depth_colored/*.png'))
    number_frames = len(ours_frames)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('depth_'+scene+'_teaser.avi', fourcc, fps, (2*out_W,  2*out_H))
    for idx in range(number_frames):
        frame_ours = cv2.imread('ours/'+scene+'/depth_colored/'+str(idx).zfill(5)+'.png')
        frame_other = cv2.imread('perframe/'+scene+'/depth_colored/'+str(idx).zfill(5)+'.png')
        frame_input = cv2.imread('input/'+scene+'/'+str(idx).zfill(5)+'.jpg')

        # edit here
        _, frame_ours = draw_text(frame_ours, "Ours (Marigold)", height=H, width=W, align='right')
        _, frame_input = draw_text(frame_input, "Input", height=H, width=W, align='left')
        _, frame_other = draw_text(frame_other, "Marigold", height=H, width=W, align='left')
    
        frame_top = cv2.hconcat([frame_input, frame_ours]) 
        frame_bot = cv2.hconcat([frame_other, frame_ours]) 
        frame = cv2.vconcat([frame_top, frame_bot])

    
        out.write(frame, )
    
    out.release()
    cv2.destroyAllWindows()

    os.system('ffmpeg -y -i depth_'+scene+'_teaser.avi -c:v libx264 -preset veryslow -crf 23 -pix_fmt yuv420p depth_'+scene+'_teaser.mp4')



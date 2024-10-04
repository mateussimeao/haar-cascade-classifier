import os

positive_images_path = 'positives/'
info_file_path = 'positives/info.lst'

with open(info_file_path, 'w') as f:
    for filename in os.listdir(positive_images_path):
        if filename.endswith('.bmp'):
            image_path = os.path.join(positive_images_path, filename)
            
            # Definir o tamanho da região de interesse (ROI)
            roi_width = 150
            roi_height = 150

            x = 100
            y = 200

            f.write(f'{filename} 1 {x} {y} {roi_width} {roi_height}\n')

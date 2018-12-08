import json
import os

# create the json blob for dataset
# we have 10000 images for train/val split and 2000 for test
# we later split to 9000 for train 1000 for val
out = []
for i in range(10000):
    imgid = i
    
    # they store train/val images separately
    loc = 'images_train'
    name = str(imgid) + ".jpg"
    caption_loc = "descriptions_train"
    caption_name = str(imgid) + ".txt"
    
    jimg = {}
    jimg['file_path'] = os.path.join(loc, name)
    jimg['id'] = imgid
    
    f = open(os.path.join(caption_loc, caption_name)) 
    sents = [line.replace("\n", "") for line in f]  # get caption sentenses
    jimg['captions'] = sents
    out.append(jimg)
    
json.dump(out, open('data_raw.json', 'w'))


# print (out[0])

# {'file_path': 'images_train\\0.jpg', 'id': 0, 'captions': ['The skateboarder is putting on a show using the picnic table as his stage.', 'A skateboarder pulling tricks on top of a picnic table.', 'A man riding on a skateboard on top of a table.', 'A skate boarder doing a trick on a picnic table.', 'A person is riding a skateboard on a picnic table with a crowd watching.']}

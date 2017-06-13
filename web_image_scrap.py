# Download images from a site
# In this case from someone S3 bucket
# note: use python 3
import urllib.request

count = 0
for i in range(0, 4000):
    f = str(i).zfill(4)
    img = "https://xya.s3.amazonaws.com/media/fotos/XXX_{}.jpg".format(f)
    try:
        if urllib.request.urlopen(img).code == 200:
            urllib.request.urlretrieve(
                img, "/Users/yyy/Desktop/img/{}.jpg".format(f))
            count += 1
    except:
        pass

print("-----------------------------------------")
print("   FINISH -> Downloaded {} elements".format(count))
print("-----------------------------------------")

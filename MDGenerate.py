import os
import sys
from airium import Airium

IMAGE = ['.png', '.jpg', '.jpeg']

def MDGenerate(dir):
    file = os.path.basename(dir) + ".md"
    content = ""
    for i in os.listdir(dir):
        subdir = os.path.join(dir, i)
        if os.path.isdir(subdir):
            content += "## {}\n".format(i)
            # get all items
            items = []
            for j in os.listdir(subdir):
                name = ".".join(os.path.splitext(j)[:-1])
                url = os.path.join(cdn, os.path.normpath(os.path.join(subdir, j)))
                suffix = os.path.splitext(j)[-1]
                if suffix in IMAGE:
                    items.append({ 'text':name, 'image':url })
            # generate html
            cnt = len(items)
            cols = 4
            rows = (cnt-1) // cols + 1
            html = Airium()
            with html.table(border='2'):
                for row in range(rows):
                    with html.tr().td(align='center').table(border='1'):
                        # image
                        with html.tr():
                            for col in range(cols):
                                index = row*cols + col
                                if index < cnt:
                                    html.td().img(src=items[index]['image'], height="150", width="150", align="center")

                        # text
                        with html.tr():
                            for col in range(cols):
                                index = row*cols + col
                                if index < cnt:
                                    html.td().p(align="center", style="width: 150px").b(_t=items[index]['text'])

            content += str(html) + "\n\n"

    with open(file, 'w') as f:
        f.write(content)


if __name__=='__main__':
    cdn = "https://hotarugali.github.io/Traffic"
    dirs = ['交通标志大全', '汽车标志大全']
    for dir in dirs:
        if os.path.isdir(dir):
            MDGenerate(dir)

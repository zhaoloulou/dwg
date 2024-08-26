# coding=UTF-8
import os
from pdf2image import convert_from_path
'''

# PDF文件路径
pdf_path = 'ziliao/type B Report GF.pdf'
pdf_path = pdf_path.encode('utf-8')

# 转换为图像
images = convert_from_path(pdf_path, poppler_path=r'D:/soft/poppler-24.07.0/Library/bin')

# 创建输出目录
output_dir = 'out/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 将每一页图像保存为JPEG文件
for i, image in enumerate(images):
    filename = f'page_{i+1}.jpg'
    output_path = os.path.join(output_dir, filename)
    image.save(output_path, 'JPEG')
    print(f'Saved {output_path}')



import ezdxf
from ezdxf import recover


def dwg_to_pdf(dwg_path, pdf_path):
    # 使用recover()打开DWG文件
    dwg = recover.open_dxf(dwg_path)

    # 使用draw_pdf()函数将DWG内容绘制到PDF
    dwg.draw_pdf(pdf_path)


# 调用函数进行转换
dwg_to_pdf('ziliao/3.dwg', 'output.pdf')


import subprocess

# PARAMS:
# Input folder
# Output folder
# Output version: ACAD9, ACAD10, ACAD12, ACAD14, ACAD2000, ACAD2004, ACAD2007, ACAD20010, ACAD2013, ACAD2018
# Output file type: DWG, DXF, DXB
# Recurse Input Folder: 0, 1
# Audit each file: 0, 1
# (Optional) Input files filter: *.DWG, *.DXF

TEIGHA_PATH = "ODAFileConverter"
INPUT_FOLDER = "3.dwg"
OUTPUT_FOLDER = "ziliao/"
OUTVER = "ACAD2018"
OUTFORMAT = "DXF"
RECURSIVE = "0"
AUDIT = "1"
INPUTFILTER = "*.DWG"

# Command to run
cmd = [TEIGHA_PATH, INPUT_FOLDER, OUTPUT_FOLDER, OUTVER, OUTFORMAT, RECURSIVE, AUDIT, INPUTFILTER]

# Run
subprocess.run(cmd, shell=True)

#dxf_to_png('ziliao/二室二厅87平米N19.dxf', 'output.png')
'''



import ezdxf
from ezdxf.addons import odafc

import matplotlib.pyplot as plt
from ezdxf import recover
from ezdxf import DXFStructureError
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend


def dxf2image(dxffile, destination_name):
    try:
        doc, auditor = recover.readfile(dxffile)
    except IOError as e:
        raise IOError("Not a DXF file or a generic I/O error.") from e
    except DXFStructureError as e:
        raise DXFStructureError("Invalid or corrupted DXF file.") from e
    # The auditor.errors attribute stores severe errors,
    # which may raise exceptions when rendering.
    if not auditor.has_errors:
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ctx = RenderContext(doc)
        out = MatplotlibBackend(ax)
        Frontend(ctx, out).draw_layout(doc.modelspace(), finalize=True)
        fig.savefig(destination_name, dpi=300)


if __name__ == "__main__":
    odafc.convert('ziliao/3.dwg', 'test.dxf', version='R2000')
    dxf2image("test.dxf", "31.jpg")



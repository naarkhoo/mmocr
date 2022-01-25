#!/bin/bash

# recog_method="RobustScanner"
# recog_method="SAR"
# recog_method="NRTR"
recog_method="SATRN"

if [ "$1" == "detect" ]; then
	python mmocr/utils/ocr.py \
        	data/vivino/data/images/0.jpg \
        	--output data/0_output_$recog_method.jpg \
        	--det TextSnake \
        	--recog $recog_method \
        	--print-result
elif [ "$1" == "train" ]; then
	python tools/train.py \
		configs/textrecog/seg/seg_r31_1by16_fpnocr_toy_dataset.py \
		--work-dir seg
else
	echo "who are you"
fi

exit 1



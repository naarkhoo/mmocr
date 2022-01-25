IMAGE_TAG := "mmocr"

build:
	docker buildx build --platform=linux/amd64 -t ${IMAGE_TAG} -f Dockerfile ../

run:
	# Make sure directories exist to prevent permission issues
	docker run \
		--rm \
		${IMAGE_TAG}

interactive:
	mkdir -p ../data ../model && \
	docker run \
		--platform=linux/amd64 \
		-it \
		-ti --net=host --ipc=host \
		-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix \
		--env="QT_X11_NO_MITSHM=1" \
		--gpus all \
		--shm-size=8g \
		--rm \
		-v ~/.aws/:/root/.aws/:ro \
		-v /home/alireza/Devel/mmocr/data:/${IMAGE_TAG}/data/ \
		-v /home/alireza/Devel/mmocr/x:/${IMAGE_TAG}/x \
		-v /home/alireza/Devel/mmocr/:/${IMAGE_TAG}/run/ \
		${IMAGE_TAG} \
		/bin/bash

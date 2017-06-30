.PHONY: pull build clean all

all:
	sudo docker run --privileged -v ${PWD}:${PWD} -w ${PWD} snapcore/snapcraft snapcraft

pull build stage prime snap clean:
	sudo docker run --privileged -v ${PWD}:${PWD} -w ${PWD} snapcore/snapcraft snapcraft $@

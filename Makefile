SRC_FILES = $(wildcard src/*.py)
ENTRY = src/main.py
BIN = findrep

all:
	echo $(SRC_FILES)

debug:
	python3 $(ENTRY)

release: dist/$(BIN)

dist/$(BIN): $(SRC_FILES)
	pyinstaller -F -n $(BIN) $(ENTRY)

clean:
	rm -fr build dist $(BIN).spec
CC = pyinstaller

SOURCES = keylogger.py
TARGET = keylogger

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $< --noconsole --onefile --distpath . --name $(TARGET) > /dev/null 2>&1

clean:
	rm -rf build $(TARGET).spec



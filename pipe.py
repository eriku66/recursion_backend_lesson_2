import os

pipe_for_reading, pipe_for_writing = os.pipe()
pid = os.fork()

if pid > 0:
    os.close(pipe_for_reading)
    message = f"Message from parent with pid {os.getpid()}"
    print(f"Parent, sending out the message - {message}")
    os.write(pipe_for_writing, message.encode())
else:
    os.close(pipe_for_writing)
    print(f"This is child PID: {os.getpid()}")
    file = os.fdopen(pipe_for_reading)
    print(f"Incoming message: {file.read()}")

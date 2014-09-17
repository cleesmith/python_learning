client_socket = socket.socket()
client_socket.connect((host , port))
connection = client_socket.makefile('wb')
try:
    with picamera.PiCamera() as camera:
        # Start a preview and let the camera warm up for 2 seconds
        camera.start_preview()
        time.sleep(2)
        start = time.time()
        stream = io.BytesIO()
        camera.resolution = (1920,1080) # HD
        for foo in camera.capture_continuous(stream, format='jpeg', use_video_port=True):
            # Write the length of the capture to the stream and flush to
            # ensure it actually gets sent
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            # Rewind the stream and send the image data over the wire
            stream.seek(0)
            connection.write(stream.read())
            # If we've been capturing for more than 30 seconds, quit
            if time.time() - start > 30:
                break
            # Reset the stream for the next capture
            stream.seek(0)
            stream.truncate()
    # Write a length of zero to the stream to signal we're done
    connection.write(struct.pack('<L', 0))
    camera.close()
finally:
    connection.close()
    client_socket.close()
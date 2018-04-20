import zlib, stomp

class MyListener(object):

    def on_error(self, headers, message):
        print('received an error %s' % message)

    def on_message(self, headers, message):
        decompressed_data=zlib.decompress(message, 16+zlib.MAX_WBITS)
        print('received a message %s' % decompressed_data)

conn = stomp.Connection([("datafeeds.nationalrail.co.uk", 61613)])
conn.set_listener('', MyListener())
conn.start()
conn.connect("d3user", "d3password")

QUEUE = "" # Your queue name here

conn.subscribe("/queue/"+QUEUE, id=1, ack='auto')

while 1:
    pass

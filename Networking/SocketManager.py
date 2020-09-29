import socket
import threading
import struct

import Crypto.RC4 as RC4
import Constants.PacketIds as PacketId
import Networking.Writer as Writer
import Networking.Reader as Reader
import Networking.PacketHelper as PacketHelper

HEADERSIZE = 5
PORT = 2050

class SocketManager:
    def __init__(self, ip):
        self.hooks = {}
        self.ip = ip
        self.sock = None
        self.active = True
        self.connected = False
        self.queue = []
        self.writer = Writer.Writer()
        self.reader = Reader.Reader()
        self.incomming_decoder = RC4.RC4(RC4.INCOMING_KEY)
        self.outgoing_encoder = RC4.RC4(RC4.OUTGOING_KEY)

    def hook(self, packet_type, func):
        if not self.active:
            print("Socket manager is not active")
            return
        if packet_type in self.hooks.keys():
            print("Packet type", packet_type, "is already hooked to function", self.hooks[packet_type])
            return
        if not PacketHelper.isValidPacket(packet_type) and packet_type != "ANY":
            print("Invalid packet_type:", packet_type)
            return
        self.hooks[packet_type] = func

    def startListener(self):
        if not self.active:
            print("Socket manager is not active")
            return
        if not self.connected:
            print("Socket is not connected")
            return
        self.listen_thread = threading.Thread(target=self._listen, args=())
        self.listen_thread.deamon = True
        self.listen_thread.start()        

    def connect(self, ip=None):
        if not self.active:
            print("Socket manager is not active")
            return
        if self.connected:
            print("Socket already connected to", self.ip, "disconnect it first")
            return
        else:
            if not ip is None:
                self.ip = ip
            print("Connecting to", self.ip)
        self.incomming_decoder.reset()
        self.outgoing_encoder.reset()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, PORT))
        self.connected = True
        self.startListener()

    def disconnect(self, join=True):
        if not self.active:
            print("Socket manager is not active")
            return
        if not self.connected:
            print("Socket already disconnected")
            return
        self.connected = False
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
        if join:
            self.listen_thread.join()

    def _listen(self):
        if not self.active:
            print("Socket manager is not active")
            return
        while 1:
            recv = None
            try:
                recv = self.sock.recv(HEADERSIZE)
            except ConnectionResetError:
                print("Client forcefully disconnected from", self.ip)
                if self.connected:
                    self.disconnect(False)
                return
            except ConnectionAbortedError:
                print("Stopped connection to", self.ip)
                if self.connected:
                    self.disconnect(False)
                return
            except OSError:#Socket is closed
                return
            packet_id = recv[4]
            size = struct.unpack("!i", recv[:4])[0]
            msg = recv
            while len(msg) < size:
                recv = self.sock.recv(size-len(msg))
                msg += self.incomming_decoder.process(recv)
            try:
                packet_type = PacketId.idToType[packet_id]
            except KeyError:
                print("Unknown packet id:", packet_id);
                continue
            if not "UNKNOWN" in packet_type:
                packet = PacketHelper.CreatePacket(packet_type)
                self.reader.resizeAndReset(size)
                self.reader.buffer = msg
                packet.read(self.reader)
                if packet.type in self.hooks.keys():
                    deamon_thread = threading.Thread(target=self.hooks[packet.type], args=(packet,))
                    deamon_thread.deamon = True
                    deamon_thread.start()
                if "ANY" in self.hooks.keys():
                    deamon_thread = threading.Thread(target=self.hooks["ANY"], args=(packet,))
                    deamon_thread.deamon = True
                    deamon_thread.start()
                

    def sendPacket(self, packet):
        if not self.active:
            print("Socket manager is not active")
            return
        if self.connected:
            if len(self.queue) == 0:
                self.queue.append(packet)
                deamon_thread = threading.Thread(target=self.emptyQueue, args=())
                deamon_thread.deamon = True
                deamon_thread.start()
            else:
                self.queue.append(packet)
        else:
            print("Socket is not connected")

    def emptyQueue(self):
        if len(self.queue) < 1:
            return
        if not self.connected:
            self.queue = []
            return
        packet = self.queue.pop(0)
        self.writer.reset()
        packet.write(self.writer)
        self.writer.writeHeader(PacketId.typeToId[packet.type])
        self.writer.buffer = self.writer.buffer[:5] + self.outgoing_encoder.process(self.writer.buffer[5:])
        self.sock.sendall(bytes(self.writer.buffer))
        if len(self.queue) > 0:
            deamon_thread = threading.Thread(target=self.emptyQueue, args=())
            deamon_thread.deamon = True
            deamon_thread.start()
            
            

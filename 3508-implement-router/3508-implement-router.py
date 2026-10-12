class Router:

    def __init__(self, memoryLimit: int):
        self.router = deque()
        self.memoryLimit = memoryLimit
        self.packets = set()
        self.dest_time= defaultdict(list)
 
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source,destination,timestamp)
        if packet in self.packets:
            return False
        
        if len(self.router) == self.memoryLimit:
            Packet = self.router.popleft()
            self.packets.remove(Packet)
            self.dest_time[Packet[1]].remove(Packet[2])
        
        self.router.append(packet)
        self.packets.add(packet)
        self.dest_time[packet[1]].append(packet[2])
        

        return True

    def forwardPacket(self) -> List[int]:
        if len(self.router) == 0:
            return []
        
        packet = self.router.popleft()
        self.dest_time[packet[1]].remove(packet[2])
        self.packets.remove(packet)
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_time:
            return 0
        
        timestamps = self.dest_time[destination]
        start = bisect_left(timestamps,startTime)
        end = bisect_right(timestamps,endTime)
        return end - start


 

        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
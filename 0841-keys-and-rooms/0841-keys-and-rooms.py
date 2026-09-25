class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        #Solved on my own :)
        def dfs(roomIndex,visited):
            if len(visited) == len(rooms):
                return True
            
            for key in rooms[roomIndex]:
                if key not in visited:
                    visited.add(key)
                    if dfs(key,visited):
                        return True
            
            return False

        visited = set()
        visited.add(0)
        return dfs(0,visited)

        
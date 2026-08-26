class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l = 0
        r = len(plants)-1
        alice_refill = 0
        bob_refill = 0
        curr_alice = capacityA
        curr_bob = capacityB

        while l<r:
            if plants[l] <= curr_alice:
                curr_alice-=plants[l]
            else:
                alice_refill+=1
                curr_alice = capacityA
                curr_alice-=plants[l]
            l+=1

            if plants[r]<= curr_bob:
                curr_bob-=plants[r]
            else:
                bob_refill+=1
                curr_bob=capacityB
                curr_bob-=plants[r]
            r-=1
            
        total = alice_refill + bob_refill

        if l==r:
            if max(curr_alice,curr_bob) < plants[l]:
                total+=1
    
        return total

        
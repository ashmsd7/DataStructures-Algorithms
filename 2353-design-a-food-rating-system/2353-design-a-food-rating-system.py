import heapq

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.cuisine_foods = {}
        self.foods_c_rating = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):

            self.foods_c_rating[food] = [cuisine, rating]

            if cuisine not in self.cuisine_foods:
                self.cuisine_foods[cuisine] = []

            heapq.heappush(
                self.cuisine_foods[cuisine],
                (-rating, food)
            )

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foods_c_rating[food][0]

        self.foods_c_rating[food][1] = newRating

        heapq.heappush(
            self.cuisine_foods[cuisine],
            (-newRating, food)
        )

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_foods[cuisine]

        while True:
            neg_rating, food = heap[0]

            if -neg_rating == self.foods_c_rating[food][1]:
                return food

            heapq.heappop(heap)
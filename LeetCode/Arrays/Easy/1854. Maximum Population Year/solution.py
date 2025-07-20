class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        counter = {}

        for birth, death in logs:
            counter[birth] = counter.get(birth, 0) + 1
            counter[death] = counter.get(death, 0) - 1

        years = sorted(counter.keys())

        population = 0
        max_population = 0
        max_year = 0

        for year in years:
            population += counter[year]
            if population>max_population:
                max_population = population
                max_year = year
        
        return max_year
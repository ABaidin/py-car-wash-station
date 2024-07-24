class Car:
    def __init__(
            self,
            comfort_class: int = 7,
            clean_mark: int = 1,
            brand: str = "some_car"
    ) -> None:
        if comfort_class in range(1, 7 + 1):
            self.comfort_class = comfort_class

        if clean_mark in range(1, 10 + 1):
            self.clean_mark = clean_mark

        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float = 1.0,
            clean_power: int = 5,
            average_rating: float = 3.5,
            count_of_ratings: int = 100
    ) -> None:
        if 1.0 <= distance_from_city_center <= 10.0:
            self.distance_from_city_center = distance_from_city_center

        if clean_power in range(1, 10 + 1):
            self.clean_power = clean_power

        if 1.0 <= average_rating <= 5.0:
            self.average_rating = average_rating

        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (
                (self.clean_power - car.clean_mark)
            * car.comfort_class
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: int | float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = (round(
            (total_rating + rating)
            / self.count_of_ratings, 1
        )
        )

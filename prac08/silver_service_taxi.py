from prac08.taxi import Taxi
class Silverservicetaxi(Taxi):
    flagfall=4.5
    def __init__(self,name,fuel,fanciness):
        super().__init__(name,fuel)
        self.fanciness= fanciness
        self.price_per_km*=fanciness
    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"
    def get_fare(self):
        return self.flagfall+super().get_fare()


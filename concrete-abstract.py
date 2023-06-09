class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, bottles_at_start, bottles_at_end):
        return '\n'.join(self.verse(bottles) for bottles in range(bottles_at_start, bottles_at_end - 1, -1))

    def verse(self, bottles):
        return Round(bottles).__str__()


class Round:
    def __init__(self, bottles):
        self._bottles = bottles

    def __str__(self):
        return self.challenge() + self.response()

    def challenge(self):
        return self.bottles_of_beer().capitalize() + " " + self.on_wall() + ", " + self.bottles_of_beer() + ".\n"

    def response(self):
        return self.go_to_the_store_or_take_one_down() + ", " + self.bottles_of_beer() + " " + self.on_wall() + ".\n"

    def bottles_of_beer(self):
        return self.anglicized_bottle_count() + " " + self.pluralized_bottle_form() + " of " + self.beer()

    def beer(self):
        return "beer"

    def on_wall(self):
        return "on the wall"

    def pluralized_bottle_form(self):
        return 'bottle' if self.is_last_beer() else 'bottles'

    def anglicized_bottle_count(self):
        return 'no more' if self.is_all_out() else self._bottles.__str__()

    def go_to_the_store_or_take_one_down(self):
        if self.is_all_out():
            self._bottles = 99
            return self.buy_new_beer()
        else:
            lyrics = self.drink_beer()
            self._bottles -= 1
            return lyrics

    def buy_new_beer(self):
        return 'Go to the store and buy some more'

    def drink_beer(self):
        return f"Take {self.it_or_one()} down and pass it around"

    def it_or_one(self):
        return 'it' if self.is_last_beer() else 'one'

    def is_all_out(self):
        return self._bottles == 0

    def is_last_beer(self):
        return self._bottles == 1


print(Bottles().song())

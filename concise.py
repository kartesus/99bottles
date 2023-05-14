class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, hi, lo):
        return '\n'.join(self.verse(n) for n in Bottles.down_to(hi, lo))

    def verse(self, n):
        return (
            f"{n if n else 'No more'} bottle{'' if n == 1 else 's'}"
            " of beer on the wall, "
            f"{n if n else 'No more'} bottle{'' if n == 1 else 's'} of beer.\n"
            f"{'Take one down and pass it around' if n else 'Go to the store and buy some more'}, "
            f"{n-1 if n-1 >= 0 else 99 if n-1 < 0 else 'No more'} bottle{'' if n-1 == 1 else 's'}"
            " of beer on the wall.\n"
        )

    @staticmethod
    def down_to(max, min):
        return range(max, min - 1, -1)

print(Bottles().song())
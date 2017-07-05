class Prime(object):
    def check(self, n):
        prime_list = []

        for i in range(2, n):
            j = 2
            counter = 0

            while j < i:
                if i % j == 0:
                    counter = 1
                    i += 1

                else:
                    j += 1

            if counter == 0:
                prime_list.append(i)
            else:
                counter = 0
        return prime_list


number = Prime()
print(number.check(11))


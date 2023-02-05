class Person:
    name = []
    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'There is no such user'
        else:
            return self.name[user_id]

if __name__ == '__main__':
    person = Person()
    user_1 = person.set_name('John')
    print('User ID: {}'.format(user_1))
    print(person.get_name(user_1))
from docassemble.base.util import Individual

class Officer(Individual):

    def get_position(self, position):
        self.position = position
        return self.position

    def how_long_position(self, how_long):
        self.how_long = how_long
        return self.how_long

    def get_business_experience(self, experience):
        self.experience = experience
        return self.experience

    def get_occupation(self,occupation):
        self.occupation = occupation
        return self.occupation

    def get_other_employers(self, employers):
        self.employers = employers
        return self.employers

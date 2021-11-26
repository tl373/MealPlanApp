class Person:
    def __init__(self,height,weight,age,gender,activity):
        if gender == "male":
            self.x = 66
            self.height = height*6.2
            self.weight = weight*12.7
            self.age = age*6.76
        else:
            self.x = 655.1
            self.height = height *4.35
            self.weight = weight*4.7
            self.age = age*4.7

        self.activity = self.determine_activity(activity)


    def determine_activity(self,activity):

        if activity == 0:
            return int(1.2)
        elif activity == 'light':
            return int(1.3)
        elif activity == 'moderate':
            return int(1.55)
        elif activity == 'heavy':
            return int(1.72)

    def select_preferences(self):
        preferences = {'Fish','Red Meat','White Meat','Vegeterian','Pescatarian','Vegan'}

    def calculate_calories(self):
        bmr_result = int(self.x+self.height+self.weight-self.age)
        output = {'Lose': self.activity * bmr_result - 500,
                  'Maintain': self.activity * bmr_result,
                  'Gain': self.activity * bmr_result + 500}

        return output
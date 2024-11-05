from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])
#it random from 1-6
#bug when dice_num is 6 because it is out of range dice_image index is only from 0-5


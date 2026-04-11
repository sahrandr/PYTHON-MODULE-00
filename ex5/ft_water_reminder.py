# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sahrandr <sahrandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/10 22:03:24 by sahrandr          #+#    #+#              #
#    Updated: 2026/04/10 22:03:30 by sahrandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
	watering = int(input("Days since last watering: "))
	if 2 < watering:
		print("Water the plants!")
	else:
		print("Plants are fine")

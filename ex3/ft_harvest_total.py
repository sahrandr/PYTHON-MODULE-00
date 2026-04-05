# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sahrandr <sahrandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/29 16:28:31 by sahrandr          #+#    #+#              #
#    Updated: 2026/03/29 16:32:11 by sahrandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	day1 = int(input("Day 1 harvest: "))
	day2 = int(input("Day 2 harvest: "))
	day3 = int(input("Day 3 harvest: "))
	print("Total harvest:", day1 + day2 + day3)
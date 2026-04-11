# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sahrandr <sahrandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/29 16:53:35 by sahrandr          #+#    #+#              #
#    Updated: 2026/03/29 17:01:23 by sahrandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def  ft_count_harvest_iterative():
	n = int(input("Days until harvest: "))
	for i in range(1, n+1):
		print(f"Day {i}")
	print("Harvest time!")
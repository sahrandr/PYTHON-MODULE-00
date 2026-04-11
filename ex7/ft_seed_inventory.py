# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sahrandr <sahrandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/30 15:33:08 by sahrandr          #+#    #+#              #
#    Updated: 2026/04/11 08:42:02 by sahrandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	seed_type = seed_type.capitalize()
	if unit == "packets":
		print(f"{seed_type} seeds: {quantity} packets available")
	elif unit == "grams":
		print(f"{seed_type} seeds: {quantity} grams total")
	elif unit == "area":
		print(f"{seed_type} seeds: covers {quantity} square meters")
	
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sahrandr <sahrandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/03 10:34:41 by sahrandr          #+#    #+#              #
#    Updated: 2026/04/03 16:07:34 by sahrandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive() -> None:
    n = int(input("Days until harvest: "))

    def helper(day: int) -> None:
        if day > n:
            print("Harvest time!")
            return
        
        print(f"Day {day}")
        helper(day + 1)

    helper(1)
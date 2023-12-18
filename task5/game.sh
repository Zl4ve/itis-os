#!/bin/bash

step=1
total_answers=0
right_answers=0
answers=()
RED='\e[31m'
GREEN='\e[32m'
RESET='\e[0m'

while :
do
	echo "Step: ${step}"

	ans=${RANDOM: -1}

	read -p "Please enter number from 0 to 9 (q - quit): " input

	case "${input}" in
		[0-9])
			total_answers=$(( total_answers + 1 ))

			if [[ "${input}" == "${ans}" ]]
				then
					echo "Hit! My number: ${ans}"
					right_answers=$(( right_answers + 1 ))
					ans_colored="${GREEN}${ans}${RESET}"
				else
					echo "Miss! My number: ${ans}"
					ans_colored="${RED}${ans}${RESET}"
			fi

			answers=("${answers[@]}" "${ans_colored}")

			let right_percent=right_answers*100/total_answers
			let wrong_percent=100-right_percent

			echo "Hit: ${right_percent}%" "Miss: ${wrong_percent}%"

			if [[ "${#answers[@]}" -lt 10 ]]
				then
					echo -e "Numbers: ${answers[@]}"
				else
					echo -e "Numbers: ${answers[@]: -10}"
			fi

			step=$(( step + 1 ))
		;;
		q)
			echo "Game is finished."
			exit 0
		;;
		*)
			echo "Invalid input! Try again."
	esac
done

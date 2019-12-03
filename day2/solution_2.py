"""
--- Part Two ---
"Good, the new computer seems to be working correctly! Keep it nearby during this mission - you'll probably use it again. Real Intcode computers support many more features than your new one, but we'll let you know what they are as you need them."

"However, your current priority should be to complete your gravity assist around the Moon. For this mission to succeed, we should settle on some terminology for the parts you've already built."

Intcode programs are given as a list of integers; these values are used as the initial state for the computer's memory. When you run an Intcode program, make sure to start by initializing memory to the program's values. A position in memory is called an address (for example, the first value in memory is at "address 0").

Opcodes (like 1, 2, or 99) mark the beginning of an instruction. The values used immediately after an opcode, if any, are called the instruction's parameters. For example, in the instruction 1,2,3,4, 1 is the opcode; 2, 3, and 4 are the parameters. The instruction 99 contains only an opcode and has no parameters.

The address of the current instruction is called the instruction pointer; it starts at 0. After an instruction finishes, the instruction pointer increases by the number of values in the instruction; until you add more instructions to the computer, this is always 4 (1 opcode + 3 parameters) for the add and multiply instructions. (The halt instruction would increase the instruction pointer by 1, but it halts the program instead.)

"With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need to determine what pair of inputs produces the output 19690720."

The inputs should still be provided to the program by replacing the values at addresses 1 and 2, just like before. In this program, the value placed in address 1 is called the noun, and the value placed in address 2 is called the verb. Each of the two input values will be between 0 and 99, inclusive.

Once the program has halted, its output is available at address 0, also just like before. Each time you try a pair of inputs, make sure you first reset the computer's memory to the values in the program (your puzzle input) - in other words, don't reuse memory from a previous attempt.

Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)

Your puzzle answer was 2505.


The explanation of this problem is super confusing. I sat down and read it multiple times before I finally understood what the problem was asking. The problem was asking to replace the 1st and 2nd address inputs with values until you found the values that produced 19690720 in the output, at address 0.

process_arr function does the same thing it did in part 1, which is process the array which holds the values in "memory".
Refactored the code from part 1 to be in a function so it can return from the method to speed up the computation.
Loop through [0..99, 0..99] inputs until desired output is reached.
"""
def process_arr(arr, pos):
    opcode = arr[pos]
    if opcode == 99:
        return False
    input_index_1 = arr[pos+1]
    input_index_2 = arr[pos+2]
    output_index = arr[pos+3]
    if opcode == 1:
        arr[output_index] = arr[input_index_1] + arr[input_index_2]
    elif opcode == 2:
        arr[output_index] = arr[input_index_1] * arr[input_index_2]
    return True

def main():
    fo = open('input.txt', "r")
    arr = fo.read().rstrip('\n').split(',')
    arr = list(map(int, arr))
    for i in range(100):
        for j in range(100):
            input_arr = arr[:]
            input_arr[1] = i
            input_arr[2] = j
            index = 0
            while process_arr(input_arr, index):
                index += 4
            output = input_arr[0]
            if output > 19690720:
                break
            elif output == 19690720:
                print(f"i: {i}, j: {j}")
                return
        if output > 19690720:
            print("not possible")
            return

if __name__ == "__main__":
    main()
